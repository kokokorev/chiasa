from colorsys import rgb_to_hls, hls_to_rgb

from numpy import array, asarray, ndarray

def rgb_to_hsl(rgb_color: array) -> str:
    """rgb to hsl translator

    Args:
        rgb_color (array): one rgb color

    Returns:
        str: one hsl color
    """
    (r, g, b) = rgb_color[0], rgb_color[1], rgb_color[2]
    (h, l, s) = rgb_to_hls(r / 255, g / 255, b / 255)
    return f"{int(h * 360)}.{int(s * 100)}.{int(l * 100)}"


def get_hex_colors_from_name(hsl_images_name: str) -> str:
    hsl_colors_underline = hsl_images_name.split('_')
    hsl_colors = [hsl_color_underline.split('.') for hsl_color_underline in hsl_colors_underline]
    hex_colors = []
    for hsl_color in hsl_colors:
        (h, s, l) = hsl_color[0], hsl_color[1], hsl_color[2]
        (r, g, b) = hls_to_rgb(int(h) / 360, int(l) / 100, int(s) / 100)
        hex_colors.append(rgb_to_hex(asarray([int(r * 255), int(g * 255), int(b * 255)])))
    return hex_colors
        
        


def rgb_to_hex(color: ndarray) -> str:
    """convert rgb (ndarray) to hex color code

    Args:
        color (ndarray): rgb color

    Returns:
        str: hex code
    """
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))