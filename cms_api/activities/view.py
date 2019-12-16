from flask_restful import reqparse, abort, Api, Resource
from flask import Flask, request, escape
from cms_api.utils.http import Http
from cms_api.middlewares.api_key import api_key
import cms_api


class ActivitiesView(Resource):
    """ 
        Activities Resource
    """
    
    def get(self):
        """
            Get All activities
        """
        query = {}
        activities =  cms_api.pipe_activities.get_activities(query)
        return Http.pipe_response(200,activities)


    def post(self):
        """
            Create Activities
        """
        data = request.json
        subject = data.get('subject')
        type_activity = data.get('type')
        done = data.get('done')

        if subject and type_activity and done:
            activities =  cms_api.pipe_activities.post_activities(data)
            return Http.pipe_response(201,activities)
        else:
            return Http.response({
                'code': 400,
                'success': False,
                'message': {'error':  'Error request data'}
            })




class ActivityView(Resource):
    """
        Activity View
    """

    def get(self,activity_id):
        activities =  cms_api.pipe_activities.details_activities(activity_id)
        return Http.pipe_response(200,activities)



    def delete(self,activity_id):
        """
            Delete Activities View 
        """
        activities =  cms_api.pipe_activities.delete_activies(activity_id)
        return Http.pipe_response(200,activities)



    def put(self, activity_id):
        """
            Update Activities
        """ 
        data = request.json
        subject = data.get('subject')
        type_activity = data.get('type')
        done = data.get('done')

        if subject and type_activity and done:
            activities =  cms_api.pipe_activities.put_activies(activity_id,data)
            return Http.pipe_response(201,activities)
        else:
            return Http.response({
                'code': 400,
                'success': False,
                'message': {'error':  'Error request data'}
            })


