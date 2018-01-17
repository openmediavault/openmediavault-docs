Services
####


Samba
====

Samba server comes from Debian software repositories. |omv| developer does not mantain this package, all bug, hotfixes and features come from Debian. Advanced features like spotlight server or time machine support is not available because they have not reach yet stable Debian or the Debian developers have not made it available in their build.

General
^^^^

The server configures samba as standalone mode. The default global section is as follows:

..  code-block::conf

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


Shares are configured in this way:

..  code-block::conf

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


You can add extra options in the general and share configuration at the bottom, where you have a multi line text field. This options are hardcoded in the mkconf script but they can be changed using :doc:`environmental variables </various/advset>`.

Privileges
^^^^

The login access in Samba is configured using privileges. This means they will not act in the file system layer they will run in the samba authentication layer. From there the access can be controlled to be read only or read/write access and guest account access. This is done with the PRIVILEGES button in the shared folder section not the ACL.
Privileges only gets only login access and from there determines if user can read or write. If write access is enabled and files/folders have restricted permissions then you will still not be able to write to folder using Samba.

Share types
^^^^
**Non-public (Private):** *Login always required, Guest Allowed denied*::

	guest ok = no
	valid users = User1, User2, @Group1, @Group2 ## this will deny all none authorized users
	read list = User1, @Group1
	write list = User2, @Group2

This means that every user will have to provide valid OMV credentials to access that share. Also this type of shares requires at least one definition of a valid user, otherwise the directive would be empty.

.. note::
	This will allow every user to log into the share.

**Semi-public:**
*When login is not provided, the guest user is used. This is the "guest allowed" option from the samba share option*::
	guest ok = yes
	read list = User1, @Group1
	write list = User2, @Group2

Notice here if you have a user that you have not set up privileges for (thank means blank tick boxes) he will be able to login anyway and have write access.

**Public only:** *The guest user is always used. This is the Guest Only option in the samba share configuration.*::

	guest ok = yes
	guest only = yes

With these options valid, read only and write user directives will be ignored when mkconf regenerates the ``/etc/samba/smb.conf`` file.

.. note::
	- The guest account is mapped to system account nobody, he doesn’t belong to group users, thus he HAS BY DEFAULT NO WRITE ACCESS just READ. This is can be reverted modifying the POSIX permissions of the share to 777.
	- These directives are NOT ACL


Questions:
^^^^
How do I enter credentials in a semi-public share?
	In most cases the user will always be logged as guest.
	You have to use windows map network drive feature to provide other login credentials different from guest.
	In Mac OS X you can use CMD+K (if you are in Finder)

Why the login keeps saying access denied?
	This is more likely caused by two things: Permission issue (ACL or non default POSIX permission mode/ownership). You need to fix the permissions in the shared folder. Samba runs as privileged (root) user, even so if parts of path don't have adecuate permissions you can still get access denied.

Why I can't edit files that other users have created?
	The default umask in samba is ``644`` for files. So to enable flexible sharing tick Enable permission inheritance in the samba share settings this will force ``664`` creation mode. Files created previously need to change their permission mode. Use reset permission utility. Check also that you don't have read only enabled. This option overrides privileges and POSIX.

FTP
====

Overview
^^^^

On top of the proftpd debian package, |omv| uses the vroot module by Castaglia. The server is configured using a DefaultRoot for this folder ``/srv/ftp``. Adding folders to the chroot is done by using vroot aliases.

This is the default behavoiour of the FTP server and cannot be changed. The vroot default path can be changed with environmental variables. The chroot also prevent symlinks for escaping that path, however you can use symlinks that point inside the chroot.

So any time you add a shared folder to the FTP, OMV will create first a vroot alias:::

	<IfModule mod_vroot.c>
	  VRootAlias "/media/dev-disk-by-label-VOLUME1/videos" "Videos"
	</IfModule>


Then that alias will have privileges assigned:::

	<Directory /Videos>
	  <Limit ALL>
	    AllowUser OR omvUser
	    DenyAll
	  </Limit>
	  <Limit READ DIRS>
	    AllowUser OR omvUser
	    DenyAll
	  </Limit>
	</Directory>

By default you're not allowed to write in the when you login, this means you cannot create folders in the landing directory, you have to enter one of the shared folders. Also due to the nature of the chroot, creating top level folders is pointless since they will be actually stored in /srv/ftp and not in the media disks.

Remote Access
^^^^^^^^^^^^^

FTP is a protocol intended for use in LAN and WAN. For accessing WAN you need to forward in your router the server port (default 21) and the passive range.

Anonymous Login
^^^^^^^^^^^^^^^

Disabled by default, the anonymous user is mapped to the system user ftp and
nogroup. There is no write access for anonymous and this is configured in the
proftpd.conf file and cannot be changed as is hard coded into the default
configuration script of the server. In this case there is no environmental
variable to change that behaviour::

	<Anonymous ~ftp>
	  User ftp
	  Group nogroup
	  UserAlias anonymous ftp
	  DirFakeUser on ftp
	  DirFakeGroup on ftp
	  RequireValidShell off
	  <Directory *>
	    HideFiles (welcome.msg)
	    HideNoAccess on
	    <Limit WRITE>
	      DenyAll
	    </Limit>
	  </Directory>
	</Anonymous>


FTP(S/ES)
^^^^^^^^^
|omv| provides two SSL/TLS modes for encrypting the FTP communication implicit and explicit FTPS.

The differences and features are explained `here <https://en.wikipedia.org/wiki/FTPS>`_ and `here <http://www.jscape.com/blog/bid/75602/Understanding-Key-Differences-Between-FTP-FTPS-and-SFTP>`_.

Enabling FTP over SSL/TLS requires first that you create or import a certificate in the corresponding section. Once the certficate is there you can choose it from SSL/TLS section in FTP. The default FTPS of the server is explicit, you can click the checkbox to enable implicit. If you choose implicit make sure you forward port 900 in your router to port 21 in your NAS server if you're accessing from WAN, otherwise the client will probably display ECONREFUSED.

Tips
^^^^

Login Group
	By default all |omv| users created in the |webui| can gain login into FTP. You can restrict to read only or read write, there is no deny access, but the user has no privileges he would not see that folder. If you want to add a layer of extra security for the login, you can create a control group to restrict login to FTP. You first create a group for example ftp_users, then at the end of the general extra options of the server we add:

	.. code-block:: xml

		​<Limit LOGIN>
		    DenyGroup !ftp_users
		</Limit>

	Users *not belonging to that group* can't log in to the FTP server.

Home Folders
	There is not straightforward way of doing this in the |webui|, but if you really need home folders for FTP, you can change the default vroot path with environmental variable ``OMV_PROFTPD_MODAUTH_DEFAULTROOT=“~”``.
	What will happen here if users will log in straight into their home folders. If you add shared folders to the server they will be displayed inside the user home folder plus any other folder present in their home folder.

LetsEncrypt
	TO Be added

NFS
====

Overview
^^^^^^^^

The configuration of the server is done using the common `NFS guidelines <https://help.ubuntu.com/community/SettingUpNFSHowTo>`_. Shared folders are actually binded to the /export directory. You can check by examining the ``/etc/fstab`` file after you have added a folder to the server. Then all folders are configured to share in /etc/exports as follows:::

	/export/Shared_1 (fsid=1,rw,subtree_check,secure,root_squash)
	/export/Videos 10.10.0.0/24 (fsid=2,rw,subtree_check,secure,nroot_squash)


Server Shares
^^^^^^^^^^^^^

The following options are available to configure from the |webui|:

	- **Shared folder:** Select a folder, the system will add an bind entry to fstab, mount that bind and add it to /etc/exports file
	- **Client:** Enter a single ip, host or network cidr notation. Only one entry is allowed at the moment. You can leave it empty if you do not want network security.
	- **Privilege:** This will append read write (rw) or read-only (ro) to ``/etc/exports``. [1]_
	- **Extra options:** Add options according the `exports manual <https://linux.die.net/man/5/exports>`_. If squash options are not specified, the mkconf script will add ``root_squash`` by default which is not displayed in the text field.

	The server also shares by default the pseudo root filesystem of /exports as NFSv4.

Clients
^^^^^^^
To access NFS shares using any debian derived linux distro:

* Mount as NFSv4 all folders in ``/export/`` in ``/mnt/nfs``::

  $ mount 172.34.3.12:/ /mnt/nfs

* Mount as NFSv3 all folders inside ``/export`` in ``/mnt/nfs``::

  $ mount 172.34.3.12:/export /mnt/nfs

* Mount as NFSv3 the folder ``/export/Videos`` in ``/mnt/nfs``::

  $ mount 172.34.3.12:/export/Videos /mnt/nfs

* Mount as NFSv4 the folder ``/export/Videos`` in ``/mnt/nfs``::

  $ mount 172.34.3.12:/Videos /mnt/nfs

Check your distro on how to proceed with different NFS versions.

NFSv4 Pseudo root filesystem
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The default /export folder is shared with this default options ``ro,wdelay,root_squash,no_subtree_check,fsid=0`` only available to change via environmental variables, so be aware that mounting this path you will encounter permission problems.

Permissions
^^^^^^^^^^^
NFS relies on uid/gid matching at the remote/local filesystem and it doesn't provide any authentication/security at all. Basic security is provided by using network allow, and squash options. If you want extra security in NFS, you will need to configure it to use kerberos ticketing system.

Tips
^^^^
Macos/OSX
	If you want to mount your NFS exports, add insecure in extra opions or use ``resvport`` in the command line.

	Example:
	 ``sudo mount -t nfs -o resvport,rw 192.168.3.1:/export/Videos /private/nfs``

Debian
	Debian distributions (and many others) always include the group users with gid=100 by default, if you want to resolve permissions easily for all users of a PC using linux add anonuid=100 in extra options. This will force all mounts to use that gid.

Symlinks
	This are not followed in NFS outside of their export path, so they have to be relative.

Remote access
	NFS was designed to be used as a local network protocol. Do not expose the NFS server to the internet. If you still need access use a VPN.


SSH
====

Overview
^^^^^^^^
Secure shell comes disabled by default in OMV, if you install |omv| on top a Debian installation, the systemd unit will be disabled after the server packages are installed. Just login into |webui| to re-enable the ssh service.

The configuration options are minimal, But you can:

- Disable the root login
- Disable password authentication
- Enable public key authentication (PKA)
- Enable compression
- Enable tunneling (for SOCKS and port forward)

An extra text field is provided to enter more options. Examine first the file /etc/ssh/sshd_config before adding extra options otherwise the option you might want to add will not be applied. In that case you need to use change the environmental variable.

Normal |omv| users created in the |webui| can access the remote shell by adding them to ssh group. Using PKA for users, requires keys to be added to their profile, you can do this in the Users section. The key has to be added in `RFC 4716 <https://tools.ietf.org/html/rfc4716>`_ format. To do that run ssh-keygen -e -f nameofthekey.pub, then paste the output in the users profile.

If you have disabled root login and need to perform root operations in the terminal, you can swap to root by typing su or su - in terminal to be prompted for root password. If you want to use sudo for root operations then you need to add the user to the sudo group.

The SFTP server comes enabled by default for root and ssh group. So POSIX folder permissions apply to non-root users accessing via SFTP.

.. note::
	**Remote WAN access**
		- Forward in your router a port different than 22. This will minimize bots fingering the ssh server.
		- Always use PKA.
		- Disable password login.
		- Disable root login.



Netatalk
========

RSync
=====


.. [1] This is not standard |omv| privileges as in the shared folder section
