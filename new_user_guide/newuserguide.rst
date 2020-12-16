
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

Openmediavault is a File Server / NAS system designed to work on most modern IBM compatible PC systems, to include typical amd64 or i386 PC’s and select ARM devices. Openmediavault (OMV) can be thought of as filling a role similar to Microsoft's Server Essentials, but extends far beyond the role of a basic File Server with additional functionality added VIA plugin’s and Dockers. OMV is designed to work with popular client operating systems and multiple filesystem types, utilizing proven data sharing techniques on small and medium sized Local Area Networks.

In meeting the needs of it's intended users, individuals and small-to-medium-sized businesses, Openmediavault is designed for flexibility.

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
Openmediavault's history began with Volker Theile, who was the only active developer of the FreeNAS project by the end of 2009.   Volker became interested in completely rewriting FreeNAS, for use on Linux.  Initially, he named the rewritten package **coreNAS** .  Shortly thereafter, Volker discarded the name **coreNAS** in favor of **Openmediavault** .  Openmediavault's initial release was on 17 October 2011.  It's built upon very mature and proven software layers and is under constant development. Openmediavault relies on the Debian project and uses their system and repositories as a base.  The project focus is on creating and maintaining a stable and extensible NAS system that is intuitive and easy to use.


Purpose
=======
The purpose of Openmediavault  (hereafter referred to as “OMV”),  is to provide a NAS system that is highly “extensible” with value added plugin’s and access to numerous Dockers that are desirable and beneficial to home users and small businesses at little to no cost.

One of the ambitions of the OMV project is to make advanced NAS technologies and features available to inexperienced users in an easy to use WEB GUI, thereby making it possible for people, without extensive knowledge of Linux, to gain easy access to advanced technologies.

Getting Involved
================
If businesses and home users find OMV to be beneficial, please consider supporting the project with a modest donation.  While OMV is free, donations to cover Web site costs, hardware for testing, and other unavoidable expenses are needed and very much appreciated. 


`Donate to OMV <https://www.openmediavault.org/?page_id=1149>`_ (Main project development)

`Donate to omv-extras.org <http://omv-extras.org/>`_  (Support for Single Board Computers and Development of Plugins.)

The OMV project is looking for coding talent and contributors.  If one has developer experience, (BASH, PHP, Python, Javascript) the project would like to hear from you.  Users with Linux experience are invited to help out on the `OMV Forum <https://forum.openmediavault.org/index.php/BoardList/>`_ . 


.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:
|
****************
About this Guide
****************

In computing, generally speaking, there are several ways to do the same thing.  By extension,  methods and methodology become progressively more advanced as a user's skill level increases.  With these notes in mind, methods found in this guide may not be considered as “Best Practice”, especially from a hardened security perspective.  The purpose and intent of this guide is to provide a walk-through to get users up and running as quickly and easily as possible.

* This guide contains links to external sources of information and software.  It's best used on a PC connected to the Internet.
* This is a community document and a work in progress.  Input and feedback are welcome and can be sent to: omvguide@gmail.com 

Beginners:
==========
This document is intended for beginners who will, primarily, be using the OMV's GUI.  Beginners are assumed to have basic knowledge of computers and their LAN systems, and a Windows or Apple PC.
The focus of this guide will be to take a technically easy route, for the widest possible cross section of new users, toward accomplishing basic tasks using methods and processes that are easy to understand and duplicate. 

Advanced Users:
===============
OMV was designed to be intuitive for advanced users and beginners alike.  
After the installation is complete, for a streamlined setup, see the Quick Start Guide.

A Cautionary Note for Advanced Users:
-------------------------------------
Many of the configuration files traditionally used to customize Debian Linux are controlled by the OMV system database.  As a result, manual edits of configuration files may be overwritten as of the next, “on-demand”, configuration change in the OMV GUI.  Further, it is possible to “break” OMV with alterations and permissions changes to the files of the boot drive, on the command line.  
In the beginning it's best to rely, primarily, on the GUI for configuration and control.  Otherwise, before attempting to customize the operating system, backing up the boot drive is highly recommended.

.. image:: /new_user_guide/images/divider.png
    :width: 400px
    :align: center
    :height: 75px
    :alt:

