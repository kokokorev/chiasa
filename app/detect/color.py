from colorsys import rgb_to_hls, hls_to_rgb
from random import choice
from numpy import array, asarray, ndarray
import os

WHEEL_COLORS = {
    'yellow':           list(range(56, 61)),
    'yellow-orange':    list(range(41, 51)),
    'orange':           list(range(21, 41)),
    'red-orange':       list(range(11, 21)),
    'red':              list(range(346, 361)) + list(range(0, 11)),
    'red-purple':       list(range(281, 346)),
    'purple':           list(range(241, 281)),
    'blue-purple':      list(range(221, 241)),
    'blue':             list(range(201, 221)),
    'blue-green':       list(range(170, 201)),
    'green':            list(range(81, 141)),
    'yellow-green':     list(range(61, 81))
}


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


def get_hex_colors_from_name(hsl_image_name: str) -> list:
    """hex from image name in hsl format

    Args:
        hsl_image_name (str): image name in hsl format

    Returns:
        list: hex colors from image
    """
    raw_hsl_colors = hsl_image_name.split('.jpg')[0].split('_')
    hsl_colors = [hsl_color_underline.split('.') for hsl_color_underline in raw_hsl_colors]
    return hsl_colors_to_hex(hsl_colors)


def hsl_colors_to_hex(hsl_colors: list) -> list:
    hex_colors = []
    for hsl_color in hsl_colors:
        (h, s, l) = hsl_color[0], hsl_color[1], hsl_color[2]
        (r, g, b) = hls_to_rgb(int(h) / 360, int(l) / 100, int(s) / 100)
        hex_colors.append(
            rgb_to_hex(
                asarray(
                    [
                        int(r * 255), 
                        int(g * 255), 
                        int(b * 255)]
                    )
                )
            )
    return hex_colors


def rgb_to_hex(color: ndarray) -> str:
    """convert rgb (ndarray) to hex color code

    Args:
        color (ndarray): rgb color

    Returns:
        str: hex code
    """
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))


def get_images_by_color(selected_color: str) -> list:
    """find images with selected color

    Args:
        selected_color (str): color for find images with him

    Returns:
        list: path ot images with selected color
    """
    # get the list of all files and directories
    path = "app/static/images/uploaded"
    image_list = os.listdir(path)
    
    images_with_seleted_color = set()
    for raw_image_name in image_list:
        # get hsl colors from images names
        # remove .jpg format and _ separator
        image_colors_dot = raw_image_name.split('.jpg')[0].split('_')
        # split by . for get hsl colors list
        image_hsl_colors = [image_color_dot.split('.') for image_color_dot in image_colors_dot]
        
        # check every hsl color
        for image_hsl_color in image_hsl_colors:
            hue = image_hsl_color[0]
            # and if hue in choises color space
            if int(hue) in WHEEL_COLORS[selected_color]:
                # add image path to set
                images_with_seleted_color.add(raw_image_name)
    
    return list(images_with_seleted_color)


def get_random_color() -> str:
    """get random color from wheel

    Returns:
        str: random color name
    """
    return choice(list(WHEEL_COLORS.keys()))


def get_complementary_palette(hsl_image_name):
    raw_hsl_colors = hsl_image_name.split('.jpg')[0].split('_')
    hsl_colors = [hsl_color_underline.split('.') for hsl_color_underline in raw_hsl_colors]
    
    hsl_complementary = []
    for hsl_color in hsl_colors:
        plus = 180
        if (int(hsl_color[0]) + plus) > 360:
            hsl_complementary.append(
                [str((int(hsl_color[0]) + plus) - 360), hsl_color[1], hsl_color[2]]
            )
        else:
            hsl_complementary.append(
                [str(int(hsl_color[0]) + plus), hsl_color[1], hsl_color[2]]
            )
    hex_colors = hsl_colors_to_hex(hsl_complementary)
    
    return hex_colors


def get_triadic_palette(hsl_image_name) -> list:
    raw_hsl_colors = hsl_image_name.split('.jpg')[0].split('_')
    hsl_colors = [hsl_color_underline.split('.') for hsl_color_underline in raw_hsl_colors]
    
    hsl_triadic_first = []
    for hsl_color in hsl_colors:
        plus = 120
        if (int(hsl_color[0]) + plus) > 360:
            hsl_triadic_first.append(
                [str((int(hsl_color[0]) + plus) - 360), hsl_color[1], hsl_color[2]]
            )
        else:
            hsl_triadic_first.append(
                [str(int(hsl_color[0]) + plus), hsl_color[1], hsl_color[2]]
            )
    
    hsl_triadic_second = []
    for hsl_color in hsl_colors:
        plus = 240
        if (int(hsl_color[0]) + plus) > 360:
            hsl_triadic_second.append(
                [str((int(hsl_color[0]) + plus) - 360), hsl_color[1], hsl_color[2]]
            )
        else:
            hsl_triadic_second.append(
                [str(int(hsl_color[0]) + plus), hsl_color[1], hsl_color[2]]
            )
    
    hex_triadic_colors_first = hsl_colors_to_hex(hsl_triadic_first)
    hex_triadic_colors_second = hsl_colors_to_hex(hsl_triadic_second)
    return hex_triadic_colors_first, hex_triadic_colors_second


def get_tetradic_palette(hsl_image_name) -> list:
    raw_hsl_colors = hsl_image_name.split('.jpg')[0].split('_')
    hsl_colors = [hsl_color_underline.split('.') for hsl_color_underline in raw_hsl_colors]
    
    hsl_tetradic_first = []
    for hsl_color in hsl_colors:
        plus = 90
        if (int(hsl_color[0]) + plus) > 360:
            hsl_tetradic_first.append(
                [str((int(hsl_color[0]) + plus) - 360), hsl_color[1], hsl_color[2]]
            )
        else:
            hsl_tetradic_first.append(
                [str(int(hsl_color[0]) + plus), hsl_color[1], hsl_color[2]]
            )
    
    hsl_tetradic_second = []
    for hsl_color in hsl_colors:
        plus = 180
        if (int(hsl_color[0]) + plus) > 360:
            hsl_tetradic_second.append(
                [str((int(hsl_color[0]) + plus) - 360), hsl_color[1], hsl_color[2]]
            )
        else:
            hsl_tetradic_second.append(
                [str(int(hsl_color[0]) + plus), hsl_color[1], hsl_color[2]]
            )
    
    hsl_tetradic_third = []
    for hsl_color in hsl_colors:
        plus = 270
        if (int(hsl_color[0]) + plus) > 360:
            hsl_tetradic_third.append(
                [str((int(hsl_color[0]) + plus) - 360), hsl_color[1], hsl_color[2]]
            )
        else:
            hsl_tetradic_third.append(
                [str(int(hsl_color[0]) + plus), hsl_color[1], hsl_color[2]]
            )
    
    hex_tetradic_colors_first = hsl_colors_to_hex(hsl_tetradic_first)
    hex_tetradic_colors_second = hsl_colors_to_hex(hsl_tetradic_second)
    hex_tetradic_colors_third = hsl_colors_to_hex(hsl_tetradic_third)
    return hex_tetradic_colors_first, hex_tetradic_colors_second, hex_tetradic_colors_third
