Certificates
############

This section allows to create or import SSH keys or SSL certificates.

SSH (Secure Shell)
==================

The public/private pair keys created or imported here are for using in the rsync client (jobs) service section. Plugins can use the internal database if they want to use these keys using the ssh certificates combo class.
The key pair will be stored in the internal database, but only the public key will be available for display just by clicking edit. Not displaying the private key is basic ssh security as it never has to leave the host where it was created. The public key can be copied to clipboard or any other transport to be added to a remote server.
Add a comment as this will be appended to the public key, this is important if you need to revoke the key pair in the remote server in case the server that generated the pair is compromised.
The keys are stored beside the database in these two files:

``/etc/ssh/openmediavault-<uuid_suffix>``  --> Private key

``/etc/ssh/openmediavault-<uuid_suffix>.pub`` --> Public key

The <uuid> suffix is the internal |omv| reference number.

.. note::

	The public key is not displayed in RFC 4716. In case the remote server is also |omv| based, you need to `convert <services.html#id7>`_ it the appropiate format.


SSL (Secure Socket Layer)
=========================

The SSL certificates created or imported here can be used by the |webui| or FTP server. Plugins can also use them by adding the SSL certificate combo class. The create window has the most common SSL certificates fields. The certificate/private pair is stored in the internal database and as files in the linux standard SSL location.
Certificate file with a <uuid> suffix, which is the internal database number:

``/etc/ssl/certificates/openmediavault-<uuid>.cert``

Private key file with the same <uuid> suffix from to his certificate pair.
``/etc/ssl/private/openmediavault-<uuid>.key``

When importing existing ssl certificates make sure they are formated/converted appropiatly.

The command that creates the certificate runs in the PHP backend and is documented `here <https://github.com/openmediavault/openmediavault/blob/20ec529737e6eca2e1f98d0b3d1ade16a3c338e1/deb/openmediavault/usr/share/openmediavault/engined/rpc/certificatemgmt.inc#L234-L358>`_. This certificates are self signed, without root CA.

LetsEncrypt
	LE certificates can be imported directly, just locate your ``etc/letsencrypt/live/<mydomain.com>/{cert,privkey}.pem`` files and copy their contents in their respective field. No need to convert.
