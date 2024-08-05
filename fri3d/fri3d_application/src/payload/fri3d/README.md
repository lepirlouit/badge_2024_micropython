# Fri3d MicroPython firmware

This is the Fri3d MicroPython firmware. In here you will not only find modules to talk to some of the hardware of the
badge. You can also find the start of what was meant to be the main launcher of the badges.

Development was discontinued and moved to pure C++ code because of issues mostly related to LVGL, OTA and SD card
access. The code is still here however, so you can use it if you want, if you keep it pure LVGL, you should be fine.

Who knows, maybe one day it gets picked up again when MicroPython has better compatibility on ESP32?

Should you want to launch the main firmware and have a look yourself, you can do this:

```python
from fri3d.application import Application

app_main = Application()
app_main.run()
```

You can also put this in main.py if you want to launch it every time.

You can then develop your own apps for inclusion in the launcher. Have a look at `user/example_app` for this.
