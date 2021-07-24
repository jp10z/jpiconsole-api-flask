from ....common.bash_utils import run_bash, run_bash_bl
from .....common.config_controller import get_device_smb_config

def exec_linux_smb_umount(device_config, parameter):
    smb_id = parameter.split(".")[1]
    mount_point = get_device_smb_config(device_config["id"], smb_id)
    if mount_point == "not found":
        return "smb_id not found"
    else:
        mount_point = mount_point["mount_point"]
    result = run_bash("sudo umount " + mount_point, device_config)
    return result