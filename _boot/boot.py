import webrepl
webrepl.start()

# SAFE MODE
from utime import sleep
from machine import Pin, reset
from esp32 import Partition

def safe_mode_act(boot_pin):

    if boot_pin.safe_mode:

        led_pin = boot_pin.led_pin
        led_on = boot_pin.led_on
        btn_pin = boot_pin.btn_pin
        reset_val = boot_pin.reset_val

        print("Pin Control: LED {}, BTN: {}".format(led_pin, btn_pin))

        safe_pin = Pin(btn_pin, Pin.IN, Pin.PULL_DOWN)
        led_pin = Pin(led_pin, Pin.OUT)
        led_pin.value(led_on)
        print("Wait 5sec - Safe Mode")
        sleep(5)
        print("Safe Mode Activate: {}".format(safe_pin.value() == reset_val))

        if safe_pin.value() == reset_val:
            led_pin.value(1 - led_on)
            Partition.set_boot(Partition('factory'))
            reset()

        sleep(1)
        led_pin.value(1 - led_on)

    else:
        print("Safe Mode: not present")


try:
    import boot_pin
    safe_mode_act(boot_pin)
    del(boot_pin)
except Exception as e:
    print(e)
    pass



# PARTITIONS // Path

import sys
import uos
import gc

bootpart = Partition(Partition.BOOT)
runningpart = Partition(Partition.RUNNING)

print("INFO - Partitions")
print("Boot: {}".format(bootpart))
print("Run: {}".format(runningpart))



part_info = runningpart.info()
part_name = part_info[4]

try:
    uos.mkdir(part_name)
except OSError as e:
    print("Path already exist")
    pass

pyversion = 'None'
try:
    with open("/{}/VERSION".format(part_name), "r") as f:
        pyversion = f.read()
except:
    pass
print("Version hash: {}".format(pyversion.strip()))

sys.path.append("/{}".format(part_name))
sys.path.append("/{}/{}".format(part_name, "lib"))
sys.path.append("/{}/{}".format(part_name, "app"))
uos.chdir("/{}".format(part_name))

print("Working Sys Path: {}".format(sys.path))

gc.collect()
