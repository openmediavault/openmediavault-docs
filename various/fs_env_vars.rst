Filesystem Environmental Variables
##################################

This is the current filesystem mount options passed when a mount button is executed in the webUI::

    OMV_FSTAB_MNTOPS_EXT2="defaults,nofail,user_xattr,noexec"
    OMV_FSTAB_MNTOPS_EXT3="defaults,nofail,user_xattr,noexec,usrjquota=aquota.user,grpjquota=aquota.group,jqfmt=vfsv0"
    OMV_FSTAB_MNTOPS_EXT4="defaults,nofail,user_xattr,noexec,usrjquota=aquota.user,grpjquota=aquota.group,jqfmt=vfsv0"
    OMV_FSTAB_MNTOPS_JFS="defaults,nofail,noexec,usrquota,grpquota"
    OMV_FSTAB_MNTOPS_XFS="defaults,nofail,noexec,usrquota,grpquota"
    OMV_FSTAB_MNTOPS_VFAT="defaults,nofail"
    OMV_FSTAB_MNTOPS_NTFS="defaults,nofail"
    OMV_FSTAB_MNTOPS_HFSPLUS="defaults,nofail,force"
    OMV_FSTAB_MNTOPS_BTRFS="defaults,nofail"
    OMV_FSTAB_MNTOPS_ISO9660="ro"
    OMV_FSTAB_MNTOPS_UDF="ro"

More information can be found `here <https://github.com/openmediavault/openmediavault/blob/master/deb/openmediavault/usr/share/php/openmediavault/globals.inc>`_.

This variables can be changed using the same method described :doc:`here </various/advset>`. Once you do that, all new mounted filesystem will inherit the new options. Problem is by the time you are reading this you already have a mounted filesystems with shares already created. The normal procedure would be delete every shared folder configuration in OMV , unmount and mount the filesystem again. To overcome this you can manually edit the internal configuration file:

``nano /etc/openmediavault/config.xml``

locate the <mntent> entry that belongs to the filesystem. You should be able to recognise it by the UUID. Once there you remove the noexec flag, you'll find in between the tags the fstab options. Something like this:

.. code-block:: xml

      <mntent>
        <uuid>f767ee54-eb3a-44c5-b159-1840a289c84b</uuid>
        <fsname>7f2d80ba-2a7c-4708-b601-673b304243fa</fsname>
        <dir>/media/7f2d80ba-2a7c-4708-b601-673b304243fa</dir>
        <type>ext4</type>
        <opts>defaults,nofail,user_xattr,noexec,usrjquota=aquota.user,grpjquota=aquota.group,jqfmt=vfsv0,acl</opts>
        <freq>0</freq>
        <passno>2</passno>
        <hidden>0</hidden>
      </mntent>

If you want to remove noexec flag, then change the opts line removing the options, should look like this::

    <opts>defaults,nofail,user_xattr,usrjquota=aquota.user,grpjquota=aquota.group,jqfmt=vfsv0,acl</opts>


Save the file with CTRL+X, run: ``omv-mkconf fstab``

You should be able to see the new options at ``/etc/fstab``, finally reboot the system and check with ``cat /proc/mounts`` that the noexec flag is no longer present for that particular mount.