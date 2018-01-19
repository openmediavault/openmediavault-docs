Netatalk :fa:`puzzle-piece`
###########################

Overview
--------

Netatalk software was expected to reach version 3.x with Debian Jessie. Unfortunatly due to some unresolved issue with the maintainers, Debian team `opted <https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=690227>`_ to leave it out of Jessie and future releases. Debian Wheezy was the latest release with netatalk. To avoid loosing netatalk as a plugin |omv| uses a debianized source of netatalk 3.x maintained by Adrian Knoth [1]_. Openmediavault does not maintain this software.

Configuration
-------------

The server panel provides minimal options to the server, but it has an extra field in case you need `more directives <http://netatalk.sourceforge.net/3.1/htmldocs/afp.conf.5.html>`_. The default configuration file is located in ``/etc/netatalk/afp.conf``. This is the default global section:

.. code-block:: guess

	[Global]
	max connections = 20
	mac charset = MAC_ROMAN
	unix charset = LOCALE
	guest account = nobody
	uam list = uams_dhx.so,uams_dhx2.so
	save password = no

Netatalk provides PAM modules, so a change of password in terminal or web interface should be reflected inmediately in AFP login.

Shared Folders
--------------

The plugin uses the privileges database, so in the same way |omv| configures Samba shares, the login is controlled using valid, read and write directives in the software layer, not the filesystem. This is an example of a share in netatalk with default options:

.. code-block:: guess

	[Documents]
	path = /media/dev-disk-by-label-VOLUME1/documents
	read only = no
	unix priv = yes
	file perm = 0664
	directory perm = 0775
	umask = 0002
	invisible dots = no
	time machine = no
	valid users = "mike"
	invalid users =
	rolist =
	rwlist = "mike"

Password
	In case you don't want to use privileges you can assign a single password (no username) to the share.

Time Machine
	Support for the Apple backup software was added in netatalk 2.x, and improved in 3.x. Just check the box in the share options to make announce an individual share as a time machine server.

Guest Access
	You can select guest access which by default is read only. A second checkbox is provided for giving write access to guest.

Quota
	You can define a size limit, in case you have multiple time machine volumes and want to prevent them to fill up the data drives.

.. [1] https://github.com/adiknoth/netatalk-debian
