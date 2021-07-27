from ....common.bash_utils import run_bash_bl
from .....common.config_controller import get_device_smb_config

def stats_linux_smb_status(device_config, parameter):
    smb_id = parameter.split(".")[1]
    smb_config = get_device_smb_config(device_config["id"], smb_id)
    if str(smb_config).startswith("ERROR: "):
        return smb_config
    path = smb_config["path"]
    result = run_bash_bl("findmnt -o SOURCE -t cifs", device_config).split("\n")
    for mnt in result:
        if path == mnt:
            return "mounted"
    return "not_mounted"