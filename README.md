# NAPALMScripts
NAPALM - Network automation and programmability
abstraction layer with multi-vendor support

• Provides functions that allows:

• Configuration operations (commit or rollback)

• Retrieve state data from network devices

• Contains methods to establish connection to network devices

• Can work in conjunction with automation tools – Ansible

• Has support for various network OS:

• IOS, IOS-XR, NX-OS, JunOS, EOS, etc.

# NAPALM Operations

Replace – Allows users to replace the existing running configuration with
an entirely new configuration.

• Merge – Allows users to merge configuration changes from a file to the
running configuration on the device.

• Compare – Compare the newly proposed configuration with the existing
one. Only applies to replace operation and not for merge operation.

• Discard – Resets the merge configuration file to an empty file. Thus, not
allowing the new configuration to be applied on the device.

• Commit – Commits the proposed configuration to the network device. In
other words, used to deploy a staged configuration.

• Rollback – Rollback (revert back) the running configuration to the saved
configured prior to the last commit.
