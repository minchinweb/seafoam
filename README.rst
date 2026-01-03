=======
Seafoam
=======

.. image:: https://raw.githubusercontent.com/MinchinWeb/seafoam/master/docs/seafoam-logo-4x.png
    :align: center
    :alt: Seafoam Logo

``Seafoam`` is a theme for `Pelican <http://docs.getpelican.com/>`_,
a static site generator written in Python.

.. image:: https://img.shields.io/pypi/v/seafoam.svg?style=flat
    :target: https://pypi.python.org/pypi/seafoam/
    :alt: PyPI version number

.. image:: https://img.shields.io/badge/-Changelog-success
    :target: https://github.com/MinchinWeb/seafoam/blob/master/docs/changelog.rst
    :alt: Changelog

.. image:: https://img.shields.io/pypi/pyversions/seafoam?style=flat
    :target: https://pypi.python.org/pypi/seafoam/
    :alt: Supported Python version

.. image:: https://img.shields.io/pypi/l/seafoam.svg?style=flat&color=green
    :target: https://github.com/MinchinWeb/seafoam/blob/master/LICENSE.txt
    :alt: License

.. image:: https://img.shields.io/pypi/dm/seafoam.svg?style=flat
    :target: https://pypi.python.org/pypi/seafoam/
    :alt: Download Count


The ``seafoam`` theme is based on Bootstrap 3, and was first used at
`Minchin.ca <http://minchin.ca>`_. 

.. image:: https://github.com/MinchinWeb/seafoam/raw/master/docs/screenshots/2.6.0/front_page.png
    :align: center
    :alt: Front Page


Installation
------------

The easiest way to install the ``seafoam`` theme is through the use
of pip. This will also install the required dependencies automatically.

.. code-block:: sh

  pip install seafoam

Alternatively, you can force the installation of ``lxml``, which is a HTML
parser that is often faster than the default, and will be used if installed:

.. code-block:: sh

  pip install seafoam[lxml]

If you are using Pelican v4.5 or newer and only namespace plugins, ``seafoam``
is set up as a namespace plugin and will automatically activate and configure
itself.

If you are using a version of Pelican older that v4.5 or non-namespace plugins,
you will need to add ``seafoam`` to your list of plugins:

.. code-block:: python

  # pelicanconf.py

  PLUGINS = [
      "pelican.plugins.seafoam",
      # others, as desired...
  ]

  # the rest of the your configuration file...


You may also need to configure the theme through the use of additional settings
(see below).


Requirements
------------

``Seafoam`` requires Pelican, the ``image_process`` plugin, the
``jinja filters`` plugin, ``beautifulsoup4``, and ``packaging``. If the
theme is installed from pip, these should be automatically installed. If
needed, they can be manually installed with pip:

.. code-block:: sh

   pip install pelican
   pip install pelican-image-process
   pip install pelican-jinja-filters
   pip install beautifulsoup4
   pip install packaging


Supported Plugins
-----------------

Seafoam also works with several other plugins for Pelican, but none of those
listed in this section are required.

- `microblogging <https://blog.minchin.ca/label/microblogging-pelican/>`_ --
  adds the ability to have "microposts", and tweaks the formatting of the theme
  based on their (assumed) shorter length.
- `readtime <https://pypi.python.org/pypi/pelican-readtime>`_ -- provides
  estimated reading time for articles. Available from PyPI as
  ``pelican-readtime``.
- `post-stats
  <https://github.com/getpelican/pelican-plugins/tree/master/post_stats>`_ --
  provides estimated reading time for articles if ``readtime`` is not available.
  Available in the `Pelican Plugins collection
  <https://github.com/getpelican/pelican-plugins/>`_.
- `neighbors <https://pypi.python.org/pypi/pelican-neighbors>`_ -- provides
  post-article links to the next and previous article on your blog and the
  next and previous article in that category. Available on PyPI as
  ``pelican-neighours``.
- `static-comments <https://blog.minchin.ca/label/static-comments/>`_ (or the
  older `pelican_comment_system
  <https://bernhard.scheirle.de/posts/2014/March/29/static-comments-via-email/>`_)
  -- add static comments to your blog. Available on PyPI as
  ``minchin.pelican.plugins.static-comments``.
- `Related Posts
  <https://github.com/getpelican/pelican-plugins/tree/master/related_posts>`_ --
  adds the ``related_posts`` variable to the article's context.
- Tipue Search
- `Fancy Tasklists (Checkboxes)
  <https://github.com/MinchinWeb/minchin.md-it.fancy-tasklists>`_ -- this
  extends the (CommonMark) Markdown checkboxes to display a number of icons
  instead.

It also replaces the functions of the following:

- `pelican-redirect-url
  <https://github.com/FriedrichFroebel/pelican-redirect-url>`_ -- this is more
  properly implemented as a theme extention, and so was directly added to
  ``seafoam``. It uses the same metadata key: ``redirect_url``.


Additional Images
-----------------

Article with header image

.. image:: https://github.com/MinchinWeb/seafoam/raw/master/docs/screenshots/2.6.0/article_with_header.png
    :align: center
    :alt: Article with Header Image

Main article body

.. image:: https://github.com/MinchinWeb/seafoam/raw/master/docs/screenshots/2.6.0/article_body.png
    :align: center
    :alt: Article Body
    
Comments
    
.. image:: https://github.com/MinchinWeb/seafoam/raw/master/docs/screenshots/2.6.0/comments.png
    :align: center
    :alt: Comments

Comment Form

.. image:: https://github.com/MinchinWeb/seafoam/raw/master/docs/screenshots/2.6.0/comment_form.png
    :align: center
    :alt: Comment Form

Main Archives

.. image:: https://github.com/MinchinWeb/seafoam/raw/master/docs/screenshots/2.6.0/archives.png
    :align: center
    :alt: Main Archives

Yearly Archives

.. image:: https://github.com/MinchinWeb/seafoam/raw/master/docs/screenshots/2.6.0/archives-year.png
    :align: center
    :alt: Yearly Archives

Monthly Archives

.. image:: https://github.com/MinchinWeb/seafoam/raw/master/docs/screenshots/2.6.0/archives-month.png
    :align: center
    :alt: Monthly Archives

404 Error Page

.. image:: https://github.com/MinchinWeb/seafoam/raw/master/docs/screenshots/2.6.0/404.png
    :align: center
    :alt: 404 Error

Fancy Checkboxes / Tasklist

.. image:: https://github.com/MinchinWeb/seafoam/raw/master/docs/screenshots/2.10.0/fancy-checkboxes.png
    :align: center
    :alt: 404 Error

.. add microblog post image

.. add Strathcona theme image

.. _pelican-settings:

Additional Settings
-------------------

These settings can be set in your ``pelicanconf.py`` file (your Pelican settings
file) to alter the behavior of the theme.

If a value is given below, this represents the effective default value. If no
value is given, the effective default value is ``None``.

If you are using this theme on a sub-site (i.e a directory of the "main site"),
look at ``MENUITEMS_2``, ``MENUITEMS_2_AT``, and ``MENUITEMS_2_AT_LINK``
settings.

If you are using this theme on a subdomain, look at the ``SITE_ROOT_URL``
setting.

If you want to disable *Image Process* for local development, see
``SEAFOAM_DEV_MODE``.

Seafoam also auto-configures itself when possible.  If you need to manually
create the default configuration, you would need the following:

.. code-block:: python

  # pelicanconf.py

  from pelican.plugins import seafoam

  THEME = seafoam.get_path()
  BOOTSTRAP_THEME = "seafoam"

  # if PLUGINS is not defined on Pelican 4.5+, these plugins will autoload
  PLUGINS = [
      "pelican.plugins.seafoam",
      "pelican.plugins.jinja_filters",
      "pelican.plugins.image_process",
      # others, as desired...
  ]

  IMAGE_PROCESS = {
    "article-feature": ["scale_in 848 848 True"],
    "index-feature": ["scale_in 263 263 True"],
  }

  # Generate 404 error page
  TEMPLATE_PAGES = {
      "404.html": "404.htm"',
  }

  # the rest of the your configuration file...

There are also a number of per-article (and per-page) metadata fields that can
be set influence how an article (or page) is processed and displayed. Please
review `those options below <#article-metadata>`_.

This documentation has to be manually updated. If the settings no longer match
the theme's behavior, or a setting is missing from here, please open a ticket
on `GitHub <https://github.com/MinchinWeb/seafoam/issues>`_.

.. use the ".. data::" directive here for Sphinx output, but on GitHub, that just causes everything to disappear

ABOUT_ME
  You can show a short blurb of text about yourself and a picture. This setting
  is the paragraph. Raw HTML is accepted. See the ``AVATAR`` setting to set the
  picture.
ADAM
  These ADAM settings were originally set up to support my genealogy sub-site
  (the original name of the the pre-processor I was using as called "Adam"). If
  this is set to ``False``, the rest of the ``ADAM_*`` settings won't be active.
  These settings are probably generic enough that you could use these for any
  generator or outside program used to help generate your site.
ADAM_COPY_DATE
  Override the copyright date in the footer. (Provide a string).
ADAM_FOOTER
  An extra "page footer" to apply to all pages. (Provide an HTML string.)
ADAM_LINK
  Link target for the Adam version text.
ADAM_UPDATED
  Override the updated date.
ADAM_VERSION
  Reported name and version of "Adam". 
ARCHIVES_URL
  Same as the regular Pelican setting.
ASSET_CSS
  Set to ``True`` if you want the ``asset`` plugin to compile your CSS.
ASSET_JS
  Set to ``True`` if you want the ``asset`` plugin to compile your Javascript.
AUTHOR
  Who to list as the copyright belonging to in the site footer.
AUTHORS_URL
  Same as the regular Pelican setting.
AVATAR
  You can show a short blurb of text about yourself and a picture. This setting
  is the path to the picture. See the ``ABOUT_ME`` setting to set the
  descriptive paragraph.
BOOTSTRAP_NAVBAR_INVERSE = False
  Apply inverse CSS setting to Navbar. Changing this will swap the top
  navigation bar between light and dark.
BOOTSTRAP_THEME = "seafoam"
  Use this to set the "colour scheme" of the framework. Valid values are
  ``seafoam`` and ``strathcona``. ``seafoam`` teal on darker green;
  ``strathcona`` is maroon on white. This is a Automatically set to ``seafoam``
  by the internal plugin if unspecified. Other values (including leaving this
  unset) are not expected to work correctly.
CATEGORIES_URL
  Same as the regular Pelican setting.
CATEGORY_IMAGES = {}
  Provide a default featured image by category. If an image is set in the
  article metadata, that will override this.

  Provide a dictionary where the key is the category name and the value is the
  path of the image, relative to the SITEURL.
CC_ATTR_MARKUP
  Optionally, you can include attribution markup in the CC license mark by
  setting this to ``True``.
CC_LICENSE
  Set a site-wide Creative Commons License by specify the "short name" of the
  license (like ``CC_BY``, or ``CC-BY-NC-ND``). Alternately, use
  ``CC_LICENSE_COMMERCIAL`` and ``CC_LICENSE_DERIVATIVES`` to "build a
  license".
CC_LICENSE_COMMERCIAL
  "yes" if commercial use is permitted, "no" otherwise. Use this in lieu of
  ``CC_LICENSE`` and in combination with ``CC_LICENSE_DERIVATIVES`` to "build a
  license".
CC_LICENSE_DERIVATIVES
  "yes" is derivatives are permitted, "no" otherwise. Use this in lieu of
  ``CC_LICENSE`` and in combination with ``CC_LICENSE_COMMERCIAL`` to "build a
  license".
CUSTOM_CSS
  Link, relative to SITEURL, to a custom CSS file.
CUSTOM_CSS_LIST = []
  Custom CSS to load; can be either absolute links, or relative links. If the
  listed item starts with ``//``, ``http://``, ``https://``, it is assumed to
  be absolute link and added as-is to the markup. Otherwise, the link is
  assumed to be relative to SITEURL.
CUSTOM_JS_LIST = []
  Custom Javascript to load; can be either scripts, absolute links, or relative
  links. If the listed item starts with ``<script``, then the item is assumed
  to be the contents of a script, including opening and closing tags, and so
  added to the pages' markup directly. If the listed item starts with ``//``,
  ``http://``, ``https://``, it is assumed to be absolute link and added as-is
  to the markup. Otherwise, the link is assumed to be relative to SITEURL.

  See also ``CUSTOM_JS_LIST_HEAD`` and ``JQUERY_JS_IN_HEAD``.
CUSTOM_JS_LIST_HEAD = []
  Exactly the same format as ``CUSTOM_JS_LIST``, but is added to the pages'
  ``<head>`` section rather than the end of the page. Generally, you will want
  to put your Javascript at the end of the page (i.e. in ``CUSTOM_JS_LIST``
  rather than here), as any Javascript referenced here must generally be
  completely loaded before the page will start being rendered.
  
  When ``JQUERY_JS_IN_HEAD == True`` (not the default), JQuery is listed before
  the other scripts listed here.
  
  See also ``CUSTOM_JS_LIST`` and ``JQUERY_JS_IN_HEAD``.
DEFAULT_LANG
  Used by Disqus to set the default display language.
DISPLAY_ARCHIVES_ON_MENU = True
  Include archives on the main site menu.
DISPLAY_BREADCRUMBS = False
  Display Breadcrumbs on site.

  See also ``MENUITEMS_2_AT`` and ``MENUITEMS_2_AT_LINK`` settings.
DISPLAY_ARTICLE_INFO_ON_INDEX
  Display the "article info" box (ususally found on the article pages) on the
  "Articles" listing page as well. (*Unconfirmed if working*)
DISPLAY_CATEGORIES_ON_MENU
  Include categories on the main site menu.
DISPLAY_CATEGORIES_ON_SIDEBAR
  Include a listing of categories on the sidebar (assuming the sidebar is
  active; see ``HIDE_SIDEBAR`` setting)
DISPLAY_PAGES_ON_MENU
  Include a listing of pages on the sidebar (assuming the sidebar is active;
  see ``HIDE_SIDEBAR`` setting)
DISPLAY_RECENT_POSTS_ON_SIDEBAR
  Include a listing of recent posts on the sidebar (assuming the sidebar is
  active; see ``HIDE_SIDEBAR`` setting). Also see the ``RECENT_POST_COUNT``
  setting.
DISPLAY_TAGS_INLINE
  .
DISPLAY_TAGS_ON_SIDEBAR = True
  Include a listing of tags on the sidebar (assuming the sidebar is active;
  see ``HIDE_SIDEBAR`` setting)
DISQUS_DISPLAY_COUNTS
  Display the number of comments (assuming Disqus comments are active; see
  ``DISQUS_SITENAME`` settings)
DISQUS_ID_PREFIX_SLUG
  Set this to ``True`` if you have configured your article URLs such that the
  slug alone will likely not be unique. Ignored if ``DISQUS_NO_ID`` is ``True``.
DISQUS_NO_ID
  This theme sets identifiers for each article's comment threads. If you are
  switching from a theme that doesn't (such as the Pelican built-in default)
  this will result in existing comments getting lost. To prevent this, set
  this setting to ``True``.
DISQUS_SITENAME
  Set to your Disqus sitename to activate Disqus comments on your site.

  You can also enable Disqus comments for pages. This is a per-page setting you
  can control by adding a field comments to you pages' metadata. Set it to
  enabled to enable comments for that page. Comment-threads for pages will have
  an id that is prefixed by ``page-``.

  You will probably only use this or the Pelican Comment System; odd results
  may come if you try to use both together. See the ``PELICAN_COMMENT_SYSTEM``
  setting.

  See also ``DEFAULT_LANG``.
DOCUTIL_CSS
  If you're using reStructuredText for writing articles and pages, you can
  include the extra CSS styles that are used by the docutils-generated HTML by
  setting this to ``True``. This can be done as a global setting or setting it
  in the metadata of a specific article or page.
FAVICON
  The location of your site's FavIcon, relative to the SITEURL.
FEED_ALL_ATOM
  Same as the regular Pelican setting. If set, a link to your Atom feed will
  appear in the site's HTML header and as a link in the footer of the site.
FEED_ALL_RSS
  Same as the regular Pelican setting. If set, a link to your RSS feed will
  appear in the site's HTML header.
GITHUB_REPO_COUNT = 5
  See ``GITHUB_USER`` setting.
GITHUB_SHOW_USER_LINK
  See ``GITHUB_USER`` setting.
GITHUB_SKIP_FORK = False
  See ``GITHUB_USER`` setting.
GITHUB_USER
  The theme can show your most recently active GitHub repos in the sidebar. To
  enable, set this to you GitHub username. Appearance and behavior can be
  controlled using the ``GITHUB_REPO_COUNT``, ``GITHUB_SKIP_FORK``, and 
  ``GITHUB_SHOW_USER_LINK`` variables.
GOOGLE_ANALYTICS
  Used to activate "classic" Google Analytics. Set this to your account's Google
  Analytics ID. Although this setting doesn't conflict with
  ``GOOGLE_ANALYTICS_UNIVERSAL``, you will in most cases only use one or the
  other. This has been deprecated by Google; see ``GOOGLE_ANALYTICS_V4``.
GOOGLE_ANALYTICS_UNIVERSAL
  Used to activate "universal" Google Analytics (this is the new version). Set
  this to your account's ID (a number). Also set
  ``GOOGLE_ANALYTICS_UNIVERSAL_PROPERTY``. Although this setting doesn't
  conflict with ``GOOGLE_ANALYTICS``, you will in most cases only use one or
  the other. This has been deprecated by Google (in June 2023); see
  ``GOOGLE_ANALYTICS_V4``.
GOOGLE_ANALYTICS_UNIVERSAL_PROPERTY
  Set this to the Google Analytics "property" this site represents. See also
  (and set) ``GOOGLE_ANALYTICS_UNIVERSAL``.
GOOGLE_ANALYTICS_V4
  Set this to your "measurement ID" to activate Google Analytics v4.
GPX_CATEGORY
  Used to process GPX "articles" differently.
GPX_DEV_URL
  The project url for the GPX Reader plugin. Provided by the plugin, when in
  use.
GPX_VERSION
  The version of the GPX Reader plugin. Provided by the plugin, when in use.
HIDE_SIDEBAR = False
  Hides the sidebar, and all it's contents. Also review the settings
  ``DISPLAY_CATEGORIES_ON_SIDEBAR``, ``DISPLAY_RECENT_POSTS_ON_SIDEBAR``,
  ``DISPLAY_TAGS_ON_SIDEBAR``, ``GITHUB_USER``, ``LINKS``, and
  ``TWITTER_USERNAME``.
HIDE_SITENAME = False
  Hides the sitename in the site navbar.
IMAGE_PROCESS = {"article-feature": ["scale_in 848 848 True"], "index-feature": ["scale_in 263 263 True"],}
  Used by the *image process* plugin. The "article-feature" and "index-feature"
  configurations are set by the included plugin if not set in your
  configuration to something else.
INDEX_COPY_DATE
  Copyright date to display on the index page (homepage) of the site.
JQUERY_JS_IN_HEAD = False
  Bootstrap depends on JQuery. Typically, good practice is to load all your
  Javascript from the end of your page. However, in certain cases, I've needed
  to load JQuery sooner. So this moves loading JQuery from the end of the page
  to the header. When active, JQuery is listed before the other scripts in
  ``CUSTOM_JS_LIST_HEAD``. See also ``CUSTOM_JS_LIST_HEAD``.
LINKS = []
  Extra links to display sidebar. Provide a list of tuples of the form
  ``('name', 'link')``.
MENUITEMS
  Extra items to add to the menu. Provide a list of tuples of the form
  ``(title, link, icon)``. ``link`` is absolute, so build them using SITEURL, 
  if needed. ``icon`` here is of the form of the CSS classes to be used; e.g.
  ``'fa fa-fw fa-pencil'``. ``icon`` can be set to ``None``.

  If this is set, the working assumption is that the site you are generating is
  a "sub-site", and this is the menu from the "master site".
MENUITEMS_2
  Extra items you want added as a sub-menu. Use in conjunction with the
  ``MENUITEMS_2_AT`` setting. Provide a list of tuples of the form
  ``(title, link, icon)``. ``link`` is absolute, so build them using SITEURL, 
  if needed. ``icon`` here is of the form of the CSS classes to be used; e.g.
  ``'fa fa-fw fa-pencil'``. ``icon`` can be set to ``None``.

  This setting is working on the assumption that your generated site in going
  to be served as a subdirectory of your "main" site (such as for GitHub
  project pages).
MENUITEMS_2_AT
  If ``MENUITEMS_2`` is set, under which (main) menu item are these to be
  displayed. This should match a "name" of one of the items on ``MENUITEMS``;
  if no match is found, these sub-menu items will not be displayed.

  When set and Breadcrumbs are enabled, all items on the site are shown to be
  under both "home" (linked to at the ``SITE_ROOT_URL``) and ``MENUITEMS_2_AT``
  (linked to at ``MENUITEMS_2_AT_LINK``).

  See also the page metadata option ``at`` if you want to do similiar to this
  for select pages only.
MENUITEMS_2_AT_LINK
  When set and Breadcrumbs are enabled, all items on the site are shown to be
  under both "home" (linked to at the ``SITE_ROOT_URL``) and ``MENUITEMS_2_AT``
  (linked to at ``MENUITEMS_2_AT_LINK``).
MICROBLOG_DEV_URL
  The project url for the microblogging plugin. Provided by the plugin, when in
  use.
MICROBLOG_VERSION
  The version of the microblogging plugin. Provided by the plugin, when in use.
NAVBAR_ON_TOP = False
  If True, the navigation menu is on top. If False, the navigation menu is
  vertical on the left side of the page. Default is False.
NEIGHBORS
  Activates the links to the next and previous articles, both in the "all
  posts" index and the category-specific index. Requires the `neighbors
  <https://pypi.python.org/pypi/pelican-neighbors>`_ plugin to be both
  installed and activated (i.e. listed under ``PLUGINS``).
OPEN_GRAPH_FB_APP_ID
  You can use this setting to provide a Facebook *app id*. See the
  ``USE_OPEN_GRAPH`` setting.
OPEN_GRAPH_IMAGE
  A default image to use with Open Graph. This is a filepath relative to your
  SITEURL. See the ``USE_OPEN_GRAPH`` setting.
PAGINATOR_LIMIT = 8
  Number of page number links to appear of the main "index" page of your
  blog. The default of 8 results in showing a link to page 1, links the
  three previous pages (8 divided by 2 and rounded down), a number
  representing the current page, links to the next three pages, and a link
  to the last page.
PDF_PROCESSOR
  If set, provides links to a PDF version of the page or article at
  ``<SITEURL>/pdf/<page.slug>.pdf``. The actual PDF files will need to be
  generated outside of *seafoam*.
PELICAN_COMMENT_SYSTEM = False
  Set this to ``True`` to active the `Static Comments
  <https://blog.minchin.ca/2022/04/static-comments-211-released.html>`_ plugin
  (``minchin.pelican.plugins.static-comments``).

  The Static Comments plugin has
  `further settings <https://github.com/minchinweb/minchin.pelican.plugins.static_comments/blob/master/docs/installation.md>`_
  that are not used directly by the theme.

  You will probably only use this or Disqus; odd results may come if you try to
  use both together. See also the ``DISQUS_SITENAME`` setting.

  See also ``PELICAN_COMMENT_SYSTEM_DISPLAY_COUNTS``,
  ``PELICAN_COMMENT_SYSTEM_EMAIL_DOMAIN``,
  ``PELICAN_COMMENT_SYSTEM_EMAIL_USER``, ``PELICAN_COMMENT_SYSTEM_FEED``,
  ``PELICAN_COMMENT_SYSTEM_FEED_ALL``, and
  ``PELICAN_COMMENT_SYSTEM_IDENTICON_SIZE``.
PELICAN_COMMENT_SYSTEM_DISPLAY_COUNTS = True
  Whether to display the number of comments
PELICAN_COMMENT_SYSTEM_EMAIL_DOMAIN
  The domain name of the email where you want the comments to be emailed to
  (i.e. the part after the ``@`` sign). See the
  ``PELICAN_COMMENT_SYSTEM_EMAIL_USER`` and ``PELICAN_COMMENT_SYSTEM``
  settings.
PELICAN_COMMENT_SYSTEM_EMAIL_USER
  The username of the email where you want the comments to be emailed to (i.e.
  the part before the ``@`` sign). See the
  ``PELICAN_COMMENT_SYSTEM_EMAIL_DOMAIN`` and ``PELICAN_COMMENT_SYSTEM``
  setting.
PELICAN_COMMENT_SYSTEM_FEED, PELICAN_COMMENT_SYSTEM_FEED_ALL
  Used internally to generate links to the Comment RSS/Atoms feeds.
PELICAN_COMMENT_SYSTEM_IDENTICON_SIZE = 72
  The size of the Identicons generated by the Pelican Comment System.
PIWIK_SITE_ID
  Used for Piwik site analytics.
PIWIK_SSL_URL = PIWIK_URL
  Used for Piwik site analytics.
PIWIK_URL
  Used for Piwik site analytics.
PLUGINS
  Same as the regular Pelican setting. If you set this, be sure to include the
  internal plugin ``pelican.plugins.seafoam`` to get the theme to
  auto-configure itself.
PRJCT
  Set to ``TRUE`` to active `prjct <https://github.com/MinchinWeb/prjct>`_
  support. Recommended segment to include in your ``pelicanconf.py``:

  .. code-block:: python

    # pelicanconf.py

    import prjct

    PRJCT = True
    PRJCT_TODO, PRJCT_DONE = prjct.todo_export.to_html_dicts()
    PRJCT_PROJECTS = prjct.multi_source.project_list()
    PRJCT_ACTIVE_PROJECTS = prjct.multi_source.active_project_list()
    PRJCT_SOMEDAY_PROJECTS = prjct.config.someday_projects()
    PRJCT_COMPLETED_PROJECTS = prjct.config.completed_projects()
    PRJCT_DESC = prjct.descriptions.to_html_dict(
        markdown_extension_config=MARKDOWN['extension_configs']
    )
    PRJCT_VERSION = prjct.__version__
    PRJCT_FOOTER_URL = prjct.__url__

  Also add prjct to our direct templates list.

  See also ``PRJCT_ACTIVE_PROJECTS``, ``PRJCT_COMPLETED_PROJECTS``,
  ``PRJCT_DESC``, ``PRJCT_DONE``, ``PRJCT_FOOTER_URL``,
  ``PRJCT_SOMEDAY_PROJECTS``, ``PRJCT_TODO``, and ``PRJCT_VERSION``.
PRJCT_ACTIVE_PROJECTS
  A list of *active* projects. Used to sort projects on the main prjct page.
  See the ``PRJCT`` setting.
PRJCT_COMPLETED_PROJECTS
  A list of *active* projects. Used to sort projects on the main prjct page.
  See the ``PRJCT`` setting.
PRJCT_DESC
  A dictionary of descriptions for each project, where the key is the name of
  the project, and will match the *tag* page where the output appears. The
  return value is assumed to be a valid HTML segment. See the ``PRJCT``
  setting.
PRJCT_DONE
  A dictionary of done to-do items for each project, where the key is the name
  of the project, and will match the *tag* page where the output appears. The
  return value is assumed to be a valid HTML segment. See the ``PRJCT``
  setting.
PRJCT_FOOTER_URL = 'https://github.com/MinchinWeb/prjct'
  *prjct* URL used for link displayed in footer. See the ``PRJCT`` setting.
PRJCT_SOMEDAY_PROJECTS
  A list of *active* projects. Used to sort projects on the main prjct page.
  See the ``PRJCT`` setting.
PRJCT_TODO
  A dictionary of open to-do items for each project, where the key is the name
  of the project, and will match the *tag* page where the output appears. The
  return value is assumed to be a valid HTML segment. See the ``PRJCT``
  setting.
PRJCT_VERSION = ''
  *prjct* version displayed in footer. See the ``PRJCT`` setting.
PYGMENTS_STYLE = 'native'
  This setting is currently ignored, and my preferred Pygments theme (style)
  (*friendly*) is included directly into the Seafoam CSS.
RECENT_POST_COUNT = 5
  Number of recent posts to display on the sidebar. See the
  ``DISPLAY_RECENT_POSTS_ON_SIDEBAR`` setting.
RELATED_POSTS_TEXT = 'Related Posts:'
  Header for related posts listing. Requires that the `Related Posts Plugin
  <https://github.com/getpelican/pelican-plugins/tree/master/related_posts>`_
  be active.
SEAFOAM_DEV_MODE = False
  Enable this to speed local development by (effectively) disabling the *Image
  Process* plugin. If you disable this in your ``pelicanconf.py``, you'll
  likely want to activate it in your ``publishconf.py`` file.
SEAFOAM_ENCODING = "uft-8"
  The encoding that Beautiful Soup uses when run by the internal plugin.
SEAFOAM_PARSER = "html.parser"
  Will be set to "lxml" is it is installed (which is the case with the most
  recent versions of the required ``image-process`` plugin).

  This is the parser that Beautiful Soup uses when run by the internal plugin.
SEAFOAM_URL = "http://blog.minchin.ca/label/seafoam/"
  The project url of the theme (automatically provided by the bundled plugin).
SEAFOAM_VERSION = ``pelican.plugins.seafoam.__version__``
  The version of the theme (automatically provided by the bundled plugin).
SITELOGO
  Link to the site logo (displayed in the navbar). This is relative to the
  SITEURL.

  See also ``SITELOGO_SIZE``.
SITELOGO_SIZE
  The width of the site logo in the navbar. Can be set to any valid CSS value
  (i.e. %, em, px, etc). I have had good luck setting this to ``100%``.

  See also ``SITELOGO``.
SITENAME
  The name of your site, displayed in the navbar.
SITEURL
  Same as the Pelican setting. Set this to where this Pelican site is actually
  hosted. Also see the ``SITE_ROOT_URL`` setting.
SITE_ROOT_URL = SITEURL
  Use this if you're hosting a subsite of some sort. This is where the links in
  logo in the navbar and the home icon in the breadcrumbs will point to. See
  also the ``MENUITEMS_2_AT`` setting.
SOCIAL
  A list of your social media sites to be listed in the sidebar. Should be a
  list of tuples in the form ('social network name', 'full link to profile').
  The theme will display the logo of the network. See the ``HIDE_SIDEBAR``
  setting.
TAGS_TEXT = "Tags"
  Text used as the header to "Tags" (articles can be filed under multiple tags,
  but assumes to be under a single (or no) category. Assumed to be plural.
TAGS_URL
  Same as the Pelican setting.
TEMPLATE_PAGES = { "404.html": "404.html", }
  Same as the Pelican setting. Automatically set by the internal plugin to
  enable a 404 error page on GitHub pages (and perhaps elsewhere).
THEME = ``pelican.plugins.seafoam.get_path()``
  Same as the Pelican setting. Automatically set by the internal plugin.
THEME_STATIC_DIR
  Same as the Pelican setting.
TWITTER_USERNAME
  You can optionally provide a this which will be used to set the Twitter
  username for the site and for the content creator.
TWITTER_WIDGET_ID
  The theme can show your twitter timeline in the sidebar. To enable, provide a
  ``TWITTER_USERNAME`` and a ``TWITTER_WIDGET_ID``.

  To get a ``TWITTER_WIDGET_ID``, go to:
  `https://twitter.com/settings/widgets <https://twitter.com/settings/widgets>`_
  and select *Create new*. You'll find the ``TWITTER_WIDGET_ID`` under the html
  or in the site url:

  https://twitter.com/settings/widgets/TWITTER_WIDGET_ID/edit
TYPOGRIFY
  Whether to activate Typography. Tyopgraphy is a library that automatically
  adds a number of typographical flourishes. The necessary CSS is automatically
  included in the *seafoam* CSS.

  The Typography Python library will needs to be installed, which is
  installable via pip: ``pip install typogrify``

  Note that with Pelican 3.6, activating both the Pelican Comment System and
  Typography at the same time cause issues. This issue was fixed in Pelican
  3.7.
USE_OPEN_GRAPH = True
  In order to make the Facebook "like" button and other social sharing options
  work better, the template contains Open Graph metatags like
  ``<meta property="og:type" content="article"/>``. You can disable them by
  setting this to ``False``.

  See also ``OPEN_GRAPH_FB_APP_ID``, and ``OPEN_GRAPH_FB_APP_ID``
  settings.

It may also be helpful to review the `settings for Pelican itself
<https://docs.getpelican.com/en/stable/settings.html>`_.

On articles, the theme also looks for the ``image`` metadata setting to provide
the *featured image* for the article.


.. _article-metadata:

Article (and Page) Metadata
---------------------------

There are also a number of per-article (and per-page) metadata fields that can
be set influence how an article (or page) is processed and displayed; this is
further to the `site-wide setting <#pelican-settings>`_ set in your
``pelicanconf.py`` file.

These are set in the frontmatter of an article (or page). Arbitrary keys are
accepted, although the theme (or *Pelican*) won't necessarily act on them.

.. TODO: Add code sample

This documentation has to be manually updated, and this section is still be
expaned. If the documentation here no longer match the theme's behavior, or a
setting is missing from here, please open a ticket on `GitHub
<https://github.com/MinchinWeb/seafoam/issues>`_.

at
  (Pages only) Additional breadcrumb "folder". This is the (link) displayed
  name; see also ``at_link`` and ``at_2`` and ``at_3``. See also
  ``MENUITEMS_2_AT`` if you want to do this for the whole site.
at_link
  (Pages only) Additional breadcrumb "folder". This is the "up" page link (i.e.
  the url), relative to the ``SITEURL``; see also ``at``.

  Setting this won't change where the actual page is served from by the server;
  if you want the URL structure to match, set the ``slug`` for the page as
  well. E.g.:

  .. code-block:: markdown

    title: My Sub-Page
    at: Breadcrumb Folder Display
    at_link: /at_folder/
    slug: at_folder/my-page

    Body of my page...

at_2
  (Pages only) Second additional breadcrumb "folder". This is the (link)
  displayed name; see also ``at`` and ``at_2_link``.
at_2_link
  (Pages only) Second additional breadcrumb "folder". This is the "up" page
  link (i.e. the url), relative to the ``SITEURL``; see also ``at_2``.
at_3
  (Pages only) Third additional breadcrumb "folder". This is the (link)
  displayed name; see also ``at`` and ``at_3_link``.
at_3_link
  (Pages only) Third additional breadcrumb "folder". This is the "up" page link
  (i.e. the url), relative to the ``SITEURL``; see also ``at_3``.
author
  Author of the article (or comment). Articles defaults ``AUTHOR``.
avatar
  Profile picture, used by comments. c.f. ``PELICAN_COMMENT_SYSTEM`` and
  ``DISQUS_SITENAME``.
category
  The (singular) category the article belongs to. See also ``tags``.
comments_count
  The number of comments attached to an article. Generally set by a plugin.
completed
  When a task was completed (or cancelled). c.f. ``tasknote`` and
  ``task_status``.
content
  Set by *Pelican* as the "body" of the article.
copy_date
  Copyright date for at article or page.
date
  publication date of the article (or page)
disable_canonical_url
  Set to ``True`` to keep from adding a canonical link in the header of the
  article or page.
due
  When a task is due. c.f. ``tasknote``.
image
  Hero (or header) image. Provided location is relative to the ``SITEURL`` in
  the generated site.
has_summary
  Set by Pelican (?) to ``True`` if a summary is available.
gpx
  Set to ``True`` to denote a GPX "post". Changes how the article is processed
  and how it is displayed. See also ``gpx_start_time`` and ``gpx_end_time``.
gpx_start_time
  When a GPX tracking file started. c.f. ``gpx``.
gpx_end_time
  When a GPX tracking file ended. c.f. ``gpx``.
metadata
  Used by the comments. The key ``website`` is the link back to the author's
  website. c.f. ``PELICAN_COMMENT_SYSTEM`` and ``DISQUS_SITENAME``.
micro
  Set to ``True`` to denote a microblog post. Changes how the article is
  processed and how it is displayed.
modified
  (Last) date a page was updated.
next_article
  refernce to the "previous" article. c.f ``prev_article``. c.f. ``NEIGHBORS``.
  Set by a plugin.
next_article_in_category
  See ``next_article``.
og_image
  OpenGraph image for the article.
prev_article
  reference to the "previous" article. c.f ``next_article``. c.f.
  ``NEIGHBORS``. Set by a plugin.
prev_article_in_category
  See ``prev_article``.
readtime_minutes
  Expected reading time for the article. Generally provided by a plugin. c.f.
  ``stats["read_min"]``.
redirect_url
  When set, will use HTML to tell the browser to redirect the user from this
  page/article to another webpage. You must provide the full URL.
related_posts
  A dictionary of "related posts"; generally set by a plugin. C.f.
  ``RELATED_POSTS_TEXT``
scheduled
  When a task is (next) scheduled for. c.f. ``tasknote``.
slug
  Used to generate the URL to the page. Must be unique (a requirement of
  *Pelican*).
stats
  Generally provided by a plugin. Key ``read_mins`` provided the expected
  reading time; c.f. ``readtime_minutes``.
subtitle
  Subtitle for the article.
summary
  A short version of the body of the article. Can be set directly, or *Pelican*
  (or a plugin) will generate it for you.

  If ``USE_OPEN_GRAPH`` is ``True``, this doubles as the Open Graph
  description.
tags
  A list of the tags applicable to the article. See also ``category``.
task_status
  The status of a task. In particular, it checks if a task is set to
  ``cancelled``. c.f. ``tasknote``.
tasknote
  Set to ``True`` to denote a task note "post". Changes how the article is
  processed and how it is displayed.

  See also ``completed``, ``due``, ``scheduled``, ``task_status``, ``tasknote_checkbox``, ``threshold_date``, 
tasknote_checkbox
  . c.f. ``tasknote``.
threshold_date
  The date a task becomes of interest (and is generally ignored before this
  date). c.f. ``tasknote``.
title
  Article title. Used several places as the "name" for links back to the
  article.
translations
  A list of translations for an article. Generated by *Pelican*.
url
  Set by *Pelican*. Location (on the webpage) of the article, relative to the
  ``SITEURL``.


Known Issues
------------

- versions before v2.13.1 break on Pelican v4.11.0.post0. Upgrade *seafoam* to
  solve this.
- activating both Typogrify and the Pelican Comment System on Pelican 3.6
  causes issues. This issue has been fixed in Pelican 3.7.
- minification (specifically,
  `pelican-minify <https://github.com/pelican-plugins/minify>`_) breaks the
  included *jQuery* and causes random spacing issues. I have had on and off
  issues since forever with minification, but my current suggestion is to turn
  it off. The latest indication that something was wrong was that the
  navigation pull down menu wouldn't work on narrow screens.

Credits
-------

Original theme developed by `Daan Debie <http://dandydev.net/>`_.

The idea that a theme could be installed as a Python package by `Jeff
Forcier <http://bitprophet.org/>`_'s `Alabaster theme
<https://github.com/bitprophet/alabaster>`_ for Sphinx.
