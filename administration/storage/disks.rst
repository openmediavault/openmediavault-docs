Disks
#####

An overview of all physical disks attached to the server. Displays basic information to identify disks, such as: manufacturer, model, serial number and capacity. A hidden column also displays the linux block device identification symlinks :file:`/dev/disk/{by-id,by-path,by-uuid}`.

Be aware that when attaching disks via USB (a docking station, cage, adapter, etc.) the internal disk information will not pass, the backend will display probably the USB-SATA controller information. The capacity should remain the same. This is a response given by the backend with ``DiskMgnt::getList`` service-method using a rock64 SBC board with a docking station attached via the USB 3.0 port:

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

All the above options are configured using smartmontools [1]_. The APM values from the interface are resumed in
seven steps with a small description to make it easier for the user to select. If you want to experiment with intermediate values that are not supported via the UI, then
you can edit the :file:`/etc/openmediavault/config.xml` by editing the XPath ``/system/storage/hdparm``, change the values for the disk, and finally run::

$ omv-salt deploy run smartmontools

When setting a spin down time make sure APM is set bellow 128, otherwise it will not work. The UI does
not narrow the APM options if spin down time is set, or disables the spin down menu when a value higher than 128 is selected.

.. note::
	For changes to be permanent, settings are stored in files that are located in :file:`/etc/smartmontools/hdparm.d/`. You can add custom files there according to the `README <https://github.com/openmediavault/openmediavault/blob/714f214346ff2e04c5ed2003628107e12c6ab29a/deb/openmediavault/etc/smartmontools/hdparm.d/README.md>`_.
	To apply the settings, run the command ``systemctl restart smartctl-hdparm.service``.

Wipe
^^^^

If you need to erase data from your disks, you can use this button. It gives the secure or quick option.

The quick option basically erases the partition table and signatures (MBR or GPT) by using this command::

$ sgdisk --zap-all /dev/sdX

After that it ensures is clean by using dd::

$ dd if=/dev/zero of=/dev/sdX bs=4M count=1

Which erases the beginning of the disk.

The secure mode will rewrite the block device entirely. This process takes a long time and is only one iteration. It uses this command::

$ shred -v -n 1 /dev/sdX


.. [1] https://www.smartmontools.org/
