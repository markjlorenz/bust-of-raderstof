# Bust of Raderstorf
> Ohio's most famous nurse.

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

```python
# Make a light go white when the pin is touched.

import time, gc, os
import neopixel
import board, digitalio
import feathers3
import touchio


# Create a NeoPixel instance
# Brightness of 0.3 is ample for the 1515 sized LED
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.3, auto_write=True, pixel_order=neopixel.RGB)

# Say hello
print("\nHello from FeatherS3!")
print("------------------\n")

# Show available memory
print("Memory Info - gc.mem_free()")
print("---------------------------")
print("{} Bytes\n".format(gc.mem_free()))

flash = os.statvfs('/')
flash_size = flash[0] * flash[2]
flash_free = flash[0] * flash[3]
# Show flash size
print("Flash - os.statvfs('/')")
print("---------------------------")
print("Size: {} Bytes\nFree: {} Bytes\n".format(flash_size, flash_free))

print("Pixel Time!\n")

# Create a colour wheel index int
color_index = 0

# Turn on the power to the NeoPixel
feathers3.set_ldo2_power(True)

touch = touchio.TouchIn(board.D18)
touch.threshold = 65000

# Rainbow colours on the NeoPixel
while True:
    # if the cap sensor is touched, set the light to a specific color_index
    print("{}, {}", touch.raw_value, touch.value)
    if touch.value:
        pixel[0] = ( 0xff, 0xff, 0xff, 0.5)
        continue

    # Get the R,G,B values of the next colour
    r,g,b = feathers3.rgb_color_wheel( color_index )
    # Set the colour on the NeoPixel
    pixel[0] = ( r, g, b, 0.5)
    # Increase the wheel index
    color_index += 1

    # If the index == 255, loop it
    if color_index == 255:
        color_index = 0
        # Invert the internal LED state every half colour cycle
        feathers3.led_blink()

    # Sleep for 15ms so the colour cycle isn't too fast
    time.sleep(0.015)
```

https://github.com/adafruit/esp-idf/blob/circuitpython-v4.4/components/esp_hw_support/sleep_modes.c#L416

## Deep sleep doesn't work
- https://github.com/adafruit/circuitpython/issues/6090
- https://github.com/espressif/esp-idf/issues/8569

