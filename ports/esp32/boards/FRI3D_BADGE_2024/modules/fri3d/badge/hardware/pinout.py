from machine import Pin


class HardwarePinout:
    class PinoutLEDS:
        def __init__(self):
            self.pin = Pin(12, Pin.OUT)

    class PinoutSPI:
        def __init__(self):
            self.pin_mosi = Pin(6, Pin.OUT)
            self.pin_miso = Pin(8, Pin.IN)
            self.pin_sck = Pin(7, Pin.OUT)

    class PinoutDisplay:
        def __init__(self):
            self.pin_rst = 48
            self.pin_dc = 4
            self.pin_cs = 5

    def __init__(self):
        self.pinout_leds = self.PinoutLEDS()
        self.pinout_spi = self.PinoutSPI()
        self.pinout_display = self.PinoutDisplay()


hardware_pinout = HardwarePinout()
