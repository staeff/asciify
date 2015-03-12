#!/usr/bin/env python
# coding=utf-8

import os
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename
from flask import send_from_directory
from PIL import Image

basedir = os.path.abspath(os.path.dirname(__file__))

UPLOAD_FOLDER = os.path.join(basedir, 'uploads')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
ASCII_PIXELS = "MNHQ$OC?7>!:-;. "

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

@app.route('/asciify/<filename>')
def uploaded_file(filename):
    img = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return convert_image_to_ascii(img)

def convert_image_to_ascii(img):
    ascii_html = '''<html><head><style>span.char {
                    display: inline-block;
                    height: 5px;
                    width: 5px;
                    font-size: 5px;
                    }</style></head><body>'''
    orig_width, orig_height = img.size
    width = 150
    height = width * orig_height / orig_width

    img = img.resize((width, height))
    pixels = img.load()

    for h in xrange(height):
        ascii_html += '<div class="line">'
        for w in xrange(width):
            pixel = list(pixels[w, h])
            if len(pixel) == 3:
                pixel.append(1)
            ascii_char = ASCII_PIXELS[int(sum(pixel[:3]) / 3.0 / 256.0 * 16)]
            ascii_html += '<span class="char" style="color: rgba%s">%s</span>' % (tuple(pixel), ascii_char)

        ascii_html += '</div>\n'
    ascii_html += '</body></html>'

    return ascii_html


if __name__ == '__main__':
    app.run(debug=True)
