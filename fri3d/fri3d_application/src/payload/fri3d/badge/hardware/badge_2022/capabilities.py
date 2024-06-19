class HardwareCapabilities:
    def __init__(self):
        self.game_on = True
        self.joystick = False
        self.onboard_buttons = True
        self.i2c = True
        self.i2s = False
        self.uart = False


hardware_capabilities = HardwareCapabilities()
