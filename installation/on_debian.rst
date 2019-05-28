Installation on Debian
######################

You can install |omv| on a Debian installation as well. 

To do so, on x86 simply install the system using the `Debian netinst images
<https://www.debian.org/CD/netinst/>`_. After that apply the commands below. 
Please do **not** install a graphical environment, use a minimal server 
installation only. For a step by step install guide have a look into the 
`Debian minimal install guide <https://www.pcsuggest.com/debian-minimal-install-guide/>`_.

On ARM devices check if there's an appropriate [Armbian](https://www.armbian.com/download/) Stretch (OMV4) or Buster (OMV5) image available. After installing Armbian then use the `armbian-config` tool to install OMV in a single step with all performance and reliability tweaks included. If there's no Armbian for your device simply follow the steps outlined below.

Debian 8 (Jessie)
-----------------

Add the package repositories::

    cat <<EOF >> /etc/apt/sources.list.d/openmediavault.list
    deb http://packages.openmediavault.org/public erasmus main
    # deb http://downloads.sourceforge.net/project/openmediavault/packages erasmus main
    ## Uncomment the following line to add software from the proposed repository.
    # deb http://packages.openmediavault.org/public erasmus-proposed main
    # deb http://downloads.sourceforge.net/project/openmediavault/packages erasmus-proposed main
    ## This software is not part of OpenMediaVault, but is offered by third-party
    ## developers as a service to OpenMediaVault users.
    # deb http://packages.openmediavault.org/public erasmus partner
    # deb http://downloads.sourceforge.net/project/openmediavault/packages erasmus partner
    EOF

Install the |omv| 3 (Erasmus) package::

    export LANG=C
    export DEBIAN_FRONTEND=noninteractive
    export APT_LISTCHANGES_FRONTEND=none
    apt-get update
    apt-get --allow-unauthenticated install openmediavault-keyring
    apt-get update
    apt-get --yes --force-yes --auto-remove --show-upgraded \
        --no-install-recommends \
        --option Dpkg::Options::="--force-confdef" \
        --option DPkg::Options::="--force-confold" \
        install postfix openmediavault
    # Initialize the system and database.
    omv-initsystem

Debian 9 (Stretch)
------------------

Install HTTPS transport for APT to prevent MITM attack while downloading keyring::

    apt-get update
    apt-get install --yes apt-transport-https

Add the package repositories::

    cat <<EOF >> /etc/apt/sources.list.d/openmediavault.list
    deb https://packages.openmediavault.org/public arrakis main
    # deb https://downloads.sourceforge.net/project/openmediavault/packages arrakis main
    ## Uncomment the following line to add software from the proposed repository.
    # deb https://packages.openmediavault.org/public arrakis-proposed main
    # deb https://downloads.sourceforge.net/project/openmediavault/packages arrakis-proposed main
    ## This software is not part of OpenMediaVault, but is offered by third-party
    ## developers as a service to OpenMediaVault users.
    # deb https://packages.openmediavault.org/public arrakis partner
    # deb https://downloads.sourceforge.net/project/openmediavault/packages arrakis partner
    EOF

Install the |omv| 4 (Arrakis) package::

    export LANG=C
    export DEBIAN_FRONTEND=noninteractive
    export APT_LISTCHANGES_FRONTEND=none
    apt-get update
    apt-get --allow-unauthenticated install openmediavault-keyring
    apt-get update
    apt-get --yes --auto-remove --show-upgraded \
        --allow-downgrades --allow-change-held-packages \
        --no-install-recommends \
        --option Dpkg::Options::="--force-confdef" \
        --option DPkg::Options::="--force-confold" \
        install postfix openmediavault
    # Initialize the system and database.
    omv-initsystem
