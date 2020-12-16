
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
    :width: 516px
    :align: center
    :height: 344px
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

