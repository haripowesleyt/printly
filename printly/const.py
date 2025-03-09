"""Defines constants used throughout the library, such as prefixes, delimiters, and mappings."""

from typing import Dict, Tuple
from .types import Color, FontStyle

HEX_PREFIX: str = "#"
"""Character that shows that a color is in HEX."""

RGB_DELIMITER: str = ","
"""Character that separates RGB values."""

COMBINATOR: str = "+"
"""Character that joins multiple font styles."""

RESET = "\033[0m"
"""Closing tag for styling: indicates end of styling"""

COLORS_RGB_MAP: Dict[Color, Tuple[int, int, int]] = {
    # Shades of Green
    "greenyellow": (173, 255, 47),
    "chartreuse": (127, 255, 0),
    "lawngreen": (124, 252, 0),
    "lime": (0, 255, 0),
    "limegreen": (50, 205, 50),
    "palegreen": (152, 251, 152),
    "lightgreen": (144, 238, 144),
    "mediumspringgreen": (0, 250, 154),
    "springgreen": (0, 255, 127),
    "mediumseagreen": (60, 179, 113),
    "seagreen": (46, 139, 87),
    "forestgreen": (34, 139, 34),
    "green": (0, 128, 0),
    "darkgreen": (0, 100, 0),
    "yellowgreen": (154, 205, 50),
    "olivedrab": (107, 142, 35),
    "olive": (128, 128, 0),
    "darkolivegreen": (85, 107, 47),
    "mediumaquamarine": (102, 205, 170),
    "darkseagreen": (143, 188, 143),
    "lightseagreen": (32, 178, 170),
    "darkcyan": (0, 139, 139),
    "teal": (0, 128, 128),
    # Shades of Blue
    "cyan": (0, 255, 255),
    "aqua": (0, 255, 255),
    "lightcyan": (224, 255, 255),
    "paleturquoise": (175, 238, 238),
    "aquamarine": (127, 255, 212),
    "turquoise": (64, 224, 208),
    "mediumturquoise": (72, 209, 204),
    "darkturquoise": (0, 206, 209),
    "cadetblue": (95, 158, 160),
    "steelblue": (70, 180, 130),
    "lightsteelblue": (176, 196, 222),
    "powderblue": (176, 224, 230),
    "lightblue": (173, 216, 230),
    "skyblue": (135, 206, 235),
    "lightskyblue": (135, 206, 250),
    "deepskyblue": (0, 191, 255),
    "dodgerblue": (30, 144, 255),
    "cornflowerblue": (100, 149, 237),
    "mediumslateblue": (123, 104, 238),
    "royalblue": (65, 105, 225),
    "blue": (0, 0, 255),
    "mediumblue": (0, 0, 205),
    "darkblue": (0, 0, 139),
    "navy": (0, 0, 128),
    "midnightblue": (25, 25, 112),
    # Shades of Red
    "indianred": (205, 92, 92),
    "lightcoral": (240, 128, 128),
    "salmon": (250, 128, 114),
    "darksalmon": (233, 150, 122),
    "crimson": (220, 20, 60),
    "red": (225, 0, 0),
    "firebrick": (178, 34, 34),
    "darkred": (139, 0, 0),
    # Shades of Orange
    "lightsalmon": (255, 160, 122),
    "coral": (255, 127, 80),
    "tomato": (255, 99, 71),
    "orangered": (255, 69, 0),
    "darkorange": (255, 140, 0),
    "orange": (255, 165, 0),
    # Shades of Yellow
    "gold": (255, 215, 0),
    "yellow": (255, 255, 0),
    "lightyellow": (255, 255, 224),
    "lemonchiffon": (255, 250, 205),
    "lightgoldenrodyellow": (250, 250, 210),
    "papayawhip": (255, 239, 213),
    "moccasin": (255, 228, 181),
    "peachpuff": (255, 218, 185),
    "palegoldenrod": (238, 232, 170),
    "khaki": (240, 230, 140),
    "darkkhaki": (189, 183, 107),
    # Shades of Purple
    "lavender": (230, 230, 250),
    "thistle": (216, 191, 216),
    "plum": (221, 160, 221),
    "violet": (238, 130, 238),
    "orchid": (218, 112, 214),
    "magenta": (255, 0, 255),
    "fuchsia": (255, 0, 255),
    "mediumorchid": (186, 85, 211),
    "mediumpurple": (147, 112, 219),
    "blueviolet": (138, 43, 226),
    "darkviolet": (148, 0, 211),
    "darkorchid": (153, 50, 204),
    "darkmagenta": (139, 0, 139),
    "purple": (128, 0, 128),
    "rebeccapurple": (102, 51, 153),
    "indigo": (75, 0, 130),
    "slateblue": (106, 90, 205),
    "darkslateblue": (72, 61, 139),
    # Shades of Pink
    "pink": (255, 192, 203),
    "lightpink": (255, 182, 193),
    "hotpink": (255, 105, 180),
    "deeppink": (255, 20, 147),
    "mediumvioletred": (199, 21, 133),
    "palevioletred": (219, 112, 147),
    # Shades of Brown
    "cornsilk": (255, 248, 220),
    "blanchedalmond": (255, 235, 205),
    "bisque": (255, 228, 196),
    "navajowhite": (255, 222, 173),
    "wheat": (245, 222, 179),
    "burlywood": (222, 184, 135),
    "tan": (210, 180, 140),
    "rosybrown": (188, 143, 143),
    "sandybrown": (244, 164, 96),
    "goldenrod": (218, 165, 35),
    "darkgoldenrod": (184, 134, 11),
    "peru": (205, 133, 63),
    "chocolate": (210, 105, 30),
    "saddlebrown": (139, 69, 19),
    "sienna": (160, 82, 45),
    "maroon": (128, 0, 0),
    "brown": (165, 42, 42),
    # Shades of Grey
    "gainsboro": (220, 220, 220),
    "lightgrey": (211, 211, 211),
    "lightgray": (211, 211, 211),
    "silver": (192, 192, 192),
    "darkgrey": (169, 169, 169),
    "darkgray": (169, 169, 169),
    "grey": (128, 128, 128),
    "gray": (128, 128, 128),
    "dimgrey": (105, 105, 105),
    "dimgray": (105, 105, 105),
    "lightslategrey": (119, 136, 153),
    "lightslategray": (119, 136, 153),
    "slategrey": (112, 128, 114),
    "slategray": (112, 128, 114),
    "darkslategrey": (49, 79, 79),
    "darkslategray": (49, 79, 79),
    "black": (0, 0, 0),
    # Shades of White
    "white": (255, 255, 255),
    "snow": (255, 250, 250),
    "honeydew": (240, 255, 240),
    "mintcream": (245, 255, 250),
    "azure": (240, 255, 255),
    "aliceblue": (240, 248, 255),
    "ghostwhite": (248, 248, 255),
    "whitesmoke": (245, 245, 245),
    "seashell": (255, 235, 248),
    "beige": (245, 245, 220),
    "oldlace": (253, 245, 230),
    "floralwhite": (255, 250, 240),
    "ivory": (255, 255, 240),
    "antiquewhite": (250, 235, 215),
    "linen": (250, 240, 230),
    "lavenderblush": (255, 240, 245),
    "mistyrose": (255, 228, 255),
}
"""Mapping of named colors to their RGB values."""

FONT_STYLE_CODES: Dict[FontStyle, int] = {
    "bold": 1,
    "italic": 3,
    "underline": 4,
    "hidden": 8,
    "strikethrough": 9,
    "double-underline": 21,
    "overline": 53,
}
"""Mapping of font styles to their code numbers."""
