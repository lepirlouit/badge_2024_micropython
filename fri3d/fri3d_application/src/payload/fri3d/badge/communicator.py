from micropython import const
from fri3d.badge.hardware import hardware_communicator
from .expansion import Expansion


HID_REPORT_SIZE = const(8)

class Communicator(Expansion):
    def __init__(self):
        super().__init__()

        self._use_i2c = False
        if self.i2c and hardware_communicator.i2c_address in self.i2c.scan():
            # communicator detected
            self._use_i2c = True
        elif self.uart:
            self.uart.init(
                baudrate=hardware_communicator.baudrate,
                bits=hardware_communicator.bits,
                parity=hardware_communicator.parity,
                stop=hardware_communicator.stop
            )

    def get_first_key(self):
        report = None
        if self._use_i2c:
            report = self.i2c.readfrom(hardware_communicator.i2c_address, HID_REPORT_SIZE)
        elif self.uart:
            report = self.uart.read(HID_REPORT_SIZE)
        if report and len(report) == HID_REPORT_SIZE:
            return report[2]


communicator = Communicator()
