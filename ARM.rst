Access Rights Management
####

In this section you can access information of |omv| users, groups and shared folders. 

User
====
Create or modify users and configuration of home folders.

Add
^^^^

Information
	The configuration panel gives you options to add, edit or remove users. When a user is created |omv| backend executes ``useradd`` in non-interactive mode with all the information passed from the text fields, this also creates an entry in ``/etc/passwd``, a hashed password in ``/etc/shadow`` and the corresponding password in the samba password database. 

	The mail field is used for cron jobs when the task is selected to run as specific user. By default users are created with ``/bin/nologin`` shell, this will prevent local and remote console access.

Group
	Add or remove users from specific groups. In linux groups can be used to control access to certain features and also for permissions. Adding a user to the ``sudo`` group will give root privileges on shell. By default all users created in the |webui| are added to the ``users`` group (gid=100). 

Public Key
	Add or remove public keys for remote access for a user.

.. :note:
	- The user information information (except password) is also stored in the internal |omv|database, along with the public keys
	- The grid parses information from the internal database and also from ``/etc/passwd`` entries with a uid higher than 1000. If you created a user in terminal then is not in the internal database. Just simply click edit and add some information to store in the internal database.


Import
^^^^

This can help when you need to bulk create users in one go. Create an spreadsheet with the corresponding data as described in the field text, save it as CSV (make sure the field separator is ``;``), then just simply::

$ cat usersfile.csv

Example::

	user1;1001;user1;user1@myserver.com;password1;sudo;1
	user2;1002;user2;user2@my.com;password2;;0
	user3;1003;user3;user3@example.com;password3;;1

Paste the contents into the import dialog

Privileges
^^^^
The button will display all current exisitng |sf| and their privileges for the particular user selected. How the privileges are stored is described further down in the |sf| `section <#shared-folder>`_


Settings
^^^^

This option is to select a shared folder as root folder for home folder. New users created in the |webui|. Existing users created before this setting was enabled will not have their home folders moved to that location. You can manually edit ``/etc/passwd`` to point them to the new location.


Group
====

Add
^^^^

Edit
^^^^

Shared Folder
====

Add
^^^^
A shared folder in |omv| is an internal database object configuration that has been created using the |webui|. The |sf| has four main components:
	
	- **Name:** The logical name. This can override the path name. Typing a name here will fill the path with the same string.
	- **Device:** The parent filesystem associated with the |sf|.
	- **Path:** The relative path to the mounted device. To share the whole disk just type ``/``.
	- **Permissions:** The default descriptive text will create the |sf| with ``root:users`` and ``775`` permission mode. 

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
    - **mntent**: This the associated filesystem reference. The number is in the ``uuid`` format, in the the fstab ``config.xml`` section should contain a <mntent> reference with this number.
    - **reldirpath**: Path relative to the parent filesystem.
    - **privileges**: The perms mode is used in the same way as octal file permissions. 0 no access, 5 read only and 7 read/write. 

When a plugin or a service uses a |sf| its stores the uuid only. Later on using helper scripts or internal CLI |omv| commands the path can be obtained just by using the ``uuid`` number.

A shared folder can be used across all over the system backend. Is available to select it in sharing services (ftp, samba, rsync, etc) at the same time. Plugins can use them also just by using the shared folder combo class.


.. note::
	- A |sf| belongs to an |omv| filesystem entry. Is not possible to unmount the filesystem volume without deleting the folder configuraton from the |webui|.
	- If a |sf| is being used by a service (ftp, plugins, etc) is not possible to delete it. Is necessary to disengage the |sf| from the service that is holding it before proceeding with removal of the configuration. This will also prevent to unmount a device from the |webui| in the filesystem section if there is still a |sf| associated with it.
	- Due to the design of the software is not possible at the moment to know what service is holding which |sf|.


Edit
^^^^

Edit |sf| is possible, but it has some limitations. The logical name cannot be changed, but you can change the default permissions and the parent device volume. Editing the parent device should decent into every service that is using a |sf|. The backend will reconfigure all services and stop/start daemons accordingly.

.. warning::

	**NFS Server**: Editing the parent device will not descent into ``/etc/fstab``. Make sure you edit the share in the NFS section so the bind can be remounted.
	
