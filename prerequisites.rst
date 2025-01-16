Requisites
=============

The |omv| system is the most flexible Network Attached Storage (NAS) on the market,
this is because it relies on the operating system Debian GNU/Linux [9]_

Any system has software and hardware requirements, also minimal
ones and recommended ones.

Hardware requirements
---------------------

======  ================  =========  ==========  ==================================
 Item    supported         Minimal     Best       Recommendation
======  ================  =========  ==========  ==================================
 DRIV    SSD/HDD/USB...    1 disk      2 disk     2 disks: 128Gib HDD + 500Gib SSD
 RAM     1Gib+ any          1Gib       4Gig       8Gib+ dual channel DDR4/DDR3
 NIC     WiFi/Ether/USB     any       10Mb NIC    1GiB NIC or 10Gb NICs: SFP fiber
 CPU     arm,x86,x64        32bit      64bit      Intel Dual Core, AMD Ryzen
======  ================  =========  ==========  ==================================

The storage drives (DRIV)
^^^^^^^^^^^^^^^^^^^^^^^^^

This is the key of the system. |omv| supports any drive hardware and any drive 
interface (SATA, ISE, SCSI, USB, SERIAL) but information and management will
depend on the disk drives supported by the Debian operating system.

Modern hard disks drives have firmware inside that reports several attributes.
Any hard disks drives is supported but |omv| only supports SMART for those
disks that are connected to an HBA in pass-through mode.

The system manages two types of storage unit classification:

System drive storage
  The Storage Disk Drive(s) used to put the system program files (by partitions), 
  **this system drive (that is in fact a couple or more partitions) 
  cannot officially be used for shared resources or as user data drive**.
  What supported brands and sizes are covered in the software requirements section below.
  The recommendation for the system drive(s) hardware could be older spinning
  Hard Disk Drives (HDD), Disk-on-Module [3]_, CompactFlash [4]_ or thumb drives (USB),
  the Solid State Disks (SDD [2]_) must be managed.

Data drive storage
  The storage disk drive(s) where the data for the defined or used shares resources
  wil be stored. **Cannot be the same of the system drive(s) and sizes will
  depends of the usage of the resources**. Shared resources are managed over
  partitions, which is discussed in the software requirements topic below.
  The recommendation for the Data drives must be Solid State Disks (SSD [2]_ disks)
  for best performance or spinning Hard Disk Drives (HDD).

The memory (RAM)
^^^^^^^^^^^^^^^^

Enough RAM is vital to maintaining peak performance. There are several combinations
of installation sizes but the **recommendation is at least 4Gib for novice administrators**.

For best practice you should have 8GiB of RAM for basic operations in default installation.
and no matter the size, RAM must be configured in Dual Channel mode [8]_ 
inclusivelly if there are little amount of, it will improve performance.

Unless other NAS systems the |omv| system can run in at least 1Gib of RAM, but
of course will need expertise.

The communication card (NIC)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A NAS system as means is a network oriented system, of course |omv| is the
most flexible NAS system in the world and allows multiple ways of communication, 
this is becouse |omv| offers several modes of shared resources like RSYNC that 
do not depends on networking. But there are few key points:

- The NAS write speed to storage is limited to the speed of your NAS computer NIC card
- The NAS write speed to storage is limited to the speed of your network
- Speed of writing to the storage depends on ratio of the number of users accessing it.

Full-duplex NICs are recommended, half-duplex NICs typically offer 10/100 Mbit/s
and storage drives far exceed those speeds but are of course supported by |omv|.

Any supported NIC vendor is determined by the support of the operating system
where |omv| system resides and runs, which is Debian GNU/Linux.

The architecture (CPU)
^^^^^^^^^^^^^^^^^^^^^^

We have already denoted in the requirements table the supported architectures or
processors (which reduces and determines which computers can be used) but this is
really a reference since it is determined by the support of the operating system
where |omv| system resides and runs, which is Debian GNU/Linux.

Any computer system supported by the common requirements of Debian operating
system could be an |omv| system installation target. **Currently we supports
amd64 (x66 64bits), i386 (x86 32bits), ARMv7+ARMv8 (arm64/armel/armhf)**.

Software requirements
---------------------

======  =================  ==============  ==============  =======================================
 Item    Software           Minimal         Best            Recommendation
======  =================  ==============  ==============  =======================================
 OS      Debian Linux       oldoldstable    stable          Current stable (plus 1 month released)
 BOOT    BIOS,UBOOT,UEFI    BIOS,mbr        BIOS,gpt        Disable Secure boot, gpt table
 SDS     HDD,SSD,USB...     2 partitions    3 partitions    Root with 120G size, 8G swap size
 DDS     HDD,SSD,USB...     1 partition     1 per share     One disk or part per shared resource
 NET     LAN,WAN,SAN,VPN    LAN             SAN,PAN,LAN     Fiber ipv4, or at least cable LAN
======  =================  ==============  ==============  =======================================

The operating system (OS)
^^^^^^^^^^^^^^^^^^^^^^^^^

The |omv| is a piece of software, it resides and runs under a key software OS
named Debian GNU/Linux as "the universal operating system" [9]_ 

Supported Debian OS versions can be checked in the :doc:`releases section </releases>`

While possible to deploy in a virtual environment, depending of the nature of
virtualization it will degrade the performance access in various ways. Installation
in LXC or any other container based solution is not supported.

Whatever the situation, the |omv| assumes that target operating system does not
have any previous installation of any of the programs used by |omv| dependencies:

=============  ==============  =================  ==========================================
 software       package          related to        Observations
=============  ==============  =================  ==========================================
 http server    nginx           |webui|            port 80 must be free at installation
 http system    php             |webui|            only OS php packages wil be used!
 display GUI    lighdm,xdm..    Desktop install    **Conflicts, any will be deinstalled**
 network man    netplan.io      Networking         network is managed by |omv| with netplan
 ssh server     ssh             Remote access      any configuration will be managed
 mbs server     samba           Shared drives      any configuration will be managed
 quota man      quota           Quota manage       any configuration will be managed
=============  ==============  =================  ==========================================

The device boot (BOOT)
^^^^^^^^^^^^^^^^^^^^^^^^^

|omv| will install on any kind of boot device and this will relies on the
operating system that is Debian. The downloable ISO image ready to use from
the oficial web page only supports at the moment amd64 with BIOS mode boot.

The System drive storage (SDS)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The system storage disk will be fully managed and taken over by the |omv| after
installed. Any brand is supported as is also supported by the Debian system.
For Flash Drive type storage devices as well as solid state drives being used as
system storage drives please refer to the last section for technical details.

In case of the official ISO instalation, will automatically partition the system
storage disk drive into 3 partitons. Consult the next table for.

In case of a manual installation on a previous Debian operating system, this 
**drive must have at least two partitions**. Consult the next table for.

============  ==========  ===========  =======================================
 Partition     Min size    Best size    Mandatory
============  ==========  ===========  =======================================
 ``/boot``      256Mib      500Mib      Optional, partition used to boot
 ``/``           4Gi        120Gib      Yes, the partition were system install
 ``swap``       100Mib      16Gib       Yes, the partition for virtual ram
============  ==========  ===========  =======================================

The Data drive storage (DDS)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The data storage disk will be partially managed by the |omv| after installed,
and only in customized installation can be a partiton of the same system drive
storage.

Each data storage drive will be managed, but regardless of the partitioning
scheme, all data drive partitions will be mounted at the ``/srv/`` path.
The **data storage drive must be a different disk drive than the system disk drive**
where the operating system is installed. **One partition of each data
drive can handle one or many shared resources.**

==============  ==========  ===========  ========================================
 Partition       Min size    Best size    Mandatory
==============  ==========  ===========  ========================================
 ``/srv/<*>``     100Mib       bigger     Yes, size as need! example 128Gib
==============  ==========  ===========  ========================================

Technical notes
---------------

Take into **consideration that as more exquisite the customization as less supported
could be.**.

|omv| allows for minimal deployment and use of the system with very minimal
hardware/software requirements, at the cost of the key knowledge, but other NAS
systems allow ease of use at the cost of high requirements. |omv| allows both as
well in a well balanced use cases! [7]_

About minimal or custom setups
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It can be noted that |omv| system can be installed on just 4Gib of system partition,
with no more than 1Gib of RAM and using a WiFi or USB connection to access it
remotely (cos is a NAS system of course), on any small device such as Raspberry
ones which are ARM, or old i386s machines no matter is those are 32 or 64 bits, 
but of course as more exquisite the configuration more knowledge will be need
as per `issue comment #131 <https://github.com/openmediavault/openmediavault-docs/issues/131#issuecomment-2546765841>`_.

Technically OMV can be installed on a single storage disk, this is possible if
it is done on a previously configured Debian system, with a free partition apart
from the 3 necessary system partitions, previously formatted and configured.
Of course this is only possible for skilled linux users.

Drive Storage technical details
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

System Drives are not managed as same of Data Drives. System drives are not so
intensively used, but Data Drives will need triks to extend the useful life.

If you use a Flash Drive, select one with static wear leveling 6, without this
the drive will have a very short lifetime. It is also recommended to install and
activate the Flash Memory plugin.

In the same Solid State Disk, or rather Drive (SSD) for x86 architectures, is
usually only recognized properly by the BIOS or UEFI, when in the BIOS/UEFI the
feature AHCI has been activated for SATA (instead of IDE). Modern computers has
by default. But on old machines the default might/could be IDE.
About ARM based computers this are not a problem, when used SATA interfaces, but
EMMC ones could need tune up cos are threated as Flash drives.

On SSDs, the cleaning action TRIM is recommended for the good performance in
the long run. Otherwise it might become slow after some time. Very old SSD's from
before 2010 usually don't support TRIM.

On SSDs Hibernation (suspend-to-disk) causes a huge amount of write actions,
|omv| is a server system so it is expected to stay always on or off.

Partition table technical details
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Of course, the supported partition tables will depend on the installation mode,
and |omv| can handle any type of partition table supported by the Debian operating
system. This is because to manage shares on new or uninitialized storage drives
it will need to create partitions or at least read structure of thems.


.. [1] https://en.wikipedia.org/wiki/Paging
.. [2] https://en.wikipedia.org/wiki/Solid-state_drive
.. [3] https://en.wikipedia.org/wiki/Solid-state_drive#DOM
.. [4] https://en.wikipedia.org/wiki/CompactFlash
.. [5] https://en.wikipedia.org/wiki/USB_flash_drive
.. [6] https://en.wikipedia.org/wiki/Wear_leveling
.. [7] https://forum.openmediavault.org/index.php?board/29-guides/
.. [8] https://en.wikipedia.org/wiki/Multi-channel_memory_architecture
.. [9] https://www.debian.org/intro/about.en.html#what
