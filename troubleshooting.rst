Troubleshooting
===============


* **The web interface has missing fields and/or items showing that have been uninstalled.**

    Clear your browser cache.

* **The web interface keeps rejecting my admin/user password.**

    If the password is correct then this is most likely caused by the rootfs partition being full. This command can help track which folders are the biggest :command:`df -hx --max-depth=1 /`

* **I only see a few items in the web interface interface like the user section of Access Rights Management.**

    You did not login as the admin user. This is the only user that can access everything.

* **I get an error every time I post in the forum especially if it is a long post and/or has links to external pages.**

    The error is deceiving. Please don't keep trying to post. The spam filter has flagged your post and it will need to be approved. Please be patient.

* **I mounted the drive using the command line or GUI tool and I can't pick that drive in the shared folder device dropdown.**

    Never mount a drive with anything other than the |omv| |webui|. This creates the necessary database entries to populate the device dropdown.

* **Samba is slow.**

    Read these threads

	- `read/write performance for SMB shares hosted on RPi4 <https://forum.openmediavault.org/index.php?thread/37285-rpi4-read-write-performance-for-smb-shares/&postID=260232#post260232>`_
	- `Tuning Samba for more speed <http://forum.openmediavault.org/index.php/Thread/12986-Tunning-Samba-for-more-speed/>`_ (note: written for OMV 2.x)
	- `Tuning Samba for more speed 2 <http://forum.openmediavault.org/index.php/Thread/14615-Tuning-Samba-for-more-speed-2//>`_ (note: written for OMV 2.x)

* **Samba share password is refused from Windows 10.**

    To fix the problem you need to change the `Network Security LAN Manager authentication level <https://social.technet.microsoft.com/Forums/windows/en-US/8249ad4c-69aa-41ba-8863-8ecd7a7a4d27/samba-share-password-refused>`_.


* **How to troubleshoot an error caused by an "Option" parameter passed to a plug-in**

    To find the root cause, run the faulty systemd unit file yourself by executing:
	#
	systemd restart <plug-in-daemon>

	If output of <plug-in> is now more vebose, then you will get a hint on STDOUT. If not, then you need to run journalctl -f in parallel to get the syslog output. Admittedly, not really novice friendly, but it's really not possible to do it any other way. OMV always tries to be as error/debug friendly as possible; by default.

* **I am using JMicron drive enclosures and some of my drives are not appearing.**

    This is likely because JMicron controllers incorrectly report identical serial numbers and other data which confuses various systems.
    |omv| provides an `UDEV rules database <https://github.com/openmediavault/openmediavault/pull/746>`_ which will fix that issue for several USB PATA/SATA bridge controllers.
    If your hardware still does not work, then please provide the information mentioned in that pull request and open a new tracker issue.

    Alternatively you can manually "fix" this by adding a rule to :file:`/lib/udev/rules.d/60-persistent-storage.rules` after the entry for "Fall back usb_id for USB devices"::

        # JMicron drive fix
        KERNEL=="sd*", ENV{ID_VENDOR}=="JMicron", SUBSYSTEMS=="usb", PROGRAM="serial_id %N", ENV{ID_SERIAL}="USB-%c", ENV{ID_SERIAL_SHORT}="%c"

    This will ensure that unique paths are created based on the serial number of the actual drives and not the enclosures.
