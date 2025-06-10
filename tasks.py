from pathlib import Path
import sys

from invoke import run, task

try:
    from minchin.releaser import make_release
except ImportError:
    print("[WARN] minchin.releaser not installed.")

try:
    from pelican.plugins.seafoam.constants import STYLES
except ImportError:
    try:
        sys.path.insert(0, "pelican/plugins/seafoam")
        from constants import STYLES
    except ImportError:
        STYLES = None
        print("[WARN] STYLES list is unavailable. Install package to fix.")


# also requires `lessc` to be installed and available from the commandline
#
# choco install nodejs-lts
# refresh-env
# npm install less -g

# TODO: provide for alternative shell on something other than Windows

p = Path(__file__).parent  # directory holding this file


@task
def build(ctx):
    """Compile the theme LESS files to CSS."""

    if STYLES is None:
        sys.exit("STYLES list is unavailable. Exiting...")

    my_bar = None
    # if progressbar:
    #     my_bar = progressbar(maximum = len(STYLES))

    for style in STYLES:
        source = p / "css_src" / "less" / f"bootstrap.{style}.less"
        dest = (
            p
            / "pelican"
            / "plugins"
            / "seafoam"
            / "static"
            / "css"
            / f"bootstrap.{style}.min.css"
        )
        run(f"lessc {source} > {dest}")
        print(f'Seafoam LESS for "{style}" compiled to CSS!')
        # TODO -- minimize css!
        #   consider css-html-js-minify


@task
def test(ctx, carefully=False, verbose=False, debug=False):
    """Generate the test Pelican site."""
    config = p / "test" / "pelicanconf.py"

    cli_args = ""
    if carefully:
        cli_args += " --fatal=warnings"
    if verbose:
        cli_args += " --verbose"
    if debug:
        cli_args += " --debug"

    run(f"pelican -s {config}{cli_args}")


@task
def serve_test(ctx, port="8000"):
    """Serve the generated test site."""
    # call using:
    # invoke serve_test --port 8001

    p4 = p / "test" / "output"
    print(p4)
    run(f"cd {p4} && start python -m http.server {port}")
