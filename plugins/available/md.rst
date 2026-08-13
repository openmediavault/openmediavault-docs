MD
##

Overview
--------

The `openmediavault-md` plugin adds support for Multiple Device (MD)
software RAID arrays to |omv|, letting you create, grow, recover and
monitor them using the `mdadm <https://en.wikipedia.org/wiki/mdadm>`_
utility under the hood.

After installation, the service is available in the navigation menu under
`Storage | Multiple Device`.

Actions
-------

The following actions are available for a RAID device via the toolbar:

* **Create**: Create a new RAID device from two or more selected devices.
* **Add**: Grow an existing array by adding one or more devices to it.
* **Remove**: Mark one or more devices as failed and remove them from the
  array, e.g. to replace a faulty disk.
* **Recover**: Add a replacement device to a degraded array to rebuild it,
  or add a spare device to a healthy array.
* **Maintenance**: Only available for redundant RAID levels (e.g. Mirror/
  RAID 1, RAID 5, RAID 6, RAID 10). Check the array for inconsistencies,
  repair them, or stop a running check/repair action. A running repair
  writes data while it runs, so avoid powering off or rebooting the system
  until it has finished; use the *Stop* action instead if it needs to be
  interrupted.
* **Show details**: Display detailed information about the selected array.
* **Delete**: Delete the selected RAID device.
