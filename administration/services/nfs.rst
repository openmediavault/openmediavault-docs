NFS
###

Overview
--------

The configuration of the server is done using the common `NFS guidelines <https://help.ubuntu.com/community/SettingUpNFSHowTo>`_. Shared folders are actually binded to the /export directory. You can check by examining the ``/etc/fstab`` file after you have added a folder to the server. All NFS server configured folders are in /etc/exports as follows::

	/export/Shared_1 (fsid=1,rw,subtree_check,secure,root_squash)
	/export/Videos 10.10.0.0/24 (fsid=2,rw,subtree_check,secure,nroot_squash)
	/export (ro,fsid=0,root_squash,no_subtree_check,hide)

The first two lines are examples, the last line is the NFSv4 pseudo file system. [1]_ [2]_


Server Shares
-------------

The following options are available to configure from the |webui|:

	- **Shared folder:** Select a folder, the system will add an bind entry to fstab, mount that bind and add it to /etc/exports file
	- **Client:** Enter a single ip, host or network CIDR notation. Only one entry is allowed at the moment. You can leave it empty if you do not want network security.
	- **Privilege:** This will append read write (rw) or read-only (ro) to ``/etc/exports``. [3]_
	- **Extra options:** Add options according the `exports manual <https://linux.die.net/man/5/exports>`_.

	The server also shares by default the pseudo root filesystem of /exports as NFSv4.

Clients
-------

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
-----------------------

The default /export folder is shared with this default options ``ro,wdelay,root_squash,no_subtree_check,fsid=0`` only available to change via environmental variables, so be aware that mounting this path you will encounter permission problems.

Permissions
-----------

NFS relies on uid/gid matching at the remote/local filesystem and it doesn't provide any authentication/security at all. Basic security is provided by using network allow, and squash options. If you want extra security in NFS, you will need to configure it to use kerberos ticketing system.

Tips
----

Macos/OSX
	If you want to mount your NFS exports, add insecure in extra options or use ``resvport`` in the command line.

	Example::

	$ sudo mount -t nfs -o resvport,rw 192.168.3.1:/export/Videos /private/nfs

Debian
	Debian distributions (and many others) always include the group users with ``gid=100`` by default, if you want to resolve permissions easily for all users of a PC using linux add ``anongid=100`` in extra options. This will force all mounts to use that gid.

Symlinks
	This are not followed outside of their export path, so they have to be relative.

Remote access
	NFS was designed to be used as a local network protocol. Do not expose the NFS server to the Internet. If you still need access use a VPN.

.. [1] https://help.ubuntu.com/community/NFSv4Howto#NFSv4_without_Kerberos
.. [2] https://www.centos.org/docs/5/html/5.1/Deployment_Guide/s3-nfs-server-config-exportfs-nfsv4.html
.. [3] This is not standard |omv| privileges as in the shared folder section
