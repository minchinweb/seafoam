---
title: Monospaced Font Test
date: 2025-06-07 18:29:09 -0700
tags:
    - test
    - markdown
---

This is a test block pulled from the [Iosevka](https://typeof.net/Iosevka/)
demo site.

```txt
ABC.DEF.GHI.JKL.MNO.PQRS.TUV.WXYZ
abc.def.ghi.jkl.mno.pqrs.tuv.wxyz
!iIlL17|¦ ¢coO08BDQ $5SZ2zs ∂96µm
float il1[]={1-2/3.4,5+6=7/8%90};
1234567890 ,._-+= >< «¯-¬_» ~–÷+×
{*}[]()<>`+-=$/#_%^@\&|~?'" !,.;:
g9q¶ Þẞðþſß ΓΔΛαβγδηθικλμνξπτυφχψ
ЖЗКНРУЭЯавжзклмнруфчьыэя <= != ==
```

Also, let's test of syntax highlighting works:

```py
# -*- coding: utf-8 -*- #
"""
Seafoam.

This is a Pelican theme. This module is the helper
code to go with it.
"""

from pathlib import Path

from pelican import signals

from .constants import __version__  # NOQA
from .formatting import table_fix
from .initialize import (
    check_settings,
    seafoam_version,
)


def get_path():
    """
    Shortcut for users whose theme is not next to
    their pelicanconf.py.

    Returns
    -------
        str: filepath to folder containing theme

    """
    # Theme directory is defined as our parent
    # directory
    return str(Path(__file__).resolve().parent)


def register():
    """Register the plugin pieces with Pelican."""
    signals.initialized.connect(check_settings)
    signals.initialized.connect(seafoam_version)
    signals.content_written.connect(table_fix)
```
