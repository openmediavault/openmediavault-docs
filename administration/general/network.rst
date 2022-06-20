Network
#######

In this section you can set several system network related settings.

General
=======

Hostname and domain settings.

Interfaces
==========

Only network interfaces that have been configured via the |webui| are
displayed in the data table. If this panel is empty right after the
installation the automatic synchronisation of the interface configuration
that was done by the installer. In this case simply start to configure
the interfaces via the |webui|.

The dashboard contains a network widget that displays the current status
of the interfaces.

Ethernet
^^^^^^^^

Just select DHCP or static. |omv| is a server so the recommended setting
is to have static IP address, if you have a proper network infrastructure
(separate router and switch). In a reboot, if the router fails to boot
you can still access the |webui| through the switch bridge. If the switch
also fails you can use a direct Ethernet connection with the static IP
address assigned to the server NIC.

Do not leave DNS setting empty; it is essential for fetching updates.
A common value is to use the same IP address as the gateway. If unsure,
just use google DNS ``8.8.8.8``.

Wake on LAN (WOL)
	This enables WOL in the kernel driver, make sure the NICs supports
	this and the feature is enabled in BIOS.

Wireless
^^^^^^^^

The configuration window displays the same IP configuration fields as
Ethernet, plus the relevant wireless values: SSID (the wireless network
name) and the password.

Whenever possible, use Ethernet for a NAS server. Wireless should not be
used in a production server; this feature is intended for extreme cases
only.

VLAN
^^^^

If your network supports VLAN, just add the parent interface and the VLAN
id.

Bond
^^^^

The configuration window provides all available `modes <https://www.kernel.org/doc/Documentation/networking/bonding.txt>`_
for the bond driver. To configure bonding, is necessary at least two
physical network interfaces. The |webui| allows the selection of less
than two. This is by design for configuration purposes. The workflow
is as follow for dual NICs:

- If the primary NIC is already working either by the installer, configure it through the |webui| as static. If set as static using the same IP address given by DHCP, it should not be necessary to re-login to the |webui|.
- Click ``Network | Interfaces | Add | Bond``, select the second available NIC, select the bond mode, fill the IP field and subnet mask values, leave gateway and DNS empty. Save and hit apply.
- Log out and access the |webui| using the new IP address assigned to the bond interface created.
- Now select the primary interface configured through |webui| in the first step, and delete it. Save and hit apply.
- Select the newly created bond interface, click edit add now the physical nic that was deleted from the step before should be available to select. Save and hit apply.
- The dashboard should now report the bond interface information (including speed).

.. note::

	* 802.3ad LACP (Link Aggregation) mode only works if physical interfaces are connected to a managed switch that supports aggregation.
	* Is not possible to achieve 2GBit bandwidth (or more depending on the number of NICs) in a single client using LACP, even if the client also has a LACP-bonded NIC or 10Gbit card;  there is no multipath support in Samba or other |omv| services in the way  Windows Server has for file sharing using SMB.
	* Higher speeds using link aggregation are limited by disk speed. When serving simultaneous clients make sure the physical media is capable of reaching the speed of the bonded NIC (e.g. SSD or RAID array).

Advanced Interface Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Proxy
=====

This panel configures the server proxies using system wide environmental
variables. All software that obeys Linux proxy environmental variables
should be able to use the proxy. This is useful for example if there are
many Debian servers in the network, when performing :command:`apt`
operations, packages can be cached in the proxy if this configured
appropriately to reduce download bandwidth.

The variables name are::

	http_proxy
	https_proxy
	ftp_proxy

This settings do not configure |omv| to act as a proxy server.

Service Discovery
=================

Announcing services via Zeroconf/mDNS is an essential feature of |omv|.
A service will be automatically announced if it is enabled. This applies
to NFS, FTP, Rsync, SMB/CIFS, SSH or the Workbench UI for example.
Plugins may also announce their service via Zeroconf/mDNS.

As this is an essential feature, this cannot be switched off in general.
However, it is possible to deactivate the advertising of individual
services using :doc:`environment variables </various/advset>`.

To get a list of supported environment variables, run the following
command::

    # omv-env list | grep ZEROCONF_ENABLED

To enable or disable a service use this command::

    # omv-env set -- OMV_XXX_ZEROCONF_ENABLED [yes|true|1|no]

Finally the modified environment variable(s) must be applied by running::

    # omv-salt stage run prepare
    # omv-salt deploy run avahi

Example::

    # omv-env set -- OMV_PROFTPD_ZEROCONF_ENABLED no
    # omv-salt stage run prepare
    # omv-salt deploy run avahi

Firewall
========

This data table is for adding iptables rules. This can be useful if you
need to secure access in your local network. Currently it is only possible
to add rules to the OUTPUT and INPUT chains in the filter table. The
configuration to load the rules at boot or network restart is done by the
systemd unit called `openmediavault-firewall`.

.. tip::
	* To avoid locking yourself out while testing, create a cron command to run every five minutes that flushes the OUTPUT/INPUT chain. Don't forget to delete the cron job after testing.::

		*/5 * * * * root /sbin/iptables -F INPUT && /sbin/iptables -F OUTPUT

	* Before adding the last rule to reject all, add a rule before the reject all, to LOG everything. This will help understand why some rules do not work. The log is saved in dmesg or syslog.

.. tip::
	When seeking support please avoid posting screenshots of the data table, this is useless because it does not give the full overview of your firewall ruleset. Instead use::

	$ iptables-save > /tmp/file.txt
