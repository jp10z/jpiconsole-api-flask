from ....common.bash_utils import run_bash
from .....common.config_controller import get_device_usb_config

def exec_linux_usb_mount(device_config, parameter):
    usb_id = parameter.split(".")[1]
    usb_config = get_device_usb_config(device_config["id"], usb_id)
    label = usb_config["label"]
    if label != "":
        result = run_bash("lsblk -o KNAME,LABEL | grep " + label, device_config)
    else:
        result = usb_config["kname"].replace("/dev/", "")
    if result != "":
        result = "/dev/" + result.split()[0]
        return run_bash("sudo mount " + result + " \"" + usb_config["mount_point"] + "\"", device_config)
    else:
        return "ERROR: not_found"