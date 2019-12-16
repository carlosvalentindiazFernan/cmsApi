from cms_api.utils.http import Http
from cms_api.middlewares.api_key import api_key
import requests


def get(url):
    r = requests.get(url)
    return {'demo':'demo'}


def post(url,params):
    """ Posr options """
    return 'post'


def delete(url,params,id):
    return 'delete'


def put(url,params,id):
    return 'Update'


