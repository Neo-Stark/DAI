#./flask/app.py

from flask import (Flask, send_from_directory, url_for, request,send_file, render_template)
from fractal_mandelbrot import fractal_mandelbrot
from img_pil import serve_pil_image
import os.path
import random
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/user/<username>')
def mostrarPerfil(username):
    return 'Usuario %s' % username

@app.route('/fractal')
def fractal():
    # filelist = os.listdir('./')
    # # for x in filelist:
    # #     if x.endswith(".png"):
    # #         try:
    # #             with open(Path + x, "w") as y:
    #                 if os.path.getctime(x)+2629746 > 

    if len(request.args)>0 and all (k in request.args for k in ('xa','xb','ya','yb','size')):
        filename = 'f'+request.args.get('xa')+request.args.get('xb')+request.args.get('ya')+request.args.get('yb')+request.args.get('size')+'.png'
        xa = float(request.args.get('xa'))
        xb = float(request.args.get('xb'))
        ya = float(request.args.get('ya'))
        yb = float(request.args.get('yb'))
        size = int(request.args.get('size'))
        if not os.path.exists('static/img/' + filename):
            image = fractal_mandelbrot(xa,ya,xb,yb,size)
            image.save(filename)
        else:
            return send_file(filename)
    else:
        image = fractal_mandelbrot()
        image.save('static/img/f-2-1.51.01.5256.png')

    return serve_pil_image(image)


@app.route('/svg')
def svg():
    figura = random.randrange(3)
    return render_template('svg.html', figura=figura)


@app.errorhandler(404)
def page_not_found(error):
    return "404 - Página no encontrada", 404