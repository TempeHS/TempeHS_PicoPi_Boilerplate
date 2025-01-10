from machine import Pin
from utime import sleep

pin = Pin("LED", Pin.OUT)

print("LED starts flashing...")
while True:
    try:
        pin.toggle()
        sleep(3)  # sleep 1sec
        print("LED is ON" if pin.value() else "LED is OFF")
    except KeyboardInterrupt:
        break
pin.off()
print("Finished.")
