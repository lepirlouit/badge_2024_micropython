import machine
import time
import lvgl_esp32
import lvgl as lv

from fri3d.badge.hardware import hardware_pinout
from fri3d.badge import leds, display
from fri3d.buttons_indev import read_buttons

def demo(np):
    n = np.n

    # cycle
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 0)
        np[i % n] = (255, 255, 255)
        np.write()
        time.sleep_ms(25)

    # bounce
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 128)
        if (i // n) % 2 == 0:
            np[i % n] = (0, 0, 0)
        else:
            np[n - 1 - (i % n)] = (0, 0, 0)
        np.write()
        time.sleep_ms(60)

    # fade in/out
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (val, 0, 0)
        np.write()

    # clear
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()


# Initialize the screen
wrapper = lvgl_esp32.Wrapper(display)
wrapper.init()

indev_drv = lv.indev_create()
indev_drv.set_read_cb(read_buttons)
indev_drv.set_display(display)
indev_drv.enable(True)

# We check some inputs at boot to see if we need to boot in a special mode
repl_pin = machine.Pin(hardware_pinout.pinout_sao.gpio2, machine.Pin.IN, machine.Pin.PULL_UP)


if repl_pin.value() == 0:
    print("Detected REPL pin active, dropping into REPL")

else:

    print("Boot complete, starting application")
    demo(leds)

    screen = lv.screen_active()
    screen.set_style_bg_color(lv.palette_darken(lv.PALETTE.GREY, 4), lv.PART.MAIN)

    label = lv.label(screen)
    label.set_text("Hello world from MicroPython")
    label.set_style_text_color(lv.color_hex(0xffffff), lv.PART.MAIN)
    label.align(lv.ALIGN.CENTER, 0, 0)

    a = lv.anim_t()
    a.init()
    a.set_var(label)
    a.set_values(10, 50)
    a.set_duration(1000)
    a.set_playback_delay(100)
    a.set_playback_duration(300)
    a.set_repeat_delay(500)
    a.set_repeat_count(lv.ANIM_REPEAT_INFINITE)
    a.set_path_cb(lv.anim_t.path_ease_in_out)
    a.set_custom_exec_cb(lambda _, v: label.set_y(v))
    a.start()

    while True:
        lv.timer_handler_run_in_period(5)
