Plugin Development
##################

The range of functions of |omv| can be expanded by means of plugins. This
section describes how to implement such plugins.

Plugins are implemented in a declarative manner, this means no JavaScript
or TypeScript knowledge is needed.

Overview
========

A plugin contains of various YAML files that have to be located in the
directory :file:`/usr/share/openmediavault/workbench`. The following
subdirectories each have a special meaning.

component.d
	This directory contains the manifest files of the pages shown in the
	|omv| |webui|.

dashboard.d
	This directory contains the manifest files of the dashboard widgets.

log.d
	This directory contains the manifest files that are used to configure
	the log content that is shown in the ``Diagnostics | System Logs``
	datatable.

navigation.d
	This directory contains the manifest files that are used to configure
	the navigation bar on the left side of the |webui|.

route.d
	This directory contains the manifest files that are used to configure
	the |webui| routes.

A manifest file must follow the following schema:

    .. code-block:: YAML

        version: "1.0"
        type: component | dashboard-widget | log | navigation-item | route
        data:
          ...

Directories
===========

component.d
-----------

A manifest file must follow the following schema:

    .. code-block:: YAML

        version: "1.0"
        type: component
        data:
          name: string
          type: navigationPage | formPage | selectionListPage | textPage | tabsPage | datatablePage | rrdPage
          config:
            ...

The `name` field contains the unique identifier of the component. It is
used to reference the component in a route configuration. The `type`
field contains one of the following supported page types:

- `formPage <https://github.com/openmediavault/openmediavault/blob/master/deb/openmediavault/workbench/src/app/core/components/limn-ui/models/form-page-config.type.ts>`_
- `selectionListPage <https://github.com/openmediavault/openmediavault/blob/master/deb/openmediavault/workbench/src/app/core/components/limn-ui/models/selection-list-page-config.type.ts>`_
- `textPage <https://github.com/openmediavault/openmediavault/blob/master/deb/openmediavault/workbench/src/app/core/components/limn-ui/models/text-page-config.type.ts>`_
- `tabsPage <https://github.com/openmediavault/openmediavault/blob/master/deb/openmediavault/workbench/src/app/core/components/limn-ui/models/tabs-page-config.type.ts>`_
- `datatablePage <https://github.com/openmediavault/openmediavault/blob/master/deb/openmediavault/workbench/src/app/core/components/limn-ui/models/datatable-page-config.type.ts>`_
- `rrdPage <https://github.com/openmediavault/openmediavault/blob/master/deb/openmediavault/workbench/src/app/core/components/limn-ui/models/rrd-page-config.type.ts>`_

The available properties of each type can be found in the corresponding models.

Example:

.. code-block:: YAML

    version: "1.0"
    type: component
    data:
      name: omv-services-clamav-onaccess-scan-form-page
      type: formPage
      config:
        request:
          service: ClamAV
          get:
            method: getOnAccessPath
            params:
              uuid: "{{ _routeParams.uuid }}"
          post:
            method: setOnAccessPath
        fields:
          - type: confObjUuid
          - type: checkbox
            name: enable
            label: _("Enabled")
            value: false
          - type: sharedFolderSelect
            name: sharedfolderref
            label: _("Shared folder")
            hint: _("The location of the files to scan on-access.")
            validators:
              required: true
        buttons:
          - template: submit
            execute:
              type: url
              url: "/services/clamav/onaccess-scans"
          - template: cancel
            execute:
              type: url
              url: "/services/clamav/onaccess-scans"

dashboard.d
-----------

The following dashboard widget types are available:

- datatable
- rrd
- chart

The available properties of each type can be found in the corresponding `model <https://github.com/openmediavault/openmediavault/blob/master/deb/openmediavault/workbench/src/app/core/components/dashboard/models/dashboard-widget-config.model.ts>`_.

Example:

.. code-block:: YAML

    version: "1.0"
    type: dashboard-widget
    data:
      id: 9984d6cc-741b-4fda-85bf-fc6471a61e97
      permissions:
        role:
          - admin
      title: _("CPU Usage")
      type: chart
      chart:
        type: gauge
        min: 0
        max: 100
        displayValue: true
        request:
          service: System
          method: getInformation
        label:
          formatter: template
          formatterConfig: "{{ value | tofixed(1) }}%"
        dataConfig:
          - label: Usage
            prop: cpuUsage
            backgroundColor: "#4cd964"

log.d
-----

Plugins can add their own log files to the |webui|. The properties of
the manifest file can be inspected `here <https://github.com/openmediavault/openmediavault/blob/master/deb/openmediavault/workbench/src/app/core/services/log-config.service.ts>`_.

Example:

.. code-block:: YAML

    version: "1.0"
    type: log
    data:
      id: clamav
      text: _("Antivirus")
      columns:
      - name: _("Date & Time")
        sortable: true
        prop: ts
        cellTemplateName: localeDateTime
        flexGrow: 1
      - name: _("Message")
        sortable: true
        prop: message
        flexGrow: 2
      request:
        service: LogFile
        method: getList
        params:
          id: clamav

navigation.d
------------

To add a new item to the navigation bar on the left side of the |webui|
a manifest file with the following `properties <https://github.com/openmediavault/openmediavault/blob/master/deb/openmediavault/workbench/src/app/core/services/navigation-config.service.ts>`_ must be created.

The menu items are ordered alphabetically. If specified, the `position`
field is added as additional sort condition.

Icons have to be specified like ``mdi:<NAME>`` or ``<NAME>``. For the first
format please have a look `here <https://materialdesignicons.com/>`_ for available icons.
For the latter please check `here <https://github.com/openmediavault/openmediavault/blob/master/deb/openmediavault/workbench/src/app/shared/enum/icon.enum.ts>`_.
If possible, use the ``<NAME>`` format to ensure that uniform icons are
used throughout the whole |webui|.

Example:

.. code-block:: YAML

    version: "1.0"
    type: navigation-item
    data:
      path: "services.clamav.onaccess-scans"
      text: _("On Access Scans")
      position: 20
      icon: "mdi:file-eye"
      url: "/services/clamav/onaccess-scans"

route.d
-------

A manifest file must follow the following schema:

    .. code-block:: YAML

        version: "1.0"
        type: route
        data:
          url: string
          title: string
          editing: boolean
          notificationTitle: string
          component: string

The `url` is used to access the page via browser. A url like ``/foo/bar``
will finally look like ``https://localhost/#/foo/bar``. The `title` field
will be shown in the breadcrumb bar.
The `component` references the page component that is displayed in the
main area of the |webui|.

Example:

.. code-block:: YAML

    version: "1.0"
    type: route
    data:
      url: "/services/clamav/onaccess-scans/create"
      title: _("Create")
      notificationTitle: _("Created on-access scan.")
      component: omv-services-clamav-onaccess-scan-form-page

Build configuration
===================

To build and apply the final |webui| configuration you need to run ``omv-mkworkbench COMMAND``
where ``COMMAND`` is ``all | dashboard | log | navigation | route | i18n``.
