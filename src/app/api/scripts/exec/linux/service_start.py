from ....common.bash_utils import run_bash

def exec_linux_service_start(device_config, parameter):
    service = parameter.split(".")[1]
    return run_bash("sudo systemctl start " + service, device_config)