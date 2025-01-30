```md
# Some feature

## Subsection

Exciting documentation in here.
Let's make a list (empty surrounding lines required):

- item 1

  - nested item 1
  - nested item 2

- item 2
- item 3
```

# Tree files and directory

Type Files:

- FILETYPE 
1.   network
1.   storage
1.   services
1.   usermgmt
1.   diagnostics

```shell

├── DEBIAN
│   ├── changelog
│   ├── compat
│   ├── control
│   ├── copyright
│   ├── install
│   ├── postinst
│   ├── postrm
│   ├── rules
│   └── triggers
└── usr
    ├── sbin
    │   └── plugin-file-name
    └── share
        └── openmediavault
            ├── confdb
            │   └── create.d
            │       └── conf.system.network.PLUGINNAME.sh
            ├── datamodels
            │   └── conf.system.network.PLUGINNAME.json
            ├── engined
            │   ├── inc
            │   │   └── PLUGINNAME.inc  # LogFileSpec
            │   ├── module
            │   │   └── PLUGINNAME.inc
            │   └── rpc
            │       └── PLUGINNAME.inc
            ├── locale
            │   ├── openmediavault-PLUGINNAME.pot
            │   ├── pl
            │   │   └── openmediavault-PLUGINNAME.po
            │   └── pl_PL
            │       └── openmediavault-PLUGINNAME.po
            └── workbench
                ├── component.d
                │   ├── omv-network-PLUGINNAME-form-page.yaml
                │   ├── omv-network-PLUGINNAME-navigation-page.yaml
                │   └── omv-network-PLUGINNAME-noip-form-page.yaml
                ├── log.d
                │   └── PLUGINNAME.yaml
                ├── navigation.d
                │   └── network.PLUGINNAME.yaml
                └── route.d
                    └── network.PLUGINNAME.yaml


```

## Files

### rpc

 `` PLUGINNAME.inc ``
 
```php 
<?php

#SET NAME filetypePluginame example - ServicesExample
class ServicesExample extends \OMV\Rpc\ServiceAbstract {

  #SET NAME filetypePluginame example - ServicesExample
	public function getName() {
		return "NAME";
	}
  
  
  #Register Method to use function
	public function initialize() {
        $this->registerMethod('getSettings');
        $this->registerMethod('setSettings');
	}
}
?>
```

### debian

``changelog``

``control`` - Set name and author plugin

``postinst`` - Creating a database, directories, and installing the necessary libraries you need

``postrm`` - Code used when uninstalling a plugin

### workbench

## Datatable Example
```yaml
version: "1.0"
type: component
data:
  name: omv-services-example-file-form-page
  type: datatablePage
  config:
    autoReload: false
    hasSearchField: true
    rowId: name
    sorters:
      - dir: asc
        prop: name
    store:
      proxy:
        service: Example
        get:
          method: getExampleList  //GET ROWS FROM rpc
    columns:
      - name: " "
        prop: image
        flexGrow: 0.15
        cellTemplateName: image
        cellTemplateConfig:
          class: "mat-icon notranslate mat-icon-no-color"
          alt: " "
          src: "{{ image }}"
      - name: _("Name")
        prop: name
        flexGrow: 1
        sortable: true
    actions:
      - type: iconButton
        icon: mdi:plus-box
        tooltip: _("Add example file")
        enabledConstraints:
          minSelected: 1
          maxSelected: 1
        execute:
          type: formDialog
          formDialog:
            title: _("Add...")
            fields:
              - type: textInput
                name: name
                label: _("Name")
                value: "{{ _selected[0].name }}"
              - type: textInput
                name: description
                label: _("Description")
                value: ""
            buttons:
              submit:
                text: _("Add")
                execute:
                  type: request
                  request:
                    service: Example
                    method: setExample
                    progressMessage: _("Adding an example  ...")
                    successNotification: _("Example has been added.")
                    successUrl: /services/example/files
```

## Form
 - NO INFORMATION

## Database write and read
 - NO INFORMATION

## Bash executables
 - NO INFORMATION

## Generating the deb file and installing

```shell
cd openmediavault-pluginame
dpkg-buildpackage -us -uc
```

``Install``

```shell
dpkg -i openmediavault-pluginname_VERSION_all.deb
```