How does it works?
##################

|omv| is a complex piece of software. Developers can easily understand how it works by looking at the source code and developing plugins. For the average user it is a little bit more complicated. Some of the mechanics on how it works are explained ahead.

Essential elements:
	**Frontend** The |webui|, is written in javascript using the extjs sencha framework. Is rendered using the nginx http engine.

	**Backend** PHP code, executes several tasks.

	**config.xml** Database file in xml format, located in :file:`/etc/openmediavault` We will refer in this explantion just as config.xml

	**omv-mkconf** Shell script that accepts arguments. The name of the argument is related to the service it configures. ie: omv-mkconf samba, omv-mkconf sharedfolders and so on. The arguments are all files located in :file:`/usr/share/openmediavault/mkconf` folder.

	**omv-engined** RPC daemon that runs all the php backend code. The nginx web server connects to this daemon through the fastcgi php socket. If an error appears in the |webui| that indicates no connection to the php socket means the daemon is not running.

	**Listeners** Php backend code that listens to changes in the database. They are located in the modules section of the code :file:`/usr/share/openmediavault/engined/modules`.

	**/var/lib/openmediavault/dirtymodules.json** File that enumerates all sections that need to be reconfigured after the database has been written.


|webui| values to/from the database
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Read
----

When a user clicks on a panel, the javascript code retrieves values from config.xml using a rpc call. The rpc call has two main components usually the service name of the section (is in the js code) and the method, usually named :code:`getSettings`. In chrome browser hit F12 to open the developer console, go to samba section. Then in the network section of the console will show several rpc.php calls. Find the one related to samba, right click and select copy as cURL.

This is the json payload sent to omv-engined:

.. code-block:: json

	{
	   "service":"SMB",
	   "method":"getSettings",
	   "params":null,
	   "options":null
	}

and the response:

.. code-block:: json

 {
   "response":{
      "enable":true,
      "workgroup":"HOME",
      "serverstring":"%h server",
      "loglevel":0,
      "usesendfile":true,
      "aio":true,
      "nullpasswords":false,
      "localmaster":false,
      "timeserver":false,
      "winssupport":false,
      "winsserver":"",
      "homesenable":false,
      "homesbrowseable":true,
      "extraoptions":""
   },
   "error":null
 }


Just after the one before, another call, this time to get the samba share list:

.. code-block:: json

	{
	   "service":"SMB",
	   "method":"getShareList",
	   "params":{
	      "start":0,
	      "limit":25,
	      "sortfield":"sharedfoldername",
	      "sortdir":"ASC"
	   },
	   "options":null
	}


And the response:

.. code-block:: json

	{
	   "response":{
	      "total":1,
	      "data":[
	         {
	            "uuid":"9e4c8405-b01c-40b6-8c46-af6be17a1ff6",
	            "enable":true,
	            "sharedfolderref":"7ee2e4d0-8173-442b-88b9-63b4c731f920",
	            "comment":"",
	            "guest":"no",
	            "readonly":true,
	            "browseable":true,
	            "recyclebin":false,
	            "recyclemaxsize":0,
	            "recyclemaxage":0,
	            "hidedotfiles":true,
	            "inheritacls":true,
	            "inheritpermissions":false,
	            "easupport":false,
	            "storedosattributes":false,
	            "hostsallow":"",
	            "hostsdeny":"",
	            "audit":false,
	            "extraoptions":"",
	            "sharedfoldername":"sf1"
	         }
	      ]
	   },
	   "error":null
	}


Write
-----

A user can do a simple task as to create a shared folder or change some settings in a service section. Whenever the user hits the save button, all fields from the section are submitted from the frontend via rpc to the internal database in :file:`config.xml`, even the ones that are not changed. This is similar on what happens when reading values however the method here is named differently when saving: :code:`setSettings`.

Stopping here, examining :file:`config.xml` in terminal will see all the new stored values, what follows is that usually a yellow button will appear to indicate that is necessary to apply changes. The yellow button happens for one reason only: the dirtymodules.json file.

So the save button does two things actually, sends information to config.xml and what is called mark the relevant module as dirty. As en example: Making a change in general samba or its shares will create a dirtymodules file like this:

.. code-block:: json

	[
	    "samba",
	    "zeroconf"
	]


Reconfiguring services
----------------------

When yellow apply button is pressed, this very long php `function <https://github.com/openmediavault/openmediavault/blob/9ddc8b66f3f666987157a0e7b84d57e7c10f9ba4/deb/openmediavault/usr/share/openmediavault/engined/rpc/config.inc#L72-L204>`_ gets executed.

In the following order, this will happen on background:

:command:`omv-mkconf samba` -> :file:`/etc/samba/smb.conf` will be completly rewritten.

:command:`omv-mkconf zeroconf` --> All files at :file:`/etc/avahi/services/{ftp,smb,web,ssh,nfs}.service` will be rewritten.

After that is time for daemon reload, so:

:command:`systemctl stop samba` followed by :command:`systemctl start samba` --> Samba daemon is restarted

:command:`systemctl stop avahi-daemon` followed by :command:`systemctl start avahi-daemon` --> avahi daemon is restarted

That php function performs also checks for dependancies, in case a configuration needs to be reconfigured or reloaded before/after another one.

Why is zeroconf marked dirty?
	Because the samba |omv| `code <https://github.com/openmediavault/openmediavault/blob/a846afb5a648cb89b2dad0fdf25ee7b261d89a78/deb/openmediavault/usr/share/openmediavault/engined/module/samba.inc#L266-L269>`_ indicates that whenever a change is performed in this section, zeroconf must be marked dirty. This is by design, avahi is configured to announce samba server if is enabled, so needs to know if |omv| Samba server is enabled or disabled. If the database shows it is disabled the avahi servie file will be removed
	The module backend is something all plugins can use. For example, a plugin that wants to use the privilege database model will have to listen to any changes in the |sf| database so it can reconfigure its files acordingly.

What can break the web interface?
	As explained, the |webui| depends on several third party software components.

		1 - Nginx http engine. The web server software is very sensitive to any syntax mistakes in ``sites-available`` folder. Any files there that do not pass syntax check will result in a fail to restart/reload nginx daemon. Also editing the openmediavault-webui nginx file improperly will result in failure. Nothing will be displayed by the browser, it will just say "Connection refused", as there is no software running on the http port.

		2 - omv-engined not running. Whenever the rpc daemon is not running, an error will pop in |webui| "Failed to connect to socket: No such file or directory".

		3 - The php-fpm socket is not running. Uncommon error, but if fiddling around with the php socket configuration or systemd to make it not start the |webui| will display "502 Bad gateway".

	All of the above errors should be able to be corrected with omv-firstaid. Offending files in sites-available should be removed from there to start the nginx server.

.. note::

	As noticed how |omv| works, the software does not parses configuration files. Any changes users add manually to smb.conf or proftpd.conf will not be reflected in the |webui|. This why some hardcoded values are suggested to be done via environmental variables. It can happen that a plugin marks samba as dirty by design then the apply button will rewrite everything and restart it also.

Not every component in |omv| is executed in the way described above. For example the filesystem backend has a much more complex mechanics.
