SMART
#####

Modern hard disks drives (and SSD's) have firmware inside that reports several attributes (usually called S.M.A.R.T values) through sensors that are relevant to assess the device condition. Those values and what they mean are explained by `here <https://en.wikipedia.org/wiki/S.M.A.R.T.>`_. Not all drives report the same amount of attributes, but all of them report some common ones which are known to be the best for assessing health [1]_.

There are several tools for accessing those attributes. |omv| reads and monitors hard drives smart values using smartmontools [2]_.

Notifications are integrated with smartmontools. Changes in S.M.A.R.T values are reported via mail.

General
-------

This enables smartd (SMART daemon). The daemon will periodically check disks attributes and compare them with previous check. You can select the daemon not to poll information if the disks are in certain power state.

Temperature is a very critical attribute. Select the desired limits for smart monitoring to report on changes [3]_.

Devices
-------
The grid displays all current block devices in the system with SMART capabilities. From this grid by selecting a drive you can configure if you want smartmontools to watch and inform for any SMART attributes changes during uptime using the edit button.

Smartmontools is configured in this file :file:`/etc/smartd.conf`.

The information button displays several tabs which provide friendly parsed information about the drive. The last tab has all the information in raw text.

The grid columns shows different identification values for the drive, the last one (Status) reports a green icon if drive is in good condition or red if drive needs some attention, if you hover on the icon a tooltip that will report more details. The code that reports the red icon is based on this function `here <https://github.com/openmediavault/openmediavault/blob/9ddc8b66f3f666987157a0e7b84d57e7c10f9ba4/deb/openmediavault/usr/share/php/openmediavault/system/storage/smartinformation.inc#L93-L98>`_ and `here <https://github.com/openmediavault/openmediavault/blob/9ddc8b66f3f666987157a0e7b84d57e7c10f9ba4/deb/openmediavault/usr/share/php/openmediavault/system/storage/smartinformation.inc#L235-L262>`_, so basically the red icon will be triggered only on attributes with the prefailure (P) flag when:

- Any attribute (P) current value is equal or less than threshold --> Bad attribute now

- The attribute (P) worst value is equal or less the threshold value --> Bad attribute in the past

- Reallocated_Sector_Ct (``id=5``) and Current_Pending_Sector (```id=197``) raw attributes values report more than 1 --> Bad sector

.. note::

	Do not enable SMART for a virtual block device (Virtualbox, Proxmox or ESXi) and expect to get reports of SMART values.

Scheduled tests
---------------

Gives an option to select four different scheduled tests:

- Short self-test
- Long self-test
- Conveyance self-test
- Offline inmediate

These tests and what they do are explained `here <https://www.smartmontools.org/wiki/TocDoc#SMARTTesting>`_ and `here <https://www.thomas-krenn.com/en/wiki/SMART_tests_with_smartctl#Long_Test>`_.

SMART only reallocates a bad sector on write. A manual method to force reallocating the pending(s) sector(s) is described `here <https://www.thomas-krenn.com/en/wiki/Analyzing_a_Faulty_Hard_Disk_using_Smartctl>`_.

.. [1] https://www.backblaze.com/blog/what-smart-stats-indicate-hard-drive-failures/
.. [2] https://www.smartmontools.org/
.. [3] https://www.backblaze.com/blog/hard-drive-temperature-does-it-matter/
