Installation on Debian
######################

You can install |omv| on an existing Debian |deb_version| installation as well.

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
tool to install |omv| in a single step with all performance and reliability tweaks
included. If there's no Armbian image for your device, simply follow the steps
outlined below.

On `Raspberry Pi OS <https://www.raspberrypi.org/software/operating-systems/>`_ the below
instructions only partially work. Please refer to a specific `installation script <https://github.com/OpenMediaVault-Plugin-Developers/installScript>`_.

.. warning::
    Before installing the |omv| package as described below, ensure that the
    `systemd-resolved` package is already installed and configured on the
    system. Otherwise the package will be installed automatically with
    |omv|, which will inevitably result in DNS resolution no longer functioning.
    This in turn means that the |omv| package cannot be installed successfully,
    as it downloads and installs additional packages during installation which
    requires functioning network connectivity.

.. note::
    The following commands must be executed as ``root`` user.

Install and configure the `systemd-resolved` if not already installed. The
configuration is only temporary and gets lost after a reboot.
After the installation of the |omv| package, this can be made permanently by
reconfiguring the network using the :command:`omv-firstaid` command.

.. code-block:: console

    apt-get install --yes systemd-resolved psmisc
    systemctl enable --now systemd-resolved.service
    systemctl restart systemd-resolved.service
    resolvectl dns <INTERFACE> <DNS_SERVER_IP>

.. note::

    If your IP address is configured by DHCP, the dhcp client may interfere
    with `systemd-resolved`, preventing the download of additional packages
    (``apt-get`` and ``wget`` fails).
    In that case, stop it with ``killall dhcpcd`` and repeat the
    ``resolvectl dns <INTERFACE> <DNS_SERVER_IP>`` command.

Install the |omv| keyring manually:

.. code-block:: console

    apt-get install --yes gnupg
    wget --quiet --output-document=- https://packages.openmediavault.org/public/archive.key | gpg --dearmor --yes --output "/usr/share/keyrings/openmediavault-archive-keyring.gpg"

Add the |omv| package repositories:

.. code-block:: console

    cat <<EOF >> /etc/apt/sources.list.d/openmediavault.list
    deb [signed-by=/usr/share/keyrings/openmediavault-archive-keyring.gpg] https://packages.openmediavault.org/public synchrony main
    # deb [signed-by=/usr/share/keyrings/openmediavault-archive-keyring.gpg] https://downloads.sourceforge.net/project/openmediavault/packages synchrony main
    ## Uncomment the following line to add software from the proposed repository.
    # deb [signed-by=/usr/share/keyrings/openmediavault-archive-keyring.gpg] https://packages.openmediavault.org/public synchrony-proposed main
    # deb [signed-by=/usr/share/keyrings/openmediavault-archive-keyring.gpg] https://downloads.sourceforge.net/project/openmediavault/packages synchrony-proposed main
    ## This software is not part of OpenMediaVault, but is offered by third-party
    ## developers as a service to OpenMediaVault users.
    # deb [signed-by=/usr/share/keyrings/openmediavault-archive-keyring.gpg] https://packages.openmediavault.org/public synchrony partner
    # deb [signed-by=/usr/share/keyrings/openmediavault-archive-keyring.gpg] https://downloads.sourceforge.net/project/openmediavault/packages synchrony partner
    EOF

.. note::
    If you are a user in mainland China, TUNA provides `mirroring services <https://mirrors.tuna.tsinghua.edu.cn/help/OpenMediaVault/>`_.

Install the |omv| package:

.. code-block:: console

    export LANG=C.UTF-8
    export DEBIAN_FRONTEND=noninteractive
    export APT_LISTCHANGES_FRONTEND=none
    apt-get update
    apt-get --yes --auto-remove --show-upgraded \
        --allow-downgrades --allow-change-held-packages \
        --no-install-recommends \
        --option DPkg::Options::="--force-confdef" \
        --option DPkg::Options::="--force-confold" \
        install openmediavault

Populate the |omv| database with several existing system settings, e.g. the network configuration:

.. code-block:: console

    omv-confdbadm populate

.. note::
    Right now only :file:`/etc/network/interfaces` is parsed to get the current network configuration.
    If the network is configured a different way (e.g. via `systemd` or `NetworkManager`), then the
    database is not populated and does not contain the necessary information to deploy the network
    configuration with `netplan` for `systemd-networkd` and `systemd-resolved`. In that case use
    :command:`omv-firstaid` to do the initial network configuration instead of the following step.

Re-deploy the network configuration via the services used by |omv|:

.. code-block:: console

    omv-salt deploy run systemd-networkd

Or alternatively use :command:`omv-firstaid` to do the initial network configuration from CLI.

.. note::
    The IP address may change during the redeployment of the network configuration, therefore
    you may lose the connection when you are connected via SSH.

By default the `root` user can now access the system via SSH as a fallback if something went
wrong during the installation, e.g. the UI is not accessible. SSH access for `root` should be
disabled for security reasons as soon as possible after the installation has been successfully
finished.

.. note::
    The user created by the Debian installer will not able to SSH into the system after |omv|
    has been installed. This is because only users who are assigned to the `_ssh` group are
    allowed to use SSH.
