import logging

from pelican import signals

logger = logging.getLogger(__name__)

def add_jinja_debug(pelican):
    """
    Allows the use of the ``{% debug %}`` filter in templates.

    See https://jinja.palletsprojects.com/en/stable/extensions/#debug-extension
    """
    pelican.env.add_extension("jinja2.ext.debug")
