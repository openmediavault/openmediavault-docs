Prequisites
=============

|omv| is the most flexible Network Attached Storage (NAS) on the market,
this is because it relies on running on the operating system Debian GNU/Linux [9]_

Any system has software and hardware requirements, also minimal
ones and recommended ones.

Hardware requirements
---------------------

======  ================  =========  ==========  ==================================
 Item    supported         Minimal     Best       Recommendation
======  ================  =========  ==========  ==================================
 DRIV    SSD/HDD/USB...     1,any      2,HHD      2 disks: Seagate Firecuda, WD Black, IronWolf
 RAM     1GiB+ any          1GiB       4Gig       8GiB+ dual channel DDR4/DDR3
 NIC     WiFi/Ether/USB     any       10Mb NIC    1GiB NIC or 10Gb NICs: SFP fiber
 CPU     arm,x86,x64        32bit      64bit      Intel Dual Core, AMD Ryzen
======  ================  =========  ==========  ==================================

Storage drives (DRIV)
^^^^^^^^^^^^^^^^^^^^^^

This is the key of the system. |omv| supports any drive hardware and any drive
interface (SATA, ISE, SCSI, USB, SERIAL) but information and management will
depend on the disk drives supported by Debian system.
**Supported Debian OS versions can be checked in the** :doc:`releases section </releases>`.

Modern storage drives have firmware inside that reports several attributes.
Any storage drives is supported but |omv| only supports SMART for those
disks that are connected to an HBA in pass-through mode.

The system manages two types of storage unit classification:

System drive storage (SDS)
  The Storage Disk Drive(s) used to put the system program files.
  **This system drive (which can consist of several partitions)
  cannot officially be used for shared resources or as user data drive**.
  The recommendation for the system drive(s) hardware could be older spinning
  Hard Disk Drives (HDD), Disk-on-Module [3]_, CompactFlash [4]_ or thumb drives (USB),
  the Solid State Disks (SDD [2]_) must be managed. Best option are
  the Helium Hard Drives (HHD).

Data drive storage (DDS)
  The storage disk drive(s) where the user data will be stored. **Cannot be
  the same of the system drive(s) and sizes will depend of the usage of the stored user data**.
  Shared resources are managed over partitions, which is discussed in the software
  requirements topic below. The recommendation for the Data drives must be
  Solid State Disks (SSD [2]_ disks) for best performance or spinning
  Hard Disk Drives (HDD) for better device durability over time.

Memory (RAM)
^^^^^^^^^^^^

Sufficient RAM is vital to maintaining peak performance. There are several combinations
of installation sizes but the **recommendation is at least 4GiB for novice administrators**.

For best practice you should have 8GiB of RAM for basic operations in default installation,
and no matter the size, RAM must be configured in Dual Channel mode [8]_
which will improve performance in low memory installations.

Unlike other NAS systems |omv| can run in with as low as 1GiB of RAM, but
of course will need expertise.

Network interface card (NIC)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A NAS system as means is a network oriented system, of course |omv| is the
most flexible NAS system in the world and allows multiple ways of communication,
this is because |omv| offers several modes of shared resources like RSYNC that
do not depends on networking. But there are few key points:

- NAS write speed to storage is limited to the speed of your NAS computer network interface.
- NAS write speed to storage is limited to the speed of your network.
- Write speed to storage depends on ratio of the number of users accessing it.

Full-duplex NICs are recommended, half-duplex NICs typically offer 10/100 Mbit/s
and storage drives far exceed those speeds but are of course supported by |omv|.

Any supported NIC vendor is determined by the support of the operating system
where |omv| system resides and runs, which is Debian GNU/Linux.

Architecture (CPU)
^^^^^^^^^^^^^^^^^^

We have already denoted in the requirements table the supported architectures or
processors (which reduces and determines which computers can be used) but this is
really a reference since it is determined by the support of the operating system
where |omv| system resides and runs, which is Debian GNU/Linux.

Any computer system supported by the common requirements of Debian operating
system could be an |omv| system installation target. **Currently supported are
AMD64 (x86/x86-64 64bits), i386 (x86 32bits), ARMv7+ARMv8 (arm64 64bits armel/armhf 32bits)**.
The i386 version is no longer officially supported since version 6, although
it is still published by the project due to the nature of |omv| technology.

Software requirements
---------------------

======  =================  ==============  ================  =========================================
 Item    Software           Minimal         Best              Recommendation
======  =================  ==============  ================  =========================================
 OS      Debian Linux       |deb_version|   |deb_version|
 BOOT    BIOS,UBOOT,UEFI    BIOS,mbr        BIOS, GPT         Disable Secure boot, GPT table
 SDS     HDD,SSD,USB...     1, 4GiB         2, 120+500GiB     Disk drive with 120G root size, 8G swap size
 DDS     HDD,SSD,USB...     0 or any        HHD,1 per share   One disk or part per shared resource
 NET     LAN,WAN,SAN,VPN    LAN             SAN,PAN,LAN       Fiber IPv4, or at least cable LAN
======  =================  ==============  ================  =========================================

Operating system (OS)
^^^^^^^^^^^^^^^^^^^^^

|omv| is a piece of software, it resides and runs under a key software OS
named Debian GNU/Linux as "the universal operating system" [9]_

**Supported Debian OS versions can be checked in the** :doc:`releases section </releases>`.

While possible to deploy in a virtual environment, depending of the nature of
virtualization it will degrade the performance access in various ways. Installation
in LXC or any other container based solution is not supported.

Whatever the situation, |omv| assumes that target operating system does not
have any previous installation of any of the programs used by |omv| dependencies:

=============  ==============  =================  ==========================================
 software       package          related to        Observations
=============  ==============  =================  ==========================================
 http server    nginx           |webui|            port 80 must be free at installation
 http system    php             |webui|            only OS php packages wil be used!
 display GUI    lighdm,xdm..    Desktop install    **Conflicts, any will be deinstalled**
 network man    netplan.io      Networking         network is managed by |omv| with netplan
 ssh server     ssh             Remote access      any configuration will be managed
 smb server     samba           Shared drives      any configuration will be managed
 quota man      quota           Quota manage       any configuration will be managed
=============  ==============  =================  ==========================================

Device boot (BOOT)
^^^^^^^^^^^^^^^^^^

The boot type and its support is determined by the Debian operating system
which supports BIOS, UEFI, PXE, UBOOT and many others, the configurations
of these depend on the installation of the operating system and once done
the |omv| can be installed without problems.

However the downloadable and ready-to-use ISO image from the official |omv| website
only supports AMD64 with BIOS mode boot at the moment. If you want to have |omv| on
other computers with another boot type/mode, then you should install Debian first
and then :doc:`manually</installation/on_debian>` |omv|.

**Supported Debian OS versions can be checked in the** :doc:`releases section </releases>`.

System drive storage (SDS)
^^^^^^^^^^^^^^^^^^^^^^^^^^

Any brand of storage disk will be supported as long as it is supported by
Debian since it is where |omv| system resides
and runs, check it at the :doc:`releases section </releases>`.

The system storage disk will be fully managed and taken over by |omv| after
installed. In case of the official ISO installation, will automatically partition
the system storage disk drive into 3 partitions. See table below for details.

In case of a manual installation on a previous Debian operating system, this
**drive should have at least two partitions**. See table below for details.

============  ==========  ===========  =======================================
 Partition     Mininmal    Best size    Mandatory
============  ==========  ===========  =======================================
 ``/boot``      256Mib      500Mib      Optional, partition used to boot
 ``/``           4Gi        120GiB      Yes, the partition were system install
 ``swap``       100Mib      16GiB       Optional, the partition for virtual ram
============  ==========  ===========  =======================================

Data drive storage (DDS)
^^^^^^^^^^^^^^^^^^^^^^^^

The data storage disk will be partially managed by the |omv| after installation,
and only in customized installation this can be a partition of the same system drive
storage.

Each data storage drive will be managed, but regardless of the partitioning
scheme, all data drive partitions will be mounted at the ``/srv/`` path.
The **data storage drive must be a different disk drive than the system disk drive**
where the operating system is installed. **One partition of each data
drive can handle one or many shared resources.**

==============  ==========  ===========  ========================================
 Partition       Min size    Best size    Mandatory
==============  ==========  ===========  ========================================
 ``/srv/<*>``     100Mib       bigger     Yes, size as need! E.g. 128GiB,500GiB,4TiB
==============  ==========  ===========  ========================================

Technical notes
---------------

Take into **consideration that the more customized the installation is, the less supported
it could be**.

|omv| allows for deployments on systems with low hardware/software specification,
at the hands of knowledgeable operator while other NAS
systems allow ease of use at the cost of high requirements.
|omv| allows both as well in a well balanced use case! [7]_

About minimal or custom setups
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Please note that |omv| systems can be installed on just 4GiB of system partition,
with no more than 1GiB of RAM and using a WiFi or USB connection to access it
remotely, on any small device such as Raspberry Pi or Banana Pi boars
which are ARM, or old i386s machines no matter if those are 32 or 64 bits,
but of course as more unique the configuration the more knowledge will be need
as per `issue comment #131 <https://github.com/openmediavault/openmediavault-docs/issues/131#issuecomment-2546765841>`_.

Technically OMV can be installed on a single storage disk, this is possible if
it is done on a previously configured Debian system, with a free partition apart
from the 3 necessary system partitions, previously formatted and configured.
Of course this is only possible for skilled Linux users.

Drive Storage technical details
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

System Drives are not managed as same of Data Drives. System drives are not so
intensively used, but Data Drives will need tricks to extend the useful life.
Drivers support is by the project https://www.smartmontools.org/wiki/TocSupport

If you use a Flash Drive, select one with static wear leveling 6, without this
the drive will have a very short lifetime. It is also recommended to install and
activate the Flash Memory plugin.

In the same Solid State Disk, or rather Drive (SSD) for x86 based architectures, is
usually only recognized properly by the BIOS or UEFI, when in the BIOS/UEFI the
feature AHCI has been activated for SATA (instead of IDE). Modern computers have that
by default. But on old machines the default might/could be IDE.
About ARM based computers this is not a problem, when used SATA interfaces, but
on eMMCs will need some tuning because they are treated like Flash drives.

On SSDs, the cleaning action TRIM is recommended for sustained long-term performance.
Otherwise it might become slow with time. Very old SSD's from before 2010 usually don't support TRIM.

Take note that eMMCs, SSDs, Flash drives will have a lifetime degradation,
excessive writes wear out those drives faster, specially in they are very cheap.

On SSDs Hibernation (suspend-to-disk) causes a huge amount of write actions,
|omv| is a server system so it is expected to stay always on or off.

About compression or encryption
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Enabling encryption on SSDs also means more writes which wear out SSDs, eMMCs
or Flash drives faster.

As well as enabling compression on filesystems like Btrfs or ZFS; although Ext4
has better commit timing; a parameter with commit=600 to 800 is best
for this particular one.

Partition table technical details
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Of course, the supported partition tables will depend on the installation mode,
and |omv| can handle any type of partition table supported by the Debian.
This is because to manage shares on new or uninitialized storage drives
it will need to create partitions or at least read structure of them.


.. [2] https://en.wikipedia.org/wiki/Solid-state_drive
.. [3] https://en.wikipedia.org/wiki/Solid-state_drive#DOM
.. [4] https://en.wikipedia.org/wiki/CompactFlash
.. [5] https://en.wikipedia.org/wiki/USB_flash_drive
.. [6] https://en.wikipedia.org/wiki/Wear_leveling
.. [7] https://forum.openmediavault.org/index.php?board/29-guides/
.. [8] https://en.wikipedia.org/wiki/Multi-channel_memory_architecture
.. [9] https://www.debian.org/intro/about.en.html#what
