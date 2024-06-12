import lvgl as lv

from fri3d.badge.buttons import buttons
from fri3d.badge.joystick import joystick

from .log import logger


class Indev:
    """
    A             : LV_KEY_ENTER
    B             : LV_KEY_ESC
    X | P0        : LV_KEY_NEXT
    Y | P1        : LV_KEY_PREV

    MENU | SELECT : LV_KEY_HOME
    START         : LV_KEY_END

    JOY_UP        : LV_KEY_UP
    JOY_DOWN      : LV_KEY_DOWN
    JOY_LEFT      : LV_KEY_LEFT
    JOY_RIGHT     : LV_KEY_RIGHT
    """
    def __init__(self) -> None:
        
        # remember the last key pressed reported to lvgl
        self.last_key_pressed = None
        
        self.assign_buttons()

        indev_drv = lv.indev_create()
        indev_drv.set_type(lv.INDEV_TYPE.KEYPAD)
        indev_drv.set_read_cb(self.read_buttons)
        indev_drv.set_display(lv.display_get_default())
        self._grp = lv.group_create()
        self._grp.set_default()
        indev_drv.set_group(self._grp)
        indev_drv.enable(True)

        self._indev_drv = indev_drv


    def assign_buttons(self):
        if 'a' in buttons:
            self.button_enter = buttons['a']

        if 'b' in buttons:
            self.button_esc = buttons['b']

        if 'x' in buttons:
            self.button_next = buttons['x']
        elif 'p0' in buttons:
            self.button_next = buttons['p0']

        if 'y' in buttons:
            self.button_prev = buttons['y']
        if 'p1' in buttons:
            self.button_prev = buttons['p1']

        if 'menu' in buttons:
            self.button_home = buttons['menu']
        elif 'select' in buttons:
            self.button_home = buttons['select']

        if 'start' in buttons:
            self.button_end = buttons['start']

        self.analog_joystick = True if 'x' in joystick and 'y' in joystick else False

    def read_buttons(self, drv, data):
        keys_pressed = []

        if self.button_enter.value():
            keys_pressed.append(lv.KEY.ENTER)
        if self.button_esc.value():
            keys_pressed.append(lv.KEY.ESC)
        if self.button_next.value():
            keys_pressed.append(lv.KEY.NEXT)
        if self.button_prev.value():
            keys_pressed.append(lv.KEY.PREV)
        if self.button_home.value():
            keys_pressed.append(lv.KEY.HOME)
        if self.button_end.value():
            keys_pressed.append(lv.KEY.END)

        if self.analog_joystick:
            j_x = joystick['x'].read()
            if j_x > 0:
                keys_pressed.append(lv.KEY.RIGHT)
            if j_x < 0:
                keys_pressed.append(lv.KEY.LEFT)

            j_y = joystick['y'].read()
            if j_y > 0:
                keys_pressed.append(lv.KEY.UP)
            if j_y < 0:
                keys_pressed.append(lv.KEY.DOWN)
        else:
            if buttons['up'].value():
                keys_pressed.append(lv.KEY.UP)
            if buttons['left'].value():
                keys_pressed.append(lv.KEY.LEFT)
            if buttons['down'].value():
                keys_pressed.append(lv.KEY.DOWN)
            if buttons['right'].value():
                keys_pressed.append(lv.KEY.RIGHT)


        if self.last_key_pressed is not None:
            if self.last_key_pressed not in keys_pressed:
                # last key released
                # logger.debug(f"released {last_key_pressed}")

                data.key = self.last_key_pressed
                data.state = lv.INDEV_STATE.RELEASED
                self.last_key_pressed = None

                if keys_pressed:
                    # another key is pressed
                    data.continue_reading = True
                else:
                    data.continue_reading = False
            else:
                # last key still pressed
                data.key = self.last_key_pressed
                data.state = lv.INDEV_STATE.PRESSED
                data.continue_reading = False
        else:
            if keys_pressed:
                # can only send 1 key pressed to lvgl, send first
                key_pressed = keys_pressed.pop(0)

                # logger.debug(f"pressed {key_pressed}")

                data.key = key_pressed
                data.state = lv.INDEV_STATE.PRESSED
                data.continue_reading = False

                self.last_key_pressed = key_pressed
