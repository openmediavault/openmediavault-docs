Custom Configuration
####################

|omv| is not a replacement for webmin, where you can configure all options in
the |webui|. Options are already preconfigured to make it easier for the
average user to install and start using the NAS server.

As mentioned before in the :doc:`FAQ </faq>` |omv| takes full control of some
services, making it difficult to intervene configuration files. Changes manually
added to configuration files will eventually overwritten at some stage by the
|omv| system.

To overcome this there are some options available to modify some of the default
|omv| configuration options and values, like the use of environmental variables.

.. _environmental_variable:

Environmental Variables
=======================

The |webui| does not provide access to ALL the configuration aspects of a complex
system like |omv|. However, the system allows to change some advanced settings
through the use of environment variables.

List environment variables
^^^^^^^^^^^^^^^^^^^^^^^^^^

A list of available environment variables can be collected via::

	# omv-env list

To get a list of all configured environment variables use the following command::

	# omv-env get

To get the value of a specific environment variable use::

	# omv-env get <OMV_NAME_OF_VARIABLE>

The list of environmental variables used for ``/etc/fstab`` filesystem with the
defaults options and how to use them is described :doc:`here </various/fs_env_vars>`.

Modify environment variables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To set or change these variables, run the following command::

	# omv-env set <OMV_NAME_OF_VARIABLE> <VALUE>
	# omv-env set OMV_SSHD_SUBSYSTEM_SFTP "/usr/lib/openssh/sftp-server"

The configured environment variables are located in the file :file:`/etc/default/openmediavault`.

Apply changes
^^^^^^^^^^^^^

To apply the custom settings you need to execute the following commands as root::

  # monit restart omv-engined
  # omv-salt stage run prepare
  # omv-salt stage run deploy

The SaltStack states
====================

If you want to deploy custom configuration settings, then you could
add additional Salt states. Please check out the SaltStack documentation
for more information how Salt and SLS files are working.

The |omv| SLS files are located in :code:`/srv/salt/omv/`.
