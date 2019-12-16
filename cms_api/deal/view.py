from flask_restful import reqparse, abort, Api, Resource
from flask import Flask, request, escape
from cms_api.utils.http import Http
from cms_api.middlewares.api_key import api_key
from cms_api.pipedrive.deals import Deals


deal_pipedrive = Deals()

class DealView(Resource):
    """
        Deal Resource 
    """

    def get(self):
        query = {}
        data =  deal_pipedrive.get_deals(query)
        return Http.pipe_response(200,data)
    

    def post(self):
        data = request.json
        title = data.get('title')

        if title :
            response_data =  deal_pipedrive.post_deals(data)
            return Http.pipe_response(201,response_data)
        else:
            return Http.response({
                'code': 400,
                'success': False,
                'message': {'error':  'Error request data'}
            })    


class DealsDetailVIew(Resource):
    """
        Deal Detail by id
    """

    def get(self,deal_id):
        data =  deal_pipedrive.details_deals(deal_id)
        return Http.pipe_response(200,data)


    def put(self, deal_id):
        data = request.json

        if data:
            response_data = deal_pipedrive.put_deals(deal_id,data)
            return Http.pipe_response(200,response_data)
        else:
            return Http.response({
                'code': 400,
                'success': False,
                'message': {'error':  'Error request data'}
            })    




    def delete(self,deal_id):
        data =  deal_pipedrive.delete_deals(deal_id)
        return Http.pipe_response(200,data)

    