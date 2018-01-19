Features
========

System
------

General settings
----------------

**General settings:** Change |webui| listening port, SSL and force SSL. Change admin password

**Notification system:** Integrated into several services in the form of email using Postfix [1]_ backend as MTA, these include scheduled tasks, services monitoring, S.M.A.R.T., MDADM and cron-apt. Since |omv| 3.0 is possible to add also third party notification systems by using scripts, more information `here <https://github.com/openmediavault/openmediavault/blob/master/deb/openmediavault/usr/share/openmediavault/notification/sink.d/README>`_ and real example on how to use it `here <https://forum.openmediavault.org/index.php/Thread/14919-GUIDE-Use-Telegram-as-notification-service/>`_.

**Network configuration:** The web interface provides configuration options for ethernet, WiFi (only WPA/WPA2 supported), bond and vlan interfaces. This also includes a panel for firewall configuration.

**Certificates:** Create or import existing SSL and SSH certificates. This certificates can by used for securing the |webui| or SSH access. Plugins can use the backend framework to select the available certificates.

**Power Management:** Scheduled power management for hibernation (S5), suspend (S3), shutdown and/or reboot.

**Service Discovery:** Using avahi-daemon [2]_ is possible to announce the following services Samba, NFS, AFP, FTP, web admin panel, to any Linux desktop with file browser that supports it (GNOME, KDE or XFCE for example). OS X can recognise AFP and Samba services in the Finder sidebar. To announce SMB to windows clients, samba uses NetBios, not avahi.

**Scheduled Tasks:** Based on cron the webUI can define tasks for running specific commands or custom scripts at certain time or regular intervals.

**Update Manager:** Displays all available packages for upgrade.

Storage
-------

**S.M.A.R.T.:** Based on smartmontools [3]_, It can display advanced information of S.M.A.R.T values in the webUI. It can also schedule health tests as well as send notifications when S.M.A.R.T. attributes values change.

**RAID Management:** Based linux RAID [4]_, you can create arrays in different 6 different configurations. Levels available are linear, 0, 1, 10, 5 and 6. The array can have disks removed or expanded using the web interface.

**File Systems:** Volume format, device mmount and unmount. More information :doc:`here </various/filesystems>`.

**LVM:** Enhanced by the LVM2 plugin, the system has the capability of formatting disks or partitions as LVM that can be used in volume groups to create logical partitions.

Access Right Management
-----------------------

**Users:** User and group managing. Using privileges is possible to restrict access/login to shares on network sharing services (FTP, Samba and AFP) without interfering Unix permissions.

**Groups:** Create and manage custom groups. System groups cannot be manipulated here.

**Shared Folders:** Simple shared folder administration. Within this section is also possible to assign ACLs and/or privileges to the shared folders.

Services
--------

**SMB/CIFS:** SMB sharing protocol using Samba [5]_ as standalone server by default.

**FTP:** Service based on proftpd [6]_. Intended for accessing shares from remote or local.

**RSync:** Server daemon. Shared folders can be defined as rsyncd modules. With scheduled tasks, rsync client can be configured for push or pull jobs.

**NFS:** Network file system protocol [7]_.

**SSH:** Remote shell access using openssh [8]_.

**TFTP:** A basic configuration panel is provided. This can complement a PXE server to deploy local network installations.

.. note::

	In |omv| version 4 the TFTP has been removed from core, and now it can be installed as an official plugin.

Diagnostics
-----------

**Dashboard:** By default the server comes with four information widgets. Network interfaces, System, Filesystem and service/daemon status. The dashboard panel can have widgets added using the plugin framework.

**System information:** The panel displays four tabs with system information and statistics graphs.

**System Logs:** Interface to view and download logs from syslog, journalctl, message, auth, ftp, rsync and samba. Plugins can attach their logs here using the framework.

**Services:** View status (enabled/disabled and running/not running) of services. Detailed information is provided by default for Samba, FTP and SSH. Plugins can use this tab to integrate their service information also.

.. [1] http://postfix.org
.. [2] https://www.avahi.org/
.. [3] https://www.smartmontools.org/
.. [4] https://raid.wiki.kernel.org/index.php/RAID_setup
.. [5] https://www.samba.org/
.. [6] http://www.proftpd.org/
.. [7] http://nfs.sourceforge.net/
.. [8] https://www.openssh.com/
