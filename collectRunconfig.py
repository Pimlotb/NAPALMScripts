# Filename:                     collectRunconfig.py
# Command to run the program:   python collectRunconfig.py

# Import dependencies

from napalm import get_network_driver
import json

# Connect to Cisco Switch and collect some basic data about it
# Using get_config to read running config
driver = get_network_driver('ios')
device = driver('10.1.1.20', 'admin', '******')
device.open()
print(json.dumps(device.get_config(),['running'])
device.close()
