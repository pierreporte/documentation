#!/usr/bin/env python3

# More flexible replacement for Sphinx Makefile.
# Usage: ./build.py <target> [language]

import sys
from subprocess import call

try:
    target = sys.argv[1].lower()
except IndexError:
    target = None

def build_command(target, build_dir, lang=None):
    base_command = ["sphinx-build", "-b", target, "-aE"]
    directories = ["source", "build/" + build_dir]
    
    if lang:
        lang_opt = ["-D", "language='" + lang + "'"]
        return base_command + lang_opt + directories
    else:
        return base_command + directories


def run_command(args):
    print(" ".join(args))
    call(args)

def show_help():
    print("Please use `" + sys.argv[0] + " <target>' where <target> is one of")
    print("  html    to build HTML files")
    print("  gettext to build POT files")
    print("  intl    to build or update PO files")

if not target or target == "help":
    show_help()

elif target == "html":
    try:
        lang = sys.argv[2]
    except IndexError:
        print("Building HTML files for default locale...")
        run_command(build_command(target, target + "/default"))
    else:
        print("Building HTML output for " + lang + " locale...")
        run_command(build_command(target, target + "/" + lang, lang))

elif target == "gettext":
    print("Generating POT files...")
    run_command(build_command(target, "locale"))

elif target == "intl":
    try:
        languages = sys.argv[2:]
        print(languages)
    except IndexError:
        print("ERROR. You must specify at least one language.")
    else:
        for lang in languages:
            print("Generating PO files for " + lang + "...")
            run_command(["sphinx-intl", "update", "-p", "build/locale", "-l", lang])

else:
    print("Unknown target `" + target + "'.")
    show_help()