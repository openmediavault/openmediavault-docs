Filesystems
###########


Overview
	The filesystem section of the |omv| web interface is where you integrate disk volumes to be part of the server. Drives/filesystems that are not mounted through the web interface are not registered in the backend database, this means you cannot use volumes to create shared folders if they were not mounted properly. *This is very important*, users that come from an existing debian installation with filesystems already present in their fstab file will see that no volumes will be available for creating shared folders even if they are mounted. For the disks to be properly integrated is better that you delete all fstab lines execept rootfs and swap, reboot your server and start mounting the disks through the web interface.

	The mount process acts like many other services in |omv|, first it writes a database entry in config.xml, this entry contains essential information:

	- UUID of the mounted entry inside config.xml <uuid>
	- Predictable device path of the filesystem  <fsname>
	- Target mount directory <dir>
	- Filesystem options <opts>
	- Filesystem type (ext3, ext4, etc) <type>
	
	You can inspect a mntent entry in config.xml it should look like this:

	.. code-block:: xml

		<mntent>
			<uuid>f767ee54-eb3a-44c5-b159-1840a289c84b</uuid>
			<fsname>/dev/disk/by-label/VOLUME1</fsname>
			<dir>/srv/dev-disk-by-label-VOLUME1</dir>
			<type>ext4</type>
			<opts>defaults,nofail,user_xattr,noexec,usrjquota=aquota.user,grpjquota=aquota.group,jqfmt=vfsv0,acl</opts>
			<freq>0</freq>
			<passno>2</passno>
			<hidden>0</hidden>
		</mntent>

	With the mntent entry in config.xml, mkconf fstab script writes the appropiate line in ``/etc/fstab``. You can indentify entries in ``/etc/fstab`` created by the web interface by looking at «openmediavault» tags. Is important to mention to not alter the information in bewteen these tags. If you delete or modify a fstab option (noexec or quota for example) the next time you mount a new disk into the server, the mkconf will pipe the original value there again. If you need persistent change read :doc:`here </various/fs_env_vars>`. Finally the backend will proceed to mount the filesystem. After this the volume is ready for creating shared folders.

Resize
	The resize button is used for exanding filesystems. This can ocurr if you decide to resize a disk partition or you have grown a RAID array.

.. warning::
	Filesystems greater than 16TB in ext4
		The default mkfs.ext4 of Debian Wheezy does not use the 64bit flag for filesystems under 16TB, this is a serious problem since RAID arrays without that flag won't be able to expand and there is no workaround more than reformat.
		Version 1.8 introduced the flag as default for newly created ext4 filesystems, independant of the size. However the current resize2fs tool in Debian Wheezy cannot handle the flag for expanding the size, so you need newer version of e2fsprogs. For avoiding recompiling the package, you can boot systemrescuecd and perform the expansion using gparted.

Delete
	The delete button actually deletes filesystems, using wipefs -a. This will flush filesystem, raid or partition-table signatures (magic strings). Be careful using this. The button is disabled until the filesystem is actually unmounted.

Unmount
	Disabled until you have deleted all shared folders asociated with that volume. Unmount will remove the entry from config.xml and /etc/fstab.

Supported Filesystems
	|omv| supports the following filesystems that can be mounted through the web interface:


.. csv-table:: |omv| supported filesystems
   :header: "Type", "Format", "Mount"
   :widths: 5, 5, 5

	ext4,yes,yes
	ext3,yes,yes
	jfs,yes,yes
	xfs,yes,yes
	btrfs,yes,yes
	zfs,no,no
	ntfs,no,yes
	hfsplus,no,yes
	ufs,no,yes
	vfat,no,yes

.. note::
	BTRFS
		- Creating multi device filesystems is not supported in the web interface. However you can add devices to your btrfs array in CLI and it will not present any problems.
		- No extra features of btrfs are available in the webui like snapshots or subvolumes. Additional subvolumes will have either be mounted outside of the OMV fstab tags or manually add mntent entries to config.xml or use advanced configuration

.. note::
	ZFS
		Support for zfs is available through `ZoL <http://zfsonlinux.org/>`_ an uses a third party plugin provided by omv-extras. The development of the plugin was done in conjunction with core of |omv|, so new code was added in the filesystem backend to improve support for zfs. The plugin registers datasets and pools in the internal database so you can create shared folders for zfs volumes. The creation of zvols is automatically recognized by |omv| so you can format them and mount them in the web interface. The iscsiplugin can also use these zvols block devices to export LUN's.


