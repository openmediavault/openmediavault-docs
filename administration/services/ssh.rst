SSH
####

Overview
--------

Secure shell comes disabled by default in |omv|, when installing |omv| on top a
Debian installation, the systemd unit will be disabled after the server
packages are installed. Just login into |webui| to re-enable the ssh service.

The configuration options are minimal, But is possible to:

- Disable the root login
- Disable password authentication
- Enable public key authentication (PKA)
- Enable compression
- Enable tunneling (for SOCKS and port forward)

An extra text field is provided to enter more options. Examine first the
file :file:`/etc/ssh/sshd_config` before adding extra options otherwise the
option will not be applied. In that case is necessary change the environmental variable.

.. _ssh_convert_rfc4716:

Normal |omv| users created in the |webui| can access the remote shell by
adding them to the ssh group. Using PKA for users requires keys to be added
to their profile, this is done in the Users section. The key has to be
added in `RFC 4716 <https://tools.ietf.org/html/rfc4716>`_ format. To do
that run::

$ ssh-keygen -e -f nameofthekey.pub

Paste the output in the users profile at ``Access Right Management | Users | <USERNAME> | Edit | Public Keys``.

The number of keys per user is unlimited. A public key in RFC 4716 looks like this::

	---- BEGIN SSH2 PUBLIC KEY ----
	Comment: "iPhone user1"
	AAAAB3NzaC1yc2EAAAADAQABAAABAQDfSQulxffUktx2P6EikkjVxDw0tT8nCW8LHLx/kl
	8t37xFQ5/OoL9m6rVzYy5CFGYt+l7DffWjL0Av7AqaM0ykZVmv2VEM6TmMo56LTlmyZdlz
	X5+GEJgCQNtDxcIYAVuPXKpLtlB/uAGzwHdZWpAen+mHgWIi4va8N5QNn4rXpkREcvM1q4
	snyAi+gyjAS2Dn4pm8zzrd9qQFnoRYzidbp5e2Rs3brOkwUco0ZkOME2Ff6SpLGaXz4DHH
	qgdTqZwHaTXEwm6kDmglCQrauIPI/ggNqz9mVEspYkskR2PM4CAty8RkZD4MQe5K3EMAFR
	aFobBSlhQ3ESCYWNXTS3bF
	---- END SSH2 PUBLIC KEY ----

The comment string is very important. This will help track down when is necessary to revoke the key in case it gets lost or stolen.


Admin Tasks
-----------

If root login has been disabled and need to perform administrative tasks in the terminal, swap to root by typing::

$ su

To use sudo for root operations add the user to the sudo group.

The SFTP server comes enabled by default for root and ssh group. So POSIX folder permissions apply to non-root users accessing via SFTP.

.. note::
	**Remote WAN access**
		- Forward in router/firewall a port different than 22. This will minimize bots fingering the ssh server.
		- Always use PKA.
		- Disable password login.
		- Disable root login.
