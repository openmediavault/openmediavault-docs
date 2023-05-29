Users
#####

In this section you can create, edit and access information of |omv| users and groups.

User
====

Here you can create or modify user information and configure the user home folders.

Add
^^^^

Information
	The configuration panel gives you options to add, edit or remove users. The table displays all
	|omv| current users.

	When a user is created |omv| backend executes :command:`useradd` in non-interactive
	mode with all the information passed from the form fields, this command also creates an
	entry in :file:`/etc/passwd`, a hashed password in :file:`/etc/shadow`. Samba service is watching any changes
	in users database section so it also sets the password in the Samba tdbsam storage backend.

	The mail field is used for cron jobs when the task is selected to run as
	specific user. By default users are created with :command:`/bin/nologin`
	shell, this will prevent local and remote console access.

Group
	Add or remove users from specific groups. In Linux groups can be used to control
	access to certain features and also for permissions.

	Adding a user to the ``sudo`` group will give them root privileges, adding
	a user to ``saned`` will give access to scanners, etc. By default all users created using
	the |webui| are added to the ``users`` group (``gid=100``).

Public Key
	Add or remove :doc:`public keys </administration/services/ssh>` for granting remote access for users.

.. note::

	- The user profile information (except password) is also stored in the internal |omv| database, along with the public keys.
	- The table shows information from internal database and also parses information from :file:`/etc/passwd` lines with a `UID` number higher than 1000. A user created in terminal is not in the internal database. This causes trouble with samba, as there is no user/password entry in the tdbsam file. Just click edit for the user, enter the same or new password, now the user has the linux and samba password synced.
	- A user can log into the |webui| to see their own profile information. Depending if the administrator has setup the username account to allow changes, they can change their password and mail account.
	- A non-privileged user can become a |webui| administrator by adding them to the ``openmediavault-admin`` group.

Import
^^^^^^

Designed for bulk user creation. Create a spreadsheet with the corresponding data as
described in the import dialog window, save it as CSV (make sure the field separator is semicolon :code:`;`), then just
simply::

$ cat usersfile.csv

Example outputs::

	# <name>;<uid>;<tags>;<email>;<password>;<shell>;<group,group,...>;<disallowusermod>
	user1;1001;user1;user1@myserver.com;password1;/bin/bash;sudo;1
	user2;1002;user2;user2@my.com;password2;/bin/sh;;0
	user3;1003;user3;user3@example.com;password3;/bin/false;;1
	user4;1004;user4;user4@test.com;password4;;;1

.. note::
	- :file:`/etc/shells` will give you a list of valid shells.
	- The last field is	a boolean for allowing the user to change their account.

Paste the contents into the import dialog.

Privileges
^^^^^^^^^^

The button opens a window that displays all current existing |sf| and their
privileges for selected user from the table. How the privileges are stored is
described further down in the :doc:`shared folder </administration/storage/sharedfolders>` section.

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
