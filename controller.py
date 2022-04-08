from flask import Flask, send_file
from flask import request
from color_detect import detect_colors


app = Flask(__name__)


@app.route('/api/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('images/uploaded_image.jpg')
        detect_colors('images/uploaded_image.jpg')
        return send_file('images/color_analysis_report.png', mimetype='image/png')
