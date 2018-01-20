Network
#######

In this section you can set several system network related settings.

General
=======

Hostname and domain settings.

Interfaces
==========

The grid only displays configured interfaces done through the |webui|. If you see this panel empty and your default interface was configured by DHCP or static during install is normal. The installer does not setup the network using |omv|, it just configures ``/etc/network/interfaces``.


Ethernet
^^^^^^^^

Just select DHCP or static. |omv| is a server so the recommended setting is to have static IP address. If you have a proper network infrastructure (separate router and switch ). In a reboot if the router fails to boot, you can still access the |webui|.

When using static configuration be aware that the window does not expand completly, if you scroll down you can see IPv6 fields and DNS. The DNS setting is essential for fetching updates, do not leave empty. A common value is to use the same IP address as the gateway, if unsure just use google DNS ``8.8.8.8``.

Wake on LAN (WOL)
	This enables WOL in the kernel driver, make sure the NICs supports this and the feature is enabled in BIOS.

Wireless
^^^^^^^^

Support for wireless network was added in |omv| 3.0. The configuration window displays the same IP configuration fields as ethernet, plus the relevant wireless values: SSID (the wireless network name) and the password. Please be aware wireless should not be used in a production server. This feature is intended extreme cases. Whenever is possible please always use ethernet for your NAS server.


Vlan
^^^^

If your network supports vlan, just add the parent interface and the VLAN id.

Bond
^^^^

The configuration window provides all available `modes <https://www.kernel.org/doc/Documentation/networking/bonding.txt>`_ for the bond driver. To configure bonding, you need at least two physical network interfaces. The |webui| lets you select less than two, this is by design for configuration purposes. The workflow is as follow for dual nics:

- If you have the primary NIC already working either by the installer, go and configure it through the |webui| as static. If set as static using the same IP address given by DHCP you should still be in control of the |webui|.
- Click ``Network->Interfaces->Add->Bond``, select the second available NIC, select the bond mode, enter the IP field values except gateway and DNS. Save and hit apply. 
- Log out and access now the |webui| using the IP address assigned in the bond interface just created.
- Now select the primary interface configured through |webui| in the first step, and delete it. Save and hit apply
- Select the newly created bond interface, click edit add now the physical nic that was deleted from the step before should be available to select. Save and hit apply


.. note::

	* 802.3ad LACP (Link Aggregation) mode only works if physical interfaces are connected to a managed switch that supports aggregation.
	* Is not possible to achieve 2GBit bandwidth (or more depending on the ammount of nics) in a single client. Even if the client also has a LACP bonded nic or 10Gbit card as there is no multipath support in samba or other |omv| services, like Windows server has for file sharing using SMB.
	* Higher speeds using link aggregation are limited by disk speed. When serving simultaneous clients make sure the phisical media is capable (SSD or RAID array) of reaching the speed of the bonded nic.


Advanced Interface setting
^^^^^^^^^^^^^^^^^^^^^^^^^^

If the network options 

Proxy
=====

This panel configures proxies using system wide enviromemtal variables. Every software that obbeys linux proxy environmental variables should be able to use the proxy configurations. This is useful for example if there are many Debian servers in the network, when performing ``apt`` operations, packages can be cached in the proxy if this configured appropiatly to reduce download bandwidth. 

The variables name are::

	http_proxy
	https_proxy
	ftp_proxy

This settings does not configure |omv| to act as a proxy.


Service Discovery
=================

This panel configures avahi-daemon announce services. You can disable selectively by service and/or change the common name announce. Plugins can add their service here also.
Avahi announces are recognized by Linux file browsers by default. Mac OSX only recognizes SMB and AFP protocol in their sidebar. 

Windows does not understand avahi announces, Samba announces to windows client using the NetBios daemon (nmbd). If windows network section does not display the samba server this settings do not change that behaviour.

Firewall
========

This is grid panel for adding iptables rules. This can be useful if you need to secure access in your local network. At the moment is only possible to add rules to the OUTPUT and INPUT chains.

.. tip::
	* To avoid locking yourself out while testing, create a cron command to run every five minutes that flushes the OUTPUT/INPUT chain.
	``*/5 * * * * root iptables -F INPUT && iptables -F OUTPUT``

	* Before adding last rule to reject all, add a rule before the reject all, to LOG everything. This will help understand why some rules do not work. The log is saved in dmesg or syslog.

When seeking support please avoid posting screenshots of the grid panel, is useless because it does not give the full overview of your ruleset. Instead use::

$ iptables-save > /tmp/file.txt

If you have no problems with the information in the ruleset then you can create a text link::

$ iptables-save | curl -F 'sprunge=<-' http://sprunge.us





 

