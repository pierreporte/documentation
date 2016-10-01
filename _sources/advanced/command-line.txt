Command line
============

.. note ::
    This is a copy of the Otter Browser man page, that you can acces by typing this command in a terminal::

        man otter-browser

Synopsis
--------

.. code-block :: none

    otter-browser [OPTIONS] [PATH|URL|TERM...]

Options
-------

.. option :: --profile=PATH

    Specifies the directory that profile (user data) is kept in. Defaults to :file:`~/.config/otter`.

.. option :: --cache=PATH

    Specifies the directory that cache data is kept in. Defaults to :file:`~/.cache/otter`.

.. option :: --session=IDENTIFIER

    Tries to load session specified by ``IDENTIFIER`` .

.. option :: --privatesession

    Starts private session.

.. option :: --sessionchooser

    Forces session chooser dialog.

.. option :: --portable

    Sets profile and cache paths to directories inside the same directory as that of application binary.

.. option :: --readonly

    Tells application to avoid writing data to disk.

.. option :: --report

    Prints out diagnostic report and exits application.

.. option :: -h, --help

    Shows the list of supported command line options.

.. option :: -v, --version

    Shows version information.

.. note::
   As a Qt application, Otter also obeys Qt command-line flags, see `the Qt documentation <http://doc.qt.io/qt-5/qguiapplication.html#QGuiApplication>`_ for complete list.

Files
-----

:file:`~/.config/otter`
    Default directory for configuration data.
:file:`~/.cache/otter`
    Default directory for cache data.
