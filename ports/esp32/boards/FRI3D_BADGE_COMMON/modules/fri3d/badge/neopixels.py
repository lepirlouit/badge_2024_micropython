from fri3d.badge.hardware import hardware

from machine import Pin
from neopixel import NeoPixel

# Create the NeoPixel object
neopixels = NeoPixel(Pin(hardware.neopixels.pin, Pin.OUT), hardware.neopixels.amount)

# Clear the pixels on import
for id in range(hardware.neopixels.amount):
    neopixels[id] = (0, 0, 0)

neopixels.write()
