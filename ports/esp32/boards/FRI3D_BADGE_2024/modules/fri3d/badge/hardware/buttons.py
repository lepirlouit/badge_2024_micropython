from .pinout import hardware_pinout


class HardwareButtons:
    def __init__(self):
        self.pinout = hardware_pinout.pinout_buttons
        self.buttons = ['a', 'b', 'x', 'y', 'menu', 'start']


hardware_buttons = HardwareButtons()