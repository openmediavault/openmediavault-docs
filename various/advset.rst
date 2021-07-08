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

The list of environmental variables used for :file:`/etc/fstab` filesystem with the
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
add additional Salt states. Please check out the `SaltStack documentation <https://docs.saltproject.io/en/latest/>`_
for more information about how it works and how to use it.

The |omv| SLS files are located at :code:`/srv/salt/omv/`.

Add custom states
^^^^^^^^^^^^^^^^^

If you want to customize the configuration of a service or any other
application that  is managed by |omv|, then you need to know where to add
your custom state file first. Start searching the location on `GitHub <https://scm.openmediavault.org/tree/master/deb/openmediavault/srv/salt/omv/deploy>`_.
You will find the corresponding location below :file:`/src/salt/omv/deploy`
in the root file system of your system. If there are no files starting
with a number, e.g. :file:`90cron.sls`, then this service is not customizable.
It is still possible, but is beyond the scope of this introduction. The
states are executed in ascending order.

Choose the order when your state needs to be executed and create a file
like :file:`<N>xxxx.sls`, where N is between 0 and 100.

To append something to an already existing configuration file use this YAML::

    <UNIQUE_IDENTIFIER>:
      file.append:
        - name: "<PATH_OF_THE_FILE>"
        - text: |
            <LINE1>
            <LINE2>
            <...>

Example::

    customize_postfix_main:
      file.append:
        - name: "/etc/postfix/main.cf"
        - text: |
            mynetworks = 127.0.0.0/8 168.100.189.0/28

For more file modifications please have a look into the `file module <https://docs.saltproject.io/en/latest/ref/modules/all/salt.modules.file.html>`_.

Finally you need to deploy your changes by running::

	# omv-salt deploy run <SERVICE_NAME>
