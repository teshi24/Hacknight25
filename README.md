# Häcknight 2025 - "Häck the Box"

## Pico Resources

- Pico Webpage https://www.waveshare.com/wiki/PicoGo
- PicoGo APP apk in [resources/Base.zip](resources/Base.zip) (Origin: https://files.waveshare.com/upload/9/90/Base.zip
-> Android only)
- use pre-installed VS-Code workspace

## How to Program on Pico

- upload what you need on Pico by copy-pasting the relevant files
- main.py will run pn Pico at start up
- make sure to turn on Pico while developing / connected to PC (otherwise, sensor values will be off)

## Connect to PicoGo App

- Ensure those files are on Pico:
- `Motor.py`
- `ST7789.py`
- `ws2812.py`
- content of `bluetooth.py` in `main.py`.
- Start bluetooth and GPS on phone
  - DO NOT connect to any bluetooth device via the phone
- Start app > scan > choose -SPP device (1234)

## Last Hint of the Day

- It's maybe a necessity to remove your robots balls.
