Software
########

Overview
--------

|omv| is a Debian based distribution. It uses apt to install packages. All
standard Debian packages are upgraded using the official Debian mirrors. |omv|
packages are upgraded using the http://packages.openmediavault.org repository.

Update Manager
--------------

The update manager displays all available packages for upgrade. You can select
them if you want to do individual or mass upgrade. The server uses cron-apt to
perform a daily apt-get update and fetch upgrade packages automatically. If you
have notifications enabled you receive an email every time packages are ready
for install.

Using CLI
---------

**apt-get**

If you want to update/upgrade in the console you can use ``apt-get update`` then
``apt-get upgrade``.

**omv-upgrade**

This is wrapper script that basically executes::

	$ apt-get update && apt-get upgrade

The full command is::

	$ apt-get update && apt-get –yes –force-yes –fix-missing –auto-remove –allow-unauthenticated –show-upgraded –option DPkg::Options::=“–force-confold” dist-upgrade

**omv-release-upgrade**

This is a script included only in the last versions of |omv| before moving to
next major release version. For example: 0.5.60 to 1.x or 1.19 to 2.x. The
command performs several tasks and modifications depending if the upgrade
includes moving to a new base distribution. For example: Debian Squeeze to
Wheezy or Wheezy to Jessie,

Installing plugins
------------------

The plugins can installed either by repository selecting from the available
list or uploading the deb package. If the plugin requires some extra software
it will fetch all remaining packages from either Debian mirrors or another
repo the plugin specifies.

Installing Software
-------------------

You have to your availability all Debian software repository to install in
your server

**Install**::

	$ apt-get install <packagename>

**Remove**::

	$ apt-get remove <packagename>

**Purge (remove package and configuration files)**::

	$ apt-get purge <packagename>

Repositories
------------

**Debian**

The OS repositories are in this file ``/etc/apt/sources.list``. The default
contents are:

|omv| 2.0 (Wheezy)::

	deb http://ftp.us.debian.org/debian wheezy main contrib non-free
	deb http://ftp.debian.org/debian/ wheezy-updates main contrib non-free
	deb http://security.debian.org/ wheezy/updates main contrib non-free


|omv| 3.0 (Jessie)::

	deb http://ftp.us.debian.org/debian jessie main contrib non-free
	deb http://ftp.debian.org/debian/ jessie-updates main contrib non-free
	deb http://security.debian.org/ jessie/updates main contrib non-free

|omv| 4.0 (Stretch)::

	deb http://ftp.us.debian.org/debian stretch main contrib non-free
	deb http://ftp.debian.org/debian/ stretch-updates main contrib non-free
	deb http://security.debian.org/ stretch/updates main contrib non-free

The above repositories point directly to US servers. Since Debian Wheezy now is possible to use
the redirector address, you only need to change the codename release. The redirector
finds the closest mirror automatically. This is can be used as default for Debian Stretch::

	deb http://deb.debian.org/debian/ stretch main contrib non-free
	deb http://deb.debian.org/debian/ stretch-updates main contrib non-free
	deb http://deb.debian.org/debian-security stretch/updates main contrib non-free


**External**

Debian provides the :file:`/etc/apt/sources.d/` folder for adding external
repositories. If there is need to add a repository from a testing or unstable
Debian just to install recent software make sure the packages are properly pinned [1]_
to avoid the system becoming unstable for adding core unsupported software by mistake.

.. [1] https://wiki.debian.org/AptPreferences
