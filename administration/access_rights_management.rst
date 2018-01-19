Access Rights Management
########################

In this section you can create and access information of |omv| users, groups
and shared folders.

User
====

Create or modify users and configuration of home folders.

Add
^^^^

Information
	The configuration panel gives you options to add, edit or remove users.
	When a user is created |omv| backend executes :command:`useradd` in
	non-interactive mode with all the information passed from the text fields,
	this also creates an entry in :file:`/etc/passwd`, a hashed password in
	:file:`/etc/shadow` and the corresponding password in the samba password
	database.

	The mail field is used for cron jobs when the task is selected to run as
	specific user. By default users are created with :command:`/bin/nologin`
	shell, this will prevent local and remote console access.

Group
	Add or remove users from specific groups. In linux groups can be used to
	control access to certain features and also for permissions. Adding a user
	to the ``sudo`` group will give root privileges on shell or adding a user
	to ``saned`` will give user access to scanners. By default all users
	created in the |webui| are added to the ``users`` group (``gid=100``).

Public Key
	Add or remove public keys for remote access for a user.

.. :note:
	- The user information information (except password) is also stored in the
	  internal |omv|database, along with the public keys
	- The grid parses information from the internal database and also from
	  :file:`/etc/passwd` entries with a uid higher than 1000. If you created a
	  user in terminal then is not in the internal database. Just simply click
	  edit and add some information to store in the internal database.
	- A user can log into the web interface to see his own profile information.
	  Depending if the adminstrator has setup the username account to allow
	  changes, they can change their password and mail account.

Import
^^^^^^

This can help when you need to bulk create users in one go. Create an
spreadsheet with the corresponding data as described in the field text, save
it as CSV (make sure the field separator is semicolon :code:`;`), then just
simply::

$ cat usersfile.csv

Example::

	user1;1001;user1;user1@myserver.com;password1;sudo;1
	user2;1002;user2;user2@my.com;password2;;0
	user3;1003;user3;user3@example.com;password3;;1

Paste the contents into the import dialog. The last field is a boolean for
allowing the user to change his account.

Privileges
^^^^^^^^^^

The button opens a windows that displays all current exisiting |sf| and their
privileges for the particular user selected. How the privileges are stored is
described further down in the |sf| `section <#shared-folder>`_.

Settings
^^^^^^^^

This option is to select a shared folder as root folder for home folder. New
users created in the |webui|. Existing users created before this setting was
enabled will not have their home folders moved to that location. You can
manually edit :file:`/etc/passwd` to point them to the new location.

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
|webui| have a gid greater than 1000. Same as usernames that are created
in CLI they are not stored in the internal database. Just edit, insert a
comment.

Shared Folder
=============

Add
^^^

A shared folder in |omv| is an internal database object configuration that
has been created using the |webui|. The |sf| these main components:

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

When a plugin or a service uses a |sf| its stores the uuid only. Later on
using helper scripts or internal CLI |omv| commands the path can be obtained
just by using the :code:`uuid` number.
A shared folder can be used across all over the system backend. Is available
to select it in sharing services (FTP, Samba, RSync, etc) at the same time.
Plugins can use them also just by using the shared folder combo class.

.. note::
	- A |sf| belongs to an |omv| filesystem entry. Is not possible to unmount the filesystem volume without deleting the folder configuraton from the |webui|.
	- If a |sf| is being used by a service (FTP, plugins, etc) is not possible to delete it. Is necessary to disengage the |sf| from the service(s) or section(s) that is holding it before proceeding with removal of the configuration. This will also prevent to unmount a device from the |webui| in the filesystem section if there is still a |sf| associated with it.
	- Due to the design of the software is not possible at the moment to know what section or service is holding which |sf|.

Edit
^^^^

Edit |sf| is possible, but it has some limitations. The logical name cannot be changed, but you can change the default permissions and the parent device volume. Editing the parent device should decent into every service that is using a |sf|. The backend will reconfigure all services and stop/start daemons accordingly.

.. warning::

	**NFS Server**: Editing the parent device will not descent into :file:`/etc/fstab`. Make sure you edit the share in the NFS section so the bind can be remounted.

Privileges
^^^^^^^^^^

Same as in the user section, the window here is relative to the shared folder.
It will display for the selected |sf| all the |omv| users/groups and their
corresponding privileges. As you can see from the code block in the
`add section <#id3>`_ privileges are expressed in the internal database in the
same manner as permissions in Linux, simplified using the octal mode:
read/write(7), read-only(5) and no access(0).
When a privilege is changed in the |webui| it descents into all relevant
services (SMB, FTP and AFP). |omv| will reconfigure everything that is using
a |sf|, this includes daemon files and stop/start daemons. This is important
as some services or plugins might not use privileges but they will have
their daemon restarted as they are using a |sf|. As explained here privileges
can be edited from `shared folder <#shared-folder>`_ or `users <#user>`_
section. But it is also possible to edit privileges from the |sf| combo
selection.
