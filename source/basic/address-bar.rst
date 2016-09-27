Address bar
===========

The address bar is the central feature of a web browser. Like every other browser, you can enter any URL, with or without specifying the protocol. Pressing :kbd:`Enter` validates the entry. Besides, there are several features worth of explaining in order to use them efficiently.

.. figure :: /_static/address-bar.png

   The empty address bar

URL completion
--------------

The URL completion is the menu appearing when text is entered in the address bar. It helps you to access exactly what you are looking for without having to remember it exactly.

.. figure :: /_static/completion-menu-entered-text.png

   The classical completion menu

The most simple form of completion provided is the text added right after the typed text. To validade the proposition, simply press :kbd:`Enter`. It is useful for frequently visited websites. For example, if you often visit the Otter Browser website, you might want to enter `otter-browser.org <http://otter-browser.org>`_. When typing the first "o", the rest of the address is proposed: :samp:`o{tter-browser.org}`. Entering more letters may correspond to new addresses. For example, if you also visit `omg-otters-are-so-cute.com <http://otters-are-so-cute.com>`_, typing the "m" after the "o" already entered, you will be proposed :samp:`om{g-otters-are-so-cute.com}`. This completion feature allows you to rapidly access you favourite sites just by entering one or two letters.

A more complex yet trivial to use completion is the displayed menu itself. It is divided into 4 sections:

Search with X
    X being the default search engine. Selecting this entry opens the search engine with the entered text as the query.
Bookmarks
    Bookmarks corresponding to the entered text.
History
    History entries corresponding to the entered text
Special pages
    Special pages (about:something) corresponding to the entered text.

.. warning ::
   The completion system considers that the entered text is always the begining of URLs domain name (not the protocol nor the subdomain). It does not seek anywhere else and not in the title of the page.

Bookmark
--------

The star at the right of the address bar indicates wether the current URL is bookmarked or not. When it is grey, it is not and clicking on the star opens a dialog to create a bookmark. When it is yellow, it means that the page is bookmarked.

.. seealso ::

   The :doc:`bookmarks` page.

History
-------

When the addres bar is empty, clicking on the arrow on its left displays the recent history of accessed URLs.

.. figure :: /_static/completion-menu-history.png

   The completion menu with an empty address bar

.. seealso ::

   The :doc:`history` page.

Shortcuts
---------

The shortcuts are a very convenient way to send a query to a search engine without having to use the search field and without having to manually select one with the mouse. To do this, you simply have to enter the keyword corresponding to the desired search engine, then enter a space, and eventually entering the query. For example, let's say you want to search :samp:`{query}` on Google (Google was already set as a search engine with the keyword :samp:`g`), simply enter :samp:`g {query}`.

.. seealso ::

   The :doc:`search-engines` page.

Configuration
-------------

The configuration of the address bar is located in the :guilabel:`Advanced` tab of the :guilabel:`Preferences` window, in the :guilabel:`Browsing` section:

.. figure :: /_static/preferences-window-advanced-tab-browsing.png

   :guilabel:`Preferences` window

The :guilabel:`Address Field Suggestions` section allows you to enable or disable the suggestion of bookmarks, history entries, search results and local files.

The :guilabel:`Address Completion` section allows you to customise the appearance of the completion menu. Below are shown the 4 possible configurations:

.. figure :: /_static/completion-menu-headers-columns.png

   With headers, columns

.. figure :: /_static/completion-menu-headers-compact.png

   With headers, compact

.. figure :: /_static/completion-menu-noheaders-columns.png

   Without headers, columns

.. figure :: /_static/completion-menu-noheaders-compact.png

   Without headers, compact