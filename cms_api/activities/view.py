from flask_restful import Resource, Api
from flask import Flask, request, escape
from cms_api.utils.http import Http
from cms_api.middlewares.api_key import api_key
import cms_api

class ActivitiesView(Resource):
    """ 
        Activities Resource
    """
    
    def get(self):
        print(cms_api.pipedriveInit.getActivities())
        resp, code = Http.response({
            'code': 200,
            'message': cms_api.pipedriveInit.getActivities()
        })

        return resp, code, {'Content-Type': 'application/json'}


    @api_key    
    def put(self, todo_id):
        name = request.args.get("name", "World")
        return Http.response({})

