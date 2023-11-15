Installation on Debian
######################

You can install |omv| on an existing Debian installation as well.

.. note::
    The installation of |omv| will be denied if a graphical desktop
    environment is detected.

.. note::
    |omv| does not import any existing settings of your system, except
    for network and time related settings. Existing settings will be
    overwritten if the service is managed by |omv|. Please reconfigure
    these services via the |webui|.

To do so, simply install the system using the `Debian netinst images
<https://www.debian.org/CD/netinst/>`_. After that apply the commands below.
Please do **not** install a graphical desktop environment or web server,
use a minimal server installation only (SSH server and standard system utilities).
For a step by step install guide have a look into the
`Debian minimal install guide <https://www.howtoforge.com/tutorial/debian-minimal-server/>`_.

On ARM devices, please check if there's an appropriate `Armbian <https://www.armbian.com/download>`_
image available. Make sure you are using the correct :doc:`Debian version </releases>`
that |omv| is based on. After installing Armbian, then use the `armbian-config`
tool to install OMV in a single step with all performance and reliability tweaks
included. If there's no Armbian image for your device, simply follow the steps
outlined below.

On `Raspberry Pi OS <https://www.raspberrypi.org/software/operating-systems/>`_ the below
instructions only partially work. Please refer to a specific `installation script <https://github.com/OpenMediaVault-Plugin-Developers/installScript>`_

Install the |omv| keyring manually::

    apt-get install --yes gnupg
    wget --quiet --output-document=- https://packages.openmediavault.org/public/archive.key | gpg --dearmor | tee "/usr/share/keyrings/openmediavault-archive-keyring.gpg"

Add the package repositories::

    cat <<EOF >> /etc/apt/sources.list.d/openmediavault.list
    deb [signed-by=/usr/share/keyrings/openmediavault-archive-keyring.gpg] https://packages.openmediavault.org/public shaitan main
    # deb [signed-by=/usr/share/keyrings/openmediavault-archive-keyring.gpg] https://downloads.sourceforge.net/project/openmediavault/packages shaitan main
    ## Uncomment the following line to add software from the proposed repository.
    # deb [signed-by=/usr/share/keyrings/openmediavault-archive-keyring.gpg] https://packages.openmediavault.org/public shaitan-proposed main
    # deb [signed-by=/usr/share/keyrings/openmediavault-archive-keyring.gpg] https://downloads.sourceforge.net/project/openmediavault/packages shaitan-proposed main
    ## This software is not part of OpenMediaVault, but is offered by third-party
    ## developers as a service to OpenMediaVault users.
    # deb [signed-by=/usr/share/keyrings/openmediavault-archive-keyring.gpg] https://packages.openmediavault.org/public shaitan partner
    # deb [signed-by=/usr/share/keyrings/openmediavault-archive-keyring.gpg] https://downloads.sourceforge.net/project/openmediavault/packages shaitan partner
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

Populate the |omv| database with several existing system settings, e.g. the network configuration::

    omv-confdbadm populate

.. note::
    Right now only `/etc/network/interfaces` is parsed to get the current network configuration.
    If the network is configured a different way (e.g. via `systemd` or `NetworkManager`), then the
    database is not populated and does not contain the necessary information to deploy the network
    configuration with `netplan` for `systemd-networkd` and `systemd-resolved`. In that case use
    `omv-firstaid` to do the initial network configuration instead of the following step.

Re-deploy the network configuration via the services used by |omv|::

    omv-salt deploy run systemd-networkd

Or alternatively use `omv-firstaid` to do the initial network configuration.
