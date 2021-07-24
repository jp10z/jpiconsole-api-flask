from ....common.bash_utils import run_bash

def stats_linux_cpu_temp(device_config):
    result = run_bash("vcgencmd measure_temp | egrep -o '[0-9]*\\.[0-9]*'", device_config)
    result = result.replace("temp=", "").replace("'C", "")
    if "orden no encontrada" in result:
        return "command vcgen error"
    else:
        return float(result)