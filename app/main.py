from flask import Flask, request, send_file
from matplotlib import image
from rename_file_mock import get_random_string
from detect import detect_color_v02 as dc

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
    image_name = f'{get_random_string()}.png'
    image.save(f'app/resources/{image_name}')
    return 'thanks form your image🦄'


if __name__ == '__main__':
    app.run(debug=True)
