import esp32
import machine


def persist():
    esp32.Partition.mark_app_valid_cancel_rollback()


def main_menu():
    nvs = esp32.NVS('fri3d.sys')
    boot_id = nvs.get_i32('boot_partition')

    partition = esp32.Partition.find(label=f'ota_{boot_id}')[0]
    partition.set_boot()
    machine.reset()
