# Otter Browser Documentation

This is the source of the documentation for [Otter Browser](http://otter-browser.org).

[MkDocs](http://mkdocs.org) is used to manage the markdown source files ant to generate static HTML files. The documentation can be browsed online and offline because the links are made to files instead of directories.

All pages are simple markdown files stored in the /docs directory and its sub-directories. The global configuration is stored in the /mkdocs.yml file.

For now, it uses the [Read the Docs](https://readthedocs.org/) theme.

To build the documentation, move to the root directory (it contains mkdocs.yml) and execute this command:

    mkdocs build --clean

The files are generated into the /site directory.
