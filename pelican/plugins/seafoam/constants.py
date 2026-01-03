__title__ = "seafoam"
__version__ = "2.15.1-dev"
__description__ = "Pelican theme, first used for Minchin.ca."
__author__ = "W. Minchin"
__email__ = "w_minchin@hotmail.com"
__url__ = "http://blog.minchin.ca/label/seafoam/"
__license__ = "MIT License"

LOG_PREFIX = "[Seafoam]"
PLUGIN_LIST = [
    "pelican.plugins.seafoam",
    "pelican.plugins.jinja_filters",
]
PRODUCTION_PLUGIN_LIST = PLUGIN_LIST + [
    "pelican.plugins.image_process",
]
STYLES = [
    "seafoam",
    "strathcona",
]
