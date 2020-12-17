
New User Guide
##############
|

.. image:: /new_user_guide/images/underconstruction.jpg
    :width: 200px
    :align: center
    :height: 200px
    :alt: Under Construction

|
.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:
|

.. image:: /new_user_guide/images/1_Title_page.jpg
    :width: 588px
    :align: center
    :height: 439px
    :alt: 
|
.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:
|
|

******************************
Introduction to Openmediavault
******************************

Openmediavault is a File Server / NAS system designed to work on most 
modern IBM compatible PC systems, to include typical amd64 or i386 PC’s 
and select ARM devices. Openmediavault (OMV) can be thought of as 
filling a role similar to Microsoft's Server Essentials, but extends 
far beyond the role of a basic File Server with additional functionality 
added VIA plugin’s and Dockers. OMV is designed to work with popular 
client operating systems and multiple filesystem types, utilizing proven 
data sharing techniques on small and medium sized Local Area Networks.

In meeting the needs of it's intended users, individuals and 
small-to-medium-sized businesses, Openmediavault is designed for 
flexibility.

.. image:: /new_user_guide/images/2_Intro.jpg
    :width: 433px
    :align: center
    :height: 289px
    :alt: 
|
.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:
|
History
=======
Openmediavault's history began with Volker Theile, who was the only 
active developer of the FreeNAS project by the end of 2009.   Volker 
became interested in completely rewriting FreeNAS, for use on Linux.  
Initially, he named the rewritten package **coreNAS** .  Shortly 
thereafter, Volker discarded the name **coreNAS** in favor of 
**Openmediavault** .  Openmediavault's initial release was on 17 
October 2011.  It's built upon very mature and proven software layers 
and is under constant development. Openmediavault relies on the Debian 
project and uses their system and repositories as a base.  The project 
focus is on creating and maintaining a stable and extensible NAS system 
that is intuitive and easy to use.


Purpose
=======
The purpose of Openmediavault  (hereafter referred to as “OMV”),  is to 
provide a NAS system that is highly “extensible” with value added 
plugin’s and access to numerous Dockers that are desirable and 
beneficial to home users and small businesses at little to no cost.

One of the ambitions of the OMV project is to make advanced NAS 
technologies and features available to inexperienced users in an easy to 
use WEB GUI, thereby making it possible for people, without extensive 
knowledge of Linux, to gain easy access to advanced technologies.

Getting Involved
================
If businesses and home users find OMV to be beneficial, please consider 
supporting the project with a modest donation.  While OMV is free, 
donations to cover Web site costs, hardware for testing, and other 
unavoidable expenses are needed and very much appreciated. 


`Donate to OMV <https://www.openmediavault.org/?page_id=1149>`_ (Main project development)

`Donate to omv-extras.org <http://omv-extras.org/>`_  (Support for Single Board Computers and Development of Plugins.)

The OMV project is looking for coding talent and contributors.  If one 
has developer experience, (BASH, PHP, Python, Javascript) the project 
would like to hear from you.  Users with Linux experience are invited to 
help out on the `OMV Forum <https://forum.openmediavault.org/index.php/BoardList/>`_ . 


.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:
|
****************
About this Guide
****************

In computing, generally speaking, there are several ways to do the same 
thing.  By extension,  methods and methodology become progressively more 
advanced as a user's skill level increases.  With these notes in mind, 
methods found in this guide may not be considered as “Best Practice”, especially from a hardened security perspective.  The purpose and intent of this guide is to provide a walk-through to get users up and running as quickly and easily as possible.

* This guide contains links to external sources of information and 
software.  It's best used on a PC connected to the Internet.
* This is a community document and a work in progress.  Input and 
feedback are welcome and can be sent to: omvguide@gmail.com 

Beginners:
==========
This document is intended for beginners who will, primarily, be using 
the OMV's GUI.  Beginners are assumed to have basic knowledge of 
computers and their LAN systems, and a Windows or Apple PC.
The focus of this guide will be to take a technically easy route, for 
the widest possible cross section of new users, toward accomplishing 
basic tasks using methods and processes that are easy to understand and 
duplicate. 

Advanced Users:
===============
OMV was designed to be intuitive for advanced users and beginners alike.  
After the installation is complete, for a streamlined setup, see the 
Quick Start Guide.

A Cautionary Note for Advanced Users:
-------------------------------------
Many of the configuration files traditionally used to customize Debian 
Linux are controlled by the OMV system database.  As a result, manual 
edits of configuration files may be overwritten as of the next, 
“on-demand”, configuration change in the OMV GUI.  Further, it is 
possible to “break” OMV with alterations and permissions changes to the 
files of the boot drive, on the command line.  
In the beginning it's best to rely, primarily, on the GUI for 
configuration and control.  Otherwise, before attempting to customize 
the operating system, backing up the boot drive is highly recommended.

.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

|
********
Hardware
********

Hardware requirements to run OMV are very modest, however, actual 
hardware requirements for specific “use cases” vary widely.  The 
following is intended only as general guidance.  

Compatibility:
============

OMV 5.X is currently supported by Debian 10, “Buster”.  
Compatible hardware and other requirements of Debian Linux are available 
at Debian.org 

64 bit hardware (amd64):
========================

The OMV project maintains convenient, fully integrated, OMV/Debian 
installation ISO's.  This is the best method for getting OMV up and 
running quickly.

32 bit Hardware (i386):
=======================

While OMV is supported by 32 bit Debian installations, it's a two step 
scripted process referenced in; “Installing on i386 32-bit Platforms”. 
The OMV project does not provide integrated 32 bit installation ISO's.

ARM Hardware:
============

The OMV project provides scripted installation support for ARM Single 
Board Computer (SBC) platforms.  Supported platforms are the Raspberry 
Pi, models 2B and higher, and the various ARM platforms supported by 
Armbian.  
Minimum Hardware requirements 
OMV/Debian will run on I386, AMD64, and select ARM platforms with 1GB 
of ram or less, but performance expectations should be adjusted 
accordingly.  The system boot drive should have a minimum of 8GB capacity.

Recommended Minimum requirements 
================================

For basic File Server operations - 1 or 2 users:

* Intel Core 2 Duo or equivalent AMD processor and 1GB of RAM.
* Any of the ARM Single Board Computers supported by OMV.

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
* Integrated video is preferred over add-on Video cards.  With OMV's headless server design, add-on Video cards are an excessive and unnecessary power drain, with no performance benefit. Installing a high end, high powered Video card in a headless server is analogous to installing a 65 to 200 watt light bulb in a closet, without a switch, and closing the door.

ARM - Single Board Computers:
-----------------------------

Performance levels vary greatly among the various models 
of **Single Board Computer** (hereafter referred to as an "**SBC**") 
that are supported by Armbian, Raspbian, and OMV.  While most will 
support file server operations for a few users, if running server 
add-on's or Dockers is a requirement, research the chosen SBC carefully 
before buying.  Armbian's `Armbian's <https://forum.armbian.com/>`_ or 
OMV's `OMV's <https://forum.openmediavault.org/>`_ forums may be of 
assistance, along with Internet product reviews.
*When considering an SBC as a primary NAS server for home use, note 
that support for SBC's is for **the current OMV release only**.  
Accordingly, SBC users should read the ending cautionary note in Operating System 
Backup.*

Raspberry PI's
^^^^^^^^^^^^^^
(Hereafter referred to as **R-PI's**.)  
Given the current market for SBC's, the majority of SBC users will 
likely be owners of R-PI's.  

OMV runs well on the R-PI 4.  While OMV will run on an R-PI model 2B and 
the various models of the R-PI 3, performance is poor.   What exactly 
does “poor performance” mean?  In this context, if the R-PI's CPU is 
running at 100%, OMV my not show up on the network and / or network 
shares may not open.  This may give the false impression that there's a 
software or permissions problem.  In other instances, the WEB GUI login 
page may not respond.
These issues may appear to be software related problems, but that's not 
always the case.  Older R-PI's are very easily over stressed and, during 
periods where the CPU is running at 100%, they may not respond to 
external input.  With this performance limitation in mind, earlier 
versions of the R-PI (2B and 3X models) should be used only as a basic 
file server for 1 or 2 user home environments, where multitasking is 
less likely.  If running automated tasks, it's best to schedule them to 
run in the early morning hours when user access would not be affected.
In addition, R-PI's suffer from USB under powering in models 2B and 3X.  
See notes regarding this issue in USB Power - A Common Raspberry PI problem

Where CPU Power may be Needed – “Transcoding”
=============================================
If a users' primary consideration in setting a up a media server, CPU 
selection or identification may need to be carefully considered. 
Transcoding is a process for translating media file formats into types 
that mobile devices understand.  Since mobile devices are low powered, 
they're not capable of re-processing high resolution media files 
smoothly so the processing burden is often transferred to the media 
server.

Pre-2011 Intel and AMD CPU's
----------------------------
`Plex <https://support.plex.tv/hc/en-us/articles/200250377-Transcoding-Media>`_, a popular media server, recommends at least 2000 on the CPU's 
`PassMark <https://www.cpubenchmark.net/cpu_list.php>`_ score for each concurrent 1080p transcoded stream.  
`(See the advice article here) <https://support.plex.tv/hc/en-us/articles/201774043-What-kind-of-CPU-do-I-need-for-my-Server->`_   However, this advice 
applies to pre-2011 Intel and AMD CPU's.  

Look up an older CPU here `PassMark CPU Benchmarks <https://www.cpubenchmark.net/cpu_list.php>`_

.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

2011 and Newer Intel CPU's
--------------------------

As of the beginning of the Sandy Bridge CPU series in 2011 and later, a core has 
been added to Intel CPU's for the sole purpose of video transcoding.  CPU's with 
Quick Sync, to include Celeron and Atom models that are relatively low powered, do 
a good job of transcoding for portable devices.

If NAS administrators have numerous smart phone users, in their homes or 
businesses, who will be watching transcoded video on the small screen, CPU loading 
and Video processing features may require some additional thought and research.  


Additional reading: 
`Intel Quick Sync versus similar AMD technology <https://www.macxdvd.com/mac-dvd-video-converter-how-to/what-is-intel-quick-sync-video.htm>`_

Selecting a Boot Drive
======================

Nearly any type of hard drive, SSD, or flash device (USB thumb-drives and 
SD-cards) 8GB or larger, will function as an OMV boot drive.

However, some notions of achieving a “Faster” or a “Better Performing NAS server” 
by using certain types of fast boot media should be dispelled.

Server booting requirements and considerations are different when compared to 
desktop and business workstation requirements.

* Given OMV's lean configuration, boot times can be fast.  Boot times of 1 minute and Shutdown times of 20 seconds are common, even when using relatively slow flash media such as USB thumb-drives and SD-cards.  (Recent models can be quite fast – check their benchmarks.)

* Typically servers are rebooted no more than once a week.  When automated, a reboot event is usually scheduled after-hours when users are not affected.  

* After the boot process is complete, most of OMV's file server functions are running from RAM.

**Conclusion – for Linux file server operations, fast boot media is not important.**

* “The WEB/GUI is more responsive with fast media.”

This is the single instance where an SSD or a spinning hard drive may create the illusion of higher performance.  In the traditional role of a NAS as a File Server, when the server boots, the Linux kernel and most of the necessary processes required to act as a File Server are loaded into RAM - the fastest possible media for execution.
Navigating OMV's WEB/GUI interface is another matter.  Loading WEB pages may call files from the boot drive, which may make the server appear to be slower, when using slow media.  However, the speed of the boot drive has little impact on overall file server function and actual NAS performance.

*The above assumes that adequate RAM has been provisioned.*

Final Notes on Choosing a Boot Drive
------------------------------------

OMV's boot requirements are very modest:
While some users prefer traditional hard drives or SSD's, the boot 
requirement can be served with USB thumb-drives and SD-cards, 8GB or 
larger.

With USB connections on the *outside* of a PC case, cloning USB drives for operating system backup is an easy process.  Given this consideration, some users prefer USB thumb-drives and other external flash media to internal drives.  Further, given the ease of operating system recovery in the event of a boot drive failure, beginners are encouraged to consider using flash media.

If flash media is used:
New name brand drives are recommended such as Samsung, SanDisk, etc.  
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
installation is detailed in  The Flash Memory Plugin. 

**Use-case exceptions where boot media larger than 32GB may be useful:**

* Running applications that utilize WEB interfaces, such as Plex, Emby, etc.

* Hosting Web or Media Servers with extensive content.

* Hosting Virtualized Guest operating systems with desktops.  (Does not apply to ARM platforms. ARM platforms can not virtualize i386 or amd64 platforms. )

(There's no penalty for starting with a smaller boot drive. Moving to a larger 
drive, if needed, can be done later.)

Note:   Buying flash devices on-line, even from reputable retailers, comes 
with the substantial risk of buying fakes.  Buying flash drives, in sealed 
packaging, from walk-in retail stores with liberal return policies is recommended.  The use of cheap generics, fakes or knockoffs is highly discouraged.  They tend to have a short life and they're known to cause problems, even if they initially test error-free.  
In addition, to detect fakes or defective media *even when new*; all SD-cards 
and USB thumb-drives, should be formatted and tested in accordance with the 
process outlined under Format and Testing Flash Media.  If they fail error 
testing, return them for a refund.

Hardware - The Bottom Line
==========================

Again, OMV/Debian's hardware requirements are modest.  Nearly any IBM 
compatible PC or Laptop produced in the last 10 years could be re-purposed 
as an OMV server.

However, it should be noted that newer hardware is, generally speaking, more 
power efficient and it's higher performing.  The power costs of running older 
equipment that is on-line, 24 hours a day, can easily pay for newer, more 
power efficient equipment over time.

Further, the supported ARM platforms are both power efficient and capable of 
providing file server functions in a home environment.  (Again, performance 
expectations should be adjusted in accordance with the capabilities of the 
hardware.)

.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

|
|
********************************************
Installing on Single Board Computers (SBC's)
********************************************

Installation guides for SBC installations are available 
in `PDF's <https://forum.openmediavault.org/index.php/Thread/28789-Installing-OMV5-on-Raspberry-PI-s-Armbian-Supported-SBC-s/?postID=214407#post214407>`_ 
or in a `Wiki <https://wiki.omv-extras.org/>`_ .

.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:
|
|
***********************************
Installing on i386 32-bit Platforms
***********************************

An installation guide for 32-bit installations is available 
in `PDF <https://forum.openmediavault.org/index.php/Thread/28789-Installing-OMV5-on-Raspberry-PI-s-Armbian-Supported-SBC-s/?postID=214407#post214407>`_ 
or in a `Wiki <https://wiki.omv-extras.org/>`_ .

.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt
|
|
************************
amd64 (64-bit) Platforms
************************

This guide assumes the user will be installing from a CD, burned 
from an image found in OMV's files 
repository `OMV's files repository <https://sourceforge.net/projects/openmediavault/files/>`_ , 
using 64 bit hardware.  

Downloading
===========

Beginners should download the latest stable version from `Sourceforge.net <https://sourceforge.net/projects/openmediavault/files/>`_ 
and copy or download the SHA or MD5 checksums for the ISO.  The 
checksum value will be used with the MD5 SHA checksum utility.  

.. note:: Windows Notepad can open MD5 files by selecting “**All Files**”, next to the file name drop down.  

.. warning:: If users install Beta versions of OMV, they are agreeing to be a “tester”.  As part of being a tester, users may experience issues or bugs that can not be resolved which may result in **lost data**.  Plan accordingly, with full data backup.**

Verify the download
-------------------

After the download is complete, verify the download with a  
`MD5 & SHA chechsum utility <http://md5-sha-checksum-utility.en.lo4d.com//>`_.  
MD5 and SHA hashes check for image corruption that may have occurred 
during the download.   

.. note:: Beginners - DO NOT SKIP THIS STEP.  The chance of image corruption is high when downloading and it's pointless to build a server with flawed software.  Even the **slightest** corruption of the installation ISO may ruin your installation and the effects may not be noticed until well after your server is built and in use.  Headaches can be avoided by checking the image.
|  
.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:
|  
|  

Installing - amd64 Platforms
============================
|  
| 

Burning a source CD
-------------------

Assuming a CD/DVD drive is installed; in most cases, double clicking an 
installation file, with an **.ISO** extension, will trigger a CD burning utility 
on a Windows Computer or a MAC.  If help is needed for this process, see the 
following link.

`How to burn an ISO image in Windows 7, 8, 10 <https://www.lifewire.com/how-to-burn-an-iso-image-file-to-a-dvd-2626156>`_
   

Creating a Bootable ISO Thumb-drive
-----------------------------------

For PC's without an Optical drive; the OMV ISO can be installed using a 
Thumbdrive as the ISO source, and install the Debian/OMV system to a second 
thumb drive.

**Before creating an ISO thumb-drive consider checking the drive using the utilities and process described below in**, Preparing Flash Media.

For assistance in creating a bootable ISO thumb-drive, see the following link.

`How to install an ISO file on a USB drive <https://www.lifewire.com/how-to-burn-an-iso-file-to-a-usb-drive-2619270>`_

|  
.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

**If installing to a standard hard drive or SSD, skip to** Installing Openmediavault.
 
.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:
|






