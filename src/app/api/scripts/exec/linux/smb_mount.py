from ....common.bash_utils import run_bash, run_bash_bl
from .....common.config_controller import get_device_smb_config

def exec_linux_smb_mount(device_config, parameter):
    smb_id = parameter.split(".")[1]
    usb_config = get_device_smb_config(device_config["id"], smb_id)
    if usb_config == "not found":
        return "smb_id not found"
    else:
        mount_point = usb_config["mount_point"]
        path = usb_config["path"]
        user = usb_config["user"]
        password = usb_config["password"]
        permissions = usb_config["permissions"]
        extra = ""
        if permissions == "user":
            extra = ",uid=$(id -u),gid=$(id -g)"
        return run_bash(
            "sudo mount -t cifs -o username=\"" + user +
            "\",password=\"" + password +
            "\"" + extra +
            " \"" + path +
            "\" \"" + mount_point +"\"", device_config)