from TRSensor import TRSensor
from Motor import PicoGo
import time


print("\nTRSensor Test Program ...\r\n")
time.sleep(3)
M = PicoGo()
TRS=TRSensor()
for i in range(100):
    if(i<25 or i>= 75):
        M.setMotor(30,-30)
    else:
        M.setMotor(-30,30)
    TRS.calibrate()
    
M.setMotor(0,0)
expected_white_total = sum(TRS.calibratedMin)
no_line_threshold = expected_white_total * 0.78

print(TRS.calibratedMin)
print(TRS.calibratedMax)
print(expected_white_total)
print(no_line_threshold)
print("\ncalibrate done\r\n")


max_speed = 20
integral = 0
last_proportional = 0

count = 0
while True:
    
    position, Sensors = TRS.readLine()
    sensor_total = sum(Sensors)
    
    if count % 20 == 0:
        print(f'calibrated: {TRS.readCalibrated()}')
        print(f'position: {position}, sensors: {Sensors}')
        print(f"sensor total: {sensor_total}")
    count += 1
    
    if sensor_total > no_line_threshold:
        # Lost line: rotate in place in last known direction
        if last_proportional >= 0:
            M.setMotor(max_speed, -max_speed)  # turn right in place
        else:
            M.setMotor(-max_speed, max_speed)  # turn left in place
    else:
        # The "proportional" term should be 0 when we are on the line.
        proportional = position - 2000

        # Compute the derivative (change) and integral (sum) of the position.
        derivative = proportional - last_proportional
        integral += proportional

        # Remember the last position.
        last_proportional = proportional
        
        '''
        // Compute the difference between the two motor power settings,
        // m1 - m2.  If this is a positive number the robot will turn
        // to the right.  If it is a negative number, the robot will
        // turn to the left, and the magnitude of the number determines
        // the sharpness of the turn.  You can adjust the constants by which
        // the proportional, integral, and derivative terms are multiplied to
        // improve performance.
        '''
        power_difference = proportional/30  + derivative*2;  

        if (power_difference > max_speed):
            power_difference = max_speed
        if (power_difference < - max_speed):
            power_difference = - max_speed
        
        if (power_difference < 0):
            M.setMotor(max_speed + power_difference, max_speed)
        else:
            M.setMotor(max_speed, max_speed - power_difference)


