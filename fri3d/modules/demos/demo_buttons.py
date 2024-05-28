import time

from fri3d.badge import buttons
from fri3d.badge import joystick


if __name__ == "__main__":

    if 'x' in joystick and 'y' in joystick:
        analog_joystick = True
        c = joystick['x'].calibrate_center()
        print("x calibrate: ", c)

        c = joystick['y'].calibrate_center()
        print("y calibrate: ", c)

    for _ in range(100):
        values = {}
        if analog_joystick:
            values['j_x'] = joystick['x'].read()
            values['j_y'] = joystick['y'].read()
        
        for b in buttons:
            values[b] = buttons[b].value()

        print(f"{values=}")

        time.sleep(0.1)
