FAQ
===

**Frequently Asked Questions**

What is OMV?
	OMV is an abbreviation of |omv|.

Is |omv| a fork of FreeNAS?
	No

When shall i use |omv|?
    If you want to set up a NAS really fast and manage it easily, then
    |omv| is the right solution for you. If you want to use a really
    free software where you are not a beta tester for a commercial
    variant, then |omv| is also a solution for you.

Does |omv| have drivers for my hardware?
	Please consult the Debian hardware compatibility list for more information.

Can I use a usb flash drive (stick) for installing the system?
	Yes, but the installation does not have any optimizations to reduce writes
	into the OS disk. The usb media will most likely start failing within a
	few weeks of usage. Most common symptom is basic command execution does
	not work, denied login, etc. More information `here <https://forum.openmediavault.org/index.php/Thread/6438-Tutorial-Experimental-Third-party-Plugin-available-Reducing-OMV-s-disk-writes-al/>`_.

What are the default credentials for the UI?
    Use the user 'admin' and the password 'openmediavault' for the first login.

Can I give administrator privileges to non-privileged users to access the web control panel?
	Yes. By default non-privileged users can only access their account profile, they can change
	password and their email address if the administrator has allowed changes on their account.
	However the current |webui| framework is designed for developers to create plugins where
	they can give limited or full access to non-privileged users. An example is the
	`openvpn plugin <https://github.com/OpenMediaVault-Plugin-Developers/openmediavault-openvpn>`_
	by `omv-extras.org <https://omv-extras.org>`_.
	A non-privileged user can become a |webui| administrator by adding them to the ``openmediavault-admin`` group.

I cannot read out SMART data for my storage device
    For storage devices connected via USB, |omv| relies entirely on the auto-detection
    functionality of the `smartmontools <https://www.smartmontools.org/>`_ applications.
    To be always up to date |omv| automatically downloads the `smartctl/smartd database <https://raw.githubusercontent.com/mirror/smartmontools/master/drivedb.h>`_
    once a week. You can do that manually by running :command:`update-smart-drivedb`
    in the CLI.
    Should it nevertheless happen that a storage device is not supported, please
    submit a request to the smartmontools project. You can find more information in
    their `FAQ <https://www.smartmontools.org/wiki/FAQ#SmartmontoolsDatabase>`_.

What is the file :file:`/etc/openmediavault/config.xml` for?
	It is the database configuration store file for |omv|. When a change is
	performed in the |webui|, the config value is stored and/or retrieved by
	RPC to/from this file.

Can I upgrade to Debian Testing/Unstable (Debian Testing/Sid) or use Ubuntu as a base distribution?
    Yes. But the end is most likely a broken |webui| and possibly broken
    system. |omv| releases are heavily tight to their Debian base distribution.
    Get more information :doc:`here </various/apt>`.

I´ve lost the |webui| password. How do I reset it?
	Simply connect via ssh into the server or login locally on the machine
	and type in: :command:`omv-firstaid`. There is an option to reset the
	|webui| password.

Can I backup or restore an existing |omv| configuration?
	There is no regular backup/restore procedure, but yes, in some way:
	keep the file :file:`/etc/openmediavault/config.xml` for references
	purposes if the option is to go for a clean re-install.

What is the default HTTP engine of |omv|?
	NGINX. The last version of |omv| with Apache was 0.5 Sardoukar.

Can I use Apache as HTTP engine?
    Yes, but is not supported. Eventually every |omv| package upgrade will
    activate NGINX again leaving the |webui| broken. A parallel Apache
    instance next to Nginx is possible, just make sure the ports are different
    otherwise the |omv| |webui| will not work.

How can use the default HTTP engine to hold my own web page?
    Do not modify |omv| default NGINX files. Place the website configurations
    in :file:`/etc/nginx/sites-available` and enable it with
    :command:`nginx_ensite <SITE>`. Read more information in the
    `NGINX documentation <http://nginx.org/en/docs/>`_.

Why does the system rewrites a configuration file(s) that I have manually edited?
    OMV takes full control of some system services. This services include
    monit, ntp, samba, network, proftpd, nginx, php5-fpm, etc. Read
    :doc:`here </various/files>`.

How can I modify an internal value of some service |omv| has control over?
	Read :doc:`here <various/advset>` for advanced configurations.

How can I modify or add a network configuration with some custom options the |webui| does not provide?
    Starting with |omv| version 5 `systemd-networkd` is used to configure the network.
    The interfaces file :file:`/etc/network/interfaces` is controlled by |omv| but
    not used anymore.
    To add network interfaces that are not configurable through the |webui| or other
    options not present, use :doc:`advanced settings <various/advset>`.
    Alternatively write your own `systemd-networkd` configuration files.

Why my disks mount paths have a long alphanumeric number?
    The long number is called UUID, it is used by fstab to mount disks. This
    number is unique per filesystem (or at least unlikely possible that
    another filesystem comes with an identical one). This helps maintaining the
    mount points. The old linux way (sda1, sdb1, etc.) is not guaranteed that
    /dev/sda1 is the same disk on next reboot. If having trouble identifying them
    in terminal, create a pool with symlinks to each file system with easy to
    remember names.

    This behaviour has been deprecated now in current |omv| releases.
    The default creation of mount paths is documented `here <https://github.com/openmediavault/openmediavault/blob/20ec529737e6eca2e1f98d0b3d1ade16a3c338e1/deb/openmediavault/usr/share/openmediavault/engined/rpc/filesystemmgmt.inc#L823-L833>`_.

I don't have a data disk, and I want to use my OS disk for storing data?
	The default behaviour of |omv| is to act as NAS server, that means OS
	files are separated from data disks.

	However if the OS disk is partitioned the system will recognise the extra
	partitions besides rootfs if is formatted. You can mount it and use it for
	shared folders.

	The current installer does not provide access to the partition manager,
	use a plain Debian iso then install |omv| on top and accommodate the
	partitions, or resize the partition after installing using Gparted or
	SystemRescueCd.

Can I install |omv| on top a running Debian system?
	Yes, but it is recommended that the current running OS not to have a desktop environment
	installed.

What is the permissions/ownership of folders in |omv| created by shared folders?
	The default is folders in ``2775`` mode, with ``root:users`` ownership.
	This means all users created in the |webui| can read, write to folders
	created by the system in the data drives using the default. The setgid allows
	group inheritance, meaning new files/folders below will always have the group
	users (GID=100) membership.

I need to delete a shared folder, why the delete button is greyed/disabled?
	Shared folder configurations can be used across different services. When
	removing a shared folder configuration is necessary to unlink it from
	every service is attached to, before the delete button becomes available.
	At the moment there is no internal database backend that can display
	information about which service is holding which shares.

What is the :command:`omv-salt` command for?
	:command:`omv-salt` is a terminal console command that is used by the
	backend of |omv| to pipe directives and values to service configuration
	files. The arguments that :command:`omv-salt` accepts are related to the
	name of the service it configures. Type :command:`omv-salt` in terminal,
	press TAB key, and the terminal will display all available arguments.

I want to experiment with |omv| or make changes to the code
	As a true open source system everything is possible. The
	recommendation is do not test with the production server to avoid
	breaking the |webui|. The best thing to do is to use a Virtual Machine.
	On `Sourceforge <http://sourceforge.net/projects/openmediavault/files/vm/VirtualBox%20images/>`_
	there are preconfigured |omv| images with virtual disks ready to launch.
	Alternatively checkout the |omv| `GIT repository <https://scm.openmediavault.org/>`_
	and use `Vagrant <https://www.vagrantup.com/>`_ to create a virtual
	machine.

What is the :command:`omv-upgrade` and :command:`omv-release-upgrade` for?
	Information about those commands are in the software :doc:`section </various/apt>`.
