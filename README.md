# Otter Browser Documentation

This is the source of the documentation for [Otter Browser](http://otter-browser.org).

[MkDocs](http://mkdocs.org) is used to manage the markdown source files ant to generate static HTML files. The documentation can be browsed online and offline because the links are made to files instead of directories.

All pages are simple markdown files stored in the /docs directory and its sub-directories. The global configuration is stored in the /mkdocs.yml file.

It uses a custom theme based on the [Bulma](http://bulma.io/) framework. The CSS is transpiled from SCSS source stored in the /bulma directory.

To build the documentation, move to the root directory (it contains mkdocs.yml) and execute these commands:

    sass --scss ./bulma/bulma.sass --compressed > ./theme/css/bulma.min.css
    mkdocs build --clean

The `sass` command, provided by the SCSS Ruby transpiler, is mandatory only when the SCSS source is modified.
