from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from resources.item import Item, ItemList
from resources.user import UserRegister
from security import authenticate, identity

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'MY_SECRET_KEY'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth

# class Student(Resource):
#     def get(self, name):
#         return {'student': name}

# api.add_resource(Student, '/student/<string:name>')

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(host='127.0.0.1', port=5001, debug=True)
