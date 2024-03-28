from neopixel import NeoPixel

from fri3d.badge.hardware import hardware_leds

# Create the NeoPixel object
leds = NeoPixel(hardware_leds.pinout.pin, hardware_leds.amount)

# Clear the pixels on import
for id in range(hardware_leds.amount):
    leds[id] = (0, 0, 0)

leds.write()
