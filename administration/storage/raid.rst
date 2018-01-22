RAID
####

|omv| uses linux software RAID driver (MD) and the mdadm utility to create arrays [1]_. Arrays created in any other linux distro should be recognized inmmediatly by the server. In most cases you can skip to the filesystem array and proceed to mount to integrate the filesystem into the database.

Overview
--------

The grid panel shows all currently available MD arrays. There is no internal database section for RAID arrays, so every arrays that is assembled in the server should be displayed here.

Create
	The following table displays levels available in the |webui|:

	.. csv-table:: RAID
	   :header: "Level", "Name", "Min. Disks", "Redundancy", "Growable"
	   :widths: 3, 3, 3, 3, 3

	   "Linear", "JBOD", "2", "No", "No"
	   "0", "Stripe", "2", "No", "No"
	   "1", "Mirror", "2", "Yes", "Yes"
	   "5", "RAID5", "3", "Yes", "Yes"
	   "6", "RAID6", "4", "Yes", "Yes"
	   "10", "Stripped Mirror", "4", "Yes", "No"

.. note::
	* RAID4 and FAULTY levels are not supported in the |webui|.
	* RAID1+0 is possible by stripping two mirrors. The create window should display both mirrors if they do not have any filesystem signatures yet.

Detail
	Displays extended information of the array the output comes from :command:`mdadm –detail /dev/mdX`
Grow
	Add disk(s) into the array.
Recover
	If the array comes from another linux server you can use this button to reassemble the array in the current server
Remove
	This is used to remove failed disks, in case one needs be replaced.
Delete
	Stop the array and zero the superblock all devices conforming the array (script :command:`/usr/sbin/omv-rmraid`). Use with caution.

Mdadm works better with unpartitioned disks, plain raw block devices. Before creating MD RAID in your system make sure disks are clean before. In the physical disk section you can perform a quick or full wipe. Quick wipe is enough to delete partition tables.

Degraded array creation in not possible in the |webui|, however the array can be created in terminal using mdadm if you want for example to convert a RAID from level 1 to 5 or 6.

Mail notifications are integrated for mdadm, these are sent everytime an array enters degraded state.

Growing
-------

Before growing array is better to clean the partition table of the new disk, specially if the disk was used before in another mdadm array, erase also the superblock::

$ mdadm --zero-superblock /dev/sdX

After adding a disk to the array, the re-syncthing process will begin inmediatly. Depending on the size of the disks this process can take several hours or even days, this is because mdadm tries to balance resources and keep usability of the system not using high CPU and RAM. To speed the process::

$ echo ${value} > /proc/sys/dev/raid/speed_limit_min #value is interpreted as kbytes/seconds

After synthing is finish is necessary to expand the filesystem usinn the resize button.

.. warning::

	* If your MD array and filesystem was created with |omv| or Debian before December 2014, then please read :doc:`here <filesystems>`.
	* Do not use RAID arrays in production with drives connected via USB, neither hubs or different ports. This includes low power devices that do not have a SATA controller, e.g. Raspberry Pi, Pogoplugs and any low entry ARM SBC.

.. [1] https://raid.wiki.kernel.org/index.php/Linux_Raid
