Internal Tools
##############

|omv| software comes with several terminal command line tools that can be used by developers and/or advanced users. Also it can be used to gather support information.


omv-confdbadm (Database)
^^^^^^^^^^^^^^^^^^^^^^^^

Most users tend to access/modify the database by using nano::

$ nano /etc/openmediavault/config.xml

This is a problem as sometimes a wrong pressed key can add strange chars out of the xml tags and make the database unreadable by the backend. 

omv-confdbadm is a tool written in python for retrieving, storing or deleting values from/to the database. This tool combined with jq [1]_ provides an easier method for interacting with the database using Shell/BASH.

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
	    },

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

Add the noexec flag to this filesystem object ``567c2bd4-3d82-45b2-b34b-a6d38e680ed3``, we need to pass the whole json object as argument::

	# omv-confdbadm update conf.system.filesystem.mountpoint '{"freq":0,"hidden":false,"passno":2,"opts":"defaults,noexec,noauto,user_xattr,usrjquota=aquota.user,grpjquota=aquota.group,jqfmt=vfsv0,acl","dir":"/media/dev-disk-by-label-ironwolf_3TB_1","uuid":"567c2bd4-3d82-45b2-b34b-a6d38e680ed3","fsname":"/dev/disk/by-label/ironwolf_3TB_1","type":"ext4"}'


Remove a filesystem from the database, this time we pass only the corresponing uuid of the object::

	# omv-confdbadm delete --uuid 567c2bd4-3d82-45b2-b34b-a6d38e680ed3 conf.system.filesystem.mountpoint


omv-rpc
^^^^^^^

This tool can execute rpc commands. This is identical of what the web frontend uses to set/get information. It accepts service, method and parameters. RPC services can be found listed in `engined/rpc folder <https://github.com/openmediavault/openmediavault/tree/master/deb/openmediavault/usr/share/openmediavault/engined/rpc>`_

**Example 1:** Get all mounted filesystems, including rootfs::

 # omv-rpc -u admin 'FileSystemMgmt' 'enumerateMountedFilesystems' '{"includeroot": true}' 

Output returns:

.. code-block:: json

 [
  {
    "devicefile": "/dev/sda1",
    "parentdevicefile": "/dev/sda",
    "uuid": "752dee88-11a3-4524-848e-d50baf0211a2",
    "label": "",
    "type": "ext4",
    "blocks": "9738548",
    "mountpoint": "/",
    "used": "5.44 GiB",
    "available": "3595554816",
    "size": "9972273152",
    "percentage": 62,
    "description": "/dev/sda1 (3.34 GiB available)",
    "propposixacl": true,
    "propquota": true,
    "propresize": true,
    "propfstab": true,
    "propcompress": false,
    "propautodefrag": false,
    "hasmultipledevices": false,
    "devicefiles": [
      "/dev/sda1"
    ]
  },
  {
    "devicefile": "dfa",
    "parentdevicefile": null,
    "uuid": null,
    "label": "dfa",
    "type": "zfs",
    "blocks": 901386.24,
    "mountpoint": "/dfa",
    "used": "5.26 MiB",
    "available": 917504000,
    "size": 923019509.76,
    "percentage": 0,
    "description": "dfa (875.00 MiB available)",
    "propposixacl": true,
    "propquota": false,
    "propresize": false,
    "propfstab": false,
    "propcompress": false,
    "propautodefrag": false,
    "hasmultipledevices": false,
    "devicefiles": "dfa"
  },
  {
    "devicefile": "/dev/sdg1",
    "parentdevicefile": "/dev/sdg",
    "uuid": "b50987a4-f111-4e94-a52e-9e6b204ac227",
    "label": "vol3",
    "type": "ext4",
    "blocks": "2030396",
    "mountpoint": "/srv/dev-disk-by-label-vol3",
    "used": "6.01 MiB",
    "available": "2056044544",
    "size": "2079125504",
    "percentage": 1,
    "description": "vol3 (1.91 GiB available)",
    "propposixacl": true,
    "propquota": true,
    "propresize": true,
    "propfstab": true,
    "propcompress": false,
    "propautodefrag": false,
    "hasmultipledevices": false,
    "devicefiles": [
      "/dev/sdg1"
    ]
  }
 ]



**Example 2:** Get all block devices with no filesystem signatures. This is used by the RAID creation window::

	# omv-rpc -u admin 'RaidMgmt' 'getCandidates' | jq


Output returns:

.. code-block:: json

 [
  {
    "devicefile": "/dev/mapper/vg-lv1",
    "size": "1296039936",
    "vendor": "",
    "serialnumber": "",
    "description": "LVM logical volume lv1 [/dev/mapper/vg-lv1, 1.20 GiB]"
  },
  {
    "devicefile": "/dev/mapper/vg-lv1",
    "size": "1296039936",
    "vendor": "",
    "serialnumber": "",
    "description": "LVM logical volume lv1 [/dev/mapper/vg-lv1, 1.20 GiB]"
  },
  {
    "devicefile": "/dev/sde",
    "size": "1610612736",
    "vendor": "QEMU",
    "serialnumber": "drive-scsi5",
    "description": "QEMU HARDDISK [/dev/sde, 1.50 GiB]"
  },
  {
    "devicefile": "/dev/sdf",
    "size": "2147483648",
    "vendor": "QEMU",
    "serialnumber": "drive-scsi4",
    "description": "QEMU HARDDISK [/dev/sdf, 2.00 GiB]"
  },
  {
    "devicefile": "/dev/sdj",
    "size": "1073741824",
    "vendor": "ATA",
    "serialnumber": "QM00009",
    "description": "QEMU HARDDISK [/dev/sdj, 1.00 GiB]"
  }
 ]


The jq tools is used to prettify the output in json.

helper-functions (Shell)
^^^^^^^^^^^^^^^^^^^^^^^^


|omv| ships with this file :file:`/usr/share/openemdiavault/scripts/helper-functions` that contains several POSIX shell functions. This are intended to make it easier for developers to create mkconf or postinst/postrm scripts. To test them just run in terminal::
 
 $ source /usr/share/openmediavault/scripts/helper-functions

Type ``omv_``, press tab key to autocomplete, this will show all functions and a small description in the name.

**Example 1:** Shared folders objects in the database do not have their complete absolute path, it has to be constructed from the relative directory and the parent filesystem. If we know the shared folder database object <uuid> then::

	$ omv_get_sharedfolder_path 2a8b04de-4e6c-4675-b761-1ddfabde2d2a

Returns::

	/media/dev-disk-by-label-VOLUME1/Videos/Unsorted

**Example 2:** Database nodes need to be created when a plugin is installed and removed when is purged. This is from omvextras MiniDLNA plugin `postinst file <https://github.com/OpenMediaVault-Plugin-Developers/openmediavault-minidlna/blob/master/debian/postinst>`_ ::

	omv_config_add_node "/config/services" "${SERVICE_XPATH_NAME}"
	omv_config_add_key "${SERVICE_XPATH}" "enable" "0"
	omv_config_add_key "${SERVICE_XPATH}" "name" "MiniDLNA Server on OpenMediaVault"
	omv_config_add_key "${SERVICE_XPATH}" "port" "8200"
	omv_config_add_key "${SERVICE_XPATH}" "strict" "0"
	omv_config_add_key "${SERVICE_XPATH}" "tivo" "0"
	omv_config_add_key "${SERVICE_XPATH}" "rootcontainer" "."
	omv_config_add_node "${SERVICE_XPATH}" "shares"
	omv_config_add_key "${SERVICE_XPATH}" "loglevel" "error"
	omv_config_add_key "${SERVICE_XPATH}" "extraoptions" ""


Notice in the postint file how it sources at the beginning ``helper-functions``. The same happens in `mkconf scripts <https://github.com/openmediavault/openmediavault/tree/master/deb/openmediavault/usr/share/openmediavault/mkconf>`_ .

.. note::
	What each function do and the parameters it accepts is documented in the `helper-functions file <https://github.com/openmediavault/openmediavault/blob/master/deb/openmediavault/usr/share/openmediavault/scripts/helper-functions>`_ .


.. [1] https://stedolan.github.io/jq/manual/v1.5/
