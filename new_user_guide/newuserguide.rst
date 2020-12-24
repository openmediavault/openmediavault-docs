##############
New User Guide
##############

.. image:: /new_user_guide/images/underconstruction.jpg
    :width: 200px
    :align: center
    :height: 200px
    :alt: Under Construction

In the interim, a complete copy of the User Guide is available → `here <https://github.com/OpenMediaVault-Plugin-Developers/docs/blob/master/Getting_Started-OMV5.pdf>`_ .

|

.. image:: /new_user_guide/images/divider-c.png
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

.. image:: /new_user_guide/images/divider-c.png
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
    :width: 1024px
    :align: center
    :height: 443px
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

* This guide contains links to external sources of information and software.  It's best used on a PC connected to the Internet.

* This is a community document and a work in progress.  Input and feedback are welcome and can be sent to: omvguide@gmail.com 

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



********
Hardware
********

Hardware requirements to run OMV are very modest, however, actual 
hardware requirements for specific “use cases” vary widely.  The 
following is intended only as general guidance.  

Compatibility:
==============

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
=============

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
before buying.  `Armbian's <https://forum.armbian.com/>`_ 
or `OMV's <https://forum.openmediavault.org/>`_ forums may be of 
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

These issues may appear to be software related, but that's not 
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
See the advice article → `here <https://support.plex.tv/hc/en-us/articles/201774043-What-kind-of-CPU-do-I-need-for-my-Server->`_   However, this advice 
applies to pre-2011 Intel and AMD CPU's.  

Look up an older CPU here →  `PassMark CPU Benchmarks <https://www.cpubenchmark.net/cpu_list.php>`_

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

.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:


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



 .. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

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

.. note::   Buying flash devices on-line, even from reputable retailers, comes with the substantial risk of buying fakes.

Buying flash drives, in sealed packaging, from walk-in retail stores with liberal return 
policies is recommended.  The use of cheap generics, fakes or knockoffs is highly discouraged.  They tend to have a short life and they're known to cause problems, even if they initially test error-free.  
In addition, to detect fakes or defective media *even when new*; all SD-cards 
and USB thumb-drives, should be formatted and tested in accordance with the 
process outlined under Format and Testing Flash Media.  If they fail error 
testing, return them for a refund.

.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

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



********************************************
Installing on Single Board Computers (SBC's)
********************************************


Installation guides for SBC installations are available 
in `PDF's <https://forum.openmediavault.org/index.php/Thread/28789-Installing-OMV5-on-Raspberry-PI-s-Armbian-Supported-SBC-s/?postID=214407#post214407/>`_ 
or in a `Wiki <https://wiki.omv-extras.org/>`_ .


.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

|

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
    :alt
|

************************
amd64 (64-bit) Platforms
************************

This guide assumes the user will be installing from a CD, burned 
from an image found in OMV's files 
repository `OMV's files repository <https://sourceforge.net/projects/openmediavault/files/>`_ , 
using 64 bit hardware.  

.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:


Downloading
===========

Beginners should download the latest stable version from `Sourceforge.net <https://sourceforge.net/projects/openmediavault/files/>`_ 
and copy or download the SHA or MD5 checksums for the ISO.  The 
checksum value will be used with the MD5 SHA checksum utility.  

.. note:: Windows Notepad can open MD5 files by selecting “**All Files**”, next to the file name drop down.  

.. warning:: If users install Beta versions of OMV, they are agreeing to be a “tester”.  As part of being a tester, users may experience issues or bugs that can not be resolved which may result in **lost data**.  Plan accordingly, with full data backup.

|

Verify the download
-------------------

After the download is complete, verify the download with a  
`MD5 & SHA chechsum utility <http://md5-sha-checksum-utility.en.lo4d.com//>`_.  
MD5 and SHA hashes check for image corruption that may have occurred 
during the download.   

.. note:: Beginners - DO NOT SKIP THIS STEP.  The chance of image corruption is high when downloading and it's pointless to build a server with flawed software.  Even the **slightest** corruption of the installation ISO may ruin your installation and the effects may not be noticed until well after your server is built and in use.  Headaches can be avoided by checking the image.

.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:
 
 

Installing - amd64 Platforms
============================
|  


Burning a source CD
-------------------

Assuming a CD/DVD drive is installed; in most cases, double clicking an 
installation file, with an **.ISO** extension, will trigger a CD burning utility 
on a Windows Computer or a MAC.  If help is needed for this process, see the 
following link.

`How to burn an ISO image in Windows 7, 8, 10 <https://www.lifewire.com/how-to-burn-an-iso-image-file-to-a-dvd-2626156>`_

|  

Creating a Bootable ISO Thumb-drive
-----------------------------------

For PC's without an Optical drive; the OMV ISO can be installed using a 
Thumbdrive as the ISO source, and install the Debian/OMV system to a second 
thumb drive.

**Before creating an ISO thumb-drive consider checking the drive using the utilities and process described below in**, Preparing Flash Media.

For assistance in creating a bootable ISO thumb-drive, see the following link.

`How to install an ISO file on a USB drive <https://www.lifewire.com/how-to-burn-an-iso-file-to-a-usb-drive-2619270>`_


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
  

Preparing Flash Media 
---------------------

To use flash media as a boot drive, a couple utilities are recommended:

`SDFormatter <https://www.sdcard.org/downloads/formatter_4/eula_windows/index.html/>`_ (get 
the latest version), and `h2testw1.4 <http://www.heise.de/ct/Redaktion/bo/downloads/h2testw_1.4.zip>`_ .

* SDFormatter installs in the same manner as a typical Windows program.  

* h2testw 1.4 is stand-alone “portable” application.  Simply unzip h2testw_1.4 onto the desktop, open the folder, and double click the executable.

Due to the rise in counterfeit media and media that reports a fake size, it's recommended that all USB thumb-drives, new or used, be formatted with SDFormatter and tested with  h2testw1.4  before using them.
|  

.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

  

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

.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:  

After the drive format is completed, open **h2testw** and select your language.

Then, click on **Select target**

.. image:: /new_user_guide/images/4_H2testw.jpg
    :width: 433px
    :align: center
    :height: 270px
    :alt:

.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:   

Under **Computer**, select the flash media previously formatted.

.. image:: /new_user_guide/images/5_H2testw_2.jpg
    :width: 390px
    :align: center
    :height: 398px
    :alt:

.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:  

Select **Write+Verify**.  (Do not check endless verify)|

.. image:: /new_user_guide/images/6_H2testw_3.jpg
    :width: 486px
    :align: center
    :height: 296px
    :alt:

.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

| A dialog box similar to the following may pop up, drawing attention to a **1MB** difference.  
| Ignore it and click on **OK**.

.. image:: /new_user_guide/images/7_H2testw_4.jpg
    :width: 497px
    :align: center
    :height: 199px
    :alt:

.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

| “Without errors” is the desired outcome. 
| (If media tests with errors or is much smaller than is indicated by its labeled size, don't use it.)  

.. image:: /new_user_guide/images/8_H2testw_5.jpg
    :width: 417px
    :align: center
    :height: 357px
    :alt:

After H2testw verifies the USB thumb-drive, do one more clean format, using 
SDFormatter, before using the thumb-drive.


.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

 

amd64 – Openmediavault Installation
===================================

If your PC platform won't boot onto a CD or USB thumb-drive with the installation 
ISO, it may be necessary to change the boot order in BIOS, to set the 
CD/DVD drive or USB boot to the top of the boot order.  This link may provide 
assistance on this topic. → `How To Enter BIOS <https://www.lifewire.com/how-to-enter-bios-2624481>`_   

If difficulties are encountered during the ISO installation, consider 
the → `Alternate 64bit installation guide <http://https://github.com/OpenMediaVault-Plugin-Developers/docs/blob/master/Adden-C-Installing_OMV5_on_32-bit_i386.pdf/>`_ 
Or use `the Wiki <https://wiki.omv-extras.org/doku.php?id=installing_omv5_i386_32_bit_pc>`_ .

.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

| 

An installation walk through:
| 

**Boot Menu:**  Select **Install**

.. image:: /new_user_guide/images/9_Install_Menu.jpg
    :width: 987px
    :align: center
    :height: 504px
    :alt:

|

**Select a Language:**  **(As needed)**

.. image:: /new_user_guide/images/10_Language.jpg
    :width: 790px
    :align: center
    :height: 423px
    :alt:

|  

**Select your Location:**  **(As appropriate.)**

.. image:: /new_user_guide/images/11_Location.jpg
    :width: 790px
    :align: center
    :height: 423px
    :alt:

|


**Configure the Keyboard:** **(Select as appropriate)**

.. image:: /new_user_guide/images/12_Key_Board.jpg
    :width: 794px
    :align: center
    :height: 426px
    :alt:

| 

**Configure the Network:**

While the default hostname is fine, 
a server name that is a bit shorter might be easier to work 
with later on.  (Something like **OMV1**).

.. image:: /new_user_guide/images/13_Config_Network.jpg
    :width: 791px
    :align: center
    :height: 197px
    :alt:
|  
**Configure the Network:**

If applicable, enter your domain name suffix.  Otherwise, for home users and businesses with 
peer to peer networks, the default entry is fine.

.. image:: /new_user_guide/images/14_Config_Network2.jpg
    :width: 779px
    :align: center
    :height: 188px
    :alt:

|  

**Set up users and passwords:**

Follow the on screen guidance for setting the root password.  While not recommended, it 
would be better to write down the **root password**, then to forget it.

.. image:: /new_user_guide/images/15_root_password.jpg
    :width: 779px
    :align: center
    :height: 263px
    :alt:

|

**Set up users and passwords:**

Follow the on screen guidance for setting up a new admin user and password. 

.. image:: /new_user_guide/images/16_Create_User.jpg
    :width: 779px
    :align: center
    :height: 188px
    :alt:

|  

**Configure the Clock:**

Select your time zone.

(NO PIC)

|  

**Partition Disks 1:**

If two storage devices are available for installation, this screen is displayed.

.. image:: /new_user_guide/images/17_Partition_Disks1.jpg
    :width: 785px
    :align: center
    :height: 165px
    :alt:

|

**Partition Disks 2:** 

If installing to a single internal drive, there will be only one selection 
available.  In this particular example, the installation is placed on a USB thumb-drive

.. image:: /new_user_guide/images/18_Partition_Disks2.jpg
    :width: 775px
    :align: center
    :height: 230px
    :alt:

|
Partition Disks 3:

(No Pic)

A 3rd window asks for confirmation of partition selections. Select Yes.

.. note::  If installing to a USB drive, at this point, it is possible to an error may pop-up regarding partitioning the drive, and recommend a reboot.  Follow the recommendation.  After the reboot, the partition operation should succeed the 2nd time around.

|  

**The system installs..........**

|

**Configure the Package Manager:  Debian Archive Mirror Country**

(NO PIC)

While the advice given in this screen is true, without testing, there's no way to know 
which Debian archive mirror is best. Without testing, picking your country or the closest 
location to your country would be the logical choice.

|

**Configure the Package Manager:  Debian Archive Mirror**

(NO PIC)

The default choice is usually best.

|

**Configure the Package Manager:  HTTP proxy**

In most cases this entry will be blank.

(If a proxy is required, note the form of entry required in the dialog box.)

.. image:: /new_user_guide/images/19_Proxy.jpg
    :width: 786px
    :align: center
    :height: 203px
    :alt:

|  

.. note::   If installing to a hard drive, the following screen may or may not appear. 

**Install the GRUB Boot Loader on a Hard Disk:**

Select the appropriate boot disk in your server.

Generally the boot drive will be **/dev/sda** which is, in most cases, the first sata port.

.. image:: /new_user_guide/images/20_Install_Grub.jpg
    :width: 786px
    :align: center
    :height: 203px
    :alt:

|

**Finish the Installation:**  Accept the default.

.. image:: /new_user_guide/images/21_Finish_Install.jpg
    :width: 788px
    :align: center
    :height: 153px
    :alt:

|

**Installation Complete:**

**Remove the CD or USB installation source**, then hit ENTER.

(Otherwise, the installation process may re-start.)

.. image:: /new_user_guide/images/22_Finish_Install2.jpg
    :width: 788px
    :align: center
    :height: 153px
    :alt:

|
.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:
|  

First Boot
==========

Allow the installation to boot.  Normally, the text above the login prompt will provide an **IP address** to be used for opening the console in a web browser.  If an IP address is available, skip the following and proceed to
 OMV - Initial Configuration


.. note:: **There are two exception cases on the first boot that users should be aware of.**

1.) **No address from the DHCP server:**

Normally, DHCP will assign an IP address to OMV and the address will be printed 
to the screen.  However, on odd occasions the following issue may be observed.

.. image:: /new_user_guide/images/23_DHCP_fail.jpg
    :width: 720px
    :align: center
    :height: 282px
    :alt:

This is due to a slow response from your DHCP server, during a fast boot process.

|

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

| 

2.) **An odd IP address is assigned, that is not in the user's network:**

In the following example, the actual network is 192.168.**1**.0/24

.. image:: /new_user_guide/images/25_DHCP_fail3.jpg
    :width: 560px
    :align: center
    :height: 328px
    :alt:

This is usually a one time event where the fix is simple – simply login as root and type ``reboot`` on the command line.  The address will be correct the second time around.

|  

**With a known IP address, proceed to** OMV - Initial Configuration .

|
.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

***************************
OMV - Initial Configuration
***************************
|

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

|  
|  
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

|  
|  
*************************************
Quick Start Guide for Advanced Users:
*************************************

* In the left hand column, start at the top with **General Settings**, and work your way down, choosing and activating the services and features you need for your use case.
* For amd64 and i386 users, a static address for the OMV server and setting the address of a `public DNS server <https://wiki.ipfire.org/dns/public-servers>`_ is recommended.  (SBC users, see the section, **Network Interfaces – SBC Users.**) As an example:  Googles servers 8.8.8.8 and 8.8.4.4 support DNSSEC for better security, and “Anycast” which will direct DNS queries to a nearby server with low network latency.  There are several choices for Public servers that support these features. `List of Public DNS Servers <https://wiki.ipfire.org/dns/public-servers>`_ .
* For a browseable network share, a minimum of one shared folder would need to be configured and that folder would need to be added to SMB/CIF to be visible on the network.  

.. image:: /new_user_guide/images/28_Quick_Start.jpg
    :width: 816px
    :align: center
    :height: 542px
    :alt:
|  
|  
***********************
Basic OMV Configuration
***********************

This section will guide new users through the initial setup of OMV.  It 
addresses how to add a plugin, enabling OMV-Extras, how to setup a 
shared folder and make it browseable on the network with an SMB/CIF share.

System Settings
===============

Under **System**, **General Settings**, in the **Web Administration** tab:

To allow a bit more time for configuration in the GUI, **beginners should consider lengthening the automatic log out time**.  
When the yellow banner appears, click **Apply**.

.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

In the **Web Administrator Password** tab, enter a **strong password**, confirm it and Save.  
(This is one of a few instances where the yellow “confirmation” banner does not appear.)  
This setting changes the GUI login password.  The user “**admin**” will remain the same.   

.. image:: /new_user_guide/images/29_Admin_PW.jpg
    :width: 673px
    :align: center
    :height: 488px
    :alt:

.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

Under **System**, **Date & Time** 

(No Pic) 

Select your **Time Zone** and “toggle ON” **Use NTP Server**.  When OMV toggle switches are **ON**, they're green. **OFF** is gray.

.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

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

.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

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

* It is recommended that users assign a static IP address to the new OMV server that is outside the range of the network's DHCP server.
* It is also recommended that users set a public DNS address.  A list of public DNS servers is available → `here <https://wiki.ipfire.org/dns/public-servers>`_ .  Use a server that supports **DNSSEC**, for better security, and **Anycast**, for low latency end point servers that are closer to user locations.
* The Netmask will be as shown, in most cases, and the Gateway address will be the address of the user's router.

**Note** When saving a new static IP address, the user will be “**going out on a limb and cutting it off**”.  Since the address provided by the network DHCP server is different from the static IP address chosen by the user, when the new address is changed, saved and applied, the GUI web page will stop responding.  This is normal and expected.  Type the new address, entered in the dialog box, into the URL line of your Web browser to reconnect.

.. image:: /new_user_guide/images/30_IP_Address.jpg
    :width: 757px
    :align: center
    :height: 574px
    :alt:


.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

|

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

|

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

.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

|

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

|  

(Optional)

Under **System**, **Monitoring**:

The initial recommended setting is **Enabled**.
(Information gathered may be of use in diagnosing potential problems.)

.. image:: /new_user_guide/images/34_Sys_Monitoring.jpg
    :width: 566px
    :align: center
    :height: 304px
    :alt:

|  

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

|

.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

|

OMV-Extras
==========

.. note::  The following does not apply to SBC or i386 users.  When using the scripted install, OMV-Extras is installed with OMV by default.))

amd64 users will have a basic set of plugin's appropriate for a basic NAS / File Server.  To 
enable the full range of plugin's available on OMV, the installation of OMV-Extras is 
required.  For a preview of what is available visit `omv-extras.org <http://omv-extras.org>`_ and select 
the version of OMV that's being installed. 

For **amd64** users who installed OMV on **SD-cards** or **USB thumb-drives**; installing 
OMV-Extras is a prerequisite for installing the **flash-memory plugin**. The flash-memory 
plugin is **required** for flash media boot drives.

.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

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

.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

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

.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:


In the same window (**System**, **Plugins**) scroll to the bottom.

Select **openmediavualt-omvextrasorg**  and click the **Install** button.

38_omv-extras3.jpg

.. image:: /new_user_guide/images/37_omv-extras2.jpg
    :width: 770px
    :align: center
    :height: 539px
    :alt:

.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

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

.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

A Basic Data Drive
==================

|

General
-------

OMV is capable of setting up basic Linux file systems in the GUI, up to, and including, 
modern “Copy on Write” file systems such as ZFS which combine check summed files, 
RAID functions, and Logical Volume Management into a single package.  However, 
advanced file systems add complexity which can make administration of a NAS 
server more challenging for a beginner. 

Until some experience is gained, it is recommended that Linux/NAS beginners use single 
disks with a native Linux file system.  In the processes described in the following, 
EXT4 will be used with a single data drive.

Some Windows users will want to use USB attached hard drives that are formatted NTFS.  
While this is possible, the drive would need to remain attached or, at a minimum, be 
connected to the server when OMV boots.  It would be better to use a Linux formatted drive 
and create a Samba share (SMB/CIF) for Windows clients, as described in Setting up a 
Shared Folder and Creating a SMB/CIF “Samba” share.

A Samba (SMB/CIF) network share understands the Windows file format and can be configured 
to accommodate DOS and extended file attributes.  Samba serves as a transparent “translator” 
for Windows data storage.

|

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

|

Data Storage - Size matters
---------------------------

In general terms, beginners should do a rough calculation of their storage requirement. When 
selecting a data drive, the initial fill rate should be between 25 and 50%.  As an example, 
if the calculated data to be stored on the NAS is 1TB, the selected drive should be between 
2 and 4TB.  With 50%+ drive free space (2 to 3TB) additional data can be accommodated, 
without the need to expand in the immediate future.  When the fill percentage reaches 75%, 
it's time to plan for more storage. 

|

Data Drive Set Up
-----------------

 .. note:: Note for Beginners and SBC users: OMV is designed to segregate the Operating System (the boot drive) from data storage.  This is “best practice” when setting up a server.  Accordingly, OMV reserves the drive it is installed on exclusively for the OS.  By default, the GUI will not allow the boot drive to be selected when creating a data share.  A second hard drive or SSD is required for data storage.



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

.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

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

The Data Drive is now prepared for a Shared Folder.

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

|

Setting up a Shared Folder
==========================

The majority of the files and folders in a new OMV installation are controlled by 
the root user.  One of the purposes of a **Shared Folder** is to set permissions that 
will allow regular users access to folders and files used for data storage.  A shared 
folder could also be called a “base share”.  The shared folder created in the 
following will be the foundation for creating a “**Network Share**”, covered later.

.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

Under **Access Rights Management**, click on **Shared Folders**, then click on the **Add** button.  

| In the following example, next to:

|   **Name:**  Add your new shared folder's **name**.  
|   **Device:**  Click on the drop down and select the drive that was previously added and formatted. \  
|   **Path:** Accept the default  
|   **Permissions:**  Click on the drop down and select **Everyone: read/write**  

.. image:: /new_user_guide/images/42_shared_folder.jpg
    :width: 782px
    :align: center
    :height:492px
    :alt:

Click the **Save** button.

| 

**The End Result:**

.. image:: /new_user_guide/images/43_shared_folder2.jpg
    :width: 704px
    :align: center
    :height: 299px
    :alt:


.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

Creating a SMB/CIF “Samba” Network Share
========================================

In order to make your shared folder viewable in **Windows Explorer**, 
under **Network**, it's necessary to make it a Samba share using the SMB 
(Server Messaging Block) protocol.  OMV makes setting up a Samba network 
share an easy task.

.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

Under **Services**, click on **SMB/CIF**.   In the **Settings** tab toggle **Enable** to **On** 
(green) and set your workgroup name.  (In Windows, the default workgroup name is, 
WORKGROUP.)  Leave the remainder of settings in this tab at their defaults, and 
click on Save.  (Confirm with “**Apply**” when the yellow banner pops up.)

.. image:: /new_user_guide/images/44_Samba.jpg
    :width: 668px
    :align: center
    :height: 430px
    :alt:

.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

Click on the Shares Tab and the +Add button.

In the popup dialog box, set the following:

|    **Shared folder**: Click on the drop down and select **Music** (or the name for the shared folder previously created.)
|    **Public:**   Click on the drop down and select the **Guests Allowed**

Scroll down with the right scroll bar and toggle **ON** (green), **Extended attributes** and **Store DOS attributes**.  

(Leave the remaining settings at defaults.)  

Click **Save** and confirm with “**Apply**” when the yellow banner appears.  The final result should appear as follows.

.. image:: /new_user_guide/images/45_Samba2.jpg
    :width: 719px
    :align: center
    :height: 389px
    :alt:

.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

Explore the New Network Share
=============================

You should now have a browseable Server with a Network share named Music, so let's take a look.
Open Windows explorer, scroll down to Network and click on it.  There's the new server OPENMEDIAVAULT.

.. image:: /new_user_guide/images/46_Samba3.jpg
    :width: 719px
    :align: center
    :height: 389px
    :alt:

*A few minutes may be required for the Windows Network to “Discover” the new server.  If users are using **Windows 10 PC's**, and the server and share do not appear, see this networking How To.*

.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

Now let's look at the server's new Samba share.  It's there and browseable.

.. image:: /new_user_guide/images/47_Samba4.jpg
    :width: 540px
    :align: center
    :height: 415px
    :alt:

.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

This share is “writable” with a standard “Copy and Paste”, from a client PC.

.. image:: /new_user_guide/images/48_Samba5.jpg
    :width: 540px
    :align: center
    :height: 415px
    :alt:

Congratulations!  You now have a functional NAS that can be expanded to accommodate additional network shares.  Simply repeat the processes in Creating A Network Share to create and make additional shares visible on your network.

|

.. image:: /new_user_guide/images/divider-c.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

|

******************************************
The Flash Memory Plugin - amd64 users only
******************************************

amd64 users who installed OMV **on flash media** will need to install the flash memory plugin.

| 

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


.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:


Under **System**, **Plugins**, scroll down to Section: **Filesystems**.

Select **openmediavualt-flashmemory** and click the **Install** button.

.. image:: /new_user_guide/images/49_OMVExtras.jpg
    :width: 717px
    :align: center
    :height: 412px
    :alt:

.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

Under **Storage**, **Flash Memory**, the following screen is now available.

.. image:: /new_user_guide/images/50_Flash_Mem.jpg
    :width: 685px
    :align: center
    :height: 487px
    :alt:

The plugin will work as is, but it will be more effective if the guidance under **Notes (optional)** is followed. 
While this guidance shows steps for nano, following are options with guidance that beginners may find easier to implement.

.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

Flash Memory Plugin – Editing /etc/fstab
----------------------------------------

There are two options for editing /etc/fstab

* (Option 1) A Linux command line text editor
* (Option 2) WinSCP and Windows Notepad can be used if WinSCP is installed

.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

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
51_Edit_fstab.jpg

.. image:: /new_user_guide/images/51_Edit_fstab.jpg
    :width: 946px
    :align: center
    :height: 481px
    :alt:

Use **Ctrl+o** to save, then **Ctrl+x** to exit

Reboot the server.  
On the command line, the following command can be used: ``reboot``

.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

Option 2: Editing /etc/fstab with WinSCP and Notepad
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This option requires the installation of WinSCP which is detailed here .

Users who are not comfortable with editing fstab using nano can use WinSCP 
and Windows Notepad to make the needed changes.  If WinSCP is not installed, 
this doc-link to → (WinSCP) will describe the process for installing WinSCP and 
logging into the OMV server for the first time.

When logged in, click on **/etc** in the left pane.  In the right pane, “**right**” 
mouse click on **fstab**, select **Edit** and **Notepad**.

.. image:: /new_user_guide/images/52_Edit_fstab2.jpg
    :width: 750px
    :align: center
    :height: 542px
    :alt:

Notepad will open the fstab file.






