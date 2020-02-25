Advanced Configuration
======================

|omv| is not a replacement for webmin, where you can configure all options in
the |webui|. Options are already preconfigured to make it easier for the
average user to install and start using the NAS server.

As mentioned before in the :doc:`FAQ </faq>` |omv| takes full control of some
services, making difficult to intervene configuration files. Changes manually
added to configuration files will eventually rewritten at some stage by the
system.

To overcome this there are some options available to modify some of the default
|omv| configuration options and values, like the use of environmental variables.


.. _environmental_variable:

Environmental Variables
-----------------------

The web does not provide access to ALL the configuration aspects of a complex
system like |omv|. However, the system allows to change some advanced settings
through the use of environment variables. To set or change these variables,
login to you |omv| system using SSH and edit the file:

:file:`/etc/default/openmediavault`

Put the variable you want to change at the end of the file with the new value.
Ensure the value is declared with double quotes.

For example we are going to change the default sftp server for SSH service.

:code:`OMV_SSHD_SUBSYSTEM_SFTP=“/usr/lib/openssh/sftp-server”`

Make your changes and save them. To apply the custom settings you need
to execute::

  # monit restart omv-engined
  # omv-salt stage run prepare
  # omv-salt stage run deploy

The list of environmental variables used for ``/etc/fstab`` filesystem with the
defaults options and how to use them is described :doc:`here </various/fs_env_vars>`.

The SaltStack states
--------------------

If you want to deploy custom configuration settings, then you could
add additional Salt states. Please check out the SaltStack documentation
for more information how Salt and SLS files are working.

The |omv| SLS files are located in :code:`/srv/salt/omv/`.
