from machine import Pin


class HardwarePinout:
    class PinoutLEDS:
        def __init__(self):
            self.pin = Pin(2, Pin.OUT)

    class PinoutSPI:
        def __init__(self):
            self.pin_mosi = Pin(23, Pin.OUT)
            self.pin_miso = Pin(19, Pin.IN)
            self.pin_sck = Pin(18, Pin.OUT)

    class PinoutDisplay:
        def __init__(self):
            self.pin_rst = 32
            self.pin_dc = 33
            self.pin_cs = 5

    def __init__(self):
        self.pinout_leds = self.PinoutLEDS()
        self.pinout_spi = self.PinoutSPI()
        self.pinout_display = self.PinoutDisplay()


hardware_pinout = HardwarePinout()
