Changelog
=========

.. Added, Changed, Depreciated, Removed, Fixed, Security

- :release:`2.13.2 <2025-11-04>`
- :bug:`-` better handling of TaskNotes, when the (WIP) TaskNote plugin is not
  installed (article listings, article page infobox).
- :support:`27` Note which article metadata keys are acted on.
- :support:`-` Remove "AddThis" support. (The service has been defunct since
  May of 2023.)
- :release:`2.13.1 <2025-11-03>`
- :bug:`-` better handling of TaskNotes, when the (WIP) TaskNote plugin is not
  installed (article page title, article page infobox, TaskNote footer
  display).
- :bug:`42` don't break on valid PEP440 versions (e.g. ``4.11.0.post0``). See
  `AutoLoader Issue #4`_.
- :support:`-` move from ``setup.py`` to ``pyproject``. See
  `AutoLoader Pull Request #2`_.
- :release:`2.13.0 <2025-09-08>`
- :feature:`40` display ``subtitle`` on Article pages.
- :feature:`-` support for *TaskNotes* (``minchin.pelican.readers.tasknotes``)
  plugin for Pelican.
- :release:`2.12.1 <2025-08-24>`
- :bug:`-` review deep list indentation
- :release:`2.12.0 <2025-06-14>`
- :feature:`-` additional CSS to add indicators added by *fancy tasklists*
  v1.2.0 (``e`` (energy), ``o`` (event), 📕 (book), 🏠 (house), 📺 (TV (show)),
  🎥 / 🎬 / 📽 / 🎞 / 🎦 (film / movie), and 🎲 (dice / play)).
- :feature:`17` update Font Awesome to v6.7.2
- :bug:`- major` update Pygments CSS
- :bug"`- major` update LESSC mixin style (for v4.3.0)
- :release:`2.11.0 <2025-06-07>`
- :feature:`4` add explicit monospaced font (Victor Mono). c.f. `Issue #29`_
  re style sets.
- :bug:`16 major` upgrade version of self-hosted fonts. Drop support for
  various old browsers; now requires Chrome 36+, Opera 23+, Firefox 39+, Safari
  12+, or iOS 10+.
- :release:`2.10.3 <2024-10-01>`
- :bug:`-` support `microblogging plugin`_ better.
  Specifically, allow the plugin to control post sort order and hide appended
  tags on the index page. Requires v1.3.0 or newer of the plugin.
- :release:`2.10.2 <2024-04-07>`
- :bug:`-` Fix indents around complex (compound) tasklists.
- :release:`2.10.1 <2024-04-07>`
- :bug:`-` additional CSS to add indicators added by *fancy tasklists* v1.1.0
  (💒 (church), and 🦷 (tooth)).
- :support:`- minor` better support for testing fancy tasklists. 
- :release:`2.10.0 <2024-03-30>`
- :feature:`-` add support for fancy tasklists/checkboxes.
- :bug:`- major` fix last paragraph spacing within lists
- :feature:`17` Upgrade Font Awesome (icons) from v4 to v6.5.1. Includes a shim
  for v4 compatibility, so no existing icons in use should need to be renamed.
  It appears that some (all?) of the icons have been re-drawn, so they may
  appear slightly different.
- :release:`2.9.2 <2024-03-04>`
- :support:`- minor` remove ``respond.js``. This was initially added to support
  Internet Explorer 6 to 8, which have since faded away. Plus it was throwing
  an Javascript error.
- :bug:`-` fix missing icons (micropost category next link) and icon spacing
  (readtime and tags in article details).
- :release:`2.9.1 <2023-07-15>`
- :support:`- minor` convert indentation to spaces
- :bug:`-` better display of micropost links
- :release:`2.9.0 <2023-07-14>`
- :feature:`-` add support for *microblogging*, through my `microblogging
  plugin`_. c.f. `blog.minchin.ca Issue #105`_.
- :bug:`- major` no longer capitalize category names, when displayed on
  sidebar. This is part of the changes to support microblogging.
- :bug:`- major` review ``og`` meta tags, particularly for featured images.
  c.f. `blog.minchin.ca Issue #104`_.
- :release:`2.8.1 <2023-06-11>`
- :bug:`-` fix link to font files
- :release:`2.8.0 <2023-06-11>`
- :feature:`20` add support for Google Analytics v4. Use
  ``GOOGLE_ANALYTICS_V4``. The previous version of Google Analytics is being
  deprecated (by Google), effective the end of June 2023.
- :feature:`-` add ``DISPLAY_ARCHIVES_ON_MENU`` to control display of
  "Archives" link on navbar.
- :feature:`-` add header image to pages (not just articles).
- :feature:`-` add *strathcona* colour scheme/theme, and supporting fonts.
- :bug:`- major` adjust supported Python versions to only include those
  currently supported upstream. Nothing has been removed that should keep older
  versions from working.
- :bug:`16 major` upgrade version of self-hosted fonts.
- :release:`2.7.1 <2022-04-30>`
- :bug:`-` fix typo in comment form.
- :support:`-` replace references to ``pelican-comment-system`` with the
  updated `Static Comments
  <https://blog.minchin.ca/2022/04/static-comments-211-released.html>`_ plugin.
- :support:`-` bump to ``minchin.releaser`` 0.8.2, and thus officially support
  Python 3.10.
- :release:`2.7.0 <2021-10-25>`
- :bug:`- major` in ``SEAFOAM_DEV_MODE``, assume that the *Image Process*
  plugin might still be active (and so supply no-op transformations rather than
  no configuration).
- :feature:`-` under "related posts", link to the category page, if applicable.
- :feature:`-` add ``TAGS_TEXT`` to customize tag label.
- :bug:`- major` have ``SEAFOAM_URL`` return the project URL.
- :feature:`-` add ``SEAFOAM_DEV_MODE`` to turn off the *image process* plugin.
- :release:`2.6.0 <2021-07-05>`
- :support:`1` add screenshots. Also `Issue #18`_.
- :feature:`-` include *seafoam* version in source HTML of generated sites
- :support:`-` updated ``setup.py``. Include tempalate and static files at new
  location.
- :support:`-` no longer include raw LESS files in distributions or in
  generated sites.
- :support:`-` now also requires ``beautifulsoup4`` and ``semantic_version``
- :bug:`- major` adjust HTML to add the ``.table`` class where needed, rather
  than applying the formatting to all HTML tables. Effectively a re-work of
  v2.4.7.
- :feature:`-` add internal plugin. This will allow the theme to automatically
  configure and activate itself. Should significantly reduced installation
  complexity. You may be able to completely remove the configuration you have
  in place for the plugin; see the release blog post for details.
- :release:`2.5.0 <2021-05-15>`
- :feature:`-` add stylized period archive pages.
- :bug:`-` fix 404 page layout issues and typos.
- :support:`-` upgrades from ``minchin.pelican.jinja-filters`` to
  ``pelican-jinja-filters`` (It's the same plugin, just under a new name on
  PyPI and packaged as a namespace plugin for Pelican 4.5 or newer.)
- :support:`-` upgrades from ``minchin.pelican.plugins.image-process`` to
  ``pelican-image-process`` (It's the same plugin, just under a new name on
  PyPI and packaged as a namespace plugin for Pelican 4.5 or newer.)
- :release:`2.4.7 <2021-04-17>`
- :bug:`-` apply table formatting without requiring the ``.table`` class
- :release:`2.4.6 <2020-07-18>`
- :bug:`-` add a new non-breaking spaces to help flow of article details on
  blog index.
- :release:`2.4.5 <2020-07-16>`
- :bug:`-` have bullet points list separators go to the next line.
- :bug:`-` only display comment count if there are comments.
- :release:`2.4.4 <2020-06-26>`
- :bug:`16` use local version of fonts.
- :release:`2.4.3 <2019-09-02>`
- :bug:`-` upgrade Tipue Search to version 7.1, and update templates to match.
- :release:`2.4.2 <2019-09-02>`
- :bug:`-` limit width of images on index pages to 100%.
- :release:`2.4.1 <2018-10-25>`
- :bug:`-` adjust 404 page text.
- :release:`2.4.0 <2018-02-03>`
- :bug:`- major` Make the output HTML a little cleaner.
- :support:`-` edit some JS and CSS links to explicitly note the version of the
  library being loaded. This should make both cache-ing and library upgrading a
  little simpler.
- :feature:`-` various CSS additions to support Gigatrees 4.4.1 (genealogy site
  generator).
- :support:`-` upgrade to ``respond.js`` v1.4.2.
- :feature:`-` add ability to add Javascript to ``<head>`` with
  ``CUSTOM_JS_LIST_HEAD``, which is designed to work very similar to
  ``CUSTOM_JS_LIST``.
- :feature:`-` add ``JQUERY_JS_IN_HEAD`` to move loading JQuery from the end of
  the page to the head section.
- :feature:`-` support local and absolute URLs for ``CUSTOM_CSS_LIST`` and
  ``CUSTOM_JS_LIST``, and scripts directly for ``CUSTOM_JS_LIST``.
- :release:`2.3.4 <2018-01-18>`
- :bug:`-` Add instructions on how to use the *404 Error* page.
- :release:`2.3.3 <2018-01-18>`
- :bug:`-` make *Archives* link work better with vertical menu and with
  sub-sites.
- :release:`2.3.2 <2017-12-08>`
- :bug:`-` fix styling of main text body when using vertical menu.
- :release:`2.3.1 <2017-11-30>`
- :bug:`-` fix styling of breadcrumbs on article pages.
- :bug:`-` fix styling of pager on search results.
- :release:`2.3.0 <2017-11-29>`
- :feature:`-` add basic support for Tuque Search plugin.
- :bug:`- major` fix issues with navbar coloring, navbar brand text + logo
  layout, and sidebar alignment.
- :feature:`-` added support for `prjct`_.
- :release:`2.2.1 <2017-11-13>`
- :bug:`-` fix reference to ``python-dateutil`` in project metadata
- :release:`2.2.0 <2017-11-13>`
- :feature:`-` include prjct template
- :feature:`15` include 404 template
- :feature:`-` use ``NAVBAR_ON_TOP`` to move the menu from the left side of the
  page to the top (Bootstrap default)
- :bug:`- major` respect Pelican's ``THEME_STATIC_DIR`` setting
- :support:`-` use ``minchin.releaser`` to put out releases
- :release:`2.1.5 <2017-05-31>`
- :bug:`11` indent definition list items
- :bug:`-` note that Image Processing v1.1.2 is broken (see their
  `Issue #2
  <https://github.com/MinchinWeb/minchin.pelican.plugins.image_process/issues/2>`_)
- :release:`2.1.4 <2017-04-09>`
- :bug:`-` ``Framework :: Pelican :: Themes`` trove classifier on PyPI now
  available.
- :release:`2.1.3 <2017-03-19>`
- :support:`2 (==2.1.3)` document most theme options
- :release:`2.1.2 <2017-03-08>`
- :bug:`-` provide universal wheels. On versions of Python before 3.4 (when the
  ``pathlib`` module was added to the standard library), we now depend on
  `pathlib2`_.
- :bug:`-` provide an absolute path.
- :release:`2.1.1 <2017-03-08>`
- :bug:`-` fix pagination links on category and tag pages. See
  `blog.minchin.ca Issue #6`_.
- :bug:`13` remove unused code in pagination template. Thanks
  `@jorgesumle`_!
- :release:`2.1.0 <2017-02-20>`
- :feature:`-` add support for `readtime`_ plugin in preference to the
  ``post-stats`` plugin to get article reading time. The former is available on
  PyPI (as ``pelican-readtime``), while the latter is not.
- :support:`2` document optionally supported plugins
- :release:`2.0.4 <2017-01-11>`
- :bug:`10` fix archive page template code to work with Jinja2 v2.9.0
- :release:`2.0.3 <2017-01-11>`
- :bug:`-` fix link colour in body area of panel-primary (fixes regression
  from version 2.0.2)
- :release:`2.0.2 <2017-01-11>`
- :bug:`-` fix link colour on panel-primary
- :bug:`-` improve layout of generated HTML
- :release:`2.0.1 <2017-01-10>`
- :bug:`8` pluralization of "1 comment" now correct
- :bug:`9` fix pagination template code to work with Jinja2 v2.9.0
- :release:`2.0.0 <2017-01-09>`
- :feature:`-` add Seafoam logo
- :support:`-` [BREAKING] rename from
  ``minchin.pelican.themes.minchindotca`` to ``seafoam``
- :feature:`-` add support for reading time via `post stats`_ plugin
- :bug:`6 major` restyle comments with bootstrap's ``media`` class (much
  cleaner template code)
- :feature:`-` add support for `pelican comment system`_
- :feature:`-` upgrade to FontAwesome 4.7.0
- :feature:`-` upgrade to jQuery 3.1.0
- :bug:`5 major` switch template variable from ``PAGES`` to ``pages`` to
  support Pelican v3.7 
- :feature:`-` switch to ``minchin.pelican.jinja_filters`` to provide
  the required Jinja filters, rather than requiring them to be manually
  added to the user's configuration file
- :bug:`-` don't print section for next and previous posts in a category if
  the article is the only one in that category
- :feature:`-` add support for Pelican Blog System
- :release:`1.1.0 <2016-09-12>`
- :feature:`-` include (thumbnail of) featured image on article listing
- :support:`-` start documentation with the changelog (this file)
- :bug:`-` Better handling for copyright and modified dates in ``footer.html``
- :feature:`-` add breadcrumbs to main blog post listing page
- :support:`-` add release machinery
- :release:`1.0.0 <2016-08-15>`
- :feature:`-` add ``setup.py``, ``README.rst``, ``CHANGELOG.rst``.
- :support:`-` move package to ``minchin.pelican.themes.minchindotca``
- :support:`-` pull code out of main Minchin.ca website repo


.. _Issue #18: https://github.com/minchinweb/seafoam/issues/18
.. _Issue #29: https://github.com/minchinweb/seafoam/issues/29

.. _AutoLoader Pull Request #2: https://github.com/minchinweb/minchin.pelican.plugins.autoloader/pull/2
.. _AutoLoader Issue #4: https://github.com/minchinweb/minchin.pelican.plugins.autoloader/issues/4

.. _blog.minchin.ca Issue #6: https://github.com/MinchinWeb/blog.minchin.ca/issues/6
.. _blog.minchin.ca Issue #104: https://github.com/MinchinWeb/blog.minchin.ca/issues/104
.. _blog.minchin.ca Issue #105: https://github.com/MinchinWeb/blog.minchin.ca/issues/105

.. _CName Issue #153: https://github.com/minchinweb/minchin.pelican.plugins.cname/issues/153

.. _microblogging plugin: https://blog.minchin.ca/label/microblogging-pelican/
.. _pelican comment system: https://github.com/getpelican/pelican-plugins/tree/master/pelican_comment_system
.. _post stats: https://github.com/getpelican/pelican-plugins/tree/master/post_stats
.. _prjct: https://github.com/MinchinWeb/prjct
.. _pathlib2: https://pypi.python.org/pypi/pathlib2
.. _readtime: https://pypi.python.org/pypi/pelican-readtime
.. _@jorgesumle: https://github.com/jorgesumle
