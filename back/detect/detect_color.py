from cv2 import FileStorage
from numpy import ndarray
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import cv2
from collections import Counter
import numpy as np
import io


def get_hex_colors(image_path: str, number_of_colors: int) -> list:
    """get hex colors from image with computer vision

    Args:
        image (ndarray): image for color detection
        number_of_colors (int): number of color to clustering

    Returns:
        list: hex colors list
    """
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # resize image to precess fewer pixels
    modified_image = cv2.resize(src=image, 
                                dsize=(600, 400), 
                                interpolation = cv2.INTER_AREA)
    # reshape image to 2 dimension array
    modified_image = modified_image.reshape(modified_image.shape[0] * modified_image.shape[1], 3)

    clf = KMeans(n_clusters=number_of_colors)
    labels = clf.fit_predict(modified_image)
    counts = Counter(labels)
    center_colors = clf.cluster_centers_
    
    # get ordered colors by iterating through the keys
    ordered_colors = [center_colors[i] for i in counts.keys()]
    # convert rgn array to hex colors
    hex_colors = [rgb_to_hex(ordered_colors[i]) for i in counts.keys()]
    
    # print colors to console for debug
    rgb_colors = [ordered_colors[i] for i in counts.keys()]
    for i in rgb_colors:
        print(
            get_color_for_console(
                int(i[0]), 
                int(i[1]), 
                int(i[2]), 
                True)
            + '       ' 
            + '\033[0m') 
    
    return hex_colors


def rgb_to_hex(color: ndarray) -> str:
    """convert rgb (ndarray) to hex color code

    Args:
        color (ndarray): rgb color

    Returns:
        str: hex code
    """
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))


def get_color_for_console(r: int, g: int, b: int, background=False) -> str:
    return '\033[{};2;{};{};{}m'.format(48 if background else 38, r, g, b)
