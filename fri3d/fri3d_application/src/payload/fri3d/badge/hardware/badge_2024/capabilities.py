class HardwareCapabilities:
    def __init__(self):
        self.game_on = False
        self.joystick = True
        self.onboard_buttons = True
        self.i2c = True
        self.i2s = True
        self.uart = True


hardware_capabilities = HardwareCapabilities()
