# Bust of Raderstorf
> Ohio's most famous nurse.

![Get inspiration from Tim](https://github.com/markjlorenz/bust-of-raderstof/raw/main/doc/demo.gif)

## Setup

1. Install CircuitPython on the board, [the boards I use from Unexpected Maker](https://esp32s3.io/) come with CircuitPython installed out of the box.

2. Copy `code.py` and `lib/` to the `CIRCUITPY` device that shows up when you connect the board's USB to your computer.

3. I used the [Mu Editor](https://codewith.mu/) to view the serial communications, this is helpful, but optional.

4. 3D print the model in `model/`.  If you have an Ender3 v2 (or clone) you can use the `.gcode` provided.

5. Wire pins `D10`, `D7`, `D3`, `D1` to the positive leg of the LEDs (I used color flashing LEDs)

6. Wire pins `D14`, and `D12` to some 26AWG motor coil wire, this will be come the touch sensors.

7. Wire the grounds

8. Pass the touch wires through the holes that lead up through the shoulder, and use a pocket knife to gently scrape away the wire insulation.

9. Place your hand on Tim's shoulder, and ask for inspiriation.  Maybe you'll get it.

![shoulder wire](https://raw.githubusercontent.com/markjlorenz/bust-of-raderstof/main/doc/IMG_7705.JPG)
![inside wiring](https://raw.githubusercontent.com/markjlorenz/bust-of-raderstof/main/doc/IMG_7706.JPG)

It's important to keep the LiPo charged to >20% of capacity, so the blue LED on the board will blink to let you know the remaining battery life.  1 blink, the battery is full.  10 blinks or more and it's time to charge.

## Working with CircuitPython

Documentation for CircuitPython: https://docs.circuitpython.org/en/latest/shared-bindings/touchio/index.html
Helper modules: https://github.com/UnexpectedMaker/esp32s3/tree/main/code
STEP file: https://github.com/UnexpectedMaker/esp32s3/blob/main/3d%20models/FeatherS3_P4.step
Discord: https://discord.com/channels/605621786616528915/613513985676935169/946623055638171728

See available modules: `help("modules")`
See the details of module:
```python
>>> import board
>>> board.
```

## Deep sleep doesn't work
- https://github.com/adafruit/circuitpython/issues/6090
- https://github.com/espressif/esp-idf/issues/8569

## Printing

![Idea Tim Printing](https://github.com/markjlorenz/bust-of-raderstof/raw/main/doc/Tim-Printing.gif)
