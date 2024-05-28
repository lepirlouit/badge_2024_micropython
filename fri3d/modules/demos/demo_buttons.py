import time

from fri3d.badge import button_a, button_b, button_x, button_y, button_menu, button_start
from fri3d.badge import joystick_axis_x, joystick_axis_y


if __name__ == "__main__":

    try:
        c = joystick_axis_x.calibrate_center()
        print("x calibrate: ", c)

        c = joystick_axis_y.calibrate_center()
        print("y calibrate: ", c)

        for _ in range(100):
            j_x = joystick_axis_x.read()
            j_y = joystick_axis_y.read()
            a = button_a.value()
            b = button_b.value()
            x = button_x.value()
            y = button_y.value()
            menu = button_menu.value()
            start = button_start.value()

            print(f"{j_x=}, {j_y=}, {a=}, {b=}, {x=}, {y=}, {menu=}, {start=}")

            time.sleep(0.1)

    except KeyboardInterrupt:
        joystick_axis_x.deinit()
        joystick_axis_y.deinit()
        pass
