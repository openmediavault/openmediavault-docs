Filesystem Environmental Variables
##################################

This is the current filesystem mount options passed when a mount button is executed in the |webui|::

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

This variables can be changed using the same method described :doc:`here </various/advset>`. Once you do that, all new mounted filesystem will inherit the new options. Problem is by the time you are reading this you already have a mounted filesystems with shares already created. The normal procedure would be delete every shared folder configuration in OMV , unmount and mount the filesystem again. To overcome this you can manually edit the internal database file::

    # nano /etc/openmediavault/config.xml

In this example we remove the `noexec` flag. First locate the `<fstab>` section, in there you will find several <mntent> entries that belongs to all registered filesystems. You should be able to recognise it by the label. Once there you can remove the `noexec` flag, in the `<opts>` line.

.. code-block:: xml

      <mntent>
        <uuid>f767ee54-eb3a-44c5-b159-1840a289c84b</uuid>
        <fsname>/dev/disk/by-label/VOLUME1</fsname>
        <dir>/srv/dev-disk-by-label-VOLUME1</dir>
        <type>ext4</type>
        <opts>defaults,nofail,user_xattr,noexec,usrjquota=aquota.user,grpjquota=aquota.group,jqfmt=vfsv0,acl</opts>
        <freq>0</freq>
        <passno>2</passno>
        <hidden>0</hidden>
      </mntent>

Change the opts line removing the `noexec`, should look like this::

    <opts>defaults,nofail,user_xattr,usrjquota=aquota.user,grpjquota=aquota.group,jqfmt=vfsv0,acl</opts>


Save the file with CTRL+X, run: ``omv-salt deploy run fstab``

You should be able to see the new options at ``/etc/fstab``, finally reboot the system and check with ``cat /proc/mounts`` that the noexec flag is no longer present for that particular mount.
