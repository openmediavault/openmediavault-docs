How does it work?
##################

|omv| is a complex piece of software. Developers can easily understand how it works by looking at the source code and developing plugins. For the average user it is a little bit more complicated. Some of the mechanics on how it works are explained ahead.

Essential elements:
	**Frontend** The |webui|, is written in TypeScript using the Angular and Angular Material frameworks. The page is delivered using the nginx web server.

	**Backend** PHP code, executes several tasks.

	**config.xml** Database file in XML format, located in :file:`/etc/openmediavault` We will refer in this explanation just as config.xml

	**omv-salt** Tool to :doc:`deploy </development/tools/omv_salt>` the configuration and services.

	**omv-engined** RPC daemon that runs all the PHP backend code. The nginx web server connects to this daemon through the FastCGI PHP socket. If an error appears in the |webui| that indicates no connection to the PHP socket means the daemon is not running.

	**Listeners** PHP backend code that listens to changes in the database. They are located in the modules section of the code :file:`/usr/share/openmediavault/engined/modules`.

	**/var/lib/openmediavault/dirtymodules.json** File that enumerates all sections that need to be reconfigured after the database has been written.


|webui| values to/from the database
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Read
----

When a user clicks on a panel, the JavaScript code retrieves values from config.xml using a RPC call. The RPC call has two main components usually the service name of the section (is in the js code) and the method. Press F12 in your favorite browser to open the developer console and go to Samba section in the |webui|. In the browsers developer tools network section you will see several rpc.php calls. Find the one related to Samba, right click and select copy as cURL.

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


Just after the one before, another call, this time to get the Samba share list:

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

A user can do a simple task as to create a shared folder or change some settings in a service section. Whenever the user hits the save button, all fields from the section are submitted from the frontend via RPC to the internal database in :file:`config.xml`, even the ones that are not changed. This is similar on what happens when reading values however the method here is named differently when saving: :code:`setSettings`.

Stopping here, examining :file:`config.xml` in terminal will see all the new stored values, what follows is that usually a yellow notification bar will appear in the |webui| to indicate that it is necessary to apply changes. The yellow notification bar happens for one reason only: the :file:`dirtymodules.json` file.

So the save button does two things actually, sends information to :file:`config.xml` and what is called mark the relevant module as dirty. As en example: Making a change in general Samba or its shares will create a :file:`dirtymodules.json` file like this:

.. code-block:: json

	[
	    "samba",
	    "zeroconf"
	]


Reconfiguring services
----------------------

When the apply button is pressed, this very long PHP `function <https://github.com/openmediavault/openmediavault/blob/5.x/deb/openmediavault/usr/share/openmediavault/engined/rpc/config.inc#L74-L180>`_ gets executed.

In the following order, this will happen in background:

:command:`omv-salt deploy run samba` -> :file:`/etc/samba/smb.conf` will be completely rewritten --> Samba daemon is restarted

:command:`omv-salt deploy run zeroconf` --> All files at :file:`/etc/avahi/services/{ftp,smb,web,ssh,nfs}.service` will be rewritten --> Avahi daemon is restarted

That PHP function also performs checks for dependencies, in case a configuration needs to be reconfigured or reloaded before/after another one.

Why is Zeroconf marked dirty?
	Because the Samba |omv| `code <https://github.com/openmediavault/openmediavault/blob/5.x/deb/openmediavault/usr/share/openmediavault/engined/module/samba.inc#L215-L222>`_ indicates that whenever a change is performed in this section, Zeroconf must be marked dirty. This is by design, Avahi is configured to announce Samba server if is enabled, so needs to know if |omv| Samba server is enabled or disabled. If the database shows it is disabled the Avahi service file will be removed.
	The module backend is something all plugins can use. For example, a plugin that wants to use the privilege database model will have to listen to any changes in the |sf| database so it can reconfigure its files accordingly.

What can break the |webui|?
	As explained, the |webui| depends on several third party software components.

		1 - Nginx HTTP engine. The web server software is very sensitive to any syntax mistakes in ``sites-available`` folder. Any files there that do not pass syntax check will result in a fail to restart/reload nginx daemon. Also editing the openmediavault-webui nginx file improperly will result in failure. Nothing will be displayed by the browser, it will just say "Connection refused", as there is no software running on the HTTP port.

		2 - omv-engined not running. Whenever the RPC daemon is not running, an error will pop in |webui| "Failed to connect to socket: No such file or directory".

		3 - The php-fpm socket is not running. Uncommon error, but if fiddling around with the PHP socket configuration or systemd to make it not start the |webui| will display "502 Bad gateway".

	All of the above errors should be able to be corrected with `omv-firstaid`. Offending files in sites-available should be removed from there to start the nginx server.

.. note::

	As noticed how |omv| works, the software does not parses configuration files. Any changes users add manually to smb.conf or any other configuration file will not be reflected in the |webui|. This is why some hardcoded values are suggested to be customized via environmental variables. It can happen that a plugin marks Samba as dirty by design then the apply button will rewrite everything and restart it also.

Not every component in |omv| is executed in the way described above. For example the filesystem backend has a much more complex mechanism.
