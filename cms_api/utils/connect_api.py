from cms_api.utils.http import Http
from cms_api.middlewares.api_key import api_key
import requests
import json

def get(url,_headers={}):
    r = requests.get(url)
    return (r.json(),r.status_code)


def post(url,payload, _headers = {}):
    """ Posr options """
    r = requests.post(
        url,
        data=json.dumps(payload),
        headers=_headers
    )
    return (json.loads(r.content),r.status_code)


def delete(url,_headers={}):
    """ Delete request opttions """
    r = requests.delete(url)
    return (json.loads(r.content),r.status_code)


def put(url,payload,_headers={}):
    """ Update reques """
    r = requests.put(
        url, 
        data=json.dumps(payload),
        headers=_headers
    )
    return ({"data":{}},r.status_code)