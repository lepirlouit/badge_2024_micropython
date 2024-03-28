from st7789 import MADCTL_MV, BGR

from .pinout import hardware_pinout


class HardwareDisplay:
    def __init__(self):
        self.pinout = hardware_pinout.pinout_display
        self.width = 296
        self.height = 240
        self.rotation = 0
        self.inversion = False
        self.rotations = [(MADCTL_MV | BGR, 296, 240, 0, 0)]


hardware_display = HardwareDisplay()
