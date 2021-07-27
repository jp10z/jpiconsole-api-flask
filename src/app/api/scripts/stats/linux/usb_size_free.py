from ....common.bash_utils import run_bash
from .....common.config_controller import get_device_usb_config

def stats_linux_usb_size_free(device_config, parameter):
    usb_id = parameter.split(".")[1]
    usb_config = get_device_usb_config(device_config["id"], usb_id)
    if str(usb_config).startswith("ERROR:"):
        return usb_config
    label = usb_config["label"]
    if label != "":
        result = run_bash("lsblk -o KNAME,LABEL | grep " + label, device_config)
    else:
        result = get_device_usb_config(device_config["id"], usb_id)["kname"].replace("/dev/", "")
    if result != "":
        result = "/dev/" + result.split()[0]
        result = run_bash("df -m | grep " + result, device_config)
        if result != "":
            result = result.split()
            return int(result[3])
        else:
            return "not_mounted"
    else:
        return "not_found"