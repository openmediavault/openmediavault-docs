Services
####


Samba
====

Samba server comes from Debian software repositories. |omv| developer does not mantain this package, all bug, hotfixes and features come from Debian. Advanced features like spotlight server or time machine support is not available because they have not reach yet stable Debian or the Debian developers have not made it available in their build.

General
----

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


You can add extra options in the general and share configuration at the bottom, where you have a multi line text field. This options are hardcoded in the mkconf script but they can be changed using :doc:`environmental variables </various/advset>`.


Privileges
----

The login access in Samba is configured using privileges. This means they will not act in the file system layer they will run in the Samba authentication layer. From there the access can be controlled to be read only or read/write access and guest account access. This is done with the PRIVILEGES button in the shared folder section not the ACL.
Privileges only gets only login access and from there determines if user can read or write. If write access is enabled and files/folders have restricted permissions then you will still not be able to write to folder using Samba.

.. important::
	Samba does not use PAM for login, it has a different password database. When the admin changes a username password (or the username changes his) using the |webui| what |omv| does is that it changes both the linux login password and the Samba internal database. If a username changes his password using shell, this will not be reflected in Samba log in.

Share types
----
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

Notice here if you have a user that you have not set up privileges for (thank means blank tick boxes) he will be able to login anyway and have write access.

**Public only:** *The guest user is always used. This is the Guest Only option in the Samba share configuration.*

.. code-block:: guess

	guest ok = yes
	guest only = yes

With these options valid, read only and write user directives will be ignored when mkconf regenerates the ``/etc/samba/smb.conf`` file.

.. note::
	- The guest account is mapped to system account nobody, he doesn’t belong to group users, thus he HAS BY DEFAULT NO WRITE ACCESS just READ. This is can be reverted modifying the POSIX permissions of the share to 777.
	- These directives are NOT ACL.


Questions:
----
How do I enter credentials in a semi-public share?
	In most cases the user will always be logged as guest.
	You have to use windows map network drive feature to provide other login credentials different from guest.
	In Mac OS X you can use CMD+K (if you are in Finder)

Why the login keeps saying access denied?
	This is more likely caused by two things:
		- Permission issue (ACL or non default POSIX permission mode/ownership). You need to fix the permissions in the shared folder. Samba runs as privileged (root) user, even so if parts of path don't have adecuate permissions you can still get access denied.
		- Out of sync password in between linux and Samba. This is very rare but it has happened. Test in ssh the following [tt]smbpasswd username[/tt] enter password and try and login again.

Why I can't edit files that other users have created?
	The default umask in Samba is ``644`` for files. To enable flexible sharing
	check `Enable permission inheritance` in the Samba share settings, this will
	force ``664`` creation mode. Files created previously need to change their
	permission mode. Check also that you don't have read only enabled. This
	option overrides privileges and POSIX.

FTP
====

Overview
----

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
----

FTP is a protocol intended for use in LAN and WAN. For accessing WAN it is required to forward the server port (default 21) and the passive range to the |omv| server.

Anonymous Login
-----

Disabled by default, the anonymous user is mapped to the system user ftp and nogroup. There is no write access for anonymous and this is configured in the ``/etc/proftpd/proftpd.conf`` file and cannot be changed as is hard coded into the default configuration script of the server. In this case there is no environmental variable to change that behaviour::

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
----
|omv| provides two SSL/TLS modes for encrypting the FTP communication implicit and explicit FTPS.

The differences and features are explained `here <https://en.wikipedia.org/wiki/FTPS>`_ and `here <http://www.jscape.com/blog/bid/75602/Understanding-Key-Differences-Between-FTP-FTPS-and-SFTP>`_.

Enabling FTP over SSL/TLS requires first that you create or import a certificate in the corresponding section. Once the certficate is there you can choose it from SSL/TLS section in FTP. The default FTPS of the server is explicit, you can click the checkbox to enable implicit. If you choose implicit make sure you forward port 900 in your router to port 21 in your NAS server if you're accessing from WAN, otherwise the client will probably display ECONREFUSED.

Tips
----

Login Group
	By default all |omv| users created in the |webui| can gain login into FTP. You can restrict to read only or read write, there is no deny access, but the user has no privileges he would not see that folder. If you want to add a layer of extra security for the login, you can create a control group to restrict login to FTP. You first create a group for example ftp_users, then at the end of the general extra options of the server we add:

	.. code-block:: guess

		​<Limit LOGIN>
		    DenyGroup !ftp_users
		</Limit>

	Only users members of that particular group will be able to log into the FTP server.

Home Folders
	There is not straightforward way of doing this in the |webui|, but if you really need home folders for FTP, you can change the default vroot path with environmental variable ``OMV_PROFTPD_MODAUTH_DEFAULTROOT=“~”``.
	What will happen here if users will log in straight into their home folders. If you add shared folders to the server they will be displayed inside the user home folder plus any other folder present in their home folder.

LetsEncrypt
	Just import your LE certificate in the ``General->Certificates->SSL`` `section <certificates.html#ssl-secure-socket-layer>`_. Then in the TLS/SSL tab, select the imported cert from the dropdown menu. Do not enable implicit ssl. You need also to add the chain file. So in the extra option field text add:

	``TLSCACertificateFile <yourpathtoLE>/etc/letsencrypt/live/<yourdomain>/chain.pem``

NFS
====

Overview
----

The configuration of the server is done using the common `NFS guidelines <https://help.ubuntu.com/community/SettingUpNFSHowTo>`_. Shared folders are actually binded to the /export directory. You can check by examining the ``/etc/fstab`` file after you have added a folder to the server. All NFS server configured folders are in /etc/exports as follows:::

	/export/Shared_1 (fsid=1,rw,subtree_check,secure,root_squash)
	/export/Videos 10.10.0.0/24 (fsid=2,rw,subtree_check,secure,nroot_squash)
	/export (ro,fsid=0,root_squash,no_subtree_check,hide)

The first two lines are examples, the last line is the NFSv4 pseudo file system. [1]_ [2]_


Server Shares
----

The following options are available to configure from the |webui|:

	- **Shared folder:** Select a folder, the system will add an bind entry to fstab, mount that bind and add it to /etc/exports file
	- **Client:** Enter a single ip, host or network CIDR notation. Only one entry is allowed at the moment. You can leave it empty if you do not want network security.
	- **Privilege:** This will append read write (rw) or read-only (ro) to ``/etc/exports``. [3]_
	- **Extra options:** Add options according the `exports manual <https://linux.die.net/man/5/exports>`_. If squash options are not specified, the mkconf script will add ``root_squash`` by default which is not displayed in the text field.

	The server also shares by default the pseudo root filesystem of /exports as NFSv4.

Clients
----
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

NFSv4 Pseudo filesystem
----
The default /export folder is shared with this default options ``ro,wdelay,root_squash,no_subtree_check,fsid=0`` only available to change via environmental variables, so be aware that mounting this path you will encounter permission problems.

Permissions
----
NFS relies on uid/gid matching at the remote/local filesystem and it doesn't provide any authentication/security at all. Basic security is provided by using network allow, and squash options. If you want extra security in NFS, you will need to configure it to use kerberos ticketing system.

Tips
----
Macos/OSX
	If you want to mount your NFS exports, add insecure in extra opions or use ``resvport`` in the command line.

	Example::

	$ sudo mount -t nfs -o resvport,rw 192.168.3.1:/export/Videos /private/nfs

Debian
	Debian distributions (and many others) always include the group users with ``gid=100`` by default, if you want to resolve permissions easily for all users of a PC using linux add ``anonuid=100`` in extra options. This will force all mounts to use that gid.

Symlinks
	This are not followed outside of their export path, so they have to be relative.

Remote access
	NFS was designed to be used as a local network protocol. Do not expose the NFS server to the internet. If you still need access use a VPN.


SSH
====

Overview
----
Secure shell comes disabled by default in OMV, if you install |omv| on top a Debian installation, the systemd unit will be disabled after the server packages are installed. Just login into |webui| to re-enable the ssh service.

The configuration options are minimal, But you can:

- Disable the root login
- Disable password authentication
- Enable public key authentication (PKA)
- Enable compression
- Enable tunneling (for SOCKS and port forward)

An extra text field is provided to enter more options. Examine first the file /etc/ssh/sshd_config before adding extra options otherwise the option you might want to add will not be applied. In that case you need to use change the environmental variable.

Normal |omv| users created in the |webui| can access the remote shell by adding them to the ssh group. Using PKA for users requires keys to be added to their profile, you can do this in the Users section. The key has to be added in `RFC 4716 <https://tools.ietf.org/html/rfc4716>`_ format. To do that run::

$ ssh-keygen -e -f nameofthekey.pub

You can paste the output in the users profile. ``Access Right Management->Users->$username->Edit->Public Keys`` 

You can add as many keys as you want. The public key looks like this::

	---- BEGIN SSH2 PUBLIC KEY ----
	Comment: "iPhone user1"
	AAAAB3NzaC1yc2EAAAADAQABAAABAQDfSQulxffUktx2P6EikkjVxDw0tT8nCW8LHLx/kl
	8t37xFQ5/OoL9m6rVzYy5CFGYt+l7DffWjL0Av7AqaM0ykZVmv2VEM6TmMo56LTlmyZdlz
	X5+GEJgCQNtDxcIYAVuPXKpLtlB/uAGzwHdZWpAen+mHgWIi4va8N5QNn4rXpkREcvM1q4
	snyAi+gyjAS2Dn4pm8zzrd9qQFnoRYzidbp5e2Rs3brOkwUco0ZkOME2Ff6SpLGaXz4DHH
	qgdTqZwHaTXEwm6kDmglCQrauIPI/ggNqz9mVEspYkskR2PM4CAty8RkZD4MQe5K3EMAFR
	aFobBSlhQ3ESCYWNXTS3bF
	---- END SSH2 PUBLIC KEY ----

The comment string is very important. This will help you track down when you need to revoke the key in case it gets lost or stolen.


Admin Tasks
----
If root login has been disabled and need to perform administrative tasks in the terminal, swap to root by typing using:: 

$ su 

To use sudo for root operations add the user to the sudo group.

The SFTP server comes enabled by default for root and ssh group. So POSIX folder permissions apply to non-root users accessing via SFTP.

.. note::
	**Remote WAN access**
		- Forward in your router a port different than 22. This will minimize bots fingering the ssh server.
		- Always use PKA.
		- Disable password login.
		- Disable root login.



Netatalk (plugin)
=====

Overview
----
Netatalk software was expected to reach version 3.x with Debian Jessie. Unfortunatly due to some unresolved issue with the maintainers, Debian team `opted <https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=690227>`_ to leave it out of Jessie and future releases. Debian Wheezy was the latest release with netatalk. To avoid loosing netatalk as a plugin |omv| uses a debianized source of netatalk 3.x maintained by Adrian Knoth [4]_. Openmediavault does not maintain this software.

Configuration
----
The server panel provides minimal options to the server, but it has an extra field in case you need `more directives <http://netatalk.sourceforge.net/3.1/htmldocs/afp.conf.5.html>`_. The default configuration file is located in ``/etc/netatalk/afp.conf``. This is the default global section:

.. code-block:: guess

	[Global]
	max connections = 20
	mac charset = MAC_ROMAN
	unix charset = LOCALE
	guest account = nobody
	uam list = uams_dhx.so,uams_dhx2.so
	save password = no

Netatalk provides PAM modules, so a change of password in terminal or web interface should be reflected inmediately in AFP login.

Shared Folders
----
The plugin uses the privileges database, so in the same way |omv| configures Samba shares, the login is controlled using valid, read and write directives in the software layer, not the filesystem. This is an example of a share in netatalk with default options:

.. code-block:: guess

	[Documents]
	path = /media/dev-disk-by-label-VOLUME1/documents
	read only = no
	unix priv = yes
	file perm = 0664
	directory perm = 0775
	umask = 0002
	invisible dots = no
	time machine = no
	valid users = "mike"
	invalid users =
	rolist =
	rwlist = "mike"

Password
	In case you don't want to use privileges you can assign a single password (no username) to the share.

Time Machine
	Support for the Apple backup software was added in netatalk 2.x, and improved in 3.x. Just check the box in the share options to make announce an individual share as a time machine server.

Guest Access
	You can select guest access which by default is read only. A second checkbox is provided for giving write access to guest.

Quota
	You can define a size limit, in case you have multiple time machine volumes and want to prevent them to fill up the data drives.

RSync
=====

The server can be configured to act as a client to pull and push data to remote locations as well as act an rsync daemon server, where other clients can retrieve or store data from/to the server. In rsync languague, the shared folders are called modules. Since |omv| version 3.0 is possible now to create remote rsync jobs using ssh as transport shell.

The rsync is divided in two tabs

Jobs (client)
----
Based on cron, the tasks can be configured to run at certain time or make it repetive. A few of the options explained:

Type
	- Local: This will run an rsync in between two internal folders of the server. For example you can use this to move data across different disks in your system
	- Remote: This will deactivate destination folder, and instead you'll need to place a destination server address. You can select here:

		Mode (remote)
			- Push: store contents to a remote server
			- Pull: Retrieve contents from a remote server

	Selecting one or the other will invert the folder as source or destination, the same as the server address.

Destination/Source Shared Folder
	Choose a shared folder where you want the contents to be stored (pull) or you want the contents from that folder to be sent to a remote server (push)

Destination/Source Server
	You need to put address server host or ip.

	Examples:

	If you are targeting the job against an rsync daemon server:
	::
		rsync://10.10.10.12/ModuleName
		username@10.10.10.12::ModuleName
		rsync://username@10.10.10.12:873/ModuleName

	If you are going to connect to another server just using ssh with public key:
	::
		username@10.10.0.12:/srv/dev-disk-by-label-VOLUME1/Documents

.. warning::
	When the rsync task is configured using ssh with PKA, the script that runs the jobs is non-interactive, this means there cannot be a neither a passphrase for the private key or a login password. Make sure your private is not created with a password (in case is imported). Also make sure the remote server can accept PKA and not enforce password login.

**Authentication (remote)**
	
	- **Password**: For the remote rsync daemon module. Is not the username login password defined in the Rights Management section of the server. Read ahead in server tab.
	- **Public Key**: Select a key. These are created/imported from ``General->Certificates->SSH`` `section <certificates.html#ssh-secure-shell>`_.

There are options are available which are the most commonly used in rsync. At the end there is an extra text field where you add more `options <http://linux.die.net/man/1/rsync>`_.

Server
----

This is the place for configuring the rsync daemon and it's modules (shared folder).

Settings
	Change listening port of the daemon and add extra configurations `directives <https://www.samba.org/ftp/rsync/rsyncd.conf.html>`_ text field.

Modules
	This is where you add shared folders to be available to the daemon. The options are explained in the module web panel. If you want to protect the modules you can select the next tab and choose a server username and establish a password. Be aware the password is only for the modules, is not the linux password. Documentation for the extra options for the modules is provided by rsyncd manual.

Configuration
	The server makes the tasks run by placing them in ``/etc/cron.d/openmediavault-rsync`` in one line per job. You can see the cron time at the beginning, then user (root) and target file that holds the actual rsync file with the final command. The files are stored in ``/var/lib/openmediavault/cron.d/``, prefixed with ``rsync`` and a <uuid>. A default ssh rsync job looks like this.

.. code-block:: shell

	#!/bin/sh
	# This configuration file is auto-generated.
	# WARNING: Do not edit this file, your changes will be lost.
	. /usr/share/openmediavault/scripts/helper-functions
	cleanup() {
	  omv_kill_children $$
	  rm -f /var/run/rsync-05260f23-5098-4f07-9250-0b38b923ac7f
	  exit
	}
	[ -e /var/run/rsync-05260f23-5098-4f07-9250-0b38b923ac7f ] && exit 1
	if ! omv_is_mounted "/srv/dev-disk-by-label-VOLUME1/" ; then
	    omv_error "Source storage device not mounted at </srv/dev-disk-by-label-VOLUME1>!"
	    exit 1
	fi
	trap cleanup 0 1 2 5 15
	touch /var/run/rsync-05260f23-5098-4f07-9250-0b38b923ac7f
	omv_log "Please wait, syncing </srv/dev-disk-by-label-VOLUME1/backupdir/> to <username@backupserver.com:/opt/backup> ...\n"
	eval $(ssh-agent) >/dev/null
	ssh-add /etc/ssh/openmediavault-484a6837-5170-468c-aa8f-0e3cb92a641e >/dev/null
	rsync --verbose --log-file="/var/log/rsync.log" --rsh "ssh -p 22" --recursive --times --archive --perms '/srv/dev-disk-by-label-VOLUME1/backupdir/' 'username@backupserver.com:/opt/backup' & wait $!
	omv_log "\nThe synchronisation has completed successfully."




.. [1] https://help.ubuntu.com/community/NFSv4Howto#NFSv4_without_Kerberos
.. [2] https://www.centos.org/docs/5/html/5.1/Deployment_Guide/s3-nfs-server-config-exportfs-nfsv4.html
.. [3] This is not standard |omv| privileges as in the shared folder section
.. [4] https://github.com/adiknoth/netatalk-debian
