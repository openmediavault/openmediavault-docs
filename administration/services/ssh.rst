SSH
####

Overview
--------

Secure shell comes enabled by default in |omv|.

.. note::
   |omv| will enable SSH access for the user ``root`` by default to be
   able to access a headless system in case of a broken installation or
   other maintenance situations. You should disable this behaviour in the
   ``Services | SSH`` page for security reasons after installation.

   To still get ``root`` access you need to create a non-privileged user
   and add them to the ``_ssh`` and ``sudo`` groups. After that you can
   SSH into the system with this non-privileged user and run ``sudo su``.

The configuration options via |webui| are minimal:

- Disable the root login
- Disable password authentication
- Enable public key authentication (PKA)
- Enable compression
- Enable tunneling (for SOCKS and port forward)

An extra options field is provided to enter more options. Examine first the
file :file:`/etc/ssh/sshd_config` before adding extra options otherwise the
option will not be applied. You may also check the SSH related :doc:`environmental variables </various/advset>`
that can be used to customize several options.

Normal users created in the |webui| can access the remote shell by
adding them to the ``_ssh`` group. Using PKA for users requires keys to be added
to their profile. This is described in the :doc:`Users </administration/users>` section. The public key has to be
added in `OpenSSH` or `RFC 4716 <https://tools.ietf.org/html/rfc4716>`_ format.

.. _ssh_convert_rfc4716:

To convert a public key run::

$ ssh-keygen -e -f nameofthekey.pub

Paste the output in the users profile at ``Users | Users | <USERNAME> | Edit | Public Keys``.

A public key in RFC 4716 looks like this::

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

.. note::
	**Remote WAN access**
		- Forward in router/firewall a port different than 22. This will minimize bots fingering the SSH server.
		- Always use PKA.
		- Disable password login.
		- Disable root login.
