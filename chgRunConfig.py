# Filename:                     chgRunConfig.py
# Command to run the program:   python chgRunConfig.py

# Import dependencies

from napalm import get_network_driver
import json

driver = get_network_driver('ios')
device = driver('10.1.1.20', 'admin', '******')
device.open()
device.load_merge_candidate(config='interface GigabitEthernet1\n ip address 10.0.0.8 255.255.255.0\n no shutdown\n end\n')
print(device.compare_config())
device.commit_config()
device.close()