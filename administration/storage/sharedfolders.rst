Shared Folders
##############

|sf| are the key functionality in |omv| around which all services revolve.
If they are located on a BTRFS file system, then it is possible to create snapshots
of those |sf|. This can be done manually or via scheduled tasks.

Add
^^^

When a |sf| is created using the add button, the window form displays the following options:

	- **Name:** The logical name. This can override the path name. Typing a
	  name here will fill the path with the same string.
	- **Device:** The parent filesystem associated with the |sf|.
	- **Path:** The relative path to the mounted device. To share the whole
	  disk just type ``/``.
	- **Permissions:** The default descriptive text will create the |sf|
	  with ``root:users`` ownership and ``775`` permission mode.

	**Available modes**

	.. csv-table::
	   :header: "Logical name", "Octal mode"
	   :widths: 20, 6

		"Administrator: read/write, Users: no access, Others: no access", 700
		"Administrator: read/write, Users: read only, Others: no access", 750
		"Administrator: read/write, Users: read/write, Everyone: no access",770
		"Administrator: read/write, Users: read only, Everyone: read-only",755
		"Administrator: read/write, Users: read/write, Everyone: read-only", 775  (Default)
		"Everyone: read/write", 777

This is how a |sf| looks inside the ``config.xml`` database:

.. code-block:: xml
    :emphasize-lines: 8-17

    <sharedfolder>
        <uuid>9535a292-11e2-4528-8ae2-e1be17cf1fde</uuid>
        <name>videos</name>
        <comment></comment>
        <mntentref>4adf0892-cf63-466f-a5aa-80a152b8dea6</mntentref>
        <reldirpath>data/videos/</reldirpath>
        <privileges>
          <privilege>
            <type>user</type>
            <name>john</name>
            <perms>7</perms>
          </privilege>
          <privilege>
            <type>user</type>
            <name>mike</name>
            <perms>5</perms>
          </privilege>
        </privileges>
    </sharedfolder>

Some of the elements explained:

    - **uuid**: Internal database reference number.
    - **name**: logical name given to the |sf|.
    - **mntent**: the associated filesystem reference. The number is in the :code:`uuid` format, the fstab section in ``config.xml`` should contain a :code:`<mntent>` reference with this number.
    - **reldirpath**: Path relative to the parent filesystem.
    - **privileges**: Users associated with the |sf| and their access level.

When a plugin or a service uses a |sf| it stores the uuid value only. Later on
using helper scripts or internal |omv| functions the full path can be obtained
just by using the :code:`uuid`. An example in shell::

$ . /usr/share/openmediavault/scripts/helper-functions && omv_get_sharedfolder_path 9535a292-11e2-4528-8ae2-e1be17cf1fde

This returns::

$ /srv/dev-disk-by-label-VOLUME1/data_general/videos

More information about `helper functions <https://github.com/openmediavault/openmediavault/blob/master/deb/openmediavault/usr/share/openmediavault/scripts/helper-functions>`_.

A shared folder can be used across all over the system backend. Is available
to select it in sharing services (FTP, Samba, RSync, etc.) at the same time.
Plugins can use them also just by using the shared folder combo class.

.. note::
	- A |sf| belongs to an internal |omv| database filesystem entry. Is not possible to unmount the filesystem without deleting the folder configuration from the |webui|.
	- If a |sf| is being used by a service (FTP, plugins, etc.) is not possible to delete it. Is necessary to disengage the |sf| from the service(s) or section(s) that is holding it before proceeding with removal. This will also prevent to unmount a device from the |webui| in the filesystem section if there is still a |sf| associated with it.
	- Due to the design of the software is not possible at the moment to know what section or service is holding which |sf|.

Edit
^^^^

Edit |sf| is possible, but it has some limitations. You can only change the parent device volume. Once the parent device is changed the backend will reconfigure every service that is using a |sf| and stop/start daemons accordingly.

Be aware that changing the parent device volume will not move the data from one filesystem to another.

.. warning::

	**NFS Server**: Editing the parent device will not descent into :file:`/etc/fstab`. Make sure you edit the share in the NFS section so the bind can be remounted.

Privileges
^^^^^^^^^^

Same as in the user section, the window here is relative to the shared folder.
It will display for the selected |sf| all the |omv| users/groups and their
corresponding privileges.

As you can see from the code block in the `add section <#id3>`_ privileges are
expressed in the internal database in the same manner as permissions in Linux, simplified
using the octal mode: *read/write(7)*, *read-only(5)* *and no access(0)*.

If a privilege is changed, it means a change in the |sf| database section. This database
event will trigger a reconfiguration of SMB, FTP and AFP, it will also restart all the
above daemons. A plugin using |sf|, but not the privilege information from the database
entry should not get reconfigured/restarted if a change occurs just in privileges.

Privileges can be edited from `shared folder <#shared-folder>`_ or `users <#user>`_
section. But it is also possible to edit privileges from the |sf| combo
selection, just click the :fa:`search` to left side of the drop down menu.


ACL (Access Control List)
^^^^^^^^^^^^^^^^^^^^^^^^^

Provides fine grained permission control besides the standard POSIX permissions. The usage of ACL is not recommended for the average home user. If a server is using an extensive list of users then ACL could suit better [1]_ [2]_.

The expanded ACL window displays three panels. Left one is a browser of the selected |sf|, so you can see the apply ACL to the current folder or a subdirectory and so on.

The left panel displays all current |omv| users and system accounts and their current ACL of the selected folder. This panel actually reads ACL from the selected folder.

The bottom panel displays the standard POSIX permission of the selected folder or subfolders in a user friendly interface.

If you want just to reset linux permissions, just use the recursive checkbox and change options only in the bottom panel, and not selecting any ACL user/group in left panel.

The ACL is applied using :command:`setfacl` [3]_ and read with :command:`getfacl` [4]_.

.. note::

	* |omv| mounts all Linux filesystems with ACL enabled. Only native linux POSIX filesystems support ACL. The button gets disabled for HFS+, NTFS, FAT, etc.
	* ZFS provides ACL support, just need to enable the pool/dataset property.

.. [1] https://help.ubuntu.com/community/FilePermissionsACLs
.. [2] http://vanemery.net/Linux/ACL/linux-acl.html
.. [3] https://linux.die.net/man/1/setfacl
.. [4] https://linux.die.net/man/1/getfacl
