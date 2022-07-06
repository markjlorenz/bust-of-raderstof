#https://docs.circuitpython.org/en/latest/shared-bindings/touchio/index.html

import time, alarm
import neopixel
import board, digitalio
import feathers3
import touchio

print("Awake from: ", alarm.wake_alarm)

# Create a NeoPixel instance
# Brightness of 0.3 is ample for the 1515 sized LED
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.3, auto_write=True, pixel_order=neopixel.RGB)

# Say hello
print("\nHello from FeatherS3!")
print("------------------\n")

print("Pixel Time!\n")

# Create a colour wheel index int
color_index = 0

# Turn on the power to the NeoPixel
feathers3.set_ldo2_power(True)

touchSleep = touchio.TouchIn(board.D12)
#touchSleep.threshold = 65000

#touchWake = touchio.TouchIn(board.D18)
#touchWake.threshold = 65000
wakeAlarm = alarm.touch.TouchAlarm(board.D18)
#wakeAlarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 15)

i = 0

# Rainbow colours on the NeoPixel
while True:    # if the cap sensor is touched, set the light to a specific color_index
    #print("{}, {}", touchSleep.raw_value, touchSleep.value)
    #if touchSleep.value:
    #    pixel[0] = ( 0xff, 0xff, 0xff, 0.5)
    #    continue

    #if touchSleep.value:
    i += 1
    if i > 300:
        print("Sleeping NOW: ", touchSleep.raw_value, touchSleep.value)
        pixel[0] = ( 0xff, 0xff, 0xff, 0.5)
        time.sleep(0.3)
        feathers3.set_ldo2_power(False)
        time.sleep(0.3)
        feathers3.set_ldo2_power(True)
        pixel[0] = ( 0xff, 0x00, 0x00, 0.5)
        time.sleep(0.3)
        feathers3.set_ldo2_power(False)
        time.sleep(0.3)
        feathers3.set_ldo2_power(True)
        pixel[0] = ( 0x00, 0xff, 0x00, 0.5)
        time.sleep(0.3)
        feathers3.set_ldo2_power(False)
        time.sleep(0.3)
        feathers3.set_ldo2_power(True)
        pixel[0] = ( 0x00, 0x00, 0xff, 0.5)
        time.sleep(0.3)
        feathers3.set_ldo2_power(False)
        time.sleep(0.3)
        feathers3.set_ldo2_power(True)
        pixel[0] = ( 0xff, 0xff, 0xff, 0.5)
        time.sleep(0.3)
        feathers3.set_ldo2_power(False)


        #alarm.exit_and_deep_sleep_until_alarms(wakeAlarm)
        alarm.light_sleep_until_alarms(wakeAlarm)
        i = 0
        print("Awake")
        feathers3.set_ldo2_power(True)

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
