# JPiConsole API FLask

jpiconsole-api-flask is an API that allows executing actions on the system on which it is installed or on remote systems

## Functions

This API has the following functions:

- Know the status of system elements, for example os, services, mount points, etc.
- Execute actions on the system, for example, mount drives, mount network services, start or stop local services, etc.
- Connect to other machines to obtain states and execute actions

## Requeriments

- OS GNU/Linux (Tested on ArchLinux, Debian10)
- Python3 and PIP
- Package `lsb_release` for lsb_release module
- Package `sshpass` for remote SSH connections
- Pip requeriments (requeriments.txt)

## API Call Example

URL: http://localhost:5001/api/stats

Metod: POST

Body JSON:

```json
{
	"device_id": "device_id",
	"parameters": [
        {
            "parameter": "Parameter.Sub-Parameter"
        },
		{
			"parameter": "lsb_release"
		},
		{
			"parameter": "docker_container_status.grafana"
		}
	]
}
```

## STATS Modules

### linux

|Parameters|Sub-Parameters|Info|
|-|-|-|
|lsb_release||Operating System Version|
|kernel||Kernel used and version of this|
|uptime||Time the system has been on|
|cpu_temp||CPU temperature (Raspberry compatible only)|
|ip|interface_name|Get the IP of an interface|
|service_status|service_name|Gets the status of a Systemd Service|
|docker_container_status|docker_container_name|Gets the state of a Docker Container, this being previously initialized|
|usb_kname|config_usb_id|Get the device path as /dev/...|
|usb_mount|config_usb_id|Gets the current mount point of the device, if it is not mounted it will say not_mounted|
|usb_size_total|config_usb_id|Gets the total size of the device in MB|
|usb_size_free|config_usb_id|Gets the free space of the device in MB|
|usb_size_used|config_usb_id|Gets the used space of the device in MB|
|usb_size_used_percent|config_usb_id|Gets the percentage of the device used in MB|
|smb_status|config_smb_id|Displays the mount status of SMB (Samba) service|

### rut240 (Router Modem Teltonika 240)

|Module|Sub-Parameters|Info|
|-|-|-|
|sim_status||Shows the status of the SIM inserted|
|sim_iccid||Shows the ICCID of the inserted SIM|
|router_temp||Shows the temperature of the router|
|connection_status||Shows the status of the signal connection|
|connection_link||Shows the status of the connection to the provider|
|connection_band||Shows the Band currently used|
|sms_list||Gets a json with the list of SMS received|

## EXEC Modules

### linux

|Module|Sub-Parameters|Info|
|-|-|-|
|usb_mount|config_usb_id|Mount a USB device|
|usb_umount|config_usb_id|Umount a USB device|
|smb_mount|config_smb_id|Mount a SMB network service|
|smb_umount|config_smb_id|Umount a SMB network service|
|service_start|service_name|Start a systemd service|
|service_stop|service_name|Stop a systemd service|
|docker_container_start|docker_container_name|Start a previously initialized Docker container|
|docker_container_stop|docker_container_name|Stop a previously initialized Docker container|