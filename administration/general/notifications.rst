Notifications
#############


Notifications work in the form of email. The backend software used here is postfix [1]_ configured as a MTA in satellite mode. The options allow to configure to send mail via SMTP servers using the standard port or use SSL/TLS. The |webui| allows inputing two delivery addresses. Both are assigned to the root user.


Configuration
=============

The central MTA configuration is stored in :file:`/etc/postfix/main.cf`

|omv| creates the :file:`/etc/postfix/recipient_canonical` to define the root (admin) and normal users mail addresses when added via the |webui|. Example::

	root rootthe@gmail.com
	mike mikeadmin@themailco.com
	@server.lan rootthe@gmail.com

When a scheduled task is defined to run as a certain user the output generated from that task, will be sent to that user defined mail.

The last line is the catch all address. For example a scheduled task set to be run as user with no mail defined in their profile will get the output generated sent to the catch all address (``rootthe@gmail.com``). The same will happen with any other mail action intended for an undefined user (not in that list)

Mails can be sent from terminal also with mail command. :command:`mail` receives from stdin.

Examples 1::

	$ echo "Message body" | mail -s "Test subject" mike

Mail will be delivered to ``mikeadmin@themailco.com`` as it is defined in canonical_recipients. The delivery address can be explicit also::

$ echo "Message body" | mail -s "Test subject" mikeadmin@themailco.com


Examples 2::

	$ echo "Message body" | mail -s "Test subject" john


Mail will delivered to ``rootthe@gmail.com`` because user **john** does not have an email address defined in canonical_recipients, so it goes to the catch all address.

.. warning::
	|omv| stores the configuration values in the database (including the password). Before posting information for support please sanitize the values.


Events
======

The server will send notifications for this events:

	- Log in from browser (If cookies are allowed, then it just sends once).
	- Use of sudo by a user not in allowed group.
	- Summary of locked users by pam_tally2 [2]_. This happens when a user or admin attempts fails to log in for more than three times.
	- MD RAID events: degraded, reshape, etc. [D]
	- Monit software: php-fpm, nginx, netatalk, rrdcached, collectd and omv-engined. [D]
	- Monit filesystem: usage and mount points. [D]
	- Monit system: CPU, Load and memory usage. [D]
	- Scheduled tasks. [D]
	- Rsync jobs. [D]
	- Cron-apt: Summary of upgrade packages available. [D]
	- SMART: Report of attribute changes. [D]

Options marked with [D] can be disabled selectivly. The rest only when the whole notification backend is disabled.


Gmail
=====

Gmail can be used in notifications. If you have 2FA enabled for the account, then is necessary to create an `app password <https://myaccount.google.com/apppasswords>`_ ::.

	SMTP Server: smtp.gmail.com
	SMTP Port: 587
	Encryption mode: STARTTLS
	Sender email: rootthe@gmail.com (include domain)
	Authentication required: Yes
	Username: rootthe@gmail.com (include domain)
	Password: <the app password here>
	Primary email: rootthe@gmail.com
	Secondary email: optional

.. note::
	Aliases are allowed. This is good for filtering later in gmail. ``rootthe@gmail.com`` can be ``rootthe+server1@gmail.com`` or ``rootthe+whatever@gmail.com``.

.. note::
	Gmail requires "access for less secure applications" to be enabled, in order for |omv| to send notifications using ``smtp.gmail.com``.  `Enable access for less secure applications <https://myaccount.google.com/lesssecureapps>`_ ::.


Third Party Notifications
=========================

Whenever a mail is dispatched by the MTA, postfix will execute a run-parts of this directory :file:`/usr/share/openmediavault/notification/sink.d`, passing the following environmental variables::

	OMV_NOTIFICATION_FROM
	OMV_NOTIFICATION_RECIPIENT
	OMV_NOTIFICATION_SUBJECT
	OMV_NOTIFICATION_DATE
	OMV_NOTIFICATION_MESSAGE_FILE

Also the following positional arguments are passed::

	$1 The path of the file containing the message text (OMV_NOTIFICATION_MESSAGE_FILE)
	$2 The FROM email address (OMV_NOTIFICATION_FROM)
	$3 The TO recipient email adresses (OMV_NOTIFICATION_RECIPIENT)

Most modern non mail notifications systems have a documented API, where you can send text using curl payloads with a secret `TOKEN`. So most common case would be to use `OMV_NOTIFICATION_MESSAGE_FILE` variable only in your script.

Your script's filename must adhere to the following standards:

	- Must belong to one or more of the following namespaces:

		- The LANANA-assigned namespace (^[a-z0-9]+$)
		- The LSB hierarchical and reserved namespaces (^_?([a-z0-9_.]+-)+[a-z0-9]+$)
		- The Debian cron script namespace (^[a-zA-Z0-9_-]+$)

	- Start with a number like this: :file:`<##>pushnotification`

.. note::
	- Do not add an extension to your script in the run-parts directory, otherwise it will get excluded.
	- Make sure the script file is executable. In this case also make sure the script is not a symlink to a mounted filesystem with `noexec` flag.


.. [1] http://www.postfix.org
.. [2] http://www.linux-pam.org/Linux-PAM-html/sag-pam_tally2.html
