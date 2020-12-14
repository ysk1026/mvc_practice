from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from com_mini_api.ext.db import url, db
from com_mini_api.ext.routes import initialize_routes

app = Flask(__name__)
CORS(app, resources={r'/api/*': {"origins": "*"}})

app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
api = Api(app)

with app.app_context():
    db.create_all()
    
print('********** INITIALIZE **********')
initialize_routes(api)