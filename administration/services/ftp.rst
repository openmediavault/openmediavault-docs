FTP
####

Overview
----

On top of the proftpd debian package, |omv| uses the vroot module by Castaglia. The server is configured using a DefaultRoot for this folder ``/srv/ftp``. Adding folders to the chroot is done by using vroot aliases.

This is the default behavoiour of the FTP server and cannot be changed. The vroot default path can be changed with environmental variables. The chroot also prevent symlinks for escaping that path, however you can use symlinks that point inside the chroot.

So any time you add a shared folder to the FTP, OMV will create first a vroot alias:::

	<IfModule mod_vroot.c>
	  VRootAlias "/media/dev-disk-by-label-VOLUME1/videos" "Videos"
	</IfModule>


Then that alias will have privileges assigned:::

	<Directory /Videos>
	  <Limit ALL>
	    AllowUser OR omvUser
	    DenyAll
	  </Limit>
	  <Limit READ DIRS>
	    AllowUser OR omvUser
	    DenyAll
	  </Limit>
	</Directory>

By default you're not allowed to write in the when you login, this means you cannot create folders in the landing directory, you have to enter one of the shared folders. Also due to the nature of the chroot, creating top level folders is pointless since they will be actually stored in /srv/ftp and not in the media disks.

Remote Access
----

FTP is a protocol intended for use in LAN and WAN. For accessing WAN it is required to forward the server port (default 21) and the passive range to the |omv| server.

Anonymous Login
-----

Disabled by default, the anonymous user is mapped to the system user ftp and nogroup. There is no write access for anonymous and this is configured in the ``/etc/proftpd/proftpd.conf`` file and cannot be changed as is hard coded into the default configuration script of the server. In this case there is no environmental variable to change that behaviour::

	<Anonymous ~ftp>
	  User ftp
	  Group nogroup
	  UserAlias anonymous ftp
	  DirFakeUser on ftp
	  DirFakeGroup on ftp
	  RequireValidShell off
	  <Directory *>
	    HideFiles (welcome.msg)
	    HideNoAccess on
	    <Limit WRITE>
	      DenyAll
	    </Limit>
	  </Directory>
	</Anonymous>


FTP(S/ES)
----
|omv| provides two SSL/TLS modes for encrypting the FTP communication implicit and explicit FTPS.

The differences and features are explained `here <https://en.wikipedia.org/wiki/FTPS>`_ and `here <http://www.jscape.com/blog/bid/75602/Understanding-Key-Differences-Between-FTP-FTPS-and-SFTP>`_.

Enabling FTP over SSL/TLS requires first that you create or import a certificate in the corresponding section. Once the certficate is there you can choose it from SSL/TLS section in FTP. The default FTPS of the server is explicit, you can click the checkbox to enable implicit. If you choose implicit make sure you forward port 900 in your router to port 21 in your NAS server if you're accessing from WAN, otherwise the client will probably display ECONREFUSED.

Tips
----

Login Group
	By default all |omv| users created in the |webui| can gain login into FTP. You can restrict to read only or read write, there is no deny access, but the user has no privileges he would not see that folder. If you want to add a layer of extra security for the login, you can create a control group to restrict login to FTP. You first create a group for example ftp_users, then at the end of the general extra options of the server we add:

	.. code-block:: guess

		​<Limit LOGIN>
		    DenyGroup !ftp_users
		</Limit>

	Only users members of that particular group will be able to log into the FTP server.

Home Folders
	There is not straightforward way of doing this in the |webui|, but if you really need home folders for FTP, you can change the default vroot path with environmental variable ``OMV_PROFTPD_MODAUTH_DEFAULTROOT=“~”``.
	What will happen here if users will log in straight into their home folders. If you add shared folders to the server they will be displayed inside the user home folder plus any other folder present in their home folder.

LetsEncrypt
	Just import your LE certificate in the ``General->Certificates->SSL`` `section <certificates.html#ssl-secure-socket-layer>`_. Then in the TLS/SSL tab, select the imported cert from the dropdown menu. Do not enable implicit ssl. You need also to add the chain file. So in the extra option field text add:

	``TLSCACertificateFile <yourpathtoLE>/etc/letsencrypt/live/<yourdomain>/chain.pem``
