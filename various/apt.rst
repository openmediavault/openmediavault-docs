Software & Update Management
############################

Overview
--------

|omv| is a Debian based distribution. It uses APT to install packages. All
standard Debian packages are upgraded using the official Debian mirrors. |omv|
packages are upgraded using the https://packages.openmediavault.org repository.

Update Manager
--------------

The update manager displays all available packages for upgrade. You can select
them if you want to do individual or mass upgrade. The server uses ``cron-apt`` to
perform a daily ``apt-get update`` and fetch upgrade packages automatically. If you
have notifications enabled you will receive an email every time packages are ready
for installation.

Using CLI
---------

**apt-get**

If you want to update/upgrade in the console you can use ``apt-get update``
then ``apt-get upgrade``.

**omv-upgrade**

This is non-interactive wrapper script that basically re-synchronizes the
package index files from their sources and installs the newest versions of
all packages currently installed on the system from the sources.

**omv-release-upgrade**

This is a script which is included only in the last versions of |omv|
before moving to the next major release version, e.g. 5.6.x to 6.x.
This command migrates the system to the next major |omv| version
(which mostly includes a Debian distribution upgrade as well).

Installing plugins
------------------

Plugins can be installed via the |webui| or CLI. If the plugin requires
some extra software, the Debian package management will fetch all
dependencies from the configured Debian package repositories.

Installing Software
-------------------

You can install all software available in the Debian repositories on your
server.

.. warning::
    Please note that the installation of additional software may impair
    or prevent the functionality of |omv|. This includes especially the
    installation of newer Python package versions via PIP which have
    already been installed via APT. Also, please do not install packages
    from Debian ``Backports``, ``Testing`` or ``Experimental`` repositories,
    as this may install incompatible package versions. |omv| is strictly
    tied to the Debian version it is based on.

    Better use a container based solution to install additional software
    to do not affect the |omv| operating system.

**Install**::

	$ apt-get install <packagename>

**Remove**::

	$ apt-get remove <packagename>

**Purge (remove package and configuration files)**::

	$ apt-get purge <packagename>

Repositories
------------

**Debian**

The OS repositories are in this file ``/etc/apt/sources.list``.

**External**

Debian provides the :file:`/etc/apt/sources.list.d/` folder for adding external
repositories. The configuration files for the |omv| package repositories
are located here.

.. warning::
    If there is a strong need to add the ``Backports``, ``Testing`` or
    ``Experimental`` Debian repository just to install the most recent
    software, then please ensure that these packages are properly pinned
    [1]_ to avoid the system becoming unstable for adding core unsupported
    software by mistake.

.. [1] https://wiki.debian.org/AptPreferences
