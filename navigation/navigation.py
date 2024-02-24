from flask import Flask
from flask_restful import Resource, Api, abort, reqparse
from marshmallow import Schema, fields

app = Flask(__name__)
app = Api(app)



class Navigation(Resource):
    def __init__(self) -> None:
        super().__init__()
        self.speed_limit = 0
    def get(self):
        return self

def abort_if_step_not_found(step_id):
    if step_id not in direction_steps:
        abort(404,message="Direction Step {} doesn't exist".format(step_id))

class Journey(Resource):
    def get(self):
        pass

    def put(self):
        pass
    
    def post(self):
        pass

    def delete(self):
        """Stops the journey and deletes it"""
        pass

direction_steps = []

class DirectionStepSchema(Schema):
    direction= fields.Str(required=True)
    distance = fields.Float(required=True)
    create_at = fields.DateTime()

class Direction(Resource):
    
    def get(self, step_id):
        abort_if_step_not_found(step_id)
        return direction_steps[step_id]
    
    def post(self,step_id):
        

    
        

class DirectionList(Resource):
    def get(self):
        return direction_steps
    
    def post(self):
        ''''''