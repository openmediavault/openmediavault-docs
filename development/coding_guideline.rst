Coding Guideline
################

These standards for code formatting and documentation must be followed by
anyone contributing to the |omv| project. Any contributions that do not
fullfill these guidelines will not be accepted.

File Formatting
---------------

Indentation
    Use 4 space tabs for writing your code. If you are modifying someone
    else's code, try to keep the coding style similar.

Line Length
    Lines shouldn't be longer than 80 characters.

Line Endings
    Line endings should be Unix-style LF.

Encoding
    Files should be saved with UTF-8 encoding.

Naming Conventions
------------------

Classes
    PHP classes should use the OMV namespace.

    .. code-block:: php

        namespace OMV\System;

        /**
         * @ingroup api
         */
        class Process {
        	use \OMV\DebugTrait;
            ...

Functions/Methods
    Functions/Methods must use camel case syntax, this convention capitalizes
    the first character of each word except the first one.

    .. code-block:: php

        public function getGecos() {
        ...
        }

        public function getHomeDirectory() {
        ...
        }

Variables
    Variables must use camel case syntax, this convention capitalizes the
    first character of each word except the first one.

    .. code-block:: php

        $fsName
        $outputFileName

Constants
    Constants should start with OMV\_ and should be all upper case.

    .. code-block:: php

        $OMV_DEFAULT_FILE = "/etc/default/openmediavault";
        $OMV_JSONSCHEMA_SORTFIELD = '"type":["string","null"]';

Multiline parameters
--------------------

Functions with many parameters may need to be split onto several lines to keep
the 80 characters/line limit. The first parameters may be put onto the same
line as the function name if there is enough space. Subsequent parameters on
following lines are to be indented using 1 tab.

.. code-block:: php

    throw new OMVException(OMVErrorMsg::E_EXEC_FAILED,
        $cmd, implode("\n", $output));

    $dispatcher->notify(($data['uuid'] == $GLOBALS['OMV_UUID_UNDEFINED']) ?
        OMV_NOTIFY_CREATE : OMV_NOTIFY_MODIFY,
        "org.openmediavault.system.storage.hdparm", $object);

Control Structures
------------------

.. code-block:: php

    for (i = 0; i < 10; i++) {
        if (foo(i)) {
            bar();
        }
    }

    switch (x) {
    case 'a':
        ...
        break;
    case "b":
        ...
        break;
    default:
        ...
        break;
    }

    if (a) {
        foo();
    } else {
        bar();
    }

    if (TRUE === $result)
        break;

    foreach ($output as $outputk => $outputv) {
        foo();
    }

Comments
--------

Single line comments
    You should use the // comment style to "comment out" code. It may be used
    for commenting sections of code too.
    Single line comments must be indented to the indent level when they are
    used for code documentation.

Block comments
    Block comments should usually be avoided. For descriptions use the //
    comments.

    .. code-block:: php

        // Parse output:
        // shadow:x:42:openmediavault
        // snmp:x:112:
        // sambashare:x:113:
        // openmediavault:x:999:
        // nut:x:114:
        foreach ($output as $outputv) {
            ...
        }

Documentation comments
    Use the `doxygen <http://www.stack.nl/~dimitri/doxygen/commands.html>`_
    syntax where possible.

    .. code-block:: php

        /**
         * Get the filesystem label.
         * @return string The filesystem label, otherwise FALSE.
         */
        public function getLabel() {
            ...
        }

        /**
         * Enumerate all disk devices on the system.
         * @return array An array containing physical disk device objects with
         *   the fields \em devicename, \em devicefile, \em model, \em size,
         *   \em description, \em vendor, \em serialnumber, \em israid and
         *   \em isrootdevice.
         */
        public function enumerateDevices() {
            ...
        }

        /**
         * Enumerate all disk devices on the system. The field \em hdparm will
         * be added to the hard disk objects if there exists additional hard
         * disk parameters (e.g. S.M.A.R.T. or AAM) that can be defined
         * individually per hard disk.
         * @param array data An array containing the following fields:
         *   \em start The index where to start.
         *   \em limit The number of objects to process.
         *   \em sortfield The name of the column used to sort.
         *   \em sortdir The sort direction, ASC or DESC.
         * @return array An array containing the requested objects. The field
         *   \em total contains the total number of objects, \em data contains
         *   the object array. An exception will be thrown in case of an error.
         */
        public function getList($data) {
            ...
        }
