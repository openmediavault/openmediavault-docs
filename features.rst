Features
======
System
-----

General settings
----
**General settings:** Change |webui| listening port, SSL and force SSL. Change admin password

**Notification system:** Integrated into several services in the form of email, these include scheduled tasks, services monitoring, SMART, MDADM and cron-apt. Since |omv| 3.0 is possible to add third party notification systems by using scripts, more information `here <https://github.com/openmediavault/openmediavault/blob/master/deb/openmediavault/usr/share/openmediavault/notification/sink.d/README>`_ and an `example <https://forum.openmediavault.org/index.php/Thread/14919-GUIDE-Use-Telegram-as-notification-service/>`_.

**Network configuration:** The webUI provides configuration options for ethernet, wifi (only WPA/WPA2 supported), bond and vlan interfaces. This also includes a panel for firewall configuration.

**Certificates:** Create or import existing SSL and SSH certificates. This certificates can by used for securing the webUI or SSH access. Plugins can use the backend framework to select the available certificates.

**Power Management:** Scheduled power management for hibernation (s5), suspend (s3), shutdown and/or reboot.

**Service Discovery:** Using avahi-daemon is possible to announce the following services SAMBA, NFS, AFP, FTP, web admin panel, to any Linux desktop with file browser that supports it (GNOME, KDE or XFCE for example). OS X can recognise AFP and SAMBA services in the Finder sidebar. To announce SMB to windows clients, samba uses NetBios, not avahi.

**Scheduled Tasks:** Based on cron and anacron the webUI can define tasks to run commands or custom scripts.

**Update Manager:** Display all available package upgrades.

Storage
----

**S.M.A.R.T.:** Based on smartmontools, It can display advanced information of S.M.A.R.T values in the webUI. It can also schedule health tests as well as send notifications when smart attirbutes values change.

**RAID Management:** Based on the well known mdadm utility, you can create raid arrays in different configurations. Levels available are linear, 0, 1, 10, 5 and 6. Disks can be removed or array expanded using the web panel

**File Systems:** Volume formatting and mounting of disks or arrays.

**LVM:** Enhanced by the LVM2 plugin, the system has the capability of formatting disks or partitions as LVM that can be used in volume groups to create logical partitions.

Access Right Management
----

**Users:** User and group managing. Using privileges is possible to restrict access/login to shares on network sharing services (FTP, Samba and AFP) without interfering Unix permissions.

**Groups:** Create and manage custom groups. System groups cannot be manipulated here.

**Shared Folders:** Simple shared folder administration. Within this section is also possible to assign ACLs and/or privileges to the shared folders.

Services
----


**SMB/CIFS:** SMB sharing protocol using samba as standalone server by default.

**FTP:** Service based on proftpd. Intended for accessing shares from remote locations.

**RSync:** Server daemon. Shared folders can be defined as rsync modules. With scheduled tasks, rsync client can be configured for push and/or pull jobs.

**NFS:** Network file system protocol.

**SSH:** Remote shell access with SFTP configured by default. `Guide <https://forum.openmediavault.org/index.php/Thread/7822-GUIDE-Enable-SSH-with-Public-Key-Authentication-Securing-remote-webUI-access-to/>`_ on how to configure ssh in |omv|.

**TFTP:** A basic configuration panel is provided. This can complement a PXE server to deploy local network installations.

.. note::

	In |omv| version 4 the TFTP has been removed from core, and it now can be installed as an official plugin.

Diagnostics
----
**Dashboard:** By default the server comes with four information widgets. Network interfaces, System, Filesystem and service/daemon status.

**System information:** The panel displays four tabs with system information generated from top and usage graphs from rrdcached.

**System Logs:** Interface to view and download logs from syslog, boot, message, auth, ftp, rsync and samba. Plugins can attach their logs here using the framework.

**Services:** View status (enabled/disabled and running/not running) of services. Detailed information is provided by default for Samba, FTP and SSH. Plugins can use this tab to integrate their service information.
