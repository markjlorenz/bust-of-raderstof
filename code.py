import time, alarm
import board, digitalio, touchio
import feathers3

# turn off the blue LED
feathers3.led_set(False)

print("\nTim Raderstof, Ohio's most famous nurse.")
print("------------------\n")

led_1 = digitalio.DigitalInOut(board.IO11)
led_1.direction = digitalio.Direction.OUTPUT

def startIdeaTime():
    led_1.value=True

def stopIdeaTime():
    led_1.value=False

wakeAlarm = alarm.touch.TouchAlarm(board.D18)
#wakeAlarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 15)

# `TouchAlarm` doesn't re-trigger if you hold down the touch, so we need a second touch pad
# that acts as a latch.'
# We also need to re-initiailze the touchLatch after sleep.
#
def initTouchLatch():
    touch = touchio.TouchIn(board.D19)
    touch.threshold = 27860 # will need to tune this value once installed
    return touch

LOOP_DELAY   = 0.1 # seconds
MINIMUM_TIME = 2   # seconds
touchLatch   = initTouchLatch()
wakeUntil    = 0

while True:
    print("now: {:0.2f}, wakeUntil: {:0.2f}, touchLatch: {}".format(time.monotonic(), wakeUntil, touchLatch.raw_value))
    if time.monotonic() < wakeUntil:
        time.sleep(LOOP_DELAY)

    elif touchLatch.value:
        wakeUntil = time.monotonic() + LOOP_DELAY

    else:
        print("Nap time")
        stopIdeaTime()
        touchLatch.deinit()
        alarm.light_sleep_until_alarms(wakeAlarm)

        print("Idea time!")
        startIdeaTime()
        touchLatch = initTouchLatch()
        wakeUntil = time.monotonic() + MINIMUM_TIME


