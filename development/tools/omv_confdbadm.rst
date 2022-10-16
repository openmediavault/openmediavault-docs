omv-confdbadm
#############

Most users tend to access/modify the database by using nano::

	$ nano /etc/openmediavault/config.xml

This is a problem as sometimes a wrong pressed key can add strange chars out of the xml tags and make the database unreadable by the backend.

:command:`omv-confdbadm` is a tool written in python for retrieving, storing or deleting values from/to the database. This tool combined with :command:`jq` [1]_ provides an easier method for interacting with the database using Shell/BASH.

To read values in the database the tool needs as last argument the datamodel path. You can find all data models path here :file:`/usr/share/openmediavault/datamodels/` prefixed with conf. Or list them with :command:`omv-confdbadm list-ids`

Lets read all the registered filesystems that have been mounted through the |webui|. Type the following command as root::

	# omv-confdbadm read --prettify conf.system.filesystem.mountpoint

Output returns:

.. code-block:: json

	[
	    {
	        "dir": "/srv/dev-disk-by-label-ironwolf_3TB_1",
	        "freq": 0,
	        "fsname": "/dev/disk/by-label/ironwolf_3TB_1",
	        "hidden": false,
	        "opts": "defaults,noauto,user_xattr,usrjquota=aquota.user,grpjquota=aquota.group,jqfmt=vfsv0,acl",
	        "passno": 2,
	        "type": "ext4",
	        "uuid": "567c2bd4-3d82-45b2-b34b-a6d38e680ed3"
	    },
	    {
	        "dir": "/media/a448c5e9-7a50-4d48-b73d-48cadbe0326e",
	        "freq": 0,
	        "fsname": "a448c5e9-7a50-4d48-b73d-48cadbe0326e",
	        "hidden": true,
	        "opts": "noauto,",
	        "passno": 0,
	        "type": "fuse.mergerfs",
	        "uuid": "4adf0892-cf63-466f-a5aa-80a152b8dea6"
	    },
	    {
	        "dir": "/export/videos",
	        "freq": 0,
	        "fsname": "/media/a448c5e9-7a50-4d48-b73d-48cadbe0326e/data_general/videos",
	        "hidden": false,
	        "opts": "bind,noauto",
	        "passno": 0,
	        "type": "none",
	        "uuid": "4457831c-309e-4693-8b0d-5db6b257194d"
	    },
	    {
	        "dir": "/export/PVR",
	        "freq": 0,
	        "fsname": "/media/a448c5e9-7a50-4d48-b73d-48cadbe0326e/data_general/videos/pvr",
	        "hidden": false,
	        "opts": "bind,noauto",
	        "passno": 0,
	        "type": "none",
	        "uuid": "dce89b85-f1e1-42e2-8d46-986de599abff"
	    }
	]


The first one is a native ext4 filesystem, the second object is storage pool, the last two are NFS binds.

**Filtering:** Get all filesystem mountpoints::

	# omv-confdbadm read conf.system.filesystem.mountpoint  | jq -r '.[]|.dir'

Output returns::

	/media/dev-disk-by-label-ironwolf_3TB_1
	/media/a448c5e9-7a50-4d48-b73d-48cadbe0326e
	/export/videos
	/export/PVR


**Selecting:** Get all filesystem objects that are registered as ext4::

	# omv-confdbadm read conf.system.filesystem.mountpoint  | jq -r '.[]|select(.type=="ext4")'

Output returns:

.. code-block:: json

	{
	  "opts": "defaults,noauto,user_xattr,usrjquota=aquota.user,grpjquota=aquota.group,jqfmt=vfsv0,acl",
	  "uuid": "567c2bd4-3d82-45b2-b34b-a6d38e680ed3",
	  "passno": 2,
	  "dir": "/media/dev-disk-by-label-ironwolf_3TB_1",
	  "fsname": "/dev/disk/by-label/ironwolf_3TB_1",
	  "freq": 0,
	  "hidden": false,
	  "type": "ext4"
	}


**Write:** This tool can also modify values in the database.

Add the `noexec` flag to this filesystem object ``567c2bd4-3d82-45b2-b34b-a6d38e680ed3``, we need to pass the whole json object as argument::

	# omv-confdbadm update conf.system.filesystem.mountpoint '{"freq":0,"hidden":false,"passno":2,"opts":"defaults,noexec,noauto,user_xattr,usrjquota=aquota.user,grpjquota=aquota.group,jqfmt=vfsv0,acl","dir":"/media/dev-disk-by-label-ironwolf_3TB_1","uuid":"567c2bd4-3d82-45b2-b34b-a6d38e680ed3","fsname":"/dev/disk/by-label/ironwolf_3TB_1","type":"ext4"}'


Remove a filesystem from the database, this time we pass only the corresponding uuid of the object::

	# omv-confdbadm delete --uuid 567c2bd4-3d82-45b2-b34b-a6d38e680ed3 conf.system.filesystem.mountpoint

.. [1] https://stedolan.github.io/jq/manual/v1.5/
