helper-functions (Shell)
########################

|omv| ships with this file :file:`/usr/share/openmediavault/scripts/helper-functions` that contains several POSIX shell functions. To test them just run in terminal::

 $ source /usr/share/openmediavault/scripts/helper-functions

Type ``omv_``, press tab key to autocomplete, this will show all functions and a small description in the name.

**Example 1:** Shared folders objects in the database do not have their complete absolute path, it has to be constructed from the relative directory and the parent filesystem. If we know the shared folder database object <uuid> then::

	$ omv_get_sharedfolder_path 2a8b04de-4e6c-4675-b761-1ddfabde2d2a

Returns::

	/media/dev-disk-by-label-VOLUME1/Videos/Unsorted

**Example 2:** Database nodes need to be created when a plugin is installed and removed when it is purged. This is from omvextras MiniDLNA plugin `postinst file <https://github.com/OpenMediaVault-Plugin-Developers/openmediavault-minidlna/blob/master/debian/postinst>`_ ::

	omv_config_add_node "/config/services" "${SERVICE_XPATH_NAME}"
	omv_config_add_key "${SERVICE_XPATH}" "enable" "0"
	omv_config_add_key "${SERVICE_XPATH}" "name" "MiniDLNA Server on OpenMediaVault"
	omv_config_add_key "${SERVICE_XPATH}" "port" "8200"
	omv_config_add_key "${SERVICE_XPATH}" "strict" "0"
	omv_config_add_key "${SERVICE_XPATH}" "tivo" "0"
	omv_config_add_key "${SERVICE_XPATH}" "rootcontainer" "."
	omv_config_add_node "${SERVICE_XPATH}" "shares"
	omv_config_add_key "${SERVICE_XPATH}" "loglevel" "error"
	omv_config_add_key "${SERVICE_XPATH}" "extraoptions" ""


Notice in the postint file how it sources at the beginning ``helper-functions``.

.. note::
	What each function do and the parameters it accepts is documented in the `helper-functions file <https://github.com/openmediavault/openmediavault/blob/master/deb/openmediavault/usr/share/openmediavault/scripts/helper-functions>`_ .

.. [1] https://stedolan.github.io/jq/manual/v1.5/
