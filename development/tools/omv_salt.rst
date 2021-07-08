omv-salt
########

This tool is used to deploy the configuration of services and to start or
stop them.

To get a list of all available deployment states::

	# omv-salt deploy list

To deploy one or more states run the following command::

	# omv-salt deploy run <NAMES>...
	# omv-salt deploy run avahi monit systemd

The tool also supports stages that bundle various tasks. To get a list
of them, run the command::

	# omv-salt stage list

The following stages are available:

- setup
	This stage is being run only once after the |omv| Debian package has
	been installed on the system. It is used to set up the system to the
	desired requirements.
- prepare
	This stage takes care that the pillar and grains are up to date and
	all modules/states are being synced to the minions.
- deploy
	Deploy the configuration of various services like SMB, FTP, ...
- all
	This stage contains the stages prepare and deploy.

If you want to deploy all states in one bunch, then you need to execute
the following command::

	# omv-salt stage run deploy
