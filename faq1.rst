FAQ
===

Frequently Asked Questions

:Question: What is OMV?**
:Answer: OMV is an abbreviation of |omv|.
..
:Q: **Is |omv| a fork of FreeNAS?**
:A:	No
..
:Q: **Does |omv| have drivers for my hardware?**
:A:	All module drivers are provided by the Debian standard kernel of oldstable release 8.9 (aka Jessie). This distribution ships with kernel 3.16 by default. You can optionally install the backport kernel 4.9. If your hardware is supported under Debian Jessie then is supported under OMV. te Jessie backport kernel 4.9 is the default kernel used by Stretch (Debian 9.3) at the moment, so it provides support for newer hardware.
..
:Q: **Can I use a usb flash drive (stick) for installing the system?**
:A:	Yes, but the installation does not have any optimizations to reduce writes into the OS disk. Your usb media will most likely start failing within a few weeks of usage. Most common symptom is basic command execution does not work, denied login, etc. More information `here <https://forum.openmediavault.org/index.php/Thread/6438-Tutorial-Experimental-Third-party-Plugin-available-Reducing-OMV-s-disk-writes-al/>`_

:Q: **What is the file `/etc/openmediavault/config.xml` for?**
:A:	Is the database configuration store file for |omv|. When a change is performed in the |webui|, the config value is stored and/or retrieve by rpc to/from this file. If this is a save change, then mkconf passes the value to the service configuration file and reloads the daemon in case is necessary.
..
:Q: **Can I upgrade to Debian Testing/Unstable (Debian Testing/Sid) or use Ubuntu as a base distribution?**
:A:	Yes you can. But you will end up most likely with a broken |webui| and possibly broken system. |omv| releases are heavily tight to their Debian base distro.
..
:Q: **I´ve lost the web interace password. How do I reset it?**
:A:	Simply connect via ssh to your server or login locally on your machine and type in: :command:`omv-firstaid`. There is an option to reset your password.
..
:Q: **Can I backup or restore and existing |omv| configuration?**
:A:	No. You can keep the file :file:`/etc/openmediavault/config.xml` for references purposes if you decide to go for a clean re-install.
..
:Q: **What is the default HTTP engine of openmediavault?**
:A:	NGINX. The last version of |omv| with Apache was 0.5 Sardoukar.
..
:Q: **Can I use Apache as HTTP engine?**
:A:	You can use it but is not supported. Eventually every |omv| package upgrade will activate NGINX again leaving you with a broken |webui|. You can run a parallel Apache instance to Nginx just make sure the ports are different otherwise your |omv| |webui| will not work.
..
:Q: **How can use the default HTTP engine to hold my own web page?**
:A:	Do not modify |omv| default NGINX files. You can place your website configurations at :file:`/etc/nginx/sites-available` and enable it with :command:`nginx_ensite <SITE>`. Read more information in the `NGINX documentation <http://nginx.org/en/docs/>`_.
..
:Q: **Why does the system rewrites a configuration file(s) that I have manually edited?**
:A:	OMV takes full control of some system services. This services include monit, ntp, samba, network, proftpd, nginx, php5-fpm, etc. Read :doc:`here </various/files>`.
..
:Q: **How can I modify an internal value of some service openmediavault has control over?**
:A:	Read :doc:`here <various/advset>` for advanced configurations.
..
:Q: **How can I modify or add a network configuration of :file:`/etc/network/interfaces` with some custom options the |webui| does not provide?**
:A:	The interfaces file is controlled by |omv|. To add network interfaces that are not configurable through the |webui| or other options not present, you need to use  :doc:`advanced settings <various/advset>`.
..
:Q: **Why my disks mount paths have a long alphanumeric number?**
:A:	The long number is called UUID, it is used by fstab to mount disks. This number is unique per filesystem (or at least unlikely possible that another filesystem comes with an identical one). This helps maintaing the mount points. The old linux way (sda1, sdb1, etc.) is not guaranteed that /sda1 is the same disk on next reboot. If you have trouble identiying them in terminal, you can always create a pool with symlinks to each file system with easy to remember names. This behaviour has been deprecated now in current omv releases including stable (Jessie). The default creation of mount paths is documented `here <https://github.com/openmediavault/openmediavault/blob/20ec529737e6eca2e1f98d0b3d1ade16a3c338e1/deb/openmediavault/usr/share/openmediavault/engined/rpc/filesystemmgmt.inc#L823-L833>`_.
..
:Q: **I don't have a data disk, and I want to use my OS disk for storing data?**
:A:	The default behaviour of |omv| is to act as NAS server, that means OS files are separated from data disks. You can use partitions in the same disk you use for OS and the system will recognise the partitions for formatting, mounting and to create shared folders. The current installer does not provide access to the partition manager, so you need to use a plain Debian iso then install |omv| on top and acommodate the partitions, or resize the partition after installing using Gparted or SystemRescueCd.
..
:Q: **Can I install openmediavault on top a running Debian system?**
:A:	Yes, but is not recommended that the running OS has a desktop environment installed.
..
:Q: **Which are the files that should not be edited by the user?**
:A:	There are several services that |omv| takes control of, The recommended list is here.
..
:Q: **What is the permissions/ownership of folders in openmediavault created by shared folders?**
:A:	The default is folders in ``2775`` mode, with ``root:users`` ownership. This means all users created in the |webui| can read, write to folders created by the system in the data drives using the default.
..
:Q: **Why are my filesystems mounted as noexec?**
:A:	This is a security measure to avoid the placement of malicious scripts in the shared folders. This will prevent any script execution in those paths, including compiling packages and binaries.
	If you need to remove the noexc flag, you need to use advanced settings.
..
:Q: **I need to delete a shared folder, why the delete button is greyed/disabled?**
:A:	Shared folder configurations can be used across different services. If you need to remove a shared folder configuration you need to unlink it from every service is attached to it before the delete button becomes available. At the moment there is no internal database backend that can display information about which service is holding which shares.
..
:Q: **What is the `omv-mkconf` command for?**
:A:	:command:`omv-mkconf` is a terminal console command that is used by the backend of |omv| to pipe directives and values to service configuration files. The arguments that :command:`omv-mkconf` accepts are related to the name of the service it configures. Type :command:`omv-mkconf` in terminal, press TAB key, and the terminal will display all available arguments.
..
:Q: **I want to experiment with openmediavault or make changes to the code**
:A:	As a true open source system you can do whatever you want with it. The recommendation is you don't do it in your home appliance server to avoid breaking the |webui|. The best thing to do is to use a Virtual Machine. On `Sourceforge <http://sourceforge.net/projects/openmediavault/files/vm/VirtualBox%20images/>`_ you can find a preconfigured |omv| virtual disk ready to launch. Alternatively checkout the |omv| `GIT repository <https://scm.openmediavault.org/>`_ and use `Vagrant <https://www.vagrantup.com/>`_ to create a virtual machine.
..
:Q: **What does `omv-update` and `omv-release-upgrade` commands do?**
:A:	Information about those commands are in the software :doc:`section </various/apt>`.
