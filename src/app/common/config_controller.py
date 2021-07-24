import json

config_file_path = "config.json"

def get_config_data():
    config_file = open(config_file_path,)
    config_file_data = json.load(config_file)    
    config_file.close()
    return config_file_data

def get_enviroment_host():
    config_file_data = get_config_data()
    return config_file_data["enviroment"]["host"]

def get_enviroment_port():
    config_file_data = get_config_data()
    return config_file_data["enviroment"]["port"]

def get_enviroment_debug():
    config_file_data = get_config_data()
    return config_file_data["enviroment"]["debug"]

def get_device_config(device_id):
    config_file_data = get_config_data()
    for device in config_file_data["devices"]:
        if device_id == device["id"]:
            return device
    return "not_found"

def get_device_usb_config(device_id, usb_id):
    config_file_data = get_config_data()
    for device in config_file_data["devices"]:
        if device_id == device["id"]:
            for usb in device["usb"]:
                if usb_id == usb["id"]:
                    return usb
    return "not_found"

def get_device_smb_config(device_id, smb_id):
    config_file_data = get_config_data()
    for device in config_file_data["devices"]:
        if device_id == device["id"]:
            for smb in device["smb"]:
                if smb_id == smb["id"]:
                    return smb
    return "not_found"