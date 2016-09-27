Startup configuration
=====================

This page describes how to set the behaviour of Otter at startup. The startup configuration is defined in the :guilabel:`Preferences` window, accessed though :menuselection:`Menu --> Settings --> Preferences...` or by pressing :kbd:`Ctrl+F12`, in the :guilabel:`Startup` section of the :guilabel:`General` tab.

.. figure :: /_static/preferences-window-general-tab.png
   
   :guilabel:`Preferences` window

The :menuselection:`Startup behaviour` drop-down list contains the five possible startup behaviours. They are explained below.

Continue previous session
-------------------------

Otter reopens the same arrangment of tabs that was present the last time the browser was exited.

Show home page
--------------

Otter opens with an URL specified in the :guilabel:`Home page` text entry below the :guilabel:`Startup behaviour` drop-down list.

The URL can be entered directly, or be set to the URL of the current tab with the :guilabel:`Use Current Page` button, or chosen in your bookmarks with the :guilabel:`Use Bookmark` button. The :guilabel:`Restore to Default` Button clears the text entry field.

Show start page
---------------

Otter opens with the :doc:`speed dial <speed-dial>`.

Show empty page
---------------

Otter opens with an empty page.

Show startup dialog
-------------------

Otter doesn't start directly but greets you with the following window:

.. figure :: /_static/startup-dialog.png

   Startup dialog

There are four options available:

:guilabel:`Continue session`
    Allows you to start a saved session with all its windows and tabs.
:guilabel:`Begin with home page`
    Does the same thing as described in the `Show home page`_ section.
:guilabel:`Begin with start page`
    Does the same thing as described in the `Show start page`_ section.
:guilabel:`Begin with blank page`
    Does the same thing as described in the `Show empty page`_ section.

Click on the :guilabel:`Open` button to execute the selected action or :guilabel:`Cancel` to exit.

.. note ::
   When Otter exits unexpectedly, its next start will show this window and you will be abe to restore your previous session even if it was not explicitly saved.