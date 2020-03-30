Troubleshooting
===============


:P: Web interface has missing fields and/or items showing that have been uninstalled.
:S: Clear your browser cache.

..

:P: I mounted the drive using the command line or GUI tool and I can't pick that drive in the shared folder device dropdown.
:S: Never mount a drive with anything other than the |omv| |webui|. This creates the necessary database entries to populate the device dropdown.

..

:P: I only see a few items in the web interface like the user section of Access Rights Management.
:S: You did not login as the admin user. This is the only user that can access everything.

..

:P: I get an error every time I post in the forum especially if it is a long post and/or has links to external pages.
:S: The error is deceiving. Please don't keep trying to post. The spam filter has flagged your post and it will need to be approved. Please be patient.

..

:P: Samba is slow.
:S: Read these threads - `Tuning Samba for more speed <http://forum.openmediavault.org/index.php/Thread/12986-Tunning-Samba-for-more-speed/>`_ and `Tuning Samba for more speed 2 <http://forum.openmediavault.org/index.php/Thread/14615-Tuning-Samba-for-more-speed-2//>`_

..

:P: Samba share password is refused from Windows 10.
:S: To fix the problem you need to change the `Network Security LAN Manager authentication level <https://social.technet.microsoft.com/Forums/windows/en-US/8249ad4c-69aa-41ba-8863-8ecd7a7a4d27/samba-share-password-refused>`_.

..

:P: The |webui| keeps rejecting my admin/user password.
:S: If the password is correct then this is most likely caused by the rootfs partition being full. This command can help track which folders are the biggest :command:`df -hx --max-depth=1 /`

..

:P: I have problem accessing the |webui| with Firefox.
:S: Try the solution mentioned in the `Sencha ExtJS forum <https://www.sencha.com/forum/showthread.php?310206-ExtJ-6-doest-not-work-on-Linux-with-Firefox-45&p=1155250&viewfull=1#post1155250>`_ or the `Mozilla bugtracker <https://bugzilla.mozilla.org/show_bug.cgi?id=1301327>`_.
