from fri3d.badge.hardware import hardware_buttons
from fri3d.badge.hardware import hardware_capabilities

from .debounced_button import DebouncedButton

buttons = {}


for n in hardware_buttons.buttons:
    pin = getattr(hardware_buttons.pinout, 'pin_button_' + n)
    buttons[n] = DebouncedButton(pin)


if hasattr(hardware_capabilities, 'has_gameon') and hardware_capabilities.has_gameon:
    from fri3d.badge.hardware import hardware_gameon

    for n in hardware_gameon.buttons:
        pin = getattr(hardware_gameon.pinout, 'pin_button_' + n)
        buttons[n] = DebouncedButton(pin)

