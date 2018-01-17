.. _installation_index:

Installation using an ISO image
###############################

Burn the installer:
	For x86 architecture you can burn the ISO directly into a usb drive using
	`etcher <https://etcher.io/>`_ or  dd linux utility. If you have a CD-DVD
	burner, you can burn the ISO into an optical media then boot from CD or DVD.
	Etcher can also be used to transfer arm images into SD cards.

Boot the installer:
	For x86 architecture, enter BIOS configuration, select to boot either from
	USB or CD and reboot. ARM images are ready to go, so boot from sd card and
	wait for the initial setup to complete. This takes around 30 minutes in
	slow devices like Raspberry PI.

Installer:
	The current ISO installer is reduced to have minimal interaction. You will
	prompted to select location, language and root password. The installer will
	pick the first available disk to deploy the the OS. Once the installer
	finished the system will reboot, make sure you remove the installer and
	select BIOS to boot from the disk where |omv| was installed. You can also
	start connecting any data drives you previously disconnected before install
	or reinstall.
