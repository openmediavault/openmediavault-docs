# Tree files and directory

Type Files:

- FILETYPE 
1.   network
1.   storage
1.   services
1.   usermgmt
1.   diagnostics

..  code-block:: shell

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


Files
-----------

rpc
-----------


 `` PLUGINNAME.inc ``
 

..  code-block:: php
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


debian
-----------

``changelog``
``control`` - Set name and author plugin
``postinst`` - Creating a database, directories, and installing the necessary libraries you need
``postrm`` - Code used when uninstalling a plugin

workbench
-----------

# Datatable

# Form

# Database write and read

# Bash executables

# Generating the deb file and installing

..  code-block:: shell
cd openmediavault-pluginame
dpkg-buildpackage -us -uc


Install
=======

..  code-block:: shell
dpkg -i openmediavault-pluginname_VERSION_all.deb
