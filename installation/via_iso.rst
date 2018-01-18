.. _installation_index:

Installation using an ISO image
###############################

Burn the installer
------------------
	For x86 architecture you can burn the ISO directly into a USB drive using
	`etcher <https://etcher.io/>`_ or  dd linux utility::

	$ sudo dd if=xxx.iso of=/dev/sdX bs=4096

	If you have a CD-DVD burner, you can burn the ISO into an optical media
	then boot from CD or DVD.

Boot the installer
------------------
	For x86 architecture, enter BIOS configuration, select to boot either from
	USB or CD and reboot.

Installer
---------
	The current ISO installer is reduced to have minimal interaction. You will
	prompted to select location, language and root password. The installer will
	pick the first available disk to deploy the the OS. Once the installer
	finished the system will reboot, make sure you remove the installer and
	select BIOS to boot from the disk where |omv| was installed. You can also
	start connecting any data drives you previously disconnected before install
	or reinstall.

	.. figure:: /_static/images/install_via_iso/install_1.png
	.. figure:: /_static/images/install_via_iso/install_2.png
	.. figure:: /_static/images/install_via_iso/install_3.png
	.. figure:: /_static/images/install_via_iso/install_4.png
	.. figure:: /_static/images/install_via_iso/install_5.png
	.. figure:: /_static/images/install_via_iso/install_6.png
	.. figure:: /_static/images/install_via_iso/install_7.png
	.. figure:: /_static/images/install_via_iso/install_8.png
	.. figure:: /_static/images/install_via_iso/install_9.png
	.. figure:: /_static/images/install_via_iso/install_10.png
	.. figure:: /_static/images/install_via_iso/install_11.png
	.. figure:: /_static/images/install_via_iso/install_12.png
	.. figure:: /_static/images/install_via_iso/install_13.png
	.. figure:: /_static/images/install_via_iso/install_14.png
	.. figure:: /_static/images/install_via_iso/install_15.png
	.. figure:: /_static/images/install_via_iso/install_16.png
	.. figure:: /_static/images/install_via_iso/install_17.png
	.. figure:: /_static/images/install_via_iso/install_18.png
	.. figure:: /_static/images/install_via_iso/install_19.png

Troubleshooting
---------------

The error `Unable to install GRUB in /dev/sda` occurs.
	In this case execute the following steps:

	- Select `Continue` in this window and also on the next which says
	  `Installation step failed`.
	- In the Debian installer main menu (which should have popped up by now),
	  select `Execute a shell` and then `Continue`.
	- Execute the following commands::

		# Chroot.
		chroot /target
		# Replace [a-z] with the drive you want to install grub to.
		# This is normally the drive you've selected to install OpenMediaVault on.
		grub-install /dev/sd[a-z]
		# Update GRUB.
		update-grub
		# Exit chroot.
		exit
		# Exit shell.
		exit

	- Select `Continue without boot loader` in the Debian installer main menu and
	  then `Continue`.
	- It should now continue the installation successfully.
