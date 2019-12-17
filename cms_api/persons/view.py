from flask_restful import reqparse, abort, Api, Resource
from flask import Flask, request, escape
from cms_api.utils.http import Http
from cms_api.middlewares.api_key import api_key
from cms_api.pipedrive.persons import Persons
import cms_api

persons = Persons()

class PersonsView(Resource):
    """ 
        Activities Resource
    """
    
    def get(self):
        """
            Get All Persons
        """
        query = {}
        data =  persons.get_persons(query)
        return Http.pipe_response(200,data)


    def post(self):
        """
            Create Persons
        """
        data = request.json
        name = data.get('name')

        if name :
            response_data =  persons.post_persons(data)
            return Http.pipe_response(201,response_data)
        else:
            return Http.response({
                'code': 400,
                'success': False,
                'message': {'error':  'Error request data'}
            })


class PersonsDetailView(Resource):
    """ Person Detail View """

    def get(self,person_id):
        """ 
            Get Persons By id
        """
        data =  persons.details_persons(person_id)
        return Http.pipe_response(200,data)


    def delete(self,person_id):
        """
            Delete Persons View 
        """
        data =  persons.delete_persons(person_id)
        return Http.pipe_response(200,data)


    def put(self, activity_id):
        """
            Update Activities
        """ 
        data = request.json

        if data:
            data_persons =  persons.put_persons(activity_id,data)
            return Http.pipe_response(200,data_persons)
        else:
            return Http.response({
                'code': 400,
                'success': False,
                'message': {'error':  'Error request data'}
            })


class PersonsActivitiesView(Resource):
    """
        List activities associated with a person
    """

    def get(self,person_id):
        """
            get associated with a person
        """
        data =  persons.get_persons_activities(person_id,{})
        return Http.pipe_response(200,data)



class PersonsDealsView(Resource):
    """
        List deals associated with a person
    """

    def get(self,person_id):
        """
            get associated with a person
        """
        data = persons.get_persons_deals(person_id,{})
        return Http.pipe_response(200,data)
