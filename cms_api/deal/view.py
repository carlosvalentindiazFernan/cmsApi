from flask_restful import Resource, Api
from flask import Flask, request, escape

class DealView(Resource):
    """
        Deal Resource 
    """

    def get(self):
        return {'Deal': 'world'}
    
    
    def put(self, todo_id):
        name = request.args.get("name", "World")
        return f'Deal, {escape(name)}!'

