from flask import Flask, send_file
from flask import request
from color_detect import detect_colors
from color_detect_v01 import get_colors, get_image


app = Flask(__name__)


@app.route('/api/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('assets/uploaded_image.jpg')
        get_colors(get_image('assets/uploaded_image.jpg'), 8, True)
        # detect_colors('assets/uploaded_image.jpg')
        # return send_file('assets/color_analysis_report.png', mimetype='image/png')
