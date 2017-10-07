

from flask import Flask
from flask_restful import Resource, Api
from flask import request
from flask import render_template
from flask import Response

from chiplotle import *
import sys

app = Flask(__name__)
api = Api(app)
plotter = instantiate_plotters( )[0]



@api.representation('text/html')
class index(Resource):
    def get(self):
        resp = Response( render_template('index.html'), mimetype='text/html')
        return resp




class drawPixel(Resource):
    def get(self):
        x = int(request.args.get('x', ''))
        y = int(request.args.get('y', ''))
        #plotter.write(hpgl.PU([(x,y)]))
        plotter.write(hpgl.PD([(x,y)]))
        #plotter.write(hpgl.PU([(x,y)]))


class goToPixel(Resource):
    def get(self):
        x = int(request.args.get('x', ''))
        y = int(request.args.get('y', ''))
        #plotter.write(hpgl.PU([(x,y)]))
        plotter.write(hpgl.PD([(x,y)]))






api.add_resource(index, '/')
api.add_resource(drawPixel, '/drawPixel')
api.add_resource(goToPixel, '/goToPixel')


if __name__ == '__main__':
    args = sys.argv


    app.run(host='192.168.0.79',port=5000,debug=True)
