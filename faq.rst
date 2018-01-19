FAQ
===

**Frequently Asked Questions**

What is OMV?
	OMV is an abbreviation of |omv|.

Is |omv| a fork of FreeNAS?
	No

Does |omv| have drivers for my hardware?
	All module drivers are provided by the Debian standard kernel of oldstable release 8.9 (aka Jessie). This distribution ships with kernel 3.16 by default. You can optionally install the backport kernel 4.9. If your hardware is supported under Debian Jessie then is supported under OMV.
	The Jessie backport kernel 4.9 is the default kernel used by Stretch (Debian 9.3) at the moment, so it provides support for newer hardware.

Can I use a usb flash drive (stick) for installing the system?
	Yes, but the installation does not have any optimizations to reduce writes into the OS disk. Your usb media will most likely start failing within a few weeks of usage. Most common symptom is basic command execution does not work, denied login, etc. More information `here <https://forum.openmediavault.org/index.php/Thread/6438-Tutorial-Experimental-Third-party-Plugin-available-Reducing-OMV-s-disk-writes-al/>`_

What is the file :file:`/etc/openmediavault/config.xml` for?
	Is the database configuration store file for |omv|. When a change is performed in the |webui|, the config value is stored and/or retrieve by rpc to/from this file. If this is a save change, then mkconf passes the value to the service configuration file and reloads the daemon in case is necessary.

Can I upgrade to Debian Testing/Unstable (Debian Testing/Sid) or use Ubuntu as a base distribution?
	Yes you can. But you will end up most likely with a broken |webui| and possibly broken system. |omv| releases are heavily tight to their Debian base distro.

I´ve lost the |webui| password. How do I reset it?
	Simply connect via ssh to your server or login locally on your machine and type in: :command:`omv-firstaid`. There is an option to reset your password.

Can I backup or restore and existing |omv| configuration?
	No. You can keep the file :file:`/etc/openmediavault/config.xml` for references purposes if you decide to go for a clean re-install.

What is the default HTTP engine of |omv|?
	NGINX. The last version of |omv| with Apache was 0.5 Sardoukar.

Can I use Apache as HTTP engine?
	You can use it but is not supported. Eventually every |omv| package upgrade will activate NGINX again leaving you with a broken |webui|. You can run a parallel Apache instance to Nginx just make sure the ports are different otherwise your |omv| |webui| will not work.

How can use the default HTTP engine to hold my own web page?
	Do not modify |omv| default NGINX files. You can place your website configurations at :file:`/etc/nginx/sites-available` and enable it with :command:`nginx_ensite <SITE>`. Read more information in the `NGINX documentation <http://nginx.org/en/docs/>`_.

Why does the system rewrites a configuration file(s) that I have manually edited?
	OMV takes full control of some system services. This services include monit, ntp, samba, network, proftpd, nginx, php5-fpm, etc. Read :doc:`here </various/files>`.

How can I modify an internal value of some service |omv| has control over?
	Read :doc:`here <various/advset>` for advanced configurations.

How can I modify or add a network configuration of :file:`/etc/network/interfaces` with some custom options the |webui| does not provide?
	The interfaces file is controlled by |omv|. To add network interfaces that are not configurable through the |webui| or other options not present, you need to use  :doc:`advanced settings <various/advset>`.

Why my disks mount paths have a long alphanumeric number?
	The long number is called UUID, it is used by fstab to mount disks. This number is unique per filesystem (or at least unlikely possible that another filesystem comes with an identical one). This helps maintaing the mount points. The old linux way (sda1, sdb1, etc.) is not guaranteed that /sda1 is the same disk on next reboot. If you have trouble identiying them in terminal, you can always create a pool with symlinks to each file system with easy to remember names.

	This behaviour has been deprecated now in current omv releases including stable (Jessie). The default creation of mount paths is documented `here <https://github.com/openmediavault/openmediavault/blob/20ec529737e6eca2e1f98d0b3d1ade16a3c338e1/deb/openmediavault/usr/share/openmediavault/engined/rpc/filesystemmgmt.inc#L823-L833>`_.

I don't have a data disk, and I want to use my OS disk for storing data?
	The default behaviour of |omv| is to act as NAS server, that means OS files are separated from data disks.

	You can use partitions in the same disk you use for OS and the system will recognise the partitions for formatting, mounting and to create shared folders.

	The current installer does not provide access to the partition manager, so you need to use a plain Debian iso then install |omv| on top and acommodate the partitions, or resize the partition after installing using Gparted or SystemRescueCd.

Can I install |omv| on top a running Debian system?
	Yes, but is not recommended that the running OS has a desktop environment installed.

Which are the files that should not be edited by the user?
	There are several services that |omv| takes control of, The recommended list is here.

What is the permissions/ownership of folders in |omv| created by shared folders?
	The default is folders in ``2775`` mode, with ``root:users`` ownership. This means all users created in the |webui| can read, write to folders created by the system in the data drives using the default.

Why are my filesystems mounted as noexec?
	This is a security measure to avoid the placement of malicious scripts in the shared folders. This will prevent any script execution in those paths, including compiling packages and binaries.

	If you need to remove the noexc flag, you need to use advanced settings.

I need to delete a shared folder, why the delete button is greyed/disabled?
	Shared folder configurations can be used across different services. If you need to remove a shared folder configuration you need to unlink it from every service is attached to it before the delete button becomes available. At the moment there is no internal database backend that can display information about which service is holding which shares.

What is the :command:`omv-mkconf` command for?
	:command:`omv-mkconf` is a terminal console command that is used by the backend of |omv| to pipe directives and values to service configuration files. The arguments that :command:`omv-mkconf` accepts are related to the name of the service it configures. Type :command:`omv-mkconf` in terminal, press TAB key, and the terminal will display all available arguments.

I want to experiment with |omv| or make changes to the code
	As a true open source system you can do whatever you want with it. The recommendation is you don't do it in your home appliance server to avoid breaking the |webui|. The best thing to do is to use a Virtual Machine. In `Sourceforge <http://sourceforge.net/projects/openmediavault/files/vm/VirtualBox%20images/>`_ you can find a preconfigured |omv| virtual disk ready to launch.

What is the :command:`omv-update` and :command:`omv-release-upgrade` do?
	Information about those commands are in the software :doc:`section </various/apt>`.
