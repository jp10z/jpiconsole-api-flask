from ....common.bash_utils import run_bash

def stats_linux_uptime(device_config):
    result = int(float(run_bash("cat /proc/uptime", device_config).split()[0]))
    day = result // (24 * 3600)
    hour = result // 3600
    hour = hour - day * 24
    if hour < 10:
        hour = "0" + str(hour)
    result %= 3600
    minutes = result // 60
    if minutes < 10:
        minutes = "0" + str(minutes)
    result %= 60
    return str(day) + " days, " + str(hour) + ":" + str(minutes)