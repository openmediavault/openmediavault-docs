Samba
#####

Samba server comes from Debian software repositories. |omv| developer does not mantain this package, all bug, hotfixes and features come from Debian. Advanced features like spotlight server or time machine support is not available because they have not reach yet stable Debian or the Debian developers have not made it available in their build.

General
-------

The server configures Samba as standalone mode. The default global section

.. code-block:: guess

	[global]
	workgroup = HOME
	server string = %h server
	dns proxy = no
	log level = 0
	syslog = 0
	log file = /var/log/samba/log.%m
	max log size = 1000
	syslog only = yes
	panic action = /usr/share/samba/panic-action %d
	encrypt passwords = true
	passdb backend = tdbsam
	obey pam restrictions = no
	unix password sync = no
	passwd program = /usr/bin/passwd %u
	passwd chat = *Enter\snew\s*\spassword:* %n\n *Retype\snew\s*\spassword:* %n\n *password\supdated\ssuccessfully* .
	pam password change = yes
	socket options = TCP_NODELAY IPTOS_LOWDELAY
	guest account = nobody
	load printers = no
	disable spoolss = yes
	printing = bsd
	printcap name = /dev/null
	unix extensions = yes
	wide links = no
	create mask = 0777
	directory mask = 0777
	use sendfile = yes
	aio read size = 16384
	aio write size = 16384
	null passwords = no
	local master = yes
	time server = no
	wins support = no


A default share example:

.. code-block:: guess
	:emphasize-lines: 16-19

	[MyDocuments]
	path = /media//dev/disk/by-label/VOLUME1/Documents/
	guest ok = no
	read only = no
	browseable = yes
	inherit acls = yes
	inherit permissions = no
	ea support = no
	store dos attributes = no
	printable = no
	create mask = 0755
	force create mode = 0644
	directory mask = 0755
	force directory mode = 0755
	hide dot files = yes
	valid users = "john"
	invalid users =
	read list =
	write list = "john"


Is possible to add extra options in the general and share configuration at the bottom with a multi line text field. This options are hardcoded in the mkconf script but they can be changed using :doc:`environmental variables </various/advset>`.


Privileges
----------

The login access in Samba is configured using privileges. This means they will not act in the file system layer they will run in the Samba authentication layer. From there the access can be controlled to be read only or read/write access and guest account access. This is done with the PRIVILEGES button in the shared folder section not the ACL.
Privileges only gets only login access and from there determines if user can read or write. If write access is enabled and files/folders that have restricted permissions then write access is not possible using Samba.

.. important::
	Samba does not use PAM for login, it has a different password database. When the admin changes a username password (or the username changes his) using the |webui| what |omv| does is that it changes both the linux login password and the Samba internal database. If a username changes his password using shell, this will not be reflected in Samba log in.

Share types
-----------

**Non-public (Private):** *Login always required, Guest Allowed denied*

.. code-block:: guess

	guest ok = no
	valid users = User1, User2, @Group1, @Group2 ## this will deny all none authorized users
	read list = User1, @Group1
	write list = User2, @Group2

This means that every user will have to provide valid OMV credentials to access that share. Also this type of shares requires at least one definition of a valid user, otherwise the directive would be empty.

.. note::
	This will allow every user to log into the share.

**Semi-public:**
*When login is not provided, the guest user is used. This is the "guest allowed" option from the Samba share option*

.. code-block:: guess

	guest ok = yes
	read list = User1, @Group1
	write list = User2, @Group2

Notice here if users are not set up privileges (thank means blank tick boxes) anyone will be able to login anyway and have write access.

**Public only:** *The guest user is always used. This is the Guest Only option in the Samba share configuration.*

.. code-block:: guess

	guest ok = yes
	guest only = yes

With these options valid, read only and write user directives will be ignored when mkconf regenerates the ``/etc/samba/smb.conf`` file.

.. note::
	- The guest account is mapped to system account nobody, he doesn’t belong to group users, thus he HAS BY DEFAULT NO WRITE ACCESS just READ. This is can be reverted modifying the POSIX permissions of the share to 777.
	- These directives are NOT ACL.


Questions
---------

How do I enter credentials in a semi-public share?
	In most cases the user will always be logged as guest.
	Use windows map network drive feature to provide other login credentials different from guest.
	In Mac OS X use CMD+K (if using Finder)

Why the login keeps saying access denied?
	This is more likely caused by two things:
		- Permission issue (ACL or non default POSIX permission mode/ownership). Fix the permissions in the shared folder. Samba runs as privileged (root) user, even so if parts of path don't have adecuate permissions, it will still respond access denied.
		- Out of sync password in between linux and Samba. This is very rare but it has happened. Test in ssh the following [tt]smbpasswd username[/tt] enter password and try and login again.

Why I can't edit files that other users have created?
	The default umask in Samba is ``644`` for files. To enable flexible sharing
	check `Enable permission inheritance` in the Samba share settings, this will
	force ``664`` creation mode. Files created previously need to change their
	permission mode. Check also that you don't have read only enabled. This
	option overrides privileges and POSIX.
