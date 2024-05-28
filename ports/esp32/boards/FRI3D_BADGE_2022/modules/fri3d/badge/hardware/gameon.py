from .pinout import hardware_pinout


class HardwareGameon:
    def __init__(self):
        self.pinout = hardware_pinout.pinout_gameon
        self.buttons = ['a', 'b', 'start', 'select', 'p0', 'p1', 'up', 'left', 'down', 'right']


hardware_gameon = HardwareGameon()