from flask import Flask, request
from rename_file_mock import get_random_string

app = Flask(__name__)


@app.route('/upload')
def upload_file() -> str:
    """
    method for send upload image form

    TODO: write image upload form

    Returns: str(): temp string before i write image upload form
    """
    return 'upload image, please🙏'


@app.route('/uploader', methods=['POST'])
def uploader_file() -> str:
    """
    method fot upload and save image

    TODO: write image uploader form

    Returns: str(): temp string before i write image uploader form
    """
    print(request.files)
    file = request.files['image']
    file.save(f'assets/{get_random_string()}.jpg')
    return 'thanks form your image🦄'


if __name__ == '__main__':
    app.run(debug=True)
