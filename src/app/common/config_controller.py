import json
import os

config_file_path = "config.json"

def validate_config_file():
    if os.path.exists(config_file_path):
        return "OK"
    else:
        return "ERROR: config.json not exists"

def get_config_data():
    if validate_config_file() == "OK":
        config_file = open(config_file_path,)
        config_file_data = json.load(config_file)    
        config_file.close()
        return config_file_data
    else:
        return validate_config_file()

def get_enviroment_host():
    config_file_data = get_config_data()
    if str(config_file_data).startswith("ERROR:") == False:
        return config_file_data["enviroment"]["host"]
    else:
        return config_file_data

def get_enviroment_port():
    config_file_data = get_config_data()
    if str(config_file_data).startswith("ERROR:") == False:
        return config_file_data["enviroment"]["port"]
    else:
        return config_file_data

def get_enviroment_debug():
    config_file_data = get_config_data()
    if str(config_file_data).startswith("ERROR:") == False:
        return config_file_data["enviroment"]["debug"]
    else:
        return config_file_data

def get_device_config(device_id):
    config_file_data = get_config_data()
    if str(config_file_data).startswith("ERROR:") == False:
        for device in config_file_data["devices"]:
            if device_id == device["id"]:
                return device
        return "ERROR: device_id not found in config.json"
    else:
            return config_file_data

def get_device_usb_config(device_id, usb_id):
    device_config = get_device_config(device_id)
    if str(device_config).startswith("ERROR:") == False:
        for usb_config in device_config["usb"]:
            if usb_id == usb_config["id"]:
                return usb_config
        return "ERROR: usb_id not found in device config"
    else:
        return device_config

def get_device_smb_config(device_id, smb_id):
    device_config = get_device_config(device_id)
    if str(device_config).startswith("ERROR:") == False:
        for smb_config in device_config["smb"]:
            if smb_id == smb_config["id"]:
                return smb_config
        return "ERROR: smb_id not found in device config"
    else:
        return device_config