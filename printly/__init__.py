"""Printly is a Python library that enhances the built-in `print()` function with direct \
    text styling: foreground color (`fg`), background color (`bg`), and font styles (`fs`).

Features:
- Supports over 140 color names (from HTML)
- Supports all RGB values (e.g., "128,0,128")
- Supports all HEX color codes (e.g., "#ff00ff")
- Supports 7 font styles: `bold`, `italic`, `strikethrough`, `underline`, `overline`, \
    `double-underline`, and `hide`
- Supports combining multiple font styles (e.g., `"bold+italic"`)
- Supports all standard `print()` parameters: `sep`, `end`, `file`, and `flush`.

Usage Examples:

1. Recommended:
>>> import printly
>>> printly.print("Hello, world!", fg="red", bg="white", fs="bold")

2. Overriding built-in `print()` function (Not Recommended)
>>> from printly import print
>>> print("Hello, world!", fg="red", bg="white", fs="bold")

3. Using the `style()` function:
>>> from printly import style
>>> styled_text = style("Hello, world!", fg="red", bg="white", fs="bold")
>>> print(styled_text)
"""

from .style import style
from .print import print  # pylint: disable=redefined-builtin

__all__ = ["style", "print"]
