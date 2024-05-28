from .pinout import hardware_pinout


class HardwareButtons:
    def __init__(self):
        self.pinout = hardware_pinout.pinout_buttons
        self.buttons = ['boot']


hardware_buttons = HardwareButtons()