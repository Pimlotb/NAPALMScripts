# Filename:                     configCommitDiscard.py
# Command to run the program:   python configCommitDiscard.py

# Import dependencies
from napalm import get_network_driver
import json

driver = get_network_driver('ios')
device = driver('10.1.1.20', 'admin', '******')
device.open()

device.load_merge_candidate(filename='floorsw.cfg')
print(device.compare_config())

if len(device.compare_config()) >0:
    choice = input("\n Would you like to commit these changes [yN]: ")
    if choice == 'y':
        print('Committing....')
        device.commit_config()
        choice = input("\n Would you like to rollback these changes [yN]: ")
        if choice == 'y':
            print('Commiting ....')
            device.commit_config()

    else:
        print("Not Commiting this change")
        device.discard_config()
else:
    print('No diff!')

device.close()
print('Done')

