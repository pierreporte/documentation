Otter Browser Documentation
===========================

This is the source of the documentation for [Otter Browser](http://otter-browser.org). It is managed by [Sphinx](http://www.sphinx-doc.org). The theme used is the same as [Read the Docs](https://readthedocs.org/).

All pages are simple reStructuredText files stored in the `/source` directory and its sub-directories. The internationalisation files are PO files stored in the `/source/locale/<lang>` directory (where `<lang>` is the language identifier) and have the same structure as the reStructuredText files.

Build the documentation
-----------------------

To build the documentation, move to the root directory (it contains the makefile) and execute this command:

    make html

The files are generated into the `/build/html` directory.

This simple command builds the documentation with the default langage (here, English). To build the different version for each language, follow the procedure described below.

Internationalisation
--------------------

Basically everything is described in the [*Internationalization*](http://www.sphinx-doc.org/en/stable/intl.html) page of the Sphinx documentation. You need to install sphinx-intl available *via* `pip install sphinx-intl` that provides the `sphinx-intl` commmand.

The first step is to generate the templates for the translation files (POT files) with this command:

    make gettext

The POT files are located in the `/build/locale` directory. This has to be done when the original text is updated.

The second step is to generate or update the PO files from the POT files, one set for each language. Run this command:

    sphinx-intl update -p build/locale -l <lang>

`<lang>` is the selected language. You can specify an arbitrary number of languages: `-l fr -l de -l pl ...`. The PO files will contains the translation. See the section below for details.

To build the translated version of the documentation, the following command must be used:

    make -e SPHINXOPTS="-D language='<lang>'" html

Only one language can be specified. The files will be generated in the `/build/html` directory and will replace the original ones.

PO files translation
--------------------

The PO files containes multiple

    #: ../../page.rst:42
    msgid ""
    "These are the built-in Sphinx builders. More builders can be added by "
    ":ref:`extensions <extensions>`."
    msgstr ""

The line `#: ../../page.rst:42` indicades which file is translated and the line number where the text to be translated is located. Follows the `msgid` keyword followed by the text to be translated (may be broken on multiple strings, one per line). The translation is located after the `msgstr` keyword, in strings as well (it is not mandatory to keep the same format as the original). **Note that reStructuredText syntax *MUST* be preserved!** PO files editors are often helpful on this point.