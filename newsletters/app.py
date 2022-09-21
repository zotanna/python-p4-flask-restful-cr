#!/usr/bin/env python3

from flask import Flask, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/newsletters.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class Index(Resource):

    def get(self):
        response_dict = {
            "index": "Welcome to the Newsletter RESTful API",
        }
        
        response = make_response(
            jsonify(response_dict),
            200
        )
        return response

api.add_resource(Index, '/')


# @app.route('/games')
# def games():

#     games = []
#     for game in Game.query.all():
#         game_dict = {
#             "title": game.title,
#             "genre": game.genre,
#             "platform": game.platform,
#             "price": game.price,
#         }
#         games.append(game_dict)

#     response = make_response(
#         jsonify(games),
#         200,
#         headers={
#             "Content-Type": "application/json",
#         }
#     )

#     return response

# @app.route('/games/<int:id>')
# def game_by_id(id):
#     game = Game.query.filter_by(id=id).first()
    
#     game_dict = game.to_dict()

#     response = make_response(
#         jsonify(game_dict),
#         200
#     )
#     response.headers["Content-Type"] = "application/json"

#     return response

# @app.route('/reviews')
# def reviews():

#     reviews = []
#     for review in Review.query.all():
#         review_dict = review.to_dict()
#         reviews.append(review_dict)

#     response = make_response(
#         jsonify(reviews),
#         200
#     )
#     response.headers["Content-Type"] = "application/json"

#     return response

# @app.route('/users')
# def users():

#     users = []
#     for user in User.query.all():
#         user_dict = user.to_dict()
#         users.append(user_dict)

#     response = make_response(
#         jsonify(users),
#         200
#     )
#     response.headers["Content-Type"] = "application/json"

#     return response

if __name__ == '__main__':
    app.run()