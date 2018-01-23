Disks
#####

An overview of all physical disks attached to the server. Displays basic information to identify disks, such as: manufacturer, model, serial number and capacity. A hidden column also displays the linux block device identification symlinks ``/dev/disk/{by-id,by-path,by-uuid}``.

Be aware that when attaching disks via USB (A docking station, cage, adapter, etc) the internal disk information will not pass, the backend will display probably the USB-SATA controller information. The capacity should remain the same. This is a response given by the backend with ``DiskMgnt::getList`` service-method using a rock64 SBC board with a docking station attached via the USB 3.0 port:

.. code-block:: json

	{  
	   "response":{  
	      "total":3,
	      "data":[  
	         {  
	            "devicename":"mmcblk1",
	            "devicefile":"/dev/mmcblk1",
	            "devicelinks":[  
	               "/dev/disk/by-id/mmc-SL16G_0x0091d901",
	               "/dev/disk/by-path/platform-ff500000.dwmmc"
	            ],
	            "model":"",
	            "size":"15931539456",
	            "description":"n/a [/dev/mmcblk1, 14.83 GiB]",
	            "vendor":"",
	            "serialnumber":"",
	            "israid":false,
	            "isroot":true
	         },
	         {  
	            "devicename":"sda",
	            "devicefile":"/dev/sda",
	            "devicelinks":[  
	               "/dev/disk/by-path/platform-xhci-hcd.8.auto-usb-0:1:1.0-scsi-0:0:0:0",
	               "/dev/disk/by-id/usb-USB_3.0_HDD_Docking_Station_2017101701E0-0:0"
	            ],
	            "model":"",
	            "size":"500107862016",
	            "description":"n/a [/dev/sda, 465.76 GiB]",
	            "vendor":"USB 3.0",
	            "serialnumber":"2017101701E0",
	            "israid":false,
	            "isroot":false
	         },
	         {  
	            "devicename":"sdb",
	            "devicefile":"/dev/sdb",
	            "devicelinks":[  
	               "/dev/disk/by-id/usb-USB_3.0_HDD_Docking_Station_2017101701E0-0:1",
	               "/dev/disk/by-path/platform-xhci-hcd.8.auto-usb-0:1:1.0-scsi-0:0:0:1"
	            ],
	            "model":"",
	            "size":"2000398934016",
	            "description":"n/a [/dev/sdb, 1.81 TiB]",
	            "vendor":"USB 3.0",
	            "serialnumber":"2017101701E0",
	            "israid":false,
	            "isroot":false
	         }
	      ]
	   },
	   "error":null
	}

Notice here ``sdb`` and ``sda`` both disks show same serial number and that is incorrect. There is no vendor and model shows as "USB 3.0".

In this cases you can access the disk information in the SMART section, not the grid but the information button. External portable USB hard drives should display information normally.

Power Options
^^^^^^^^^^^^^

Pressing the edit button with a selected disk will give the following options available to set:

	- Advanced power management (APM)
	- Automatic accoustic management (Not all drives support this)
	- Spindown time (ST)
	- Write cache

All the above options are configured using hdparm [1]_. The APM values from the interface are resumed in
seven steps with a small description to make it easier for the user to select. If you want to experiment with intermediate values then
you can edit :file:`/etc/openmediavault/config.xml` find this xpath ``/storage/hdparm``, change the values for the disk, finally run::

$ omv-mkconf hdparm

Reboot, check if APM has been set with::

$ hdparm -I /dev/sdX

When setting a spindown time make sure APM is set bellow 128, otherwise it will not work. The web framework does 
not narrow the APM options if spin down time is set, or disables the spindown menu when a value higher than 128 is selected.

.. note::
	For changes to be permanent, settings are stored in this file :file:`/etc/hdparm.conf`, however those settings are 
	applied using a ``UDEV ADD+`` that executes :file:`/lib/udev/hdparm` which parses that file. For changes to be applied 
	inmediatly server needs to be suspended/resumed or rebooted.

Wipe
^^^^

If you need to erase data from your disks, you can use this button. It gives the secure or quick option.

The quick option basically erases the partition table and signatures (MBR or GPT) by using this command::

$ sgdisk --zap-all /dev/sdX

After that it ensures is clean by using dd::

$ dd if=/dev/zero of=/dev/sdX bs=4M count=1

Which erases the beggining of the disk.

The secure mode will rewrite the block device entirely. This process takes a long time and is only one iteration. It uses this command::

$ shred -v -n 1 /dev/sdX


.. [1] https://linux.die.net/man/8/hdparm