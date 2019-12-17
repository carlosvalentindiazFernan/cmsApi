import time
import os
from flask import request, jsonify


class Http:
    """
    Http custom class
    """

    @staticmethod
    def response(data={}):
        """
        Create standarized response object
        """

        code = data['code'] if 'code' in data else 200
        status = data['success'] if 'success' in data else True
        message = data['message'] if 'message' in data else ''
        service = data['object'] if 'object' in data else os.environ.get('APP_NAME')
        route = request.path

        info = {
            "service": service,
            "code": code,
            "status": status,
            "message": message,
            "request": int(time.time()),
            "url": route
        }

        if 'data' in data:
            info['data'] = data['data']

        return (info), code


    @staticmethod
    def pipe_response(status=200,data={}):
        resp, code = Http.response({
            'code': status,
            'success': data['success'],
            'message': data['menssage']
        })
        return resp, code, {'Content-Type': 'application/json'}
        