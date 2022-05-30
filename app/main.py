from tkinter import image_names
from xmlrpc.client import Boolean
from flask import Flask, Response, request, render_template, flash, redirect, url_for
from detect import detect_color as dc
import os
from detect import color


TMP_IMAGE_NAME = 'tmpname.jpg'
TMP_IMAGE_PATH = f'app/static/images/uploaded/{TMP_IMAGE_NAME}'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app = Flask(__name__)


@app.route('/')
def index() -> str:
    """open page with color wheel and upload image button

    Returns:
        str: index.html page whith color wheel
    """
    return render_template('index.html')


def allowed_file(filename: str):
    """check the file has correct extencion

    Args:
        filename (str): uploaded image name
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['POST'])
def upload() -> Response:
    """upload new image and redirect to iploaded image page

    Returns:
        Response: responce with uploaded image page
    """
    if request.method == 'POST':
        # if image not in request -> redirect to color wheel
        if 'image' not in request.files:
            return redirect(url_for('index'))
        
        # get image from request
        image = request.files['image']
        
        # if image has an empty file name -> redirect to color wheel
        if image.filename == '':
            return redirect(url_for('index'))
        
        if image and allowed_file(image.filename):
            # save image with temporary name
            image.save(TMP_IMAGE_PATH)
            # get hsl colors from image
            image_hsl_colors: list = dc.get_hsl_colors(
                image_path=TMP_IMAGE_PATH,
                number_of_colors=5
            )
            # create image name with hsl colors
            hsl_image_name = '_'.join(image_hsl_colors) + '.jpg'
            # rename from temporary name to hsl name 
            image_path = TMP_IMAGE_PATH.replace(TMP_IMAGE_NAME, f'{hsl_image_name}')
            os.rename(f'{TMP_IMAGE_PATH}', f'{image_path}')
            
            return redirect(url_for('uploaded', image_path=hsl_image_name))


@app.route('/uploaded/<string:image_path>', methods=['GET'])
def uploaded(image_path: str) -> str:
    """send page with uploaded image

    Args:
        image_path (str): path to image

    Returns:
        str: uploaded.html page with uploaded image
    """
    hex_colors = color.get_hex_colors_from_name(image_path.split('.jpg')[0])
    print(hex_colors)
    return render_template(
        'uploaded.html', 
        image_path=image_path,
        first_color=hex_colors[0],
        second_color=hex_colors[1],
        third_color=hex_colors[2],
        fourth_color=hex_colors[3],
        fifth_color=hex_colors[4]
        )


if __name__ == '__main__':
    app.run(debug=True)
