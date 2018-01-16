Configuration files
=====


The following is the list of file you should not edit by hand. |omv| has complete control over these files and any changes will be overwrriten on demand.

**Filesystem:** :file:`/etc/fstab` This file contains all mount entries, physical and network ones. |omv| identifies them by using the «openmediavault» tags, in between those you should not delete entries or change options. Any new mount drive or network entry will rewrite fstab in between those lines, reverting any changes you have done. Please refer here for advanced editing options of fstab.

**Network:** :file:`/etc/network/interfaces` The explanation is already in the :doc:`FAQ </FAQ>`

**NGINX:** /etc/nginx/openmediavault-webgui.d/security.conf,/etc/nginx/sites-enabled/openmediavault-webgui,

**PHP5-FPM:** :file:`/etc/php5/fpm/pool.d/openmediavault-webgui.conf`

**POSTFIX:** Any configuration files by postfix should not be edited unless you know what you are doing. You run the risk of breaking the notification system.

**MONIT:** :file:`/etc/monit/monitrc,/etc/monit/conf.d/openmediavault-{servicename}`

**SAMBA:** :file:`/etc/samba/smb.conf` Use the extra options in general or by share to define options not present in the webUI.

**FTP:** :file:`/etc/proftpd/proftpd.conf` Use the extra options in general or per share to add directives not available in the webUI.

**NFS:** :file:`/etc/exports` Use environmental variables if you want to change the pseudo root filesystem options for NFSv4.

**APT**
	- :file:`/etc/apt/sources.list` This is default debian repository server file. Read more information here.
	- :file:`/etc/apt/sources.list.d/openmediavault.list` This is the server package repository for OMV.
