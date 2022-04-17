from flask import Flask, request
from detect import detect_color as dc

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
    image_hex_colors: list = dc.get_hex_colors(
        image=dc.convert_image(image),
        number_of_colors=5
    )
    image_name = ''.join(image_hex_colors)
    image.save(f'app/resources/{image_name}.jpg')
    return 'thanks form your image🦄'


if __name__ == '__main__':
    app.run(debug=True)
