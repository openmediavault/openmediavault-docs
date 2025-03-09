Filesystems
###########

Overview
	The filesystem section of the |omv| |webui| is where you integrate disk volumes to be part of the server. Drives/filesystems that are not mounted through the |webui| are not registered in the backend database, this means you cannot use volumes to create shared folders if they were not mounted properly. *This is very important*, users that come from an existing debian installation with filesystems already present in their fstab file will see that no volumes will be available for creating shared folders even if they are mounted. For the disks to be properly integrated it is better to delete all fstab lines except rootfs and swap, reboot your server and start mounting the disks through the |webui|.

	The mount process acts like many other services in |omv|, first it writes a database entry in ``config.xml``, this entry contains essential information:

	- UUID of the database object `<uuid>`
	- Predictable device path of the filesystem `<fsname>`
	- Target mount directory `<dir>`
	- Filesystem options `<opts>`
	- Filesystem type (EXT3, EXT4, etc.) `<type>`

	You can inspect a `mntent` entry in ``config.xml`` located in ``/etc/openmediavault/``, it should look like this:

	.. code-block:: xml

		<mntent>
			<uuid>f767ee54-eb3a-44c5-b159-1840a289c84b</uuid>
			<fsname>/dev/disk/by-label/VOLUME1</fsname>
			<dir>/srv/dev-disk-by-label-VOLUME1</dir>
			<type>ext4</type>
			<opts>defaults,nofail,user_xattr,usrjquota=aquota.user,grpjquota=aquota.group,jqfmt=vfsv0,acl</opts>
			<freq>0</freq>
			<passno>2</passno>
			<hidden>0</hidden>
		</mntent>

	With the `mntent` entry in ``config.xml``, :command:`omv-salt deploy run fstab` script writes the appropriate line in ``/etc/fstab``. You can identify entries in ``/etc/fstab`` created by the |webui| by looking at «openmediavault» tags. It is important to mention to not alter the information in between these tags. If you delete or modify a fstab option (`noexec` or `quota` for example) the next time you mount a new disk into the server, :command:`omv-salt deploy run fstab` will deploy the original value there again. If you need persistent change use :doc:`environmental variables </various/fs_env_vars>`. Finally the backend will proceed to mount the filesystem. After this the volume is ready for creating shared folders.

Resize
	The resize button is used for expanding filesystems. This can occur if you decide to resize a disk partition or you have grown a RAID array by adding one or more disks.

Delete
	The delete button actually deletes filesystems, using :command:`wipefs -a`. This will flush filesystem, raid or partition-table signatures (magic strings). Be careful using this. The button is disabled until the filesystem is actually unmounted.

Unmount
	Disabled until you have deleted all shared folders associated with that volume. Unmount will remove the entry from ``config.xml`` and ``/etc/fstab``.

Supported Filesystems
	|omv| supports the following filesystems that can be mounted through the |webui|:


.. csv-table:: |omv| supported filesystems
   :header: "Type", "Format", "Mount"
   :widths: 5, 5, 5

    btrfs,yes,yes
    exfat,no,yes
    ext3,yes,yes
    ext4,yes,yes
    f2fs,yes,yes
    hfsplus,no,yes
    iso9660,no,yes
    jfs,yes,yes
    msdos,no,yes
    ntfs,no,yes
    udf,no,yes
    ufs,no,yes
    umsdos,no,yes
    vfat,no,yes
    xfs,yes,yes
    zfs,no,no

.. note::
	BTRFS
		- Creating multi device filesystems is not supported in the |webui|. However you can add devices to your btrfs array in CLI and it will not present any problems.
		- No extra features of btrfs are available in the webui like snapshots or subvolumes. Additional subvolumes will have either be mounted outside of the OMV fstab tags or manually add mntent entries to config.xml or use advanced configuration

.. note::
	ZFS
		Support for ZFS is available through `ZoL <http://zfsonlinux.org/>`_ and requires the use of a third party plugin provided by omv-extras. This includes code added to the OMV filesystem backend. The plugin allows you to create shared folders for ZFS volumes. On AMD64, if ZFS support is desired, it is recommended to first use omv-extras install the third-party openmediavault-kernel plugin and use that to install the ProxMox (PVE) kernel, which has precompiled support for ZFS and may improve stability. After that, install the ZFS plugin.
