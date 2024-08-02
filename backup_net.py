import os
import datetime
from netmiko import ConnectHandler

backup_folder = 'config_backups'
os.makedirs(backup_folder, exist_ok=True)

device = {
    'device_type': 'cisco_ios',
    'ip': 'your_router_ip',
    'username': 'admin',
    'password': 'admin',
}

connection = ConnectHandler(**device)
config_output = connection.send_command('show run')

timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
filename = f"{backup_folder}/config_{timestamp}.txt"

with open(filename, 'w') as backup_file:
    backup_file.write(config_output)

connection.disconnect()
