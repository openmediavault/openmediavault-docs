Prerequisites
=============

Before installing |omv| make sure your hardware is supported.

* **CPU**: Any x86-64 or ARM compatible processor
* **RAM**: 1 GiB capacity
* **HDD**:

  * **System Drive**: min. 4 GiB capacity
  * **Data Drive**: capacity according to your needs

.. note::
   The whole disc will be occupied by the system and swap space [1]_, so size
   doesn't matter so much. Data storage on the system disc is not supported.

Spinning Harddisk, SSD [2]_, Disk-on-Module [3]_, CompactFlash [4]_ or USB thumb
drive [5]_ type drives can be used as system drive.

If you use a Flash Drive, select one with static wear leveling [6]_, without
this the drive will have a very short lifetime. It is also recommended to
install and activate the :ref:`Flash Memory plugin <plugin_3rd_party>`. The
entire disk is used as system disk and can not be used to store user data.

.. [1] https://en.wikipedia.org/wiki/Paging
.. [2] https://en.wikipedia.org/wiki/Solid-state_drive
.. [3] https://en.wikipedia.org/wiki/Solid-state_drive#DOM
.. [4] https://en.wikipedia.org/wiki/CompactFlash
.. [5] https://en.wikipedia.org/wiki/USB_flash_drive
.. [6] https://en.wikipedia.org/wiki/Wear_leveling
