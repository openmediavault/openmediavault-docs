.. _installation_index:

Installation on Debian
######################

You can install |omv| on a Debian installation as well. To do so, simply
install the system using the `Debian netinst images <https://www.debian.org/CD/netinst/>`_.
After that apply the following commands. Please do **not** install a graphical
environment, use a minimal server installation only. For a step by step
install guide have a look `here <https://www.pcsuggest.com/debian-minimal-install-guide/>`_.

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

Install the |omv| package::

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

Add the package repositories::

    cat <<EOF >> /etc/apt/sources.list.d/openmediavault.list
    deb http://packages.openmediavault.org/public arrakis main
    # deb http://downloads.sourceforge.net/project/openmediavault/packages arrakis main
    ## Uncomment the following line to add software from the proposed repository.
    # deb http://packages.openmediavault.org/public arrakis-proposed main
    # deb http://downloads.sourceforge.net/project/openmediavault/packages arrakis-proposed main
    ## This software is not part of OpenMediaVault, but is offered by third-party
    ## developers as a service to OpenMediaVault users.
    # deb http://packages.openmediavault.org/public arrakis partner
    # deb http://downloads.sourceforge.net/project/openmediavault/packages arrakis partner
    EOF

Install the |omv| package::

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
