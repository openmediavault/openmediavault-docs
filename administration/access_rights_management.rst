Access Rights Management
########################

In this section you can create, edit and access information of |omv| users, groups
and shared folders.

User
====

Create or modify users information and configuration of home folders.

Add
^^^^

Information
	The configuration panel gives you options to add, edit or remove users. The grid dispays all
	|omv| current users.

	When a user is created |omv| backend executes :command:`useradd` in non-interactive 
	mode with all the information passed from the web text fields, this also command creates an 
	entry in :file:`/etc/passwd`, a hashed password in :file:`/etc/shadow`. Samba service is watching any changes
	in users database section so it also sets the password in the samba tdbsam storage backend.

	The mail field is used for cron jobs when the task is selected to run as
	specific user. By default users are created with :command:`/bin/nologin`
	shell, this will prevent local and remote console access.

Group
	Add or remove users from specific groups. In linux groups can be used to control 
	access to certain features and also for permissions. 

	Adding a user to the ``sudo`` group will give him root privileges, adding 
	a user to ``saned`` will give access to scanners, etc. By default all users created using 
	the |webui| are added to the ``users`` group (``gid=100``).

Public Key
	Add or remove :doc:`public keys </administration/services/ssh>` for granting remote access for users. 

.. note::

	- The user profile information (except password) is also stored in the internal |omv|database, along with the public keys.
	- The grid shows information from internal database and also parses information from :file:`/etc/passwd` lines with a `UID` number higher than 1000. A user created in terminal is not in the internal database. This causes trouble will samba, as their is no user/password entry in the tdbsam file. Just click edit for the user, enter the same or new password, now the user has the linux and samba password synced.
	- A user can log into the web interface to see his own profile information. Depending if the adminstrator has setup the username account to allow changes, they can change their password and mail account.

Import
^^^^^^

Designed for bulk user creation. Create a spreadsheet with the corresponding data as
described in window the field text, save it as CSV (make sure the field separator is semicolon :code:`;`), then just
simply::

$ cat usersfile.csv

Example outputs::

	user1;1001;user1;user1@myserver.com;password1;sudo;1
	user2;1002;user2;user2@my.com;password2;;0
	user3;1003;user3;user3@example.com;password3;;1

Paste the contents into the import dialog. The last field is a boolean for
allowing the user to change his account.

Privileges
^^^^^^^^^^

The button opens a windows that displays all current exisiting |sf| and their
privileges for selected user from the grid. How the privileges are stored is
described further down in the `shared folder <#shared-folder>`_ section.

Settings
^^^^^^^^

Option to select a |sf| as root for home folders for new users created in the 
|webui|. Previously existing users created before enabling this setting will not have
their home folders moved to this new location. You can manually edit :file:`/etc/passwd` 
to point them to the new location. Also existing users data in default linux location :file:`/home`
has to be moved manually.

Group
=====

Add
^^^

Create groups and select the members. You can select current |omv| users
and system accounts. Information is stored in ``config.xml`` and
:file:`/etc/group`.

Import
^^^^^^

Bulk import works in similar as user account import. Just a csv text,
delimited with a semicolon :code:`;`. The dialog displays the necessary
fields.

Edit
^^^^
Just to add or remove members from groups. Default groups created in the
|webui| have a ``GID`` greater than ``1000``. Same as usernames, groups created
in terminal are not stored in the internal database. Just edit, insert a
comment and their information should now be stored in ``config.xml``.

Shared Folder
=============

Shared folder in |omv| is an internal database object configuration that
has been created using the |webui|.

Add
^^^

When a |sf| is created using the add button, the windows form displays the following options:

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
    - **mntent**: This the associated filesystem reference. The number is in the :code:`uuid` format, in the the fstab ``config.xml`` section should contain a :code:`<mntent>` reference with this number.
    - **reldirpath**: Path relative to the parent filesystem.
    - **privileges**: Users associated with the |sf| and their access level.

When a plugin or a service uses a |sf| its stores the uuid value only. Later on
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
	- A |sf| belongs to an internal |omv| database filesystem entry. Is not possible to unmount the filesystem without deleting the folder configuraton from the |webui|.
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
