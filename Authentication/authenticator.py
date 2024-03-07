from flask import Flask, request
from flask_restful import Resource, Api, abort, reqparse
from marshmallow import Schema, fields

def create_app(config_filename):
    app = Flask(__name__)
    #app.config.from_pyfile(config_filename)
    api = Api(app)
    api.add_resource(UserDatabase,"/userlist")
    return app


userList = {}

user_fields = {
    'email' : fields.String,
    'name' : fields.String
}

def abort_if_userid_not_found(user_id):
    if user_id not in userList:
        abort(404, message="Could not find user id")

def abort_if_user_exists(user_id):
    if user_id in userList:
        abort(409, message="User already exists, use patch...")

class UserSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Str(required=True)
    create_at = fields.DateTime()

class UserDatabase(Resource):
    def get(self,userid):
        abort_if_userid_not_found(userid)
        return {"data" : "Hello User"}
    
    def put(self,userid):
        abort_if_user_exists(userid)
        data = request.get_json()
        userList[userid] = data
        return userList[userid], 201

    def delete(self,userid):
        abort_if_userid_not_found(userid)
        del userList[userid]
        return '', 204



if __name__ == "__main__":
    app.run(debug=True)