from flask import Flask, Response, request, render_template, redirect, url_for
from detect import detect_color as dc
from detect import color
import os


IMAGE_DIR = 'app/static/images/uploaded/'
TMP_IMAGE_NAME = 'tmpname.jpg'
TMP_IMAGE_PATH = f'{IMAGE_DIR}{TMP_IMAGE_NAME}'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index() -> Response:
    """open page with color wheel and upload image button

    Returns:
        Response: index.html page with color wheel and random selected color
    """
    return redirect(url_for('select_color', selected_color=color.get_random_color()))


@app.route('/color/<string:selected_color>', methods=['GET'])
def select_color(selected_color: str) -> str:
    """open page with color wheel and upload image button

    Returns:
        str: index.html page whith color wheel
    """
    images_names = color.get_images_by_color(selected_color)
    images_lists = list(split_list(images_names, 3))
    return render_template(
        'index.html',
        first_column=images_lists[0],
        second_column=images_lists[1],
        third_column=images_lists[2]
    )


def split_list(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))


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
    hex_colors = color.get_hex_colors_from_name(image_path)
    
    comp_colors = color.get_complementary_palette(image_path)
    
    triadic_colors_first, triadic_colors_second = color.get_triadic_palette(image_path)
    
    tetradic_colors_first, tetradic_colors_second, tetradic_colors_third = color.get_tetradic_palette(image_path)
    print(triadic_colors_first)
    return render_template(
        'uploaded.html', 
        image_path=image_path,
        first_color=hex_colors[0],
        second_color=hex_colors[1],
        third_color=hex_colors[2],
        fourth_color=hex_colors[3],
        fifth_color=hex_colors[4],
        
        # complementary
        first_comp_color=comp_colors[0],
        second_comp_color=comp_colors[1],
        third_comp_color=comp_colors[2],
        fourth_comp_color=comp_colors[3],
        fifth_comp_color=comp_colors[4],
        
        # triadic
        first_tri_color_one=triadic_colors_first[0],
        second_tri_color_one=triadic_colors_first[1],
        third_tri_color_one=triadic_colors_first[2],
        fourth_tri_color_one=triadic_colors_first[3],
        fifth_tri_color_one=triadic_colors_first[4],
        
        first_tri_color_two=triadic_colors_second[0],
        second_tri_color_two=triadic_colors_second[1],
        third_tri_color_two=triadic_colors_second[2],
        fourth_tri_color_two=triadic_colors_second[3],
        fifth_tri_color_two=triadic_colors_second[4],
        
        # tetradic
        first_tetr_color_one=tetradic_colors_first[0],
        second_tetr_color_one=tetradic_colors_first[1],
        third_tetr_color_one=tetradic_colors_first[2],
        fourth_tetr_color_one=tetradic_colors_first[3],
        fifth_tetr_color_one=tetradic_colors_first[4],
        
        first_tetr_color_two=tetradic_colors_second[0],
        second_tetr_color_two=tetradic_colors_second[1],
        third_tetr_color_two=tetradic_colors_second[2],
        fourth_tetr_color_two=tetradic_colors_second[3],
        fifth_tetr_color_two=tetradic_colors_second[4],
        
        first_tetr_color_three=tetradic_colors_third[0],
        second_tetr_color_three=tetradic_colors_third[1],
        third_tetr_color_three=tetradic_colors_third[2],
        fourth_tetr_color_three=tetradic_colors_third[3],
        fifth_tetr_color_three=tetradic_colors_third[4]
        )


def allowed_file(filename: str):
    """check the file has correct extencion

    Args:
        filename (str): uploaded image name
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(debug=True)
