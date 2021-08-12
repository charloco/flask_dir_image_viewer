from flask import *
import os
from os.path import isfile

app = Flask(__name__)
header = '''
<!DOCTYPE html>
<html lang="en">

 <head>
 <title>png image viewer</title>
 </head>
  <body>
  <table>
  <tbody><tr><td>
  <ul>
'''
ender = '''
  </tr></tbody>
  </table></body>
'''

@app.route("/")
def index():
    template = "<li><a href=show/%s>%s</a></li>"
    entries = os.listdir()
    links = []
    for entry in entries:
        if isfile(entry) and entry.endswith("png"):
            links.append(template%(entry,entry))
    return header + "\n".join(links) + "</ul></td>" + ender
@app.route("/show/<image_name>")
def show_image(image_name):
    template = "<li><a href=/show/%s>%s</a></li>"
    entries = os.listdir()
    links = []
    for entry in entries:
        if isfile(entry) and entry.endswith("png"):
            links.append(template%(entry,entry))
    return header + "\n".join(links) + "</ul></td>" +"<td><img src=/image/%s></td>"%image_name + ender
@app.route("/image/<image_name>")
def send_image(image_name):
    return send_file(image_name, mimetype='image/png')

app.run(host="0.0.0.0", port=8090)
