Users
#####

User management in |omv| is supported by the users mnagement of the operating system 
it runs on.

However, |omv| also maintains control over these users, **so management is a team effort
between the Debian operating system and the OMV software system** internal database.

**Users** in |omv| is divided into three subsections: ``Settings``, ``Users`` and ``Groups``.

About home user
^^^^

Due to the nature explained, users are supposed to have their own private place for files 
that is called "*home*".

This private file location or "*home*" place, **depending on the type of service, 
automatically becomes a shared location**.

This place is configured in the ``Settings`` subsection of the |webui| interface 
of |omv|, as *User home directory*

Settings
========

This is the first subsection of the **Users** management section of |webui|.

Allows to select a |sf| as root for *home* place for new users created in the
|webui|.

* If you dont enable *User home directory*, when created an user:

  * Will not have a private place for files if you use the |omv| |webui|
  * Will have a private place for files if you use :command:`useradd` command
  * The "skel" templates from Debian only will be used in last case

* If you already enable *User home directory*, when created an user:

  * Will have a private place for files no matter way you use to create!
  * The "skel" templates from Debian will be used always

* If you disabled and re-enabled *User home directory* and viceversa:

  * Previously existing users created before enabling/disabling this setting 
    will not have their *home* directory moved to the new location.
  * Previously existing users  created before enabling/disabling this setting
    can change *home* by editing :file:`/etc/passwd` to point them to the new 
    location.
  * Also existing users data in default linux location :file:`/home`
    or previously existing *home* has to be moved manually too.

User
====

This allows to *Create* or *Edit* users as well as their permissions, there is a 
special option that allows batch loading called *Import*. Those are under the "+" 
button of the configuration panel.

Information
    The table information displays all |omv| current users in listing format. 
    Using the *table icon* button of the configuration panel, you can customized 
    the columns  of this listing format by add or remove information columns.

Create
^^^^

This brings to you the creation form, important fields are:

Name
    This must be only numbers and letters.

Password
    This fiel will provide the password of the user.

Group
	This field allows to add or remove users from specific groups. Groups are the means of access 
    for multiple users to multiple shared resources.

    Some groups only affect the system (as of Linux), others are specific to the |omv| system.
	By default all users created using	the |webui| are added to the ``users`` group (``gid=100``).

Public Key
	Add or remove :doc:`public keys </administration/services/ssh>` for granting remote access for users.


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

Permissions
^^^^^^^^^^^

The button opens a window that displays all current existing |sf| and their
permissions for selected user from the table. How the permissions are stored is
described further down in the :doc:`shared folder </administration/storage/sharedfolders>` section.


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

Technical details
=================

When a user is created |omv| backend executes :command:`useradd` in non-interactive
mode with all the information passed from the form fields, this command also creates an
entry in :file:`/etc/passwd`, a hashed password in :file:`/etc/shadow`. Samba service is watching any changes
in users database section so it also sets the password in the Samba tdbsam storage backend.

The mail field is used for cron jobs when the task is selected to run as
specific user. By default users are created with :command:`/bin/nologin`
shell, this will prevent local and remote console access.

.. attention::

	- The user profile information (except password) is also stored in the internal |omv| database, along with the public keys.
	- The table shows information from internal database and also parses information from :file:`/etc/passwd` lines with a `UID` number higher than 1000. A user created in terminal is not in the internal database. This causes trouble with samba, as there is no user/password entry in the tdbsam file. Just click edit for the user, enter the same or new password, now the user has the linux and samba password synced.
	- A user can log into the |webui| to see their own profile information. Depending if the administrator has setup the username account to allow changes, they can change their password and mail account.
	- A non-privileged user can become a |webui| administrator by adding them to the ``openmediavault-admin`` group.
