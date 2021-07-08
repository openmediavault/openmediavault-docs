omv-rpc
#######

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

The :command:`jq` tool is used to prettify the output in JSON.
