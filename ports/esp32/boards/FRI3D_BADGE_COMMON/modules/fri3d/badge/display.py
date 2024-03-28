from st7789 import ST7789

from fri3d.badge.hardware import hardware_display

from .spi import spi

display = ST7789(
    spi=spi,
    width=hardware_display.width,
    height=hardware_display.height,
    rotation=hardware_display.rotation,
    rotations=hardware_display.rotations,
    reset=hardware_display.pinout.pin_rst,
    dc=hardware_display.pinout.pin_dc,
    cs=hardware_display.pinout.pin_cs,
    inversion=hardware_display.inversion,
    buffer_size=hardware_display.width * hardware_display.height * 2,
)

display.init()
