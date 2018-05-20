.. _installation_index:

Installation
############

Before you begin:
	- Check if your hardware is supported on the system :doc:`requirements
	  page </prerequisites>`.
	- `Download <https://sourceforge.net/projects/openmediavault/files/>`_ an
	  installation image file for your system. |omv| provides ISO installers
	  for x86 architecture and several preconfigured images for ARM devices.
	- Disconnect all harddisks except the future system drive. This way you
	  avoid an accidental install on a storage drive (which will be configured
	  after installation anyway).

Installation variants:
	Choose your installation variant and follow the instructions.

	* :doc:`Dedicated drive </installation/via_iso>` - Advised method via ISO image. This runs OMV from its own drive.
	* :doc:`USB flash drive </installation/on_usb>` - This runs |omv| from a USB flash dive.
	* :doc:`Debian Operating System </installation/on_debian>` - This runs |omv| as a services on top of a Debian OS.
	* `Debian Operating System via deboostrap <https://forum.openmediavault.org/index.php/Thread/12070-GUIDE-DEBOOTSTRAP-Installing-Debian-into-a-folder-in-a-running-system/>`_. Use this as a last resource in case the installer does not recognize a specific essential hardware component like hard disk (NVME) or a network card that needs a higher kernel (backport).
	* :doc:`SD card </installation/via_image>` - This runs |omv| from a SD card.

First time use:
	If you have a screen attached, KVM or IMPI console the login screen will
	display the current IP address assigned for the |webui|. Open your browser
	and type that IP address. The default |webui| login credential is
	``admin:openmediavault``, the ``root`` password is the one you setup during
	installation.

	For ARM images the root password is the same as admin password.
