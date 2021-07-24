from ....common.bash_utils import run_bash
from .....common.config_controller import get_device_usb_config

def stats_linux_usb_kname(device_config, parameter):
    usb_id = parameter.split(".")[1]
    label = get_device_usb_config(device_config["id"], usb_id)
    if label != "not_found":
        label = get_device_usb_config(device_config["id"], usb_id)["label"]
    else:
        return "not_found"
    if label != "":
        result = run_bash("lsblk -o KNAME,LABEL | grep " + label, device_config)
    else:
        result = get_device_usb_config(device_config["id"], usb_id)["kname"].replace("/dev/", "")
    if result != "":
        return "/dev/" + result.split()[0]
    else:
        return "not_found"