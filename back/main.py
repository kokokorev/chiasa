from flask import Flask, request
from detect import detect_color as dc
import os

app = Flask(__name__)


@app.route('/upload')
def upload_file() -> str:
    """method for send upload image form

    Returns:
        str: temp string before i write image upload form
    """
    return 'upload image, please🙏'


@app.route('/uploader', methods=['POST'])
def uploader_file() -> str:
    """method fot upload and save image

    TODO:
        write image uploader form

    Returns:
        str: temp string before i write image uploader form
    """
    image = request.files['image']
    
    dir_path = 'back/resources/'
    temp_image_name = 'tmpname'
    image.save(f'{dir_path}{temp_image_name}.jpg')
    
    image_hex_colors: list = dc.get_hex_colors(
        image_path=f'{dir_path}{temp_image_name}.jpg',
        number_of_colors=5
    )
    hex_image_name = ''.join(image_hex_colors)
    os.rename(f'{dir_path}{temp_image_name}.jpg', f'{dir_path}{hex_image_name}.jpg')
    return 'thanks form your image🦄'


if __name__ == '__main__':
    app.run(debug=True)
