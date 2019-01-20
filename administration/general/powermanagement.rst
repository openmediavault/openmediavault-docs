Power Management
################

Monitoring
^^^^^^^^^^

Configures cpufrequtils and sets the default options for the governor to be **conservative** by default in x86 architectures if enabled. If architecture is different then governor is set as **ondemand**.

:file:`/etc/default/cpufrequtils`

.. code-block:: guess

	ENABLE="true"
	GOVERNOR="conservative"
	MAX_SPEED="0"
	MIN_SPEED="0"

:file:`/etc/default/loadcpufreq`

.. code-block:: guess

	ENABLE="true"

All values above can be changed via :ref:`environmental variables <environmental_variable>`.


Power button
^^^^^^^^^^^^

Configures the action to take when pressing the mechanical power button of the server.


Scheduled
^^^^^^^^^

Based on cron, is possible to define shutdown, hibernation or suspend times for the server



