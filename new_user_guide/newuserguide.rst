##############
New User Guide
##############

.. image:: /new_user_guide/images/underconstruction.jpg
    :width: 200px
    :align: center
    :height: 200px
    :alt: Under Construction

In the interim, a complete copy of the User Guide is available → `here <https://github.com/OpenMediaVault-Plugin-Developers/docs/blob/master/Getting_Started-OMV5.pdf>`_ .


.. image:: /new_user_guide/images/divider-c.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:


.. image:: /new_user_guide/images/1_Title_page.jpg
    :width: 588px
    :align: center
    :height: 439px
    :alt:

.. image:: /new_user_guide/images/divider-c.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

******************************
Introduction to Openmediavault
******************************

|omv| is a File Server / NAS system designed to work on most
modern IBM compatible PC systems, to include typical amd64 or i386 PC’s
and select ARM devices. |omv| can be thought of as
filling a role similar to Microsoft's Server Essentials, but extends
far beyond the role of a basic File Server with additional functionality
added VIA plugin’s and Dockers. |omv| is designed to work with popular
client operating systems and multiple filesystem types, utilizing proven
data sharing techniques on small and medium sized Local Area Networks.

In meeting the needs of it's intended users, individuals and
small-to-medium-sized businesses, |omv| is designed for
flexibility.

.. image:: /new_user_guide/images/2_Intro.jpg
    :width: 1024px
    :align: center
    :height: 443px
    :alt:

.. image:: /new_user_guide/images/divider-c.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

History
=======

Openmediavault's history began with Volker Theile, who was the only
active developer of the FreeNAS project by the end of 2009.   Volker
became interested in completely rewriting FreeNAS, for use on Linux.
Initially, he named the rewritten package **coreNAS** .  Shortly
thereafter, Volker discarded the name **coreNAS** in favor of
**openmediavault** .  |omv|'s initial release was on 17
October 2011.  It's built upon very mature and proven software layers
and is under constant development. |omv| relies on the Debian
project and uses their system and repositories as a base.  The project
focus is on creating and maintaining a stable and extensible NAS system
that is intuitive and easy to use.

Purpose
=======
The purpose of |omv|, is to
provide a NAS system that is highly “extensible” with value added
plugin’s and access to numerous Dockers that are desirable and
beneficial to home users and small businesses at little to no cost.

One of the ambitions of the |omv| project is to make advanced NAS
technologies and features available to inexperienced users in an easy to
use |webui|, thereby making it possible for people, without extensive
knowledge of Linux, to gain easy access to advanced technologies.

Getting Involved
================
If businesses and home users find |omv| to be beneficial, please consider
supporting the project with a modest donation.  While |omv| is free,
donations to cover Web site costs, hardware for testing, and other
unavoidable expenses are needed and very much appreciated.


`Donate to openmediavault <https://www.openmediavault.org/?page_id=1149>`_ (Main project development)

`Donate to omv-extras.org <http://omv-extras.org/>`_  (Support for Single Board Computers and Development of Plugins.)

The |omv| project is looking for coding talent and contributors.  If one
has developer experience, (BASH, PHP, Python, Javascript) the project
would like to hear from you.  Users with Linux experience are invited to
help out on the `openmediavault Forum <https://forum.openmediavault.org/index.php/BoardList/>`_.

.. image:: /new_user_guide/images/divider-c.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

****************
About this Guide
****************

In computing, generally speaking, there are several ways to do the same
thing.  By extension,  methods and methodology become progressively more
advanced as a user's skill level increases.  With these notes in mind,
methods found in this guide may not be considered as “Best Practice”, especially from a hardened security perspective.  The purpose and intent of this guide is to provide a walk-through to get users up and running as quickly and easily as possible.

* This guide contains links to external sources of information and software.  It's best used on a PC connected to the Internet.

* This is a community document and a work in progress.  Input and feedback are welcome and can be sent to: omvguide@gmail.com

Beginners:
==========
This document is intended for beginners who will, primarily, be using
the |omv|'s GUI.  Beginners are assumed to have basic knowledge of
computers and their LAN systems, and a Windows or Apple PC.
The focus of this guide will be to take a technically easy route, for
the widest possible cross section of new users, toward accomplishing
basic tasks using methods and processes that are easy to understand and
duplicate.

Advanced Users:
===============
Openmediavault was designed to be intuitive for advanced users and beginners alike.
After the installation is complete, for a streamlined setup, see the 
`Quick Start Guide <https://openmediavault.readthedocs.io/en/5.x/new_user_guide/newuserguide.html#quick-start-guide-for-advanced-users>`_ .  

A Cautionary Note for Advanced Users:
-------------------------------------
Many of the configuration files traditionally used to customize Debian
Linux are controlled by the |omv| system database.  As a result, manual
edits of configuration files may be overwritten as of the next,
“on-demand”, configuration change in the |omv| GUI.  Further, it is
possible to “break” |omv| with alterations and permissions changes to the
files of the boot drive, on the command line.
In the beginning it's best to rely, primarily, on the GUI for
configuration and control.  Otherwise, before attempting to customize
the operating system, backing up the boot drive is highly recommended.

.. image:: /new_user_guide/images/divider-c.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

********
Hardware
********

Hardware requirements to run |omv| are very modest, however, actual
hardware requirements for specific “use cases” vary widely.  The
following is intended only as general guidance.

Compatibility:
==============

|omv| 5.X is currently supported by Debian 10, “Buster”.
Compatible hardware and other requirements of Debian Linux are available
at Debian.org

64 bit hardware (amd64):
========================

The |omv| project maintains convenient, fully integrated, |omv|/Debian
installation ISO's.  This is the best method for getting |omv| up and
running quickly.

32 bit Hardware (i386):
=======================

While |omv| is supported by 32 bit Debian installations, it's a two step
scripted process referenced in; `Installing on i386 32-bit Platforms`_ . 
The |omv| project does not provide integrated 32 bit installation ISO's.

ARM Hardware:
=============

The |omv| project provides scripted installation support for ARM Single
Board Computer (SBC) platforms.  Supported platforms are the Raspberry
Pi, models 2B and higher, and various ARM platforms supported by
the `Armbian Project <https://www.armbian.com/download/>`_ .

Minimum Hardware requirements
=============================

|omv|/Debian will run on I386, AMD64, and select ARM platforms with 1GB
of ram or less, but performance expectations should be adjusted
accordingly.  The system boot drive should have a minimum of 8GB capacity.

Recommended Minimum requirements
================================

For basic File Server operations - 1 or 2 users:

* Intel Core 2 Duo or equivalent AMD processor and 1GB of RAM.
* Any of the ARM Single Board Computers supported by |omv|.

If flash media is used, (USB thumb-drives, SD-cards, etc.) the system
boot drive should have at least 16GB capacity, for longer life.

Recommended Hardware and Considerations for a good use experience
=================================================================

i386 or amd64
-------------

* Intel i3 (or equivalent AMD processor), 4GB ram or better (ECC preferred) and a 16GB system boot drive will provide good performance in home or small business use cases.
* As the number of NAS users increase and server processes are added, processing power and memory requirements increase.
* For file caching, in support of normal file system operations, performance is better with more RAM.
* The number of a Motherboard's SATA or SAS ports can be a factor if future storage expansion is needed.
* A case design that accommodates the physical installation of additional hard drives can be helpful.
* Integrated video is preferred over add-on Video cards.  With |omv|'s headless server design, add-on Video cards are an excessive and unnecessary power drain, with no performance benefit. Installing a high end, high powered Video card in a headless server is analogous to installing a 65 to 200 watt light bulb in a closet, without a switch, and closing the door.

ARM - Single Board Computers:
-----------------------------

Performance levels vary greatly among the various models
of **Single Board Computer** (hereafter referred to as an "**SBC**")
that are supported by Armbian, Raspbian, and |omv|.  While most will
support file server operations for a few users, if running server
add-on's or Dockers is a requirement, research the chosen SBC carefully
before buying.  `Armbian's <https://forum.armbian.com/>`_
or `openmediavault's <https://forum.openmediavault.org/>`_ forums may be of
assistance, along with Internet product reviews.
*When considering an SBC as a primary NAS server for home use, note that support for SBC's is for* **the current openmediavault release only**.
*Accordingly, SBC users should read the ending cautionary note in* `Operating System Backup`_ .

Raspberry PI's
^^^^^^^^^^^^^^
(Hereafter referred to as **R-PI's**.)
Given the current market for SBC's, the majority of SBC users will
likely be owners of R-PI's.

|omv| runs well on the R-PI 4.  While |omv| will run on an R-PI model 2B and
the various models of the R-PI 3, performance is poor.   What exactly
does “poor performance” mean?  In this context, if the R-PI's CPU is
running at 100%, |omv| my not show up on the network and / or network
shares may not open.  This may give the false impression that there's a
software or permissions problem.  In other instances, the |webui| login
page may not respond.

These issues may appear to be software related, but that's not
always the case.  Older R-PI's are very easily over stressed and, during
periods where the CPU is running at 100%, they may not respond to
external input.  With this performance limitation in mind, earlier
versions of the R-PI (2B and 3X models) should be used only as a basic
file server for 1 or 2 user home environments, where multitasking is
less likely.  If running automated tasks, it's best to schedule them to
run in the early morning hours when user access would not be affected.
In addition, R-PI's suffer from USB under powering in models 2B and 3X.
See notes regarding this issue in `USB Power - A Common Raspberry PI problem`_ .    

Where CPU Power may be Needed – “Transcoding”
=============================================
If a users' primary consideration in setting a up a media server, CPU
selection or identification may need to be carefully considered.
Transcoding is a process for translating media file formats into types
that mobile devices understand.  Since mobile devices are low powered,
they're not capable of re-processing high resolution media files
smoothly so the processing burden is often transferred to the media
server.

----

Pre-2011 Intel and AMD CPU's
----------------------------
`Plex <https://support.plex.tv/hc/en-us/articles/200250377-Transcoding-Media>`_, a popular media server, recommends at least 2000 on the CPU's
`PassMark <https://www.cpubenchmark.net/cpu_list.php>`_ score for each concurrent 1080p transcoded stream.
See the advice article → `here <https://support.plex.tv/hc/en-us/articles/201774043-What-kind-of-CPU-do-I-need-for-my-Server->`_   However note that this advice
applies to pre-2011 Intel and AMD CPU's.

Look up an older CPU here →  `PassMark CPU Benchmarks <https://www.cpubenchmark.net/cpu_list.php>`_



2011 and Newer Intel CPU's
--------------------------

As of the beginning of the Sandy Bridge CPU series in 2011 and later, a core has
been added to Intel CPU's for the sole purpose of video transcoding.  CPU's with 
`Quick Sync <https://en.wikipedia.org/wiki/Intel_Quick_Sync_Video>`_  , to include Celeron and Atom models that are 
relatively low powered, do a good job of transcoding for portable devices.

If NAS administrators have numerous smart phone users, in their homes or
businesses, who will be watching transcoded video on the small screen, CPU loading
and Video processing features may require some additional thought and research.


Additional reading:
`Intel Quick Sync versus similar AMD technology <https://www.macxdvd.com/mac-dvd-video-converter-how-to/what-is-intel-quick-sync-video.htm>`_

----

Selecting a Boot Drive
======================

Nearly any type of hard drive, SSD, or flash device (USB thumb-drives and
SD-cards) 8GB or larger, will function as an |omv| boot drive.

However, some notions of achieving a “Faster” or a “Better Performing NAS server”
by using certain types of fast boot media should be dispelled.

Server booting requirements and considerations are different when compared to
desktop and business workstation requirements.

* Given |omv|'s lean configuration, boot times can be fast.  Boot times of 1 minute and Shutdown times of 20 seconds are common, even when using relatively slow flash media such as USB thumb-drives and SD-cards.  (Recent models can be quite fast – check their benchmarks.)

* Typically servers are rebooted no more than once a week.  When automated, a reboot event is usually scheduled after-hours when users are not affected.

* After the boot process is complete, most of |omv|'s file server functions are running from RAM.

**Conclusion – for Linux file server operations, fast boot media is not important.**

* “The WEB/GUI is more responsive with fast media.”

This is the single instance where an SSD or a spinning hard drive may create the illusion of higher performance.  In 
the traditional role of a NAS as a File Server, when the server boots, the Linux kernel and most of the necessary 
processes required to act as a File Server are loaded into RAM - the fastest possible media for execution.

Navigating |omv|'s WEB/GUI interface is another matter.  Loading WEB pages may call files from the boot drive, which may 
make the server appear to be slower, when using slow media.  However, the speed of the boot drive has little impact on 
overall file server function and actual NAS performance.

*The above assumes that adequate RAM has been provisioned.*

----

Final Notes on Choosing a Boot Drive
------------------------------------

Openmediavault’s boot requirements are very modest:
While some users prefer traditional hard drives or SSD's, the boot
requirement can be served with USB thumb-drives and SD-cards, 8GB or
larger.

With USB connections on the *outside* of a PC case, cloning USB drives for `operating system backup`_ is an easy 
process.  Given this consideration, some users prefer USB thumb-drives and other external flash media to internal 
drives.  Further, given the ease of operating system recovery in the event of a boot drive failure, beginners are 
encouraged to consider using flash media.

If flash media is used:

**New** name brand drives are recommended such as Samsung, SanDisk, etc.
While not absolutely essential for the purpose; USB3 thumb-drives are
preferred, due to their more advanced controllers, and SD-cards branded
A1 for their improved random read/write performance.  **USB3** thumb-drives
and **A1** spec'ed SD-cards are faster and, generally speaking, more
reliable than similar items with older specifications.

While boot drive size matters, bigger is not always better.  An
acceptable size trade off for wear leveling and speed of cloning is
between 16 and 32GB.  (“**Wear leveling**” will be explained during the
installation and configuration of the flash-memory plugin.)

The flash-memory plugin is required for flash media.  It's purpose and
installation is detailed in `The Flash Memory Plugin <https://openmediavault.readthedocs.io/en/5.x/new_user_guide/newuserguide.html#the-flash-memory-plugin-amd64-users-only>`_ .   

**Use-case exceptions where boot media larger than 32GB may be useful:**

* Running applications that utilize WEB interfaces, such as Plex, Emby, etc.

* Hosting Web or Media Servers with extensive content.

* Hosting Virtualized Guest operating systems with desktops.  (Does not apply to ARM platforms. ARM platforms can not virtualize i386 or amd64 platforms. )

(There's no penalty for starting with a smaller boot drive. Moving to a larger
drive, if needed, can be done later.)

.. note::   Buying flash devices on-line, even from reputable retailers, comes with the substantial risk of buying fakes.

Buying flash drives, in sealed packaging, from walk-in retail stores with liberal return
policies is recommended.  The use of cheap generics, fakes or knockoffs is highly discouraged.
They tend to have a short life and they're known to cause problems, even if they initially test
error-free.  In addition, to detect fakes or defective media *even when new*; all SD-cards
and USB thumb-drives, should be formatted and tested in accordance with the process outlined
under `Format and Test Flash Media`_ . 

----

Hardware - The Bottom Line
==========================

Again, |omv|/Debian's hardware requirements are modest.  Nearly any IBM
compatible PC or Laptop produced in the last 10 years could be re-purposed
as an |omv| server.

However, it should be noted that newer hardware is, generally speaking, more
power efficient and it's higher performing.  The power costs of running older
equipment that is on-line, 24 hours a day, can easily pay for newer, more
power efficient equipment over time.

Further, the supported ARM platforms are both power efficient and capable of
providing file server functions in a home environment.  (Again, performance
expectations should be adjusted in accordance with the capabilities of the
hardware.)

.. image:: /new_user_guide/images/divider-c.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

********************************************
Installing on Single Board Computers (SBC's)
********************************************


Installation guides for SBC installations are available
in `PDF's <https://forum.openmediavault.org/index.php/Thread/28789-Installing-OMV5-on-Raspberry-PI-s-Armbian-Supported-SBC-s/?postID=214407#post214407/>`_
or in a `Wiki <https://wiki.omv-extras.org/>`_ .


.. image:: /new_user_guide/images/divider-c.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

***********************************
Installing on i386 32-bit Platforms
***********************************


An installation guide for 32-bit installations is available
in `PDF <https://forum.openmediavault.org/index.php/Thread/28789-Installing-OMV5-on-Raspberry-PI-s-Armbian-Supported-SBC-s/?postID=214407#post214407/>`_
or in a `Wiki <https://wiki.omv-extras.org/>`_ .


.. image:: /new_user_guide/images/divider-c.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

************************
amd64 (64-bit) Platforms
************************

This guide assumes the user will be installing from a CD, burned
from an image found in |omv|'s files
repository `openmediavault's files repository <https://sourceforge.net/projects/openmediavault/files/>`_ ,
using 64 bit hardware.

----

Downloading
===========

Beginners should download the latest stable version from `Sourceforge.net <https://sourceforge.net/projects/openmediavault/files/>`_
and copy or download the SHA or MD5 checksums for the ISO.  The
checksum value will be used with the MD5 SHA checksum utility.

.. note:: Windows Notepad can open MD5 files by selecting “**All Files**”, next to the file name drop down.

.. warning:: If users install Beta versions of |omv|, they are agreeing to be a “tester”.  As part of being a tester, users may experience issues or bugs that can not be resolved which may result in **lost data**.  Plan accordingly, with full data backup.

Verify the download
-------------------

After the download is complete, verify the download with a
`MD5 & SHA checksum utility <http://md5-sha-checksum-utility.en.lo4d.com//>`_.
MD5 and SHA hashes check for image corruption that may have occurred
during the download.

.. note:: Beginners - DO NOT SKIP THIS STEP.  The chance of image corruption is high when downloading and it's pointless to build a server with flawed software.  Even the **slightest** corruption of the installation ISO may ruin your installation and the effects may not be noticed until well after your server is built and in use.  Headaches can be avoided by checking the image.

----

Installing - amd64 Platforms
============================

Burning a source CD
-------------------

Assuming a CD/DVD drive is installed; in most cases, double clicking an
installation file, with an **.ISO** extension, will trigger a CD burning utility
on a Windows Computer or a MAC.  If help is needed for this process, see the
following link.

`How to burn an ISO image in Windows 7, 8, 10 <https://www.lifewire.com/how-to-burn-an-iso-image-file-to-a-dvd-2626156>`_

Creating a Bootable ISO Thumb-drive
-----------------------------------

For PC's without an Optical drive; the |omv| ISO can be installed using a
Thumbdrive as the ISO source, and install the Debian/|omv| system to a second
thumb drive.

**Before creating an ISO thumb-drive consider checking the drive using the utilities and process described below in**, Preparing Flash Media.

For assistance in creating a bootable ISO thumb-drive, see the following link.

`How to install an ISO file on a USB drive <https://www.lifewire.com/how-to-burn-an-iso-file-to-a-usb-drive-2619270>`_

----

**If installing to a standard hard drive or SSD, skip to** Installing |omv|.

----

Preparing Flash Media
---------------------

To use flash media as a boot drive, a couple utilities are recommended:

`SDFormatter <https://www.sdcard.org/downloads/formatter_4/eula_windows/index.html/>`_ (get
the latest version), and `h2testw1.4 <http://www.heise.de/ct/Redaktion/bo/downloads/h2testw_1.4.zip>`_ .

* SDFormatter installs in the same manner as a typical Windows program.

* h2testw 1.4 is stand-alone “portable” application.  Simply unzip h2testw_1.4 onto the desktop, open the folder, and double click the executable.

Due to the rise in counterfeit media and media that reports a fake size, it's recommended that all USB thumb-drives, new or used, be formatted with SDFormatter and tested with  h2testw1.4  before using them.

----

Format and Test Flash Media
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Using SDFormatter, do a clean format:
(While SDFormatter was designed for SD-cards, it can format USB thumb-drives
for error testing.  For those who would prefer a formatter specifically for a
USB thumb-drive; `HPUSBDISK.EXE <https://www.mediafire.com/file/693jiig27dk846h/HPUSBDisk.exe/file/>`_  )

SDFormatter will detect a USB thumb-drive.  A volume label is optional and the
default options are fine.

.. image:: /new_user_guide/images/3_SDFormatter.jpg
    :width: 372px
    :align: center
    :height: 438px
    :alt:

Click on **Format**

----

After the drive format is completed, open **h2testw** and select your language.

Then, click on **Select target**

.. image:: /new_user_guide/images/4_H2testw.jpg
    :width: 433px
    :align: center
    :height: 270px
    :alt:

----

Under **Computer**, select the flash media previously formatted.

.. image:: /new_user_guide/images/5_H2testw_2.jpg
    :width: 390px
    :align: center
    :height: 398px
    :alt:

----

Select **Write+Verify**.  (Do not check endless verify)

.. image:: /new_user_guide/images/6_H2testw_3.jpg
    :width: 486px
    :align: center
    :height: 296px
    :alt:

----

A dialog box similar to the following may pop up, drawing attention to a **1MB** difference.
Ignore it and click on **OK**.

.. image:: /new_user_guide/images/7_H2testw_4.jpg
    :width: 497px
    :align: center
    :height: 199px
    :alt:

----

“Without errors” is the desired outcome.
(If media tests with errors or is much smaller than is indicated by its labeled size, don't use it.)

.. image:: /new_user_guide/images/8_H2testw_5.jpg
    :width: 417px
    :align: center
    :height: 357px
    :alt:

After H2testw verifies the USB thumb-drive, do one more clean format, using
SDFormatter, before using the thumb-drive.

----

amd64 – |omv| Installation
===================================

If your PC platform won't boot onto a CD or USB thumb-drive with the installation
ISO, it may be necessary to change the boot order in BIOS, to set the
CD/DVD drive or USB boot to the top of the boot order.  This link may provide
assistance on this topic. → `How To Enter BIOS <https://www.lifewire.com/how-to-enter-bios-2624481>`_

If difficulties are encountered during the ISO installation, consider
the → `Alternate 64bit installation guide <http://https://github.com/OpenMediaVault-Plugin-Developers/docs/blob/master/Adden-C-Installing_OMV5_on_32-bit_i386.pdf/>`_
Or use `the Wiki <https://wiki.omv-extras.org/doku.php?id=installing_omv5_i386_32_bit_pc>`_ .

----

An installation walk through:

**Boot Menu:**  Select **Install**

.. image:: /new_user_guide/images/9_Install_Menu.jpg
    :width: 987px
    :align: center
    :height: 504px
    :alt:

**Select a Language:**  **(As needed)**

.. image:: /new_user_guide/images/10_Language.jpg
    :width: 790px
    :align: center
    :height: 423px
    :alt:

**Select your Location:**  **(As appropriate.)**

.. image:: /new_user_guide/images/11_Location.jpg
    :width: 790px
    :align: center
    :height: 423px
    :alt:

**Configure the Keyboard:** **(Select as appropriate)**

.. image:: /new_user_guide/images/12_Key_Board.jpg
    :width: 794px
    :align: center
    :height: 426px
    :alt:

**Configure the Network:**

While the default hostname is fine,
a server name that is a bit shorter might be easier to work
with later on.  (Something like **OMV1**).

.. image:: /new_user_guide/images/13_Config_Network.jpg
    :width: 791px
    :align: center
    :height: 197px
    :alt:

**Configure the Network:**

If applicable, enter your domain name suffix.  Otherwise, for home users and businesses with
peer to peer networks, the default entry is fine.

.. image:: /new_user_guide/images/14_Config_Network2.jpg
    :width: 779px
    :align: center
    :height: 188px
    :alt:

**Set up users and passwords:**

Follow the on screen guidance for setting the root password.  While not recommended, it
would be better to write down the **root password**, then to forget it.

.. image:: /new_user_guide/images/15_root_password.jpg
    :width: 779px
    :align: center
    :height: 263px
    :alt:

**Set up users and passwords:**

Follow the on screen guidance for setting up a new admin user and password.

.. image:: /new_user_guide/images/16_Create_User.jpg
    :width: 779px
    :align: center
    :height: 188px
    :alt:

**Configure the Clock:**

Select your time zone.

(NO PIC)

**Partition Disks 1:**

If two storage devices are available for installation, this screen is displayed.

.. image:: /new_user_guide/images/17_Partition_Disks1.jpg
    :width: 785px
    :align: center
    :height: 165px
    :alt:

**Partition Disks 2:**

If installing to a single internal drive, there will be only one selection
available.  In this particular example, the installation is placed on a USB thumb-drive

.. image:: /new_user_guide/images/18_Partition_Disks2.jpg
    :width: 775px
    :align: center
    :height: 230px
    :alt:

Partition Disks 3:

(No Pic)

A 3rd window asks for confirmation of partition selections. Select Yes.

.. note::  If installing to a USB drive, at this point, it is possible to an error may pop-up regarding partitioning the drive, and recommend a reboot.  Follow the recommendation.  After the reboot, the partition operation should succeed the 2nd time around.

**The system installs..........**

**Configure the Package Manager:  Debian Archive Mirror Country**

(NO PIC)

While the advice given in this screen is true, without testing, there's no way to know
which Debian archive mirror is best. Without testing, picking your country or the closest
location to your country would be the logical choice.

----

**Configure the Package Manager:  Debian Archive Mirror**

(NO PIC)

The default choice is usually best.

**Configure the Package Manager:  HTTP proxy**

In most cases this entry will be blank.

(If a proxy is required, note the form of entry required in the dialog box.)

.. image:: /new_user_guide/images/19_Proxy.jpg
    :width: 786px
    :align: center
    :height: 203px
    :alt:

.. note::   If installing to a hard drive, the following screen may or may not appear.

**Install the GRUB Boot Loader on a Hard Disk:**

Select the appropriate boot disk in your server.

Generally the boot drive will be **/dev/sda** which is, in most cases, the first sata port.

.. image:: /new_user_guide/images/20_Install_Grub.jpg
    :width: 786px
    :align: center
    :height: 203px
    :alt:

**Finish the Installation:**  Accept the default.

.. image:: /new_user_guide/images/21_Finish_Install.jpg
    :width: 788px
    :align: center
    :height: 153px
    :alt:

**Installation Complete:**

**Remove the CD or USB installation source**, then hit ENTER.

(Otherwise, the installation process may re-start.)

.. image:: /new_user_guide/images/22_Finish_Install2.jpg
    :width: 788px
    :align: center
    :height: 153px
    :alt:

----

First Boot
==========

Allow the installation to boot.  Normally, the text above the login prompt will provide an **IP address** to be used for opening the console in a web browser.
If an IP address is available, skip the following and proceed to `Initial Configuration`_.


.. note:: **There are two exception cases on the first boot that users should be aware of.**

1.) **No address from the DHCP server:**

Normally, DHCP will assign an IP address to |omv| and the address will be printed
to the screen.  However, on odd occasions the following issue may be observed.

.. image:: /new_user_guide/images/23_DHCP_fail.jpg
    :width: 720px
    :align: center
    :height: 282px
    :alt:

This is due to a slow response from your DHCP server, during a fast boot process.

**An easy method of finding the IP address is:**

At the login prompt type ``root``

Enter your previously set root password.

At the # prompt type: ``ip addr``

.. image:: /new_user_guide/images/24_DHCP_fail2.jpg
    :width: 722px
    :align: center
    :height: 264px
    :alt:

To access the WEB control panel, the IP address for the wired Ethernet
interface is needed.  In this case it's **192.168.1.55**  (**/24**, the subnet mask,
can be ignored.)

2.) **An odd IP address is assigned, that is not in the user's network:**

In the following example, the actual network is 192.168.**1**.0/24

.. image:: /new_user_guide/images/25_DHCP_fail3.jpg
    :width: 560px
    :align: center
    :height: 328px
    :alt:

This is usually a one time event where the fix is simple – simply login as root and type ``reboot`` on the command line.  The address will be correct the second time around.

**With a known IP address, proceed to** `Initial Configuration`_.

.. image:: /new_user_guide/images/divider-c.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

***************************
Initial Configuration
***************************

Web console login
==================

In a web browser, type in the IP address provided by the first boot screen:

Set the language of your choice.

The user name is ``admin`` and default password is ``openmediavault``

(In the following, by clicking on the **eye icon**, the default password is shown unmasked.)

.. image:: /new_user_guide/images/26_Int_Config1.jpg
    :width: 734px
    :align: center
    :height: 480px
    :alt:

SSH Login:
----------

Under Services, SSH, check that the toggle switch for “**Permit root login**” is **ON**  (Green) .
If necessary make the change and Save.  After clicking on “**Save**” a yellow
banner “**The configuration has been changed**” will appear.  For the change to be
applied, the **Apply** button must be clicked.

.. note:: The yellow confirmation banner is a final “SANITY” check and, in most cases, is required to finalize changes.)


.. image:: /new_user_guide/images/27_Permit_Root.jpg
    :width: 698px
    :align: center
    :height: 509px
    :alt:


.. image:: /new_user_guide/images/divider-c.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:


*************************************
Quick Start Guide for Advanced Users:
*************************************

* In the left hand column, start at the top with **General Settings**, and work your way down, choosing and activating the services and features you need for your use case.
* For amd64 and i386 users, a static address for the |omv| server and setting the address of a `public DNS server <https://wiki.ipfire.org/dns/public-servers>`_ is recommended.  (SBC users, see the section, **Network Interfaces – SBC Users.**) As an example:  Googles servers 8.8.8.8 and 8.8.4.4 support DNSSEC for better security, and “Anycast” which will direct DNS queries to a nearby server with low network latency.  There are several choices for Public servers that support these features. `List of Public DNS Servers <https://wiki.ipfire.org/dns/public-servers>`_ .
* For a browsable network share, a minimum of one |sf| would need to be configured and that folder would need to be added to SMB/CIF to be visible on the network.

.. image:: /new_user_guide/images/28_Quick_Start.jpg
    :width: 816px
    :align: center
    :height: 542px
    :alt:

.. image:: /new_user_guide/images/divider-c.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

***********************
Basic Configuration
***********************

This section will guide new users through the initial setup of |omv|.  It
addresses how to add a plugin, enabling OMV-Extras, how to setup a
|sf| and make it browsable on the network with an SMB/CIF share.

System Settings
===============

Under **System**, **General Settings**, in the **Web Administration** tab:

To allow a bit more time for configuration in the GUI, **beginners should consider lengthening the automatic log out time**.
When the yellow banner appears, click **Apply**.

----

In the **Web Administrator Password** tab, enter a **strong password**, confirm it and Save.
(This is one of a few instances where the yellow “confirmation” banner does not appear.)
This setting changes the GUI login password.  The user “**admin**” will remain the same.

.. image:: /new_user_guide/images/29_Admin_PW.jpg
    :width: 673px
    :align: center
    :height: 488px
    :alt:

----

Under **System**, **Date & Time**

(No Pic)

Select your **Time Zone** and “toggle ON” **Use NTP Server**.  When |omv| toggle switches are **ON**, they're green. **OFF** is gray.

----

Under, **System**, **Network**, **General** tab.

**Hostname**:
The hostname is the name that will appear on your network and on the command line.  While the default is fine, the hostname can be changed here.

**Domain name**:
If needed, the Domain suffix can be changed here.  (Very few users will use Fully Qualified Domain Names.)

.. image:: /new_user_guide/images/30_Host_Domain.jpg
    :width: 781px
    :align: center
    :height: 446px
    :alt:

----

Network Interfaces – SBC Users
------------------------------

Part of the SBC installation process was setting the wired interface to DHCP.  SBC users should consider leaving their wired network interface set to DHCP, until Docker and Portainer are installed.

If a static IP address is needed:

Note that your SBC has been assigned an IP address by your LAN's DHCP server.  (Typically, a router.) See your router's documentation for information on setting a “Static”, or  “Reserved” DHCP lease.

Network Interfaces – i386/amd64 Users
-------------------------------------

Under, **System**, **Network**, **Interfaces** tab:
Highlight / click on the **interface** found under the **Name** column, and click the **Edit** button.
(*As of the release of **Debian 9/OMV4**, the interface name might not be the traditional **eth0**.  A variety of names may be found, such as **eno1** or others.   Use the first interface line/name found.*)

* It is recommended that users assign a static IP address to the new |omv| server that is outside the range of the network's DHCP server.
* It is also recommended that users set a public DNS address.  A list of public DNS servers is available → `here <https://wiki.ipfire.org/dns/public-servers>`_ .  Use a server that supports **DNSSEC**, for better security, and **Anycast**, for low latency end point servers that are closer to user locations.
* The Netmask will be as shown, in most cases, and the Gateway address will be the address of the user's router.

**Note** When saving a new static IP address, the user will be “**going out on a limb and cutting it off**”.  Since the address provided by the network DHCP server is different from the static IP address chosen by the user, when the new address is changed, saved and applied, the GUI web page will stop responding.  This is normal and expected.  Type the new address, entered in the dialog box, into the URL line of your Web browser to reconnect.

.. image:: /new_user_guide/images/30_IP_Address.jpg
    :width: 757px
    :align: center
    :height: 574px
    :alt:

----

Server Notifications
--------------------

Under **System**, **Notification**, **Settings**:

If enabled, E-mail entries in the **Settings** Tab are required if users want to take
advantage of automated server notifications and reports.  Other actions and scripts,
in **Scheduled Jobs** for example, can use this information to E-mail a report of task
execution or status, as users may deem necessary.

To gather the required information for entry in the **Settings** Tab, users should refer
to the settings for their E-mail clients.  Note that most ISP's are using **SSL/TLS** secured
E-mail connections.

**Fill in** * **fields with user E-mail requirements and settings.**

.. image:: /new_user_guide/images/31_Notifications.jpg
    :width: 831px
    :align: center
    :height: 645px
    :alt:

The **Notifications** tab allows the selection of various functions for monitoring and error reporting.

If using a minimalist platform, such as older hardware or SBC's,  E-mail's regarding system
resources, memory, etc., may become bothersome.  Unchecking **Enabled** boxes under **System** would
eliminate excess E-mails, while maintaining **Storage reports** on hard drive health and file system errors.

.. image:: /new_user_guide/images/32_Notifications2.jpg
    :width: 831px
    :align: center
    :height: 645px
    :alt:


.. note:: Using Storage Notifications is highly recommended.
If SMART is **enabled**, under **Storage**, **SMART**, and short drive self-tests are
enabled on spinning drives in the **Scheduled Tests** tab, the system may notify the user of
hard drive errors *before* a hard drive fails completely.

For an explanation of drive self-tests and an example of how to set up a drive self-test, see the section;
Drive Self-Tests

----

(Optional)

Under **System**, **Power Management**

* In the **Settings** Tab, toggle **monitoring on** (recommended).
* In the Power button drop down, amd64 and i386 users should select the action preferred.  Since power buttons are not available on some SBC installations, SBB users may chose to select “Nothing”.
* The Scheduled Jobs tab allows for the automation of a various power related tasks, such as an scheduled reboot.

.. image:: /new_user_guide/images/33_Power_Mangement.jpg
    :width: 566px
    :align: center
    :height: 304px
    :alt:

(Optional)

Under **System**, **Monitoring**:

The initial recommended setting is **Enabled**.
(Information gathered may be of use in diagnosing potential problems.)

.. image:: /new_user_guide/images/34_Sys_Monitoring.jpg
    :width: 566px
    :align: center
    :height: 304px
    :alt:

Under **System**, **Update Management**:

First, click on the **Check** button, to refresh available updates for your platform.
(This may take a few minutes)

Checking the box by **Package information** will update all packages at once.  (Recommended for beginners.)  Otherwise, individual packages may be selected as desired or needed.

**amd64** and **i386** users may be offered a list of “firmware updates”.  Select firmware updates that apply to your specific hardware.  However, there's no “penalty” for selecting firmware updates that do not apply.

Beginners should leave the 2nd Tab, Settings, with default settings.

.. image:: /new_user_guide/images/35_Update_Management.jpg
    :width: 566px
    :align: center
    :height: 304px
    :alt:

----

OMV-Extras
==========

.. note::  The following does not apply to SBC or i386 users.  When using the scripted install, OMV-Extras is installed with OMV by default.))

amd64 users will have a basic set of plugin's appropriate for a basic NAS / File Server.  To
enable the full range of plugin's available on |omv|, the installation of OMV-Extras is
required.  For a preview of what is available visit `omv-extras.org <http://omv-extras.org>`_ and select
the version of |omv| that's being installed.

For **amd64** users who installed |omv| on **SD-cards** or **USB thumb-drives**; installing
OMV-Extras is a prerequisite for installing the **flash-memory plugin**. The flash-memory
plugin is **required** for flash media boot drives.

----

Installing OMV-Extras
---------------------

To enable OMV-Extras, a file is downloaded that will be used in the server console.
Select the following link and download the associated file for OMV5.

`omvextrasorg for OMV5 <omv-extras.org/openmediavault-omvextrasorg_latest_all5.deb>`_

.. image:: /new_user_guide/images/36_omv-extras.jpg
    :width: 559px
    :align: center
    :height: 402px
    :alt:

Save the file.

----

Under **System**, **Plugins**:
Click on the **Upload** button.  **Browse** to the file downloaded, above.  Select
it and click **OK**.

.. image:: /new_user_guide/images/37_omv-extras2.jpg
    :width: 688px
    :align: center
    :height: 360px
    :alt:

A dialog window will popup that says, “Checking for Plugins”.
(OMV-Extras is being added to the default plugin list.)

----

In the same window (**System**, **Plugins**) scroll to the bottom.

Select **openmediavault-omvextrasorg** and click the **Install** button.

.. image:: /new_user_guide/images/38_omv-extras3.jpg
    :width: 770px
    :align: center
    :height: 539px
    :alt:

----

(Optional, but recommended)

Under **System**, **OMV-Extras**:

In the **Settings** Tab, highlight **OMV-Extras.org Testing** and click **Edit**.  **Enable** and Save.

.. image:: /new_user_guide/images/39_omv-extras4.jpg
    :width: 657px
    :align: center
    :height: 342px
    :alt:

To insure that all plugins are available, go back to System, Plugins, and
click the Check button.  This will refresh the page and fully populate it with
plugins that may be missing.

----

A Basic Data Drive
==================

General
-------

|omv| is capable of setting up basic Linux file systems in the GUI, up to, and including,
modern “Copy on Write” file systems such as ZFS which combine check summed files,
RAID functions, and Logical Volume Management into a single package.  However,
advanced file systems add complexity which can make administration of a NAS
server more challenging for a beginner.

Until some experience is gained, it is recommended that Linux/NAS beginners use single
disks with a native Linux file system.  In the processes described in the following,
EXT4 will be used with a single data drive.

Some Windows users will want to use USB attached hard drives that are formatted NTFS.
While this is possible, the drive would need to remain attached or, at a minimum, be
connected to the server when |omv| boots.  It would be better to use a Linux formatted drive
and create a Samba share (SMB/CIF) for Windows clients, as described in Setting up a
|sf| and Creating a SMB/CIF “Samba” share.

A Samba (SMB/CIF) network share understands the Windows file format and can be configured
to accommodate DOS and extended file attributes.  Samba serves as a transparent “translator”
for Windows data storage.

RAID+USB = Potential Problems
-----------------------------

Setting up RAID of any type using “USB to drive” connections is discouraged.  RAID over
USB has known problems. The USB interface (there are several flavors) may filter some
the characteristics of hard drives, fail to pass SMART stat's and ATA drive commands, delay
the assembly of a RAID array, etc. While USB may work in some RAID cases, it's not as
reliable as using a standard hard drive interface. If RAID of any type is considered to be
a requirement, drives should be connected with SATA or SAS ports.

If users choose to use RAID over USB connections, it is done at their own risk with the
potential for the total loss of stored data.  RAID issues involving SBC's, USB connected
hard drives, or USB RAID enclosures are not supported on the forum.

RAID is often confused with backup which is far more important.  For more information, see
the explanation of backup, in Backups and Backup-strategy.

Data Storage - Size matters
---------------------------

In general terms, beginners should do a rough calculation of their storage requirement. When
selecting a data drive, the initial fill rate should be between 25 and 50%.  As an example,
if the calculated data to be stored on the NAS is 1TB, the selected drive should be between
2 and 4TB.  With 50%+ drive free space (2 to 3TB) additional data can be accommodated,
without the need to expand in the immediate future.  When the fill percentage reaches 75%,
it's time to plan for more storage.

Data Drive Set Up
-----------------

 .. note:: Note for Beginners and SBC users: |omv| is designed to segregate the Operating System |omv|(the boot drive) from data storage.  This is “best practice” when setting up a server.  Accordingly, |omv| reserves the drive it is installed on exclusively for the OS.  By default, the GUI will not allow the boot drive to be selected when creating a data share.  A second hard drive or SSD is required for data storage.



With a data drive installed or connected.

Under **Storage**, **Disks**:

**Highlight the data disk** and click on **Wipe**.  When prompted, click **Quick** and **Yes**.
(*Reformatting a disk with GPT formatting present may result in an error.  Simply re-run the wipe operation a 2nd time.*)

.. image:: /new_user_guide/images/40_disks1.jpg
    :width: 844px
    :align: center
    :height: 555px
    :alt:

((The first device in the above list **/dev/sda** is the boot drive.))

----

Under **Storage**, **File Systems**:

Click on **Create**.  In the Popup Window use the **drop down** to **select the drive**
previously wiped.  Provide a **Label** of your choice, accept the default File System **EXT4**
and click on **OK**.  Confirm the “format device” warning.

Allow a few minutes for the format to complete.  When the message
“**File system creation has completed successfully**” is displayed, click on **Close**.

.. image:: /new_user_guide/images/41_disks2.jpg
    :width: 844px
    :align: center
    :height: 555px
    :alt:

**In the same Window**:

Click on the newly created **file system line**, and click on the **Mount** button.  When the yellow confirmation banner appears, click on **Apply**.

The Data Drive is now prepared for a |sf|.

.. image:: /new_user_guide/images/divider-c.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

************************
Creating A Network Share
************************

Network shares are the primary reason for setting up and running a NAS.   While
easy access to data provides convenience to users, storing and backing up data in a
centralized location makes it much more manageable.

Setting up a |sf|
==========================

The majority of the files and folders in a new |omv| installation are controlled by
the root user.  One of the purposes of a **Shared Folder** is to set permissions that
will allow regular users access to folders and files used for data storage.  A shared
folder could also be called a “base share”.  The |sf| created in the
following will be the foundation for creating a “**Network Share**”, covered later.

----

Under **Access Rights Management**, click on **Shared Folders**, then click on the **Add** button.

In the following example, next to:

|   **Name:**  Add your new |sf|'s **name**.
|   **Device:**  Click on the drop down and select the drive that was previously added and formatted.
|   **Path:** Accept the default
|   **Permissions:**  Click on the drop down and select **Everyone: read/write**

.. image:: /new_user_guide/images/42_shared_folder.jpg
    :width: 782px
    :align: center
    :height:492px
    :alt:

Click the **Save** button.

**The End Result:**

.. image:: /new_user_guide/images/43_shared_folder2.jpg
    :width: 704px
    :align: center
    :height: 299px
    :alt:

----

Creating a SMB/CIF “Samba” Network Share
========================================

In order to make your |sf| viewable in **Windows Explorer**,
under **Network**, it's necessary to make it a Samba share using the SMB
(Server Messaging Block) protocol.  |omv| makes setting up a Samba network
share an easy task.

----

Under **Services**, click on **SMB/CIF**.   In the **Settings** tab toggle **Enable** to **On**
(green) and set your workgroup name.  (In Windows, the default workgroup name is,
WORKGROUP.)  Leave the remainder of settings in this tab at their defaults, and
click on Save.  (Confirm with “**Apply**” when the yellow banner pops up.)

.. image:: /new_user_guide/images/44_Samba.jpg
    :width: 668px
    :align: center
    :height: 430px
    :alt:

----

Click on the Shares Tab and the +Add button.

In the popup dialog box, set the following:

|    **Shared folder:** Click on the drop down and select **Music** (or the name for the |sf| previously created.)
|    **Public:**   Click on the drop down and select the **Guests Allowed**

Scroll down with the right scroll bar and toggle **ON** (green), **Extended attributes** and **Store DOS attributes**.

(Leave the remaining settings at defaults.)

Click **Save** and confirm with “**Apply**” when the yellow banner appears.  The final result should appear as follows.

.. image:: /new_user_guide/images/45_Samba2.jpg
    :width: 719px
    :align: center
    :height: 389px
    :alt:

----

Explore the New Network Share
=============================

You should now have a browsable Server with a Network share named Music, so let's take a look.
Open Windows explorer, scroll down to Network and click on it.  There's the new server OPENMEDIAVAULT.

.. image:: /new_user_guide/images/46_Samba3.jpg
    :width: 719px
    :align: center
    :height: 389px
    :alt:

*A few minutes may be required for the Windows Network to “Discover” the new server.  If users are using **Windows 10 PC's**, and the server and share do not appear, see this networking How To.*

----

Now let's look at the server's new Samba share.  It's there and browsable.

.. image:: /new_user_guide/images/47_Samba4.jpg
    :width: 540px
    :align: center
    :height: 415px
    :alt:

----

This share is “writable” with a standard “Copy and Paste”, from a client PC.

.. image:: /new_user_guide/images/48_Samba5.jpg
    :width: 540px
    :align: center
    :height: 415px
    :alt:

Congratulations!  You now have a functional NAS that can be expanded to accommodate additional network shares.  Simply repeat the processes in Creating A Network Share to create and make additional shares visible on your network.

.. image:: /new_user_guide/images/divider-c.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

******************************************
The Flash Memory Plugin - amd64 users only
******************************************

amd64 users who installed |omv| **on flash media** will need to install the flash memory plugin.

Flash Media and Wear Leveling
=============================

While modern flash media drive is solid state, it's life is limited by the number of write cycles
it can withstand before it goes “read only”.  When a specified number of flash memory blocks refuse
to erase, the device's controller will set it “read only”.  At that point, the device's useful life
is over.

To extend the life of flash media, most modern flash devices have **wear leveling** built into their
controllers.  If blocks are written, but not erased, they experience no wear.  If blocks are erased,
the next new write is set on adjacent blocks that have never been written before.  As data is erased
and written, blocks are used starting at the beginning of the device's addressable storage range and
proceeding, in sequence, working toward the end.  When the end of the range is reached, the process
starts at the beginning and cycles through again.  This wear leveling process avoids writing a
single location to failure, and spreads wear evenly throughout.

With wear leveling and two drives of the same type, a drive that is twice the size will last roughly
two times longer than the smaller drive.  While this is a strong vote for using a larger flash drive,
when backups are considered, drives of twice the size also take twice as long to image and their
image files are twice as large.  (When using flash media as a boot drive, a practical trade-off
should be considered in the suggested 16 to 32GB range.)

The Purpose of the Plugin
=========================

The primary purpose of the Flash Memory Plugin is to reduce the frequency of writes to flash media
by consolidating very small writes into one, larger, bulk write.  This reduces the number of blocks
physically written to the Flash Device being used as the boot drive.  The plugin can reduce the number
of blocks written to the Flash drive by an order of magnitude or, potentially, 1/10th the amount that
would otherwise be written.  By extension, a drive of a given size might last up to 10 times longer
than it would without the Flash Media plugin.

Installing the Plugin
=====================

The prerequisite for installing this plugin is the installation of OMVExtras.  If OMVExtras is not
installed, it is required to proceed.

----

Under **System**, **Plugins**, scroll down to Section: **Filesystems**.

Select **openmediavualt-flashmemory** and click the **Install** button.

.. image:: /new_user_guide/images/49_OMVExtras.jpg
    :width: 717px
    :align: center
    :height: 412px
    :alt:

----

Under **Storage**, **Flash Memory**, the following screen is now available.

.. image:: /new_user_guide/images/50_Flash_Mem.jpg
    :width: 685px
    :align: center
    :height: 487px
    :alt:

The plugin will work as is, but it will be more effective if the guidance under **Notes (optional)** is followed.
While this guidance shows steps for nano, following are options with guidance that beginners may find easier to implement.

----

Flash Memory Plugin – Editing /etc/fstab
----------------------------------------

There are two options for editing /etc/fstab

* (Option 1) A Linux command line text editor
* (Option 2) WinSCP and Windows Notepad can be used if WinSCP is installed

----

Option 1: Editing /etc/fstab with nano
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The first example will use **nano**.  This option requires the installation of PuTTY which is detailed here.

Using PuTTY, SSH into the server.  Log in as root and enter the root password.

On the command line, type the following and hit enter.
``nano /etc/fstab``

.. note:: In nano, the mouse does not move the cursor.  The cursor is moved with the keyboard's arrow keys to the insertion point.  Type to insert text and use the backspace key to erase text if need.   If a mistake is made, exit without saving and go back in again.

From the plugin's **Notes, Step 3**:

* First:  We're going to add two statements **,noatime,nodiratime** to the **/** partition (the root partition) exactly as shown.  The text addition is highlighted in green.
* Second:  Note the partition with **swap** in it.  Per Step 4, we're going to comment this line out, using a  **#**  at the beginning of the line.  The **#** is an addition, and is highlighted in green.


.. image:: /new_user_guide/images/51_Edit_fstab.jpg
    :width: 946px
    :align: center
    :height: 481px
    :alt:

Use **Ctrl+o** to save, then **Ctrl+x** to exit

Reboot the server.
On the command line, the following command can be used: ``reboot``

----

Option 2: Editing /etc/fstab with WinSCP and Notepad
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This option requires the installation of WinSCP which is detailed here .

Users who are not comfortable with editing fstab using nano can use WinSCP
and Windows Notepad to make the needed changes.  If WinSCP is not installed,
this doc-link to → (WinSCP) will describe the process for installing WinSCP and
logging into the |omv| server for the first time.

When logged in, click on **/etc** in the left pane.  In the right pane, “**right**”
mouse click on **fstab**, select **Edit** and **Notepad**.

.. image:: /new_user_guide/images/52_Edit_fstab2.jpg
    :width: 750px
    :align: center
    :height: 542px
    :alt:

Notepad will open the fstab file.

----

First: Find the root partition -  it's the line with  /  and insert **noatime,nodiratime,** after **ext4** and **one space** as shown.

Second: Find the swap partition – it's the line with **swap** and insert a **#** at the beginning of the line as shown.

.. image:: /new_user_guide/images/53_Edit_fstab3.jpg
    :width: 750px
    :align: center
    :height: 542px
    :alt:

| Do **File**, **Save**.  Close Notepad.
| Exit WinSCP.
| Reboot the server, from the GUI.  

**Done**

.. note::  In the latest version of the Flash Memory plugin, there are extended instructions that go beyond editing etc/fstab.  Those instructions apply to mdadm RAID and are NOT for beginners.

.. image:: /new_user_guide/images/divider-c.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:


*****************************
Hard Drive Health and SMART
*****************************

Hard drives are the hardware component most likely to fail, in a server, over time.  With continuous use, spinning hard 
drives last roughly 4 to 7 years, but there are notable exceptions where hard drive life may be significantly shorter or 
longer.

Given that storage failure is inevitable, the best overall strategy to avoid losing data is 100% backup of the entire 
data store.  Further, it is equally important to monitor the condition of a server's storage media to prevent silent 
data corruption and, unknowingly, replicating corrupted data to a backup device.

Another characteristic of hard drives is that they rarely fail all at once.  While it is possible for a drive to fail 
abruptly, and without notice, it is a fairly rare occurrence.  Typically hard drives begin to fail slowly, 
gradually accelerating toward a point in time where they become unreadable.  This unfortunate circumstance, where data lost to 
a corrupted or completely unreadable hard drive, might be avoidable with automated testing and monitoring.

To protect the server's data, enabling SMART is strongly recommended.

----

Enable SMART
============

In **Storage**, **S.M.A.R.T.**, in the **Settings** tab, **enable** SMART.


.. image:: /new_user_guide/images/78_SMART.jpg
    :width: 826px
    :align: center
    :height: 470px
    :alt:

----

Drive Self-Tests
================

Drive self-tests are a tool for early discovery of hard drive issues.  Periodic testing of hard drives will uncover the 
majority of hard drive issues as they begin to develop and, hopefully, before a drive fails completely.   The following 
illustration shows the setup for automated short tests, for an individual hard drive.  (Each hard drive will require its 
own scheduled tests.)  In this example, a short self-test is run every Saturday at 1:00AM)

.. image:: /new_user_guide/images/79_SMART2.jpg
    :width: 1084px
    :align: center
    :height: 827px
    :alt:

A **Short** self-test runs for a few minutes and is an “on-line” procedure, meaning that drives are still accessible during 
the test.  A **Long** self-test is an “off-line” test, meaning drives are not accessible during the test.  While a Short test 
does a quick check of a drive's components, a Long test does everything in a Short test then checks the media (platters) 
for bad sectors and other imperfections.  Repairs are made, if possible, such as reallocating bad sectors.  

The down side of a Long test is that it is L-O-N-G, where drive size and spindle speed are factors in the length of the 
test.  Long tests are off-line and, since entire platter surfaces are scanned, it may push a drive that's beginning to 
failure closer to an actual failure as the test detects and attempts to repair problems.

There are many opinions on which tests to use and the frequency of testing.

* Some data center admins schedule short self-tests once a week and a long test once every 30 to 60 days.  (Remember, when scheduling a Long self-test, schedule it for after-hours periods where the server is not in use.)
* Some home NAS admin's schedule a short test, once a week, skipping Long tests altogether.

There's no exact right or wrong but the self-test tool should be used as an aid to monitor drive health, in avoiding 
data corruption and loss.    

----

SMART Attributes
================

There are numerous SMART attributes to consider.  Unfortunately, only a handful are standardized among the various drive 
OEM's and many have little to no practical meaning to the end user.  Given the variation between drive OEM's, the 
interpretation of a specific SMART stat may require going to the drive OEM's support site.  

A good explanation of individual SMART attributes, and a brief explanation for each, can be found → 
here `here <https://en.wikipedia.org/wiki/S.M.A.R.T.>`_ .

Where spinning drives are concerned, thanks to the ongoing 
`BackBlaze drive study <https://www.backblaze.com/b2/hard-drive-test-data.html>`_ , a correlation has been made between 
impending drive failure and specific SMART stat's.

**SMART stats loosely related to drive failure:**

**SMART 5 – Reallocated_Sector_Count**

**SMART 187 – Reported_Uncorrectable_Errors**

**SMART 188 – Command_Timeout**

**SMART 197 – Current_Pending_Sector_Count**

**SMART 198 – Offline_Uncorrectable**

Any one count of the above stats may be meaningless, but it should be noted and closely monitored.  If any of the above 
begin to increment upward, as of the 2nd or 3rd count, home or small business admins might want to consider ordering a 
replacement drive.

**SMART 199 - UltraDMA CRC errors**

While not directly linked to drive failure, it's worth noting that counts on SMART stat 199 are usually hardware or 
cable related.   This may be due to loose or a bad SATA / SAS cable, a connectivity problem, or an interface issue of some 
kind with the motherboard or the drive interface board.


Drive Failure - The Bottom Line
===============================

When using scheduled drive self-tests in conjunction with SMART E-mail notifications (see Server Notifications), server 
admin's and home users will be afforded better protection against the data corruption and data loss due to a failing hard 
drive.

.. image:: /new_user_guide/images/divider-c.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

*************************
Final Installation Notes:
*************************


1. Permissions to the shared folder created in this guide, and the SMB network share layered on top of it, are completely open.  While these permission settings are OK for home environments, the server should not be exposed to the Internet by forwarding port 80 or 443.  As users gain knowledge and experience, they should consider tightening up permissions on the underlying Shared Folders and SMB/CIFS network shares.

2. **Important:**  Put your new server on a good surge suppression power strip, at the absolute minimum. An UPS system is preferred and is best practice.  In consumer electronics, the majority of failures are related to power supplies and adverse conditions created by line power.  The prime causes of power issues and failures are short duration surges, high voltage spikes, brown-outs, and sustained over-volt or under-volt conditions.  A good UPS system is designed to counteract these problems.  Further, the file system on the boot drive is at risk of corruption from sudden (dirty) shutdowns due to power loss.  An UPS minimizes these risks. 


.. image:: /new_user_guide/images/divider-c.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

***************************************
Utilities to Help With |omv| Management
***************************************

Being able to work from the command line would be very useful to users, 
who may need to gather detailed information on the OS and platform 
hardware, for troubleshooting and for an occasional edit to a 
configuration file.  Much can be learned with the following utilities 
that allow users to look at |omv| “under the hood”.

----

WinSCP
======

WinSCP allows users, beginners and experienced alike, to visualize the Linux file structure in a manner similar to Windows Explorer.  WinSCP installs on a Window Client and connects to Linux servers, allowing users to work with their server remotely. 

One of the more useful features of WinSCP is that it gives users the ability to edit Linux configuration files with a familiar editor like Notepad.  For experienced Linux Desktop users who would like to use WinSCP, it will run from WINE (in Linux Mint, Ubuntu and others)

WinSCP can be downloaded here. → `WinSCP <https://winscp.net/eng/download.php>`_ 

----

Installing WinSCP
-----------------

During the installation process, if prompted, select the **Explorer Interface**.  
This display shows the remote file system only.  If the Explorer Interface is 
not offered it can be selected, after the installation, under View, 
**Preferences**, **Environment**, **Interface**.

----

On the first run, the login screen is presented.  Click on **New Site** and type in the **IP address** of the new server.

Click on **Save**.

.. image:: /new_user_guide/images/54_WinSCP.jpg
    :width: 515px
    :align: center
    :height: 349px
    :alt:

----

In Site name: The server's IP address is displayed.  Optionally, the site name can be changed.  If using WinSCP for a single server, a desktop short cut may be useful.  Click on **OK**.


.. image:: /new_user_guide/images/55_WinSCP2.jpg
    :width: 416px
    :align: center
    :height: 269px
    :alt:

----

The **login screen** will come back.  Double click on the new site name.  The following is normal for the first SSH connection to any client or server. Click **Yes**. 

.. image:: /new_user_guide/images/56_WinSCP3.jpg
    :width: 496px
    :align: center
    :height: 286px
    :alt:

The first prompt is for the username.  Enter ``root``

The second prompt is for the root password.  Enter the root ``password``.

.. note::  R-PI users would enter the user ``pi`` and the pi ``password`` or a previously added user with admin privileges.  Due to the restrictions of a non-root “sudo” environment, WinSCP will be restricted from root functions.  This restriction can be mitigated, but it's beyond the scope of this guide.  

The following link may of assistance:  Connect as root (sudo) using WINSCP **

----

WinSCP opens with a two pane window. Selections are made in the left 
pane; operations are done on the right.  The folder srv was selected on the 
left.  **dev-disk-by-label-DATA** was highlighted on the right.  A right 
click of the mouse brings up an operations menu.  **Properties** was 
selected.  In this particular popup,  permissions could be changed.  
(Without backup, this is NOT a recommended action for beginners.  Backup 
is covered later.) 

.. image:: /new_user_guide/images/57_WinSCP4.jpg
    :width: 686px
    :align: center
    :height: 678px
    :alt:

In a similar manner, a configuration file can be highlighted in the 
right pane.  A right click of the mouse brings up the menu, select **EDIT** 
and Windows notepad, or the internal editor can be used for editing 
configuration files.  Either choice is much easier than using **nano** or 
**vi** on the Linux command line.

While they can be done in WinSCP, very large file copies, moves, or deletes 
are best done using Midnight Commander.

----

PuTTY
=====

PuTTY is similar to a Window's command prompt, but it allows users to 
work on |omv|'s command line from a remote PC.   If PuTTY was not 
installed as part of your installation process, install it on a Windows 
PC.  It's available here. → `PuTTY <https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html>`_

Using PuTTY is as simple as typing in the server's IP address in the 
**Host Name** field and clicking on open.  There will be a warning for a 
first time connection – click **OK**.  Then, login on the command line.

.. image:: /new_user_guide/images/58_PuTTY.jpg
    :width: 591px
    :align: center
    :height: 521px
    :alt:

----

MC (Midnight Commander)
=======================

Midnight Commander is a command line file utility that utilizes a very 
cleverly created graphical environment.  It's very useful for 
navigating through |omv|'s directory structure.  It excels in efficient 
copying, moving, and deleting folders and files.

The installation process:

* Use PuTTY to get to |omv|'s command line.
* Log in as ``root``.
* On the command line type the following;  ``apt-get install mc``
* When prompted continue with “``Y``”
(R-PI users will log in as ``pi`` and use ``sudo apt-get install mc``)

When the installation finishes, on the command line, type ``mc``

Midnight Command is a two pane window where the source is the left pane 
and the destination is the right pane.  Copies and moves are done, left 
to right.  Since it's possible to navigate to any location on the |omv| 
host, in either pane, the source and destination can be set for any 
location.

A mouse works in MC.  Click on the various menu items at the top and 
bottom, to select them. Similarly, files or folders can be selected by 
clicking on them.  To level up, click on the ``/..`` at the top left of 
either window.  

.. image:: /new_user_guide/images/59_mc.jpg
    :width: 841px
    :align: center
    :height: 525px
    :alt:

.. warning::  Beginners - Midnight Commander is powerful and potentially dangerous.  MC does not have “Undo”.  A careless operation on the boot drive, such as accidental file “Move” or “Delete”, can ruin your installation.

Work with MC carefully and before doing anything extensive with it, the appropriate backups are recommended.  Operating System Backup – Data Backup.

----

Win32DiskImager
===============

Win32DiskImager is a utility that's designed to write raw image files to SD-cards and 
USB drives.  What makes it stand out from similar utilities is that it can “read” a flash 
drive and create an image file from the contents of the device.  If users decide to use an 
SD-card or a USB thumb-drive as a boot drive; the ability to read flash media devices makes 
`Win32DiskImager <https://sourceforge.net/projects/win32diskimager/>`_  useful for cloning 
flash boot drives. 

Details for using Win32DiskImager are found in Operating System Backup, under  Cloning Flash Media.

----

Virtual Box
===========

Virtual Box is a cross platform virtualization platform that will work with both servers and 
clients.  For learning about |omv|, there simply is no better tool than working with an |omv| Virtual 
Machine (VM).  An |omv| VM can be built, configured, and put on the local network complete with shares, 
in the same manner as real hardware.  VM's can be created, cloned, used for test beds, and destroyed 
without consequence.  Many advanced |omv| users fully test upgrades, Docker's, plugin's, server add-ons 
and changes in configuration, in |omv| VM's before upgrading or reconfiguring their real-world servers.

If users have a Windows client with at least 6GB RAM and plenty of hard disk space, installing Virtual 
Box is highly recommended. → `Virtual Box <https://www.virtualbox.org/>`_ 

.. image:: /new_user_guide/images/divider-c.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

***************************
Backups and Backup-strategy
***************************

It's important to understand the concept of backup and why backup is important.  In understanding the 
concept of backup, an automotive analogy may be helpful.  

If one has a car and that car has a spare tire, is the “car” backed up?  The answer is “No”.  There 
are a great number of things that can happen to a car that can disable it, until parts are replaced 
or the car is otherwise repaired.  These items would include the battery, alternator, any component 
of the ignition system, the transmission, the cooling system, etc., etc.  To backup the car, **a second 
car is needed**.  This is why using RAID of any type is not backup.  At best RAID could be thought of 
as a “spare tire” for a PC.

Where the automotive analogy fails, generally speaking, is that when a car fails it can be repaired.  
In computing, if a user's personal data is lost without backup, it's permanently lost.  There are 
many possible events where data may be corrupted beyond recovery (viruses, ransomware) or is 
completely lost due to drive failures, a failing drive controller, or other hardware failures.   This 
is why real data back up is far more important than the computing equivalent of a spare tire (RAID).

----

Backing Up Data
===============



.. image:: /new_user_guide/images/60_1rst_level_backup.jpg
    :width: 523px
    :align: center
    :height: 450px
    :alt:

The scenario depicted in this graphic represents true backup.  There are two full copies of data.  
With two separate copies, this backup strategy is superior to traditional RAID1 for home or small 
business use cases for a couple reasons.

* Rsync can be used with most USB connected hard drives where RAID1, when used with USB connected drives, is notably unreliable.

* If there's a drive error, an accidental deletion, a virus, or other data related issue; in RAID1 the effects are instantly replicated to the second drive.  With Rsync, both drives are independent and, in most cases, the second disk will be available after the source disk fails.  In any case, the Rsync replication interval allows time for admin intervention before the second disk is affected.  

.. image:: /new_user_guide/images/divider-c.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

***************************************
Full Disk Mirroring / Backup with Rsync
***************************************

While individual shared folders can be replicated using Services, Rsync, a more efficient approach is using an Rsync Command line, in a scheduled job, under System, Scheduled Jobs to mirror a drive.  This method allows for replicating the file and folder contents of an entire data drive, to an external drive or a second internal drive of adequate size.  

* To implement something similar to the following example; it's necessary to add and mount a destination drive, in accordance with the section labeled A Basic Data Drive. 
* When formatted, the hard drives used in this example were labeled to indicate their function. 
**This is a good practice that will help new users to easily identify drives and avoid admin mistakes.**
* Dissimilar sized drives can be used, provide that the destination drive is large enough to hold the source drive's data.

----

The following Rsync command line is an example of how a data drive can be mirrored onto a second drive.

``rsync -av --delete /srv/dev-disk-by-label-DATA/ /srv/dev-disk-by-label-RSYNC/``

The source drive is on the left (ending with **DATA**) and the destination is on the right (ending with **RSYNC**).  In 
this example, the entire contents of dev-disk-by-label-**DATA** would be copied to dev-disk-by-label-**RSYNC**

The switches are:

**-a  Archive Mode**.  Archive mode adds an array of options to an Rsync command. It's the equivalent of switches -r -l -p -t -g -o and -D which copies files and folders recursively, copies links and devices, preserves permissions, groups, owners and file time stamps.

**-v  Increase Verbosity**.  This can be useful when examining Rsync command output or log files.

**--delete    Deletes files in the destination drive that are not in the source**.  If accidental 
deletion protection is desired, this switch could be left out of the command line.  However, from 
time to time, it would necessary to be temporarily re-added the **--delete switch** to purge 
previously deleted and unwanted files from the destination drive.

----

To find the appropriate Rsync command line entries for the user's server, under **Storage**, **File Systems** 
click on **down arrow** at the top right edge of a column.  On the pop down menu, select **Columns** and check 
the **Mount Point** box.

Under the **Mount Point** column (red boxes) are the full paths needed for the source drive 
(in this example **/srv/dev-disk-by-label-DATA**) and the destination drive 
(in this example **/srv/dev-disk-by-label-RSYNC**).

.. image:: /new_user_guide/images/61_rsync.jpg
    :width: 1094px
    :align: center
    :height: 525px
    :alt:

To construct the appropriate command line, add a slash “/” after each drive path, in the full 
command line as follows:

``rsync -av --delete /srv/dev-disk-by-label-DATA``**/** ``/srv/dev-disk-by-label-RSYNC``**/**

.. warning:: **Beginners Warning, Note and Sanity Check**
*  Getting the source (left) and destination (right) in the correct order, in the command line, is **CRUCIAL**.  If they're accidentally *reversed*, the **empty** source drive will delete all data on the **destination** drive.  
*  The safest option would be to leave the switch **--delete** out of the command line until it confirmed that two full copies exist.

----

As previously mentioned, this Rsync operation can be manually run or automated under:
**System**, **Scheduled Jobs**, as shown in the illustration.  Copy and paste the Rsync command 
line into the command box and select scheduling parameters as desired.

.. image:: /new_user_guide/images/62_rsync2.jpg
    :width: 833px
    :align: center
    :height: 589px
    :alt:

User Options for Backup:

* **Automated:**

As configured above, and **ENABLED** (green), this Scheduled Job will run the Rsync command 
line once a week, on Monday, at 05:00AM.  After the first run of the command, which may 
take an extended period to complete, a week or more would be a good backup interval.  Generally 
speaking, the backup interval should be long enough to allow for the discovery of a data 
disaster (drive failure, a virus, accidentally deleted files, etc.), with some time to 
intervene before the next automated backup replicates the problem to the 2nd drive.  This is 
also a drawback of using automation; if data loss or corruption is not noticed by the user, 
those problems will be replicated to the back up drive during the next Rsync event.  Longer 
automated backup intervals, such as two weeks or even a month, allow more time to discover issues 
and disable replication.

* **Manual Run:**

If the job is **disabled** (the **ENABLED** toggle switch is gray), the job won't run automatically. 
However, the job can be run manually, at any time, by clicking on the job and the Run button.  
This may be the best option for users who do not check their server regularly.

* **Delete Protection:**

Removing the **--delete** switch from the command adds delete protection, and may allow the retrieval 
of files accidentally deleted from the source drive.  As previously noted, to clean up the 
destination drive of intentionally deleted and unwanted files, the --delete switch could be manually 
entered into the command line, from time to time, as may be deemed necessary. 

**Keep in mind**:  In the event of a failing or failed data drive it is **crucial** that the 
drive-to-drive Rsync job is turned **OFF**, if automated.  Similarly, after noting a problem, DO NOT run the job manually.** \

The Bottom Line:

The additional cost for full data backup using Rsync is the cost of an external drive, or an 
additional internal drive, of adequate size. For the insurance provided, the additional cost is very 
reasonable. 

----

Recovery from a Data Drive failure - Using an Rsync'ed backup
=============================================================

General:
--------

*Again, as a reminder, when the NAS primary drive is failing or has failed, it's crucial to 
turn **OFF** an automated drive-to-drive Rsync command line.*


Restoration Without a Replacement Drive:
----------------------------------------

Without a replacement drive on site, which would be the most likely case for most home users 
and small businesses, the backup Rsync'ed “destination” disk can become the data source for 
network shares.  This involves repointing existing shared folders, from the old drive location, 
to the backup drive.  All simple services layered on top of the shared folder, to include 
SMB/CIF shares and other shared folder services, will follow the shared folder to the new 
location on the back up drive.

Repointing a Shared Folder:
^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the following example, the data drive has failed and it's been determined that it's not 
repairable.  Under **Storage**, **File Systems** we have a **missing** source drive (labeled DATA) that's 
**referenced**.

.. image:: /new_user_guide/images/63_rsync_recover.jpg
    :width: 960px
    :align: center
    :height: 347px
    :alt:

.. note::  There may be ERROR dialog boxes regarding the failed mount of existing shared folders.  With a missing but referenced drive, this is to be expected.  When all shares are redirected, these error messages will stop.

----

The actual references to the failed DATA drive are the **Shared Folders** assigned to the drive, 
named **Documents** and **Music** as follows:

.. image:: /new_user_guide/images/64_rsync_recover2.jpg
    :width: 960px
    :align: center
    :height: 347px
    :alt:

Since the DATA drive no longer exists and there's an *exact duplicate* of all folders and files on the 
backup drive, we'll repoint the shared folder named **Documents** to the RSYNC backup.  Click on the 
**Documents** Shared Folder, above, and the **Edit** button.

----

In the **Edit Shared Folder** Dialog Box, click the **drop down button** on the **Device** Line and select the 
destination / backup drive.  (In this example the drive with **RSYNC** in the label is the backup.)  A 
confirmation dialog box will prompt **“Do you really want to relocate the shared folder?”**  
Click “**Yes**” and “**Save**”.

(Remember that *all* contents of the now missing source drive and the destination drive were *identical* 
as of the last backup, to include the path statement.  Changes are not necessary.  Repointing the 
share is just a matter of selecting **the backup drive**.)

.. image:: /new_user_guide/images/65_rsync_recover3.jpg
    :width: 638px
    :align: center
    :height: 440px
    :alt:

Click on **Save**, confirm the change, and it's done.

Do the same process for all remaining Shared Folders.  (In this example, Music was repointed as well, 
but not shown.)  Again, error dialog boxes may appear during the process.  Acknowledge them (with **OK**)  
but do not revert, or back out of change confirmations.  When all Shared Folders are redirected to the 
backup drive and saved, the error dialog boxes will end.

----

In the final result:

With one operation per shared folder, all shared folders have been redirected to the backup drive 
labeled RSYNC.

.. image:: /new_user_guide/images/66_rsync_recover4.jpg
    :width: 638px
    :align: center
    :height: 440px
    :alt:

----

In this case there were SMB network shares layered on top of the Shared Folders above.  The SMB 
network shares followed their associated Shared Folders, without additional configuration, so SMB 
shares are up and running on the Network.

.. image:: /new_user_guide/images/67_rsync_recover5.jpg
    :width: 638px
    :align: center
    :height: 440px
    :alt:

In addition, most simple services that are applied to these shared folders, would follow 
the shared folder when it is repointed to the backup drive.

----

One last operation is needed to completely remove the failed DATA drive.  Go to **Storage**, 
**File Systems** and note that missing drive DATA is no longer referenced.  When clicking on the 
failed drive, the **Delete** button is now active.   **Delete** the drive.

.. image:: /new_user_guide/images/68_rsync_recover6.jpg
    :width: 638px
    :align: center
    :height: 440px
    :alt:

At this point, all shares in this example have been successfully redirected to the backup drive 
and the server is fully functional again.

.. image:: /new_user_guide/images/divider-c.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

**************************************************
Second Level Backup – Replication to a Second Host
**************************************************

.. image:: /new_user_guide/images/69_rsync_2L_backup.jpg
    :width: 1115px
    :align: center
    :height: 532px
    :alt:

The first item to note, is that this scenario can be accomplished using a LAN client, as the second 
host, and it could be a Windows client.  The additional cost would be the price of a second drive of 
sufficient size (internal or external) to house the second copy of data, attached to a remote host.  
The Remote Mount Plugin can mount a Windows network share (a user name and password with write access 
is required) and Rsync can be configured to replicate NAS data to the Windows share.

As illustrated above, the second host could be a low cost SBC.  This scenario can be designed with a 
number of desirable features.

* First, if backing-up to a second server platform, two fully independent copies of data are possible.
* When using an SBC with |omv| installed:

If the primary server failed completely, the second platform can be configured to take over as a backup file server.  With all data backed up and resident on the SBC, this data can be made available to the network with SMB shares.

* Other than re-homing clients to the shares on the backup device, there's no recovery time and no “crisis” involved in getting data back on-line.  It's already there.

The costs for this level of backup are very reasonable, with the cost of a hard drive of adequate size 
and an SBC.  Good performing SBC's are available for $50 USD or less.  Older PC platforms or laptops 
could be configured as a backup server as well. 

----

As an illustration of the backup server concept, the following is a File explorer example of an |omv| 
NAS server and an SBC used for backing-up the main server's files.

.. image:: /new_user_guide/images/69_rsync_2L_backup2.jpg
    :width: 638px
    :align: center
    :height: 440px
    :alt:

This particular R-PI (OMV-RPI) is replicating all of the data shares of the OMV-SERVER and is 
re-sharing the same data to the network.  Again, Rsync replication jobs of individual shares can be 
scheduled as desired, or triggered manually.

** The Practical details for setting up Primary Server to Backup Server share replication, using Remote Mount and Local Rsync Jobs will be covered in future documentation.**

----

While replication to an independent host is an excellent method of avoiding data loss catastrophes, 
there are other potential events which can threaten irreplaceable data.  Fires, roof or plumbing leaks 
and other unforeseen events can result in the loss of data, even on two independent hosts.  For these 
reasons, backup professionals and experienced server administrators recommend an off-site copy.  While 
this may seem extreme, it's actually fairly easy to accomplish.  It can be done with an SBC or an old 
laptop, connected wirelessly, and housed in a utility shed with AC power.  Some users set up a backup 
host in a family members' house, and replicate changed data over the internet.  

In the bottom line, if users want to keep their irreplaceable data, an absolute minimum of two full 
copies is recommended, with a 3rd off-site copy preferred.  As previously noted, effective backup 
strategies do not have to be expensive and are relatively easy to set up.  

For further information on Backup concepts and best practices, an excellent explanation of Backup is 
provided by  `Backblaze.com <https://www.backblaze.com/blog/the-3-2-1-backup-strategy/>`_ .

.. image:: /new_user_guide/images/divider-c.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

************************
Operating System Backup:
************************

By design, the OMV/Debian operating system installs on its own partition, segregated from data.  This 
makes copying or cloning the |omv| boot/OS drive an easy process.  So, one might ask, why is a clone or a 
copy of the operating system important?

Building |omv|, from scratch, using the installer ISO is a 15-minute proposition, give or take. While it 
takes longer, roughly 45 minutes to an hour, the actual hands-on portion of an SBC build is even less.  

As users configure their servers, add services, reconfigure shares, move their data around, tweak 
access controls, etc., servers tend to become “works in progress”. Configuring a server to the user's 
preferences can be an evolution that may take weeks or even months.  If a complete server rebuild is 
required, the customization, add-ons, and the collection of various user tweaks may take several hours 
to recreate.  It is this time and effort that Operating System Backup will preserve.

There are several ways to duplicate an operating system boot drive, but many can be technically 
involved; requiring network access to remote servers, bootable utilities and somewhat complex processes.

Given the low cost of flash media and with sockets mounted on the outside of a PC case, SD-cards and 
USB thumb-drives lend themselves to cloning and very quick recovery.

----

The Benefits of Maintaining Operating System Backup
===================================================

In accordance with `“Murphy's Law” <http://murphys-laws.com/murphy/murphy-laws.html>`_, users may 
encounter issues where things go wrong.  As examples, users may test software on their active server 
or try new settings. On occasion, installing an add-on may have unintended consequences.  Trying new 
settings or working on the command line, may break |omv| in a way that might not be recoverable.  In 
other cases, there may be instances where a software update goes south – the source repository may 
go off-line in the middle of an update resulting in broken packages.

In all of these cases, having a confirmed working clone of the boot drive will allow users to “drop 
back” to a known good state.  The “FIX” would be as simple as shutting down and booting the server on 
a known working clone.

The advantages of maintaining operating system backup are obvious.  Beginners, with very little 
knowledge of Linux, can work with their servers without fear, which facilitates learning.  If a Linux 
update causes ill effects, it's possible to drop back and selectively install packages to isolate the 
exact cause of the problem.  If an add-on update doesn't work (direct installed software, a plugin, 
Docker, etc.), the user can gracefully back out of the update and leave the older (but working) 
software package in place.

It's the easiest, quickest, and most effective fix, for resolving problems with |omv| and the underlying 
Debian Operating System.

**The practical issues of maintaining boot drive clones – when to update and rotate?**

1. It makes sense to apply Linux Operating System updates and wait a week or so, to insure that all is 
working and that there are no ill effects.  If all is well, update the backup and rotate.

2. The above would also apply to add-on packages, Docker, or plugin upgrades. (Plex, Urbackup, Pi-Hole, 
etc.)

3. If a network share is added, deleted, or any aspect of the NAS is reconfigured that changes the 
operation of the NAS; the backup would need to be updated.  (Otherwise, the configuration of the 
previously cloned boot drive would not mesh with the configuration and contents of data storage drives.)

4. If a cloning mistake is made (let's respect Murphy's Law), a 3rd clone could become a “fallback of 
last resort”.  Given that Linux package upgrades and |omv| sub-version upgrades have little to no effect 
on network shares or the high level configuration of the NAS, a 3rd clone can be maintained that is 
updated only when the NAS configuration is changed.

----

A Last Important Note About Backing Up your OS
----------------------------------------------

Just as it is in the commercial world, where support for a product may be discontinued, the open source 
community is constantly moving forward as well.

Users may believe that an ISO file, or image, contains all the software needed for a build.  In some 
current build cases, that assumption would be incorrect.  Linux distro's, during the initial build and 
to finalize the installation, may depend on on-line software repositories.  After the installation is 
complete, patches and updates may be applied which rely on on-line repositories as well.

Can it be assumed that those same software repositories and resources will be available on some future 
date, exactly as they were at the time of a current build?  The answer is “No”.  Distributions of a 
specific Linux version, complete with specific applications, fully patched and updated, can be built 
for a **limited time**.

Therefore, if users have extensively configured builds, are using specialty hardware (such as SBC's) or 
are using |omv| to serve a critical function; it would be wise to backup the boot drive to an image file, 
or Clone the fully configured working installation to separate media, and save one or more copies for 
future use.

----

Cloning Flash Media
===================

To avoid issues that can result from dissimilar sizes, it's best to clone images from/to identical 
SD-cards or USB thumb-drives.  Otherwise, it's easier to clone if a new drive is slightly larger than 
the working drive.

(And while it's an advanced technique, `Gparted <https://gparted.org/livecd.php>`_ can be used to slightly shrink flash drive partitions, 
to fit on the smaller of the two flash drives.)

**The Cloning Process for USB thumbdrives and SD-Cards**

* Install `Win32Diskimager <https://sourceforge.net/projects/win32diskimager/>`_ on a Windows PC.
* Format the new SD-Card or USB thumb-drive with `SDFormatter <https://www.sdcard.org/downloads/formatter_4/eula_windows/index.html>`_
* Test the new card or USB drive with h2testw1.4 `h2testw1.4 <http://www.heise.de/ct/Redaktion/bo/downloads/h2testw_1.4.zip>`_,   One test is enough.  (Do not select endless verify.)  

If the device registers errors, or if the capacity is significantly different from what is that's 
marked on the label (a fake), return it for refund or throw it away.

**At this point you should consider marking your working SD-card (with permanent marker?) to make sure you don't mix it up with the blank card. Otherwise, it is possible to read a “blank card” and use the blank image to "overwrite" the working card.**

* Insert the working card and start Win32Diskimager

**SANITY Check**, make sure you inserted your working SD-card / USB thumb-drive at this point.

**Note:**  Windows will not be able to read the format of the partitions on the working boot drive and 
offer to format it for you.  **DO NOT** format the drive.  Close the dialog box with the **X**. 

* In most instances, Win32Diskimager will detect USB thumb-drives and SD-cards, and set the Device drive letter.  However, it would be prudent to check the letter Windows assigns to the drive with Windows Explorer.

* First click on the folder ICON and navigate to the location where you'll store your image file. Type a name in the file line. (OMV-RPI2.img was used for this example, but users can add a date to the name as well, such as OMV-RPI2-04-30-2018.img)

* Check the box for “**Read Only Allocated Partition**”.  (With larger drives, this option avoids imaging unused space which saves significant time when reading a drive to a new image and, later, when writing the image to another drive.)

* Click **Read**.


.. image:: /new_user_guide/images/70_OS_backup.jpg
    :width: 494px
    :align: center
    :height: 337px
    :alt:

When the **read** is done, this is **crucial**, click the **Verify Only** button. This will compare 
the image file just created, to the boot drive.  **DO NOT SKIP Verification**.  (Win32Diskimager has a 
known bug which may affect a very small number of use cases.)

* If verification passes, pull the working boot drive and store it close by.  If verification FAILS, the image file is corrupt and cannot be used.

**If the user/admin is running a business or is in another time sensitive scenario, where the NAS server can not be out of service for an extended period; the server can be booted on the source drive while the clone is being written.  Thereafter, the drive swap could be accomplished during a low use period.**

While the resultant image file may be quite large, if the file is retained, it can be used to write 
another thumbdrive at a later date.  In such a case, the image file itself can be saved as a dated 
backup and archived.  The size of the image can be reduced significantly, by using 7zip to compress 
it before storage.

* Insert the new flash drive and start Etcher.  (Etcher typically detects flash drives as well.)

* Select the image file previously created, verify the destination flash media drive, and click the FLASH! button.

One of Etcher's features is that it writes the image and verifies it in a single operation.  If the 
operation is successful, the working boot drive has been cloned.  Insert the new clone into the server 
and boot it up.  With a successful boot up on the clone, user/admin's will have two verified copies 
of their server's boot drive. 

**Note** – Win32diskimager will write an SD-Card or USB drive, but verification is required and it's 
a second operation.  Etcher combines the write and verification in a single process.  If users walk 
away, during the write operation, which can take a long of time, Etcher is the best choice for writing 
flash media. 

.. image:: /new_user_guide/images/divider-c.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

******************************************
Add-on's – Adding Value to Your OMV server
******************************************

General
=======

The `|omv| Forum <https://forum.openmediavault.org/index.php/BoardList/>`_ has an extensive 
`Guides <https://forum.openmediavault.org/index.php/Board/29-Guides/>`_ section.  Whether a user's 
preference is videos or printed text, there's something for everyone among the numerous “How-To's”.  
Beginners and Advanced users alike should take a few minutes to familiarize themselves with the 
content in the Guides section of the Forum.


|omv|'s Plugins
==============

|omv| has numerous plugin's.  Some are integrated into the base package by |omv|'s developer Volker 
Theile.  Examples are iSCSItarget, usbbackup, among others.

Still more were created by |omv| plugin developers, such as Remote Mount, the flash-memory plug-in, 
backup plugins, and more.  

Many plugins are integrations of third party packages such as SNAPRAID, MergerFS, etc.  While 
questions or issues regarding the integration of plugin's, into |omv|, are of interest to |omv|'s 
developers, questions regarding the **operation** of plugins are best directed to the application's supporting 
web site.


Dockers - General
=================

While Dockers are an avenue toward adding *extensive* functionality to |omv|, they are an advanced topic 
that may prove to be frustrating for beginners.  To get started, beginners should consider installing 
Docker, then  Portainer, as found under System, OMV-Extras.  While it's command line oriented, this 
`Docker Tutorial <https://docker-curriculum.com/>`_ is very helpful for understanding basic concepts.  
User authored `Docker - How To's <https://forum.openmediavault.org/index.php/Board/29-Guides/>`_ can be 
found on the |omv| forum.


So, What is a “Docker”?
-----------------------

Dockers are a type of Virtual Machine (VM) that share the Linux kernel and memory spaces with the 
host.  A Docker is spawned from a Docker image.  The resultant VM equivalent, that's built from a 
Docker image, is referred to as a “container”.  A container is fully self-sufficient, bare-bones, 
Linux operating system.  The idea behind a Docker image is to create a Linux installation, that is 
as small and as lean as possible, that includes all necessary dependencies required to run the 
Docker application and nothing more.  Since these containers tend to be very small, they can 
be constructed and destroyed in rapidly.  (After downloading, usually, in a matter of seconds.)

Dockers are more resource efficient when compared to running a full VM in a hypervisor, due to 
direct allocation of hardware resources.  Typically, VM hypervisors provision fixed blocks of memory 
and may require access to dedicated hard disk space or block device partitions. Whether these 
dedicated resources are used by the VM or not, they're no longer available to the Host operating 
system or other VM's.  A Docker, on the other hand, uses the needed memory space to run its processes 
and the host's hard drive for storage, without wasted resources.  Resource management is lean and 
tight, allowing more Docker containers to run concurrently with much greater efficiency.

----

Installing Docker
-----------------

Installing OMV-Extras is a prerequisite to installing Docker.

----

Under **System**, **OMV-Extras**, select the **Docker** tab. 

**Before installing Docker**, take note of the Docker Storage location.   **/var/lib/docker** is on the 
**boot drive**.  This location is not an issue for hard drives and SSD's of medium capacity 
(notionally, 128GB or larger.)  However, when using flash media to boot (8 to 32GB), the boot drive 
is not a good location for media servers or downloader type Dockers.  There are two possible solutions:

* The easiest solution is to change the Docker Storage path to a data drive.  If the default path is 
changed, downloader output and metadata created by media servers (Plex and others) will be stored on 
a data drive by default.

* A more advanced solution would be to leave the default storage location in place (var/lib/docker) 
and configure the Downloaders and media servers to store their output and metadata on a data drive, 
but this requires individual configuration of each Docker.

.. image:: /new_user_guide/images/71_Docker.jpg
    :width: 677px
    :align: center
    :height: 483px
    :alt:

To install Docker, click the **Docker Button** and select **Install**.

An install dialog box will popup and scroll as files are downloaded and installed.  At the end, **Done** 
will be displayed.  Click the **Close** button.

The **Status** line will report: **Installed and running**.

----

Installing Portainer
^^^^^^^^^^^^^^^^^^^^

Under **System**, **OMV-Extras**, in the **Docker** tab, scroll down to the **Portainer** section.

General:

While Portainer is a Docker itself, it is the control interface through which Dockers are downloaded 
and configured in |omv|.

Click the **Install Portainer** button.

.. image:: /new_user_guide/images/72_Portainer.jpg
    :width: 900px
    :align: center
    :height: 490px
    :alt:

An install dialog box will popup and scroll as files are downloaded and installed.  At the end, 
**Done** will be displayed.  Click the **Close** button.

----

With a successful install, the **Status** line will change to reflect “**up**” time:

.. image:: /new_user_guide/images/73_Portainer2.jpg
    :width: 810px
    :align: center
    :height: 157px
    :alt:

Finally, click on the **Open Web** button.

----

At this point, Portainer is completely unconfigured.  The first configuration requirement is setting 
a password for the Admin user.  Take note of this password.  It will be needed to log into 
Portainer again.

Then click on **Create User**

.. image:: /new_user_guide/images/74_Portainer3.jpg
    :width: 632px
    :align: center
    :height: 473px
    :alt:

In the next log in, there will be a login dialog with two empty fields.  Enter the username admin 
in the top field and the password in the bottom field.

----

When this screen pops up, Click on **Local**, then **Connect**

.. image:: /new_user_guide/images/75_Portainer4.jpg
    :width: 742px
    :align: center
    :height: 465px
    :alt:

----

**Dismiss** the News and Click on **Local**

The following screen will now be the “**Home**” screen.  Using “Local” menu selections on the 
left, this is where Docker Images are downloaded, containers are created, etc.

.. image:: /new_user_guide/images/76_Portainer5.jpg
    :width: 1029px
    :align: center
    :height: 433px
    :alt:

This concludes the installation of Docker and Portainer.

----

Dockers - It's about choices
============================

While there are 100,000+ Dockers, available on the `Docker Hub <https://hub.docker.com/explore/>`_ , all are not created equal.  The 
offerings, from Docker authors, range from a one-off experiment with no documentation (users are 
on their own) to organizations like Linuxserver.io that specialize in building first-rate 
Docker images.  `Linuxserver.io <https://www.linuxserver.io/>`_ offers Dockers that have been thoroughly tested, they support 
multiple architectures, they provide detailed container setup instructions, their offerings 
are “Tagged” and they retain inventories of their older images.

----

Selecting a Docker - Primary Considerations
-------------------------------------------

**First:**

When installing a Docker, for the greatest chance of success, it is suggested that users follow the guidance provided in 
`Guides Section <https://forum.openmediavault.org/index.php/Board/29-Guides/>`_ of the |omv| forum.

**Second:**

Potential Docker users should first look for Dockers that support their **architecture**.  The three primary architectures 
supported by |omv| are **ARMHF** or **ARM64**,  **i386**(32 bit), and **amd64*(64 bit).  In most cases, 32bit Dockers will run 
on 64bit hardware.  \**\While there may be exceptions, i386 and amd64 Docker images may not run on ARM platforms. 
“**Multi-arch**” (multiple architecture) Docker images are more platform flexible.\**\

**Third:**

To increase the chance of success, when attempting to install a Docker without a guide, look for the more popular Dockers 
with the highest number of “**pulls**” on the Docker Hub.
 `(hub.docker.com) <https://hub.docker.com/search/?isAutomated=0&isOfficial=0&page=1&pullCount=0&q=+plex&starCount=0>`_  
 There are good reasons why these Dockers are broadly popular – they tend to work.

 **Forth:**

In the vast majority of cases, Dockers that fail to work won't have anything to do with |omv| or the Docker Plugin.  Their 
issues tend to be with selecting the **wrong architecture**, selecting the **wrong network mode** (host, bridged, macvlan) for 
the application, other configuration issues (such as port 80 OMV/Docker conflicts), permissions problems or the Dockers 
themselves.

Since most Dockers share Network ports with the host (|omv|), it's important to use ports that are not currently in use.  To 
get a better understanding of network ports and for commands that will reveal ports that are in use, refer to this forum 
post for more information:

`[How-To] Define exposed ports in Docker which do not interfere with other services/applications <https://forum.openmediavault.org/index.php/Thread/28506-How-To-Define-exposed-ports-in-Docker-which-do-not-interfere-with-other-services/>`_ 


.. image:: /new_user_guide/images/divider-c.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:


********************
When things go wrong
********************

First take note of any error dialog boxes.  On most Windows and Linux machines it's possible to copy and paste the text out 
of a dialog box by holding down the left mouse button and dragging the mouse pointer over text, to highlight it.  Then use 
the keys with Ctrl+c  (to copy), then click in a Notepad document and use Ctrl+v (to paste).  This basic information will 
be helpful, in searching out the details related to the problem.


The First Resource – The Internet
=================================

Users should search the internet first.  The solutions for many generic problems can be found with 
`google <https://www.google.com/>`_ ,  `yippy <https://yippy.com/>`_ ,  `duckduckgo <https://duckduckgo.com/>`_ , and 
other search engines.  When searching on key words that match error message or the problem users may be 
having, in some cases, answers can be found quickly in real time.  This is the fastest and often the best way to learn how 
to fix server problems.  Since |omv| is based on “**Debian**”, it may be a useful search term.

While the search function of the |omv| forum site will produce “hits” on search criteria, it is by no means all inclusive.  
If **OMV** is included in search criteria, a Google search may generate more result hits on information found on the |omv| 
forum, than the forum's integrated search function.

With information from searches, users should make an effort to address their own issues.  This approach tends to be the path 
to the fastest answers and greatly facilitates the learning process.

The Openmediavault Forum
========================

→ `Forum <https://forum.openmediavault.org/index.php/BoardList/>`_      

When coming to the forum for help:

First search the forum.  In many cases, user problems can be resolved with a few searches and a bit of reading.  However, 
look at the dates of posts and the version of |omv| referenced.  Posts that are 3 or more years old may not apply to the 
current |omv| version.

If posting a problem on the forum, start at the forum index, and look for the category that looks to be appropriate for 
the post.  Along with an explanation of the the issue, the |omv| version, the appropriate logs and command line output, if 
known, and the hardware platform in use are the absolute minimums required.  Realize that, without information, even the 
most experienced users, Moderators, and / or Developers will not be able to provide assistance.

* Ask the right questions.  For beginners, this can be deceptively difficult.  There's some “straight forward” guidance on this topic here →  Ask the right questions.
* While |omv|'s forum is known for responsiveness, it's unrealistic to expect answers in real time. It may be a matter of days before a forum member, who is familiar with the described problem, will read and respond to a post.
* When looking at answers, try to focus on the information presented, not the perceived tone. Remember that support is provided “gratis”, so act accordingly.
* Be open-minded.  The reason why users post on the forum should be because they couldn't solve a problem on their own.  With that in mind, when an experienced forum user replies, taking the time to make a suggestion or requesting more information, forum users should follow up and post the result. Whether the issue is fixed or not, user posts help other users with the same or a similar problem.
* If a forum post or a “How To” fixes your problem, or gets you through a configuration issue, consider giving the author a “Like” or “Thanks”.  The gesture is free and it's an indicator to other users who may have the same problem.  In essence, you'd be saying “I agree” or “this worked for me”.
* When users are experiencing problems with their data store (a file system issue, a hard drive, array, etc.) the working assumption on the part of experienced forum users and moderators will be that users have full data backup.  Accordingly, recommendations for correcting filesystems, hard drives, and RAID array issues may result in the loss of data.  Keep this in mind.


----

Common Problems
===============

Problem: After a reboot, the web page is not available.  (Bad Gateway or 404 error.)

Solution: This may happen on an odd occasion.  Instead of doing a dirty shutdown, SSH in with PuTTY, and issue the command:  reboot.  The system will reboot.  Login.


Problem: Web interface has missing fields and/or items showing that have been uninstalled.

Solution: Clear your browser cache and, always, login to the Web console using the user, admin.


Problem: I mounted the drive using the command line and I can't select that drive in the shared folder device dropdown.

Solution: Never mount a drive with anything other than the OMV web interface. This creates the necessary database entries to populate the device dropdown.


Problem: I only see a few items in the web interface like the user section of Access Rights Management.

Solution: You did not login as the admin user. This is the only user that can access everything.

Problem: Samba is slow.

Solution: Read these threads - Tuning Samba for more speed and Tuning Samba for more speed 2
(**This does not apply to SBC images – Samba has already been optimization on these platforms.**)

Problem: You see an error where a domain name/host could not be resolved

Solution: You probably need to set your DNS server in System -> Network -> Interfaces


Problem: "No Network Interfaces" when looking at the console, after boot up.

Solution: Most of the time, this is caused by the system taking too long to get a DHCP IP address before the message is written. The adapter's address can be checked by logging in with any user (root is a good choice) and typing ip addr  


Problem: I have an SBC and I'm having trouble with RAID. (OR) I have USB connected RAID array.
N/A: USB RAID is not supported. 

----

USB Power - A Common Raspberry PI problem
-----------------------------------------

General:
^^^^^^^^

Many problems with R-PI's, in versions prior to the R-PI4, are related to under-powering.  While the R-PI4 is 
much improved, depending on the power requirements of connected periferals, it is not exempt from power problems.  
The issues caused by under-powering can range from bizarre behavior to data corruption on storage devices.

Do I have a problem?
^^^^^^^^^^^^^^^^^^^^

With all peripherals attached that are normally used – use the command ``dmesg`` on the CLI and scroll through the 
output.  If an undervoltage situation exists, it will be noted in the output.

What is the problem?
^^^^^^^^^^^^^^^^^^^^

Beyond using a power supply with the appropriate current rating for the R-PI model, it should be noted that a USB power 
source must meet certain voltage specifications “at the socket”.  In essence, the output voltage of a USB power supply 
can't be increased to compensate for external voltage losses typical when using a long USB cable with small gauge wire.

Making matters worse is, models prior to the R-PI4 use a micro USB plug as the power connection.  The tiny contacts of 
a micro USB connection, combined with cables for micro USB that have small gauge wires, drop power supply voltage 
significantly.

----

**Consider the following chart of voltage losses, versus wire length and gauge**

(Note that voltage drops increase as current draw requirements rise.)

.. image:: /new_user_guide/images/80_R-PI_Power.jpg
    :width: 451px
    :align: center
    :height: 286px
    :alt:


Potential Remedies:
^^^^^^^^^^^^^^^^^^^

* Use a power supply that meets at least the minimum recommended current rating for the R-PI model being used.
* Use the shortest possible USB cable.  Cables that are 1 foot / 30cm or less, made of thick gauge wire are  preferred.  If a short USB cable is not long enough to place an R-PI in a convenient location, use an AC extension cord rather than a long USB cable.
* Avoid using direct connected USB powered hard drives.  The additional current load will drop voltage and may stress a weak power supply.  A self powered USB hub or a drive dock is preferred. 
* Avoid leaving peripherals attached, such as a monitor, keyboard or a mouse.  Even when they're not used, they consume power.

.. image:: /new_user_guide/images/divider-c.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:


**************
A Closing Note
**************

We, who support the Openmediavault project, hope you've found this guide to be useful and that you'll find your 
Openmediavault server to be efficient, easy to use, and enjoyable. 






