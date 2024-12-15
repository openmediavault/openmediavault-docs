Users
#####

The user management in |omv| is provided by the user management of the
operating system on which it is running.

However, |omv| also maintains control over these users, **so management is a team effort**
between the Debian operating system and the internal database of |omv|.

Users that are managed via the |webui| are so-called *non-system users*.
This type of users are identified by their *UID*, which is in a specific
range, usually between 1000 and 60000. The same applies to
*non-system groups* that are managed via the |webui|. They are identified
by their *GID* which is usually in the range from 1000 to 60000.
Check ``/etc/login.defs`` for more information.

The **Users** management section in the |webui| is divided into three
subsections: ``Settings``, ``Users`` and ``Groups``.

Users can log into the |webui| to see their own profile information. The
administrator can prohibit this behaviour for each user individually.


Settings
========

User home directory
-------------------

Due to the nature explained, users are supposed to have their own private place for
files that is called "*home*", depending on the type of service, automatically becomes
a personal private shared location.

You can optionally select a |sf| as root for the *home* directories of all non-system users.

If *User home directory* is disabled and a new user is created, the following happens:

  * No home directory will be created and assigned to the user

If *User home directory* is enabled and a new user is created, the following happens:

  * A home directory will be created in the selected |sf| and assigned to the user
  * The "skel" templates from Debian will applied to the new home directory

If *User home directory* is enabled, the following actions will be performed on existing users:

  * The home directory path will be updated for all existing non-system users.
  * The previous home directory content will NOT be moved to the new location. This has to be done manually.

If *User home directory* is disabled, the following actions will be performed on existing users:

  * The home directory will be unset for all existing non-system users.
  * The home directory content will NOT be deleted.


User
====

This page lists all non-system users and allows you to *Create* or *Edit*
those users as well as their |sf| *Permissions*. There is also a special
option that allows you to *Import* multiple users at once.

Create
------

This page is intended for creating a new user. The following form fields are available:

Name
    This must be only numbers and letters. Its the "username" of the login credentials
    and must be all lowercase to avoid confusion.

Password
    This field will provide the password of the user.

Shell
    The shell is only used for remote access to interact with the server.
    By default the form will offers :command:`/usr/bin/sh` shell, but is recommended usage of
    the :command:`/usr/bin/nologin` shell to prevent local and remote console access.

Groups
    This field allows to add or remove users from specific groups. Groups are the means of access
    for multiple users to multiple shared resources.

    Some groups only affect the system (as of Linux), others are specific to the |omv| system.
    By default all users created using the |webui| are added to the ``users`` group (``gid=100``).

SSH public keys
    Add or remove :doc:`public SSH keys </administration/services/ssh>` for granting remote access for users.

Disallow account modification
    Disallow the user to modify their own account information.

Tags
    Specify tags to categorize the user.


Import
------

Designed for bulk user creation. The user data must be entered as CSV data.
An example is prepared as a comment.

Those fields are the same as the form of the *Create* user page.

The field of *UID* must be numeric and must be in the range from 1000 to 60000 (check ``/etc/login.defs`` for more information).

Example data::

    # <name>;<uid>;<tags>;<email>;<password>;<shell>;<group,group,...>;<disallowusermod>
    user1;1001;user1;user1@myserver.com;password1;/bin/bash;sudo;1
    user2;1002;user2;user2@my.com;password2;/bin/sh;;0
    user3;1003;user3;user3@example.com;password3;/bin/false;;1
    user4;1004;user4;user4@test.com;password4;;;1

Edit
----

Here you can modify the user information, the fields are the same as the form of the *Create* user page.

Permissions
-----------

All existing |sf| and the access rights of the user to be edited are displayed
on this page. The following access rights are available:

- Read/Write
- Read-only
- No access

These settings are used by the services to configure the access rights for the users.

.. note::

    Please note that these settings have no effect on file system permissions.

How the permissions are stored is described further down in the :doc:`shared folder </administration/storage/sharedfolders>` section.


Group
=====

This page lists all non-system groups and allows you to *Create* or *Edit* those groups as well as their |sf| *Permissions*. There is also a special option that allows you to *Import* multiple groups at once.


Create
------

This page is intended for creating a new group. The following form fields are available:

Name
    This must be only numbers and letters.

Members
    This field allows to add or remove users for this group.

Import
------

Designed for bulk group creation. The group data must be entered as CSV data.
An example is prepared as a comment.

Those fields are the same as the form of the *Create* group page.

The field of *GID* must be numeric and must be in the range from 1000 to 60000 (check ``/etc/login.defs`` for more information).

Edit
----

Here you can modify the group information, the fields are the same as the form of the *Create* group page.

Permissions
-----------

All existing |sf| and the access rights of the group to be edited are displayed
on this page. The following access rights are available:

- Read/Write
- Read-only
- No access

These settings are used by the services to configure the access rights for the groups.

.. note::

    Please note that these settings have no effect on file system permissions.

How the permissions are stored is described further down in the :doc:`shared folder </administration/storage/sharedfolders>` section.


Technical details
=================

When a user is created |omv| backend executes :command:`useradd` in non-interactive
mode with all the information passed from the form fields. This command is responsible for creating an
entry in :file:`/etc/passwd` and a hashed password in :file:`/etc/shadow`.

The |omv| backend monitors all database changes to users to allow other services to react to these changes.
This ensures, for example, that the *Samba* user database is updated when a user password is changed.

.. attention::

    - The user profile information (except password) is also stored in the
      internal |omv| database, along with the public keys.
    - A non-privileged user can become a |webui| administrator by adding them
      to the ``openmediavault-admin`` group.

Manual management
-----------------

If a user is created via the |webui|, no corresponding group with the name of the user is created.

A user created in terminal by the :command:`useradd` command will not be in the |omv| internal
database. This causes trouble with some services, by example *Samba*, as there is no
user/password entry in the ``tdbsam`` database of *Samba*.

To synchronize users or groups that have not been created in the |webui|, simply
perform an *Edit* action and change the password or membership.

Shared home directories
-----------------------

If *User Home directory* is enabled and configured properly, then the home directories can be shared by some services as well, e.g. *Samba* and *FTP*.
