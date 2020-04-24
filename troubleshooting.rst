Troubleshooting
===============


* **Web interface has missing fields and/or items showing that have been uninstalled.**

    Clear your browser cache.

* **I mounted the drive using the command line or GUI tool and I can't pick that drive in the shared folder device dropdown.**

    Never mount a drive with anything other than the |omv| |webui|. This creates the necessary database entries to populate the device dropdown.

* **I only see a few items in the web interface like the user section of Access Rights Management.**

    You did not login as the admin user. This is the only user that can access everything.

* **I get an error every time I post in the forum especially if it is a long post and/or has links to external pages.**

    The error is deceiving. Please don't keep trying to post. The spam filter has flagged your post and it will need to be approved. Please be patient.

* **Samba is slow.**

    Read these threads - `Tuning Samba for more speed <http://forum.openmediavault.org/index.php/Thread/12986-Tunning-Samba-for-more-speed/>`_ and `Tuning Samba for more speed 2 <http://forum.openmediavault.org/index.php/Thread/14615-Tuning-Samba-for-more-speed-2//>`_

* **Samba share password is refused from Windows 10.**

    To fix the problem you need to change the `Network Security LAN Manager authentication level <https://social.technet.microsoft.com/Forums/windows/en-US/8249ad4c-69aa-41ba-8863-8ecd7a7a4d27/samba-share-password-refused>`_.

* **The |webui| keeps rejecting my admin/user password.**

    If the password is correct then this is most likely caused by the rootfs partition being full. This command can help track which folders are the biggest :command:`df -hx --max-depth=1 /`

* **I have problem accessing the |webui| with Firefox.**

    Try the solution mentioned in the `Sencha ExtJS forum <https://www.sencha.com/forum/showthread.php?310206-ExtJ-6-doest-not-work-on-Linux-with-Firefox-45&p=1155250&viewfull=1#post1155250>`_ or the `Mozilla bugtracker <https://bugzilla.mozilla.org/show_bug.cgi?id=1301327>`_.

* **I am using JMicron drive enclosures and some of my drives are not appearing.**

    This is likely because JMicron controllers incorrectly report identical serial numbers and other data which confuses various systems.

    You can "fix" this by adding a rule to :file:`/lib/udev/rules.d/60-persistent-storage.rules` after the entry for "Fall back usb_id for USB devices"::

        # JMicron drive fix
        KERNEL=="sd*", ENV{ID_VENDOR}=="JMicron", SUBSYSTEMS=="usb", PROGRAM="/root/serial.sh %k", ENV{ID_SERIAL}="USB-%c", ENV{ID_SERIAL_SHORT}="%c"
    
    You will also need to create :file:`/root/serial.sh` containing the following::

        #!/bin/bash
        /sbin/hdparm -I /dev/$1 | grep 'Serial Number' | awk '{print $3}'

    This will ensure that unique paths are created based on the serial number of the actual drives and not the enclosures.
    
        Just in case the udev rule above will not work, replace the ENV{ID_VENDOR}=="JMicron" parameter with ATTRS{idVendor} and ATTRS{idProduct} data coming from lsusb command output as follows (example coming from JMicron JM20337 USB PATA/SATA bridge chipset):
    
        KERNEL=="sd*", ATTRS{idVendor}=="152d", ATTRS{idProduct}=="2338", SUBSYSTEMS=="usb", PROGRAM="/root/serial.sh %k", ENV{ID_SERIAL}="USB-%c", ENV{ID_SERIAL_SHORT}="%c"

