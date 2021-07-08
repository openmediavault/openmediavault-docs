.. _administration_index:

Administration
##############

Configuration changes are not applied immediately, instead you can
determine when this happens. This enables several changes to be activated
at the same time, which reduces unnecessary waiting times.

.. note::

    |omv| does not display the submodules that are affected by the
    configuration changes. If you still want to know which submodules are
    affected, simply run ``cat /var/lib/openmediavault/dirtymodules.json``
    in the CLI.

.. toctree::
    :maxdepth: 3

    general/index
    storage/index
    access_rights_management
    services/index
    ../various/advset
