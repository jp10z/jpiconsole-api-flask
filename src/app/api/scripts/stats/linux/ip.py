from ....common.bash_utils import run_bash

def stats_linux_ip(device_config, parameter):
    interface = parameter.split(".")[1]
    result = run_bash("ip -4 addr show " + interface + " | grep inet", device_config)
    if "does not exist" in result:
        return "interface " + interface + " does not exist"
    elif "" == result:
        return "no_ip"
    else:
        return result.split()[1].split("/")[0]