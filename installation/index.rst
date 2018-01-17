.. _installation_index:

Installation
############


Before you begin:
	- Check if your hardware is supported on the system :doc:`requirements page </prerequisites>`.
	- `Download <https://sourceforge.net/projects/openmediavault/files/>`_. an installation image file for your system. Openmediavault provides iso installers for x86 architecture and several preconfigured images for arm devices.
	- Disconnect all harddisks except the future system drive. This way you avoid an accidental install on a storage drive (which will be configured after installation anyway).

Burn the installer:
	For x86 architecture you can burn the iso directly into a usb drive using `etcher <https://etcher.io/>`_ or  dd linux utility. If you have a CD-DVD burner, you can burn the iso into an optical media then boot from CD or DVD.
	Etcher can also be used to transfer arm images into sd cards.

Boot the installer:
	For x86 architecture, enter BIOS configuration, select to boot either from USB or CD and reboot. 
	ARM images are ready to go, so boot from sd card and wait for the initial setup to complete. This takes around 30 minutes in slow devices like raspberry pi.

Installer:
	The current iso installer is reduced to have minimal interaction. You will prompted to select location, language and root password. The installer will pick the first available disk to deploy the the OS. Once the installer finished the system will reboot, make sure you remove the installer and select BIOS to boot from the disk where |omv| was installed. You can also start connecting any data drives you previously disconnected before install or reinstall


First time use:
   If you have a screen attached, KVM or IMPI console the login screen will display the current ip address assigned for the |webui|. Open your browser and type that IP address. The default username:password is :code:`admin:openmediavault`, the root password is the one you setup during install.
   For arm images the root password is the same as admin password.

.. toctree::
  :maxdepth: 2
