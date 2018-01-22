Scheduled Jobs
##############

Overview
--------

You can configure common and repetitive command(s) or scripts in this section. Is based on cron using the ``minute hour day Week month`` crontab syntax [1]_. Due to web framework limitation, ranges are not supported. If you need a range you can configure a task for each day or simply use terminal with::

$ crontab -e

The grid panel reflects all current created cron jobs done via the |webui|. The second field reflects the schedule in crontab language.

Options
-------

**Username:** Under what user should the command/script be executed. You can select root, system accounts and |omv| users.

**Mail Notification:** Send all the command/script output to the mail defined in the username profile. If the task is running as root, the mail recipient will be the one defined in notifications for primary and secondary delivery. If |omv| user is defined in the task and has an email configured in his :doc:`profile </administration/access_rights_management>` the notification will be sent to that mail address.

Configuration
-------------

The server configures all tasks done in the |webui| creating this file ``/etc/cron.d/openmediavault-userdefined`` on demand as single lines per job.

.. code-block:: guess

	SHELL=/bin/sh
	PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
	# m h dom mon dow user    command
	12 18 * * * root /var/lib/openmediavault/cron.d/userdefined-04dc9701-881f-4440-93e2-66c385df4068 | mail -E -s "Cron - Movies" -a "From: Cron Daemon <root>" root >/dev/null 2>&1
	50 18 * * * root /var/lib/openmediavault/cron.d/userdefined-69a1cf21-3099-4d37-bb8f-df3fecfac988 >/dev/null 2>&1
	@daily root /var/lib/openmediavault/cron.d/userdefined-f04f0bbb-03d3-4d45-9efb-e1e980cbbaf3 >/dev/null 2>&1

First is the cron time or interval, then username finally the command. The actual command is wrapped in a shell script located in this folder ``/var/lib/openmediavault/cron.d/``. All files in there are prefixed with ``username`` and the internal database uuid.

.. warning::
	- When using a single command to be executed, make sure this does not have any bashism. This because the cron wrapper script gets executed in pure shell #!/bin/sh. If you need to use something in bash wrap your command(s) in a bash script.
	- @hourly, @daily, @weekly and @monthly are just nicknames. If you select @daily and your computer is shutdown at midnight the task will not run [1]_.

.. [1]  https://linux.die.net/man/5/crontab
