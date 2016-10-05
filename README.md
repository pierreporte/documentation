Otter Browser Documentation
===========================

This is the source of the documentation for [Otter Browser](http://otter-browser.org). It is managed by [Sphinx](http://www.sphinx-doc.org). The theme used is the same as [Read the Docs](https://readthedocs.org/).

All pages are simple reStructuredText files stored in the `/source` directory and its sub-directories. The internationalisation files are PO files stored in the `/source/locale/<lang>` directory (where `<lang>` is the language identifier) and have the same structure as the reStructuredText files.

Build the documentation
-----------------------

To build the documentation, move to the root directory (it contains the makefile) and execute this command:

    ./build.py html

The files are generated into the `/build/html/default` directory.

Usually, a Makefile is used with Sphinx documentations. However, we have specific needs, especially for internationalisation, that couldn’t be fully satisfied with the default build system. For this reason, we use a Python scripts that does pretty much the same thing but with the exact behaviour we need.

This simple command builds the documentation with the default langage (here, English). To build the different version for each language, follow the procedure described below.

Internationalisation
--------------------

Basically everything is described in the [*Internationalization*](http://www.sphinx-doc.org/en/stable/intl.html) page of the Sphinx documentation. You need to install sphinx-intl available *via* `pip install sphinx-intl` that provides the `sphinx-intl` commmand.

The first step is to generate the templates for the translation files (POT files) with this command:

    ./build.py gettext

The POT files are located in the `/build/locale` directory. This has to be done when the original text is updated.

The second step is to generate or update the PO files from the POT files, one set for each language. Run this command:

    ./build.py intl <lang>

`<lang>` is the selected language. You can specify an arbitrary number of languages: `./build.py intl fr de pl ...`. The PO files will contains the translation. See the section below for details.

To build the translated version of the documentation, the following command must be used:

    ./build.py html <lang>

Only one language can be specified. The files will be generated in the `/build/html/<lang>` directory.

PO files translation
--------------------

The empty PO files containes multiple lines like this:

    #: ../../page.rst:42
    msgid ""
    "These are the built-in Sphinx builders. More builders can be added by "
    ":ref:`extensions <extensions>`."
    msgstr ""

The line `#: ../../page.rst:42` indicades which file is translated and the line number where the text to be translated is located. Follows the `msgid` keyword followed by the text to be translated (may be broken on multiple strings, one per line). The translation is located after the `msgstr` keyword, in strings as well (it is not mandatory to keep the same format as the original). **Note that reStructuredText syntax *MUST* be preserved!** PO files editors are often helpful on this point.

When the `msgstr` is followed by an empty string (`""`), as it is always when the PO files are newly created, the corresponding text remains in the original language when the translated documentation is build.