Users
#####

User management in |omv| is supported by the users mnagement of the operating system 
it runs on.

However, |omv| also maintains control over these users, **so management is a team effort
between the Debian operating system and the OMV software system** internal database.

**Users** management is divided into three subsections: ``Settings``, ``Users`` and ``Groups``.

Groups means access for multiple users to multiple shared resources.

An user can log into the |webui| to see their own profile information.

With this section we can manage also permissions of shared resources.
Unlike user permissions, group permissions allow you to define access
for multiple users to the same resource.

About home user
^^^^

Due to the nature explained, users are supposed to have their own private place for
files that is called "*home*", depending on the type of service, automatically becomes 
a personal private shared location.

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

This allows to *Create* or *Edit* users as well as their *Permissions*, there is a
special option that allows batch loading called *Import*.

The options of *Create* and *Import* are under the "+" button of the configuration panel.

The option of *Edit* an user is next to the "+" button.

The option of *Permissions* are next to the "Edit" button.

Erasing or deleting an user is the "Trash" icon next to the "Permission" button.

Information
    The table information displays all |omv| current users in listing format.
    Using the *table icon* button of the configuration panel, you can customized
    the columns  of this listing format by add or remove information columns.

    Take note that **to edit or delete an user you must select one** from the list.

Create
^^^^

This brings to you the creation form, this option is offered after hit the "+"
button of the configuration menu panel of the *Users* subsection. important fields are:

Name
    This must be only numbers and letters. Its the "username" of the login credentials
    and must be all lowercase to avoid confution.

Password
    This fiel will provide the password of the user.

Group
    This field allows to add or remove users from specific groups. Groups are the means of access
    for multiple users to multiple shared resources.

    Some groups only affect the system (as of Linux), others are specific to the |omv| system.
    By default all users created using the |webui| are added to the ``users`` group (``gid=100``).

Shell
    The shell is only used for remote access to interact with the server.
    By default the form will offers :command:`/bin/sh` shell, but is recommended usage of
    the :command:`/bin/nologin` shell to prevent local and remote console access.

Public Key
    Add or remove :doc:`public keys </administration/services/ssh>` for granting remote access for users.


.. attention::

    Depending if the administrator has setup the username account to allow changes,
    they can change their password and mail account.

Import
^^^^^^

Designed for bulk user creation, it brings a form filed like a spreadsheet to fill up with the
corresponding data as described in the import dialog window.

Those fields are the same as the form of the *Create* user subsection.

The field of "uid" do not appears on the creation form, must be numeric
and must be over 1000.

The field of "disallowusermod" is a boolean for allowing user to change their account.

Example data::

	# <name>;<uid>;<tags>;<email>;<password>;<shell>;<group,group,...>;<disallowusermod>
	user1;1001;user1;user1@myserver.com;password1;/bin/bash;sudo;1
	user2;1002;user2;user2@my.com;password2;/bin/sh;;0
	user3;1003;user3;user3@example.com;password3;/bin/false;;1
	user4;1004;user4;user4@test.com;password4;;;1

.. note::

    You can create a spreadsheet with the corresponding data as described in the import dialog window
    save it as CSV using the field separator as semicolon to carry its content in plain text editor,
    then copy its content and paste the contents into the import dialog.

Edit
^^^^

The button to edit and modify user details. You only can modify one user per time.

Its basically the same form of the creation option, same rules apply.

Permissions
^^^^^^^^^^^

The button to edit and modify users access. You only can modify one user per time.

The button opens a window that displays all current existing |sf| and their
permissions for selected user from the table. How the permissions are stored is
described further down in the :doc:`shared folder </administration/storage/sharedfolders>` section.


Group
=====

This allows to *Create* or *Edit* groups as well as their *Permissions*, there is a
special option that allows batch loading called *Import*.

The options of *Create* and *Import* are under the "+" button of the configuration panel.

The option of *Edit* a group is next to the "+" button.

The option of *Permissions* are next to the "Edit" button.

Erasing or deleting a group is the "Trash" icon next to the "Permission" button.

Information
    The table information displays all |omv| current groups in listing format.
    Using the *table icon* button of the configuration panel, you can customized
    the columns  of this listing format by add or remove information columns.

    Take note that **to edit or delete a group you must select one** from the list
    and **this group must be not in usage** by any shared resource or any user..

Add
^^^

This brings to you the creation form, this option is offered after hit the "+"
button of the configuration menu panel of the *Groups* subsection. important fields are:

Name
    This must be only numbers and letters. The group information is stored in ``config.xml`` and
    the :file:`/etc/group` file.

Members
    This field allows to add or remove users for this group.  You can select
    current |omv| existing users.

    Some groups only affect the system (as of Linux), others are specific to
    the |omv| system. By default all users created using the |webui| are added
    to the ``users`` group (``gid=100``).

Import
^^^^^^

Designed for bulk group creation, it brings a form filed like a spreadsheet to fill up with the
corresponding data as described in the import dialog window; it works in similar as user account import.

Those fields are the same as the form of the *Create* group subsection.

The field of "uid" do not appears on the creation form, must be numeric
and must be over 1000.

Edit
^^^^

The button to edit and modify membership. You only can modify one group per time,
and means or implicts that one or several users will be modified at time.

Its basically the same form of the creation option, same rules apply.

Permissions
^^^^^^^^^^^

The button to edit and modify group access. You only can modify one group per time.

Group permissions allow you to define access (for multiple users) to shared resources.

The button opens a window that displays all current existing |sf| and their
permissions for selected group from the table. How the permissions are stored is
described further down in the :doc:`shared folder </administration/storage/sharedfolders>` section.


Technical details
=================

When a user is created |omv| backend executes :command:`useradd` in non-interactive
mode with all the information passed from the form fields, this command also creates an
entry in :file:`/etc/passwd`, a hashed password in :file:`/etc/shadow`.

Services will perform sync operations like Samba service, that is watching any changes
in users database section so it also sets the password in the Samba ``tdbsam`` storage backend;
others just dont sync such operations like Rsync service, cos has their own user management.

The mail field is used for cron jobs when the task is selected to run as
specific user.

.. attention::

	- The user profile information (except password) is also stored in the
          internal |omv| database, along with the public keys. So then when
          user or group are created information should now be stored in ``config.xml``.
	- The table shows information from internal database and also parses information
          from :file:`/etc/passwd` lines with a `UID` number higher than 1000.
	- A non-privileged user can become a |webui| administrator by adding them
          to the ``openmediavault-admin`` group.

Manual management
^^^^^^^^^^^^^^^^^

Unless normal action of :command:`useradd`, |omv| backend when performs such action
do not create a personal group.

A user created in terminal by the :command:`useradd` command will not be in the internal
database. This causes trouble with some services; by example *Samba*, as there is no
user/password entry in the ``tdbsam`` database of samba.

To synchronize users or groups that have not been created in the |webui|, simply
perform an edit action and change the password or membership.

Shared Home
^^^^^^^^^^^

The private file location or "*home*" place will become a shared resource of any user
created, if *User Home directory* is already configure and place is valid.

This becomes a shared resource only in some services, mostly Samba and Ftp services.
