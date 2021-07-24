from ....common.bash_utils import run_bash_bl

def stats_rut240_sms_list(device_config):
    result = run_bash_bl("gsmctl --sms --list all", device_config)
    sms_list = result.split("------------------------------")
    sms_sms = []
    for sms_i in sms_list:
        if sms_i != "\n":
            sms_lines = sms_i.split("\n")
            sms_lines[:] = [x for x in sms_lines if x]
            sms = {}
            sms["index"] = int(sms_lines[0].replace("Index: ", ""))
            sms["date"] = sms_lines[1].replace("Date: ", "")
            sms["sender"] = sms_lines[2].replace("Sender: ", "")
            sms["text"] = sms_lines[3].replace("Text: ", "")
            sms_sms.append(sms)
    return sms_sms