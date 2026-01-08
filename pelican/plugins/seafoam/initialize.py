import logging

from packaging.specifiers import SpecifierSet
from packaging.version import Version

from pelican import __version__ as pelican_version

from .constants import (
    LOG_PREFIX,
    PLUGIN_LIST,
    PRODUCTION_PLUGIN_LIST,
    __url__,
    __version__,
)

try:
    import lxml
except ImportError:
    lxml = None

logger = logging.getLogger(__name__)


def pelican_namespace_plugin_support():
    """
    Determine if the installed version of Pelican natively supports namespace
    plugins.

    In short, the Pelican version must be greater than 4.5.0.

    Return:
        bool: if namespace plugins are supported
    """
    # see https://github.com/minchinweb/minchin.pelican.plugins.autoloader/blob/master/minchin/pelican/plugins/autoloader.py

    pelican_parced_version = Version(pelican_version)
    needed_spec = SpecifierSet(">= 4.5.0")

    return pelican_parced_version in needed_spec


def seafoam_dev_mode_active(pelican):
    """
    Check if Seafoam Development Mode is active.
    """
    if (
        "SEAFOAM_DEV_MODE" in pelican.settings.keys()
        and pelican.settings["SEAFOAM_DEV_MODE"]
    ):
        logger.warning(
            "%s Development Mode is active. Image Process has been disabled.",
            LOG_PREFIX,
        )
        return True
    else:
        pelican.settings["SEAFOAM_DEV_MODE"] = False
        return False


def check_settings(pelican):
    """
    Insert defaults in Pelican settings, as needed.
    """
    logger.debug("%s massaging settings, setting defaults." % LOG_PREFIX)

    # THEME = seafoam.get_path()

    # A default value is set for "THEME", so simply testing for its lack won't
    # work

    # if "THEME" not in pelican.settings.keys():
    if True:
        from . import get_path  # to avoid circular imports

        # this needs to be set directly, because this setting has already been
        # read
        pelican.theme = get_path()
        # setting THEME doesn't seem to be used directly by Pelican, but set
        # here in case someone else comes looking
        pelican.settings["THEME"] = pelican.theme
        logger.debug('%s THEME set to "%s"' % (LOG_PREFIX, pelican.theme))
    else:
        logger.debug(
            "%s THEME previously set manually. Is %s" % (LOG_PREFIX, pelican.theme)
        )

    # BOOTSTRAP_THEME = 'seafoam'
    if "BOOTSTRAP_THEME" not in pelican.settings.keys():
        pelican.settings["BOOTSTRAP_THEME"] = "seafoam"
        logger.debug(
            '%s BOOTSTRAP_THEME set to "%s"'
            % (LOG_PREFIX, pelican.settings["BOOTSTRAP_THEME"])
        )
    else:
        logger.debug(
            '%s BOOTSTRAP_THEME previously set manually. Is "%s".'
            % (LOG_PREFIX, pelican.settings["BOOTSTRAP_THEME"])
        )

    # PLUGINS = [
    #     'pelican.plugins.seafoam',
    #     'pelican.plugins.jinja_filters',
    #     'pelican.plugins.image_process',
    #     # others, as desired...
    # ]
    if seafoam_dev_mode_active(pelican):
        seafoam_plugins = PLUGIN_LIST
    else:
        seafoam_plugins = PRODUCTION_PLUGIN_LIST

    if (
        "PLUGINS" not in pelican.settings.keys()
        and not pelican_namespace_plugin_support()
    ):
        pelican.settings["PLUGINS"] = list()
        for k in seafoam_plugins:
            pelican.settings["PLUGINS"].append(k)
            logger.debug('%s "%s" appended to PLUGINS' % (LOG_PREFIX, k))
        # force update of plugins
        pelican.init_plugins()

    elif "PLUGINS" in pelican.settings.keys():
        for k in seafoam_plugins:
            if k not in pelican.settings["PLUGINS"]:
                pelican.settings["PLUGINS"].append(k)
                logger.debug('%s "%s" appended to PLUGINS' % (LOG_PREFIX, k))
        # force update of plugins
        pelican.init_plugins()

    # IMAGE_PROCESS = {
    #     "article-feature": ["scale_in 848 848 True"],
    #     "index-feature": ["scale_in 263 263 True"],
    # }
    if "IMAGE_PROCESS" not in pelican.settings.keys():
        pelican.settings["IMAGE_PROCESS"] = dict()

    if seafoam_dev_mode_active(pelican):
        # return the given image
        pelican.settings["IMAGE_PROCESS"]["article-feature"] = [lambda x: x]
        pelican.settings["IMAGE_PROCESS"]["index-feature"] = [lambda x: x]
    else:
        # "article feature" images are the headers on the article pages
        # don't scale these up.
        if "article-feature" not in pelican.settings["IMAGE_PROCESS"].keys():
            pelican.settings["IMAGE_PROCESS"]["article-feature"] = [
                "scale_in 848 848 False"
            ]
            logging.debug('%s added "article-feature" to IMAGE_PROCESS' % LOG_PREFIX)
        # "index feature" images are the header images, but displayed to the
        # side of the article summary on the index (or listing page)
        # These can be scaled up. 
        if "index-feature" not in pelican.settings["IMAGE_PROCESS"].keys():
            pelican.settings["IMAGE_PROCESS"]["index-feature"] = [
                "scale_in 263 263 True"
            ]
            logging.debug('%s added "index-feature" to IMAGE_PROCESS' % LOG_PREFIX)

    # TEMPLATE_PAGES
    # Generate 404 error page
    # TEMPLATE_PAGES = {
    #     "404.html": "404.html",
    # }
    if "TEMPLATE_PAGES" not in pelican.settings.keys():
        pelican.settings["TEMPLATE_PAGES"] = dict()
    if "404.html" not in pelican.settings["TEMPLATE_PAGES"].keys():
        pelican.settings["TEMPLATE_PAGES"]["404.html"] = "404.html"
        logging.debug('%s added "404.html" to TEMPLATE_PAGES' % LOG_PREFIX)

    if "SEAFOAM_PARSER" not in pelican.settings.keys():
        if lxml:
            pelican.settings["SEAFOAM_PARSER"] = "lxml"
        else:
            pelican.settings["SEAFOAM_PARSER"] = "html.parser"
        logging.debug(
            '%s SEAFOAM_PARSER set to "%s"'
            % (LOG_PREFIX, pelican.settings["SEAFOAM_PARSER"])
        )
    else:
        logging.debug(
            '%s SEAFOAM_PARSER previously set manually. Is "%s"'
            % (LOG_PREFIX, pelican.settings["SEAFOAM_PARSER"])
        )

    if "SEAFOAM_ENCODING" not in pelican.settings.keys():
        pelican.settings["SEAFOAM_ENCODING"] = "utf-8"
        logging.debug(
            '%s SEAFOAM_ENCODING set to "%s"'
            % (LOG_PREFIX, pelican.settings["SEAFOAM_ENCODING"])
        )
    else:
        logging.debug(
            '%s SEAFOAM_ENCODING previously set manually. Is "%s"'
            % (LOG_PREFIX, pelican.settings["SEAFOAM_ENCODING"])
        )

    if "TAGS_TEXT" not in pelican.settings.keys():
        pelican.settings["TAGS_TEXT"] = "Tags"

    # Template debugging is only active if (Seafoam) Debug mode is generally on
    if "SEAFOAM_TEMPLATE_DEBUG" not in pelican.settings.keys() or not seafoam_dev_mode_active(pelican):
        pelican.settings["SEAFOAM_TEMPLATE_DEBUG"] = False
        logging.debug(
            '%s SEAFOAM_TEMPLATE_DEBUG previously set manually. Is "%s"'
            % (LOG_PREFIX, pelican.settings["SEAFOAM_TEMPLATE_DEBUG"])
        )

    if "DISPLAY_SOURCE_PATH" not in pelican.settings.keys():
        pelican.settings["DISPLAY_SOURCE_PATH"] = False
        logging.debug(
            '%s DISPLAY_SOURCE_PATH previously set manually. Is "%s"'
            % (LOG_PREFIX, pelican.settings["DISPLAY_SOURCE_PATH"])
        )


def seafoam_version(pelican):
    """
    Insert seafoam version into Pelican context.
    """

    if "SEAFOAM_VERSION" not in pelican.settings.keys():
        pelican.settings["SEAFOAM_VERSION"] = __version__
        logger.debug(
            '%s Adding Seafoam version "%s" to context.' % (LOG_PREFIX, __version__)
        )
    else:
        logger.debug(
            '%s SEAFOAM_VERSION already defined. Is "%s".'
            % (LOG_PREFIX, pelican.settings["SEAFOAM_VERSION"])
        )

    if "SEAFOAM_URL" not in pelican.settings.keys():
        pelican.settings["SEAFOAM_URL"] = __url__
        logger.debug('%s Adding Seafoam URL "%s" to context.' % (LOG_PREFIX, __url__))
    else:
        logger.debug(
            '%s SEAFOAM_URL already defined. Is "%s".'
            % (LOG_PREFIX, pelican.settings["SEAFOAM_URL"])
        )
