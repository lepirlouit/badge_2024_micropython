from . import pinout


class Hardware:
    class NeoPixels:
        def __init__(self):
            self.pin = pinout.neopixels
            self.amount = 5

    def __init__(self):
        self.neopixels = self.NeoPixels()


hardware = Hardware()
