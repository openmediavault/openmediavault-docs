Advanced Configuration
=========

OpenMediaVault is not a replacement for webmin, where you can configure all options in the web interface. Options are already preconfigured to make it easier for the average user to install and start using the NAS server.

As mentioned before in the FAQ OpenMediaVault takes full control of some services, making difficult to intervene configuration files. Changes manually added to configuration files will eventually rewritten at some stage by the system. The list of common files not to intervene is listed :doc:`here <various/conffiles>`

To overcome this there are some options available to modify some of the default OpenMediaVault configuration options and values, like the use of environmental variables

Environmental Variables
----
The web UI cannot provide access to ALL the configuration aspects of a complex system like OpenMediaVault. However, the system allows to change some advanced settings through the use of environment variables. To set or change these variables, login to you OpenMediaVault system using SSH and edit the file:

:file:`/etc/default/openmediavault`

Put the variable you want to change at the end of the file with the new value. Ensure the value is declared with double quotes

For example we are going to change the default sftp server for SSH service.

:code:`OMV_SSHD_SUBSYSTEM_SFTP=“/usr/lib/openssh/sftp-server”`

Make your changes, save, restart engined service openmediavault-engined restart and run omv-mkconf ssh, finally reload the SSH service via webUI or systemd

The list of all available environment variables can be found here

The list of environmental variables used for /etc/fstab filesystem with the defaults options and how to used them is described here

The mkconf folder
----

The other advanced configuration is the use of :code:`mkconf/{service}.d/` folder type

The mkconf scripts bundled in openmediavault core and plugins are in :code:`/usr/share/openmediavault/mkconf/{service}.d/` folder. Those scripts are executed by run-parts in alphabetical order when a change is done in the webUI so the configuration is piped to the corresponding .conf file on their respective service.

These scripts are useful for placing extra configurations for services in a way that server will not overwrite the files every time you change something in the webUI.