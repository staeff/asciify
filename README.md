# asciify

This app allows the upload of image files ('png', 'jpeg', 'jpg', 'gif'). The image gets stored on the server and an ascii-representation of the image 
get created.
The app is build with flask

## Installation

* optional: create a virtualenv
* Install flask, etc. `$ pip install -r requirements`
* create folder 'uploads'

## Run the app

* python app.py

## Bugs and Problems

* Filenames are checked literal, currently just lowercase. Make it work for different variation.
* Is it possible to check for the actual file contents with something similar to the `file` command?
* gifs give an error.

## Further ideas/ToDo

* setup production deployment (gunicorn with apache or nginx)
* create thumbnails of the images and show them on the startpage
* choose if colored or b/w ascii art
* save ascii art locally
* copy ascii art to clipboard
* users (save ascii art, bla und blubb)

