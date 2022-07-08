import asyncio
import time, alarm, math
import board, digitalio, touchio
import feathers3

# turn off the blue LED
feathers3.led_set(False)

print("\nTim Raderstof, Ohio's most famous nurse.")
print("------------------\n")

led_1 = digitalio.DigitalInOut(board.IO10)
led_1.direction = digitalio.Direction.OUTPUT
led_2 = digitalio.DigitalInOut(board.IO7)
led_2.direction = digitalio.Direction.OUTPUT
led_3 = digitalio.DigitalInOut(board.IO3)
led_3.direction = digitalio.Direction.OUTPUT
led_4 = digitalio.DigitalInOut(board.IO1)
led_4.direction = digitalio.Direction.OUTPUT

def allOn(trueOrFalse):
    led_1.value = trueOrFalse
    led_2.value = trueOrFalse
    led_3.value = trueOrFalse
    led_4.value = trueOrFalse

async def ideaTime(duration):
    allOn(True)
    await asyncio.sleep(duration)

async def checkTouchLatch(touchLatch):
    MAX_TIME = 5  # seconds
    MAX_MONO = time.monotonic() + MAX_TIME

    print("touchLatch: {}".format(touchLatch.raw_value))

    while touchLatch.value:
        if (time.monotonic() * 1000) % 100 <= 1:
            print("touchLatch: {}".format(touchLatch.raw_value))

        if time.monotonic() > MAX_MONO:
            print("WATCH DOG FORCING EXIT")
            break

        allOn(True)
        await asyncio.sleep(0)

# LiPo is good from 3.2 to 4.2 volts, so we will blink a reverse-percentage
# 0 blinks means we are fully charged.
# 10 blinks means the battery is at 3.2v and must be charged immediatly.
# 5 blinks means the battery is at 3.7v mid-charge.
#
async def batteryReport():
    voltage = feathers3.get_battery_voltage()
    print("Battery: {:0.1f}\n".format(voltage))
    BATTERY_MIN = 3.2
    BATTERY_MAX = 4.2
    batteryPercent = (voltage - BATTERY_MIN) / (BATTERY_MAX - BATTERY_MIN)
    #batteryBlinks = math.floor(10 - batteryPercent * 10)
    batteryBlinks = math.floor(batteryPercent * 10)
    while batteryBlinks > 0:
        feathers3.led_set(True)
        await asyncio.sleep(0.1)
        batteryBlinks -= 1
        feathers3.led_set(False)
        await asyncio.sleep(0.1)

wakeAlarm = alarm.touch.TouchAlarm(board.D16)
#wakeAlarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 15)

# `TouchAlarm` doesn't re-trigger if you hold down the touch, so we need a second touch pad
# that acts as a latch.'
# We also need to re-initiailze the touchLatch after sleep.
#
def initTouchLatch():
    touch = touchio.TouchIn(board.D17)
    touch.threshold = 19200 # will need to tune this value once installed
    return touch

#while True:
#    allOn(True)

async def main():
    MIN_TIME = 2   # seconds
    touchLatch   = initTouchLatch()

    while True:
        print("Nap time")
        touchLatch.deinit()
        alarm.light_sleep_until_alarms(wakeAlarm)

        print("Idea time!")
        touchLatch          = initTouchLatch()
        batteryBlinkTask    = batteryBlinkTask = asyncio.create_task(batteryReport())
        ideaTimeTask        = asyncio.create_task(ideaTime(MIN_TIME))
        checkTouchLatchTask = asyncio.create_task(checkTouchLatch(touchLatch))
        await asyncio.gather(batteryBlinkTask, ideaTimeTask, checkTouchLatchTask)
        allOn(False)

asyncio.run(main())

