Installation on Debian
######################

You can install |omv| on a Debian installation as well.

To do so, on x86 simply install the system using the `Debian netinst images
<https://www.debian.org/CD/netinst/>`_. After that apply the commands below.
Please do **not** install a graphical environment, use a minimal server
installation only. For a step by step install guide have a look into the
`Debian minimal install guide <https://www.pcsuggest.com/debian-minimal-install-guide/>`_.

On ARM devices check if there's an appropriate `Armbian <https://www.armbian.com/download>`_
Buster (Debian 10) image available. After installing Armbian then use the
`armbian-config` tool to install OMV in a single step with all performance and reliability
tweaks included. If there's no Armbian for your device simply follow the steps outlined
below.

On `Raspberry Pi OS <https://www.raspberrypi.org/software/operating-systems/>`_ the below
instructions only partially work. Please refer to a specific `installation script <https://github.com/OpenMediaVault-Plugin-Developers/installScript>`_

Install the openmediavault keyring manually::

    apt-get install --yes gnupg
    wget -O "/etc/apt/trusted.gpg.d/openmediavault-archive-keyring.asc" https://packages.openmediavault.org/public/archive.key
    apt-key add "/etc/apt/trusted.gpg.d/openmediavault-archive-keyring.asc"

Add the package repositories::

    cat <<EOF >> /etc/apt/sources.list.d/openmediavault.list
    deb https://packages.openmediavault.org/public shaitan main
    # deb https://downloads.sourceforge.net/project/openmediavault/packages shaitan main
    ## Uncomment the following line to add software from the proposed repository.
    # deb https://packages.openmediavault.org/public shaitan-proposed main
    # deb https://downloads.sourceforge.net/project/openmediavault/packages shaitan-proposed main
    ## This software is not part of OpenMediaVault, but is offered by third-party
    ## developers as a service to OpenMediaVault users.
    # deb https://packages.openmediavault.org/public shaitan partner
    # deb https://downloads.sourceforge.net/project/openmediavault/packages shaitan partner
    EOF

.. note::
    If you are a user in mainland China, TUNA provides `mirroring services <https://mirrors.tuna.tsinghua.edu.cn/help/openmediavault/>`_.

Install the |omv| package::

    export LANG=C.UTF-8
    export DEBIAN_FRONTEND=noninteractive
    export APT_LISTCHANGES_FRONTEND=none
    apt-get update
    apt-get --yes --auto-remove --show-upgraded \
        --allow-downgrades --allow-change-held-packages \
        --no-install-recommends \
        --option DPkg::Options::="--force-confdef" \
        --option DPkg::Options::="--force-confold" \
        install openmediavault-keyring openmediavault

    omv-confdbadm populate
