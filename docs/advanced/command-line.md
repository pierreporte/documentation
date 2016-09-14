# Command Line

This page describes how to use the command line interface of Otter. The same informations can be obtained on the man page: `man otter-browser`.

## Synopsis

    otter-browser [OPTIONS] [PATH|URL|TERM...]

## Options

* `--profile=PATH` specifies the directory that profile (user data) is kept in. Defaults to ~/.config/otter.
* `--cache=PATH` specifies the directory that cache data is kept in. Defaults to ~/.cache/otter.
* `--session=IDENTIFIER` tries to lead session specified by `IDENTIFIER`.
* `--privatesession` starts private session.
* `--sessionchooser` forces session chooser dialog.
* `--portable` sets profile and cache paths to directories inside the same directory as that of application binary.
* `--readonly` tells application to avoid writing data to disk.
* `--report` prints out diagnostic report and exits application.
* `-h` or `--help` shows the list of supported command line options.
* `-v` or `--version` shows version information.

As a Qt application, Otter also obeys Qt command-line flags, see [the Qt documentation](http://doc.qt.io/qt-5/qguiapplication.html#QGuiApplication) for complete list.
