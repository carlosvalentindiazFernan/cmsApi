from .connect_api import get
import requests
import os


class Pipedrive:
    """ 
        Pipedrive Connection 
    """    
    
    def __init__(self):
        self.app = None
        self._url = 'http://httpbin.org/get'


    def init_api(self,app):
        self.app = app
        if not (
            app.config.get('PIPEDRIVE_URL')
            or app.config.get('PIPEDRIVE_KEY')
        ):
            raise RuntimeError('Either PIPEDRIVE_URL '
                               'or PIPEDRIVE_KEY needs to be set.')

    def key(self):
        if not (
            os.environ.get('API_KEY')
        ):
            raise RuntimeError('PIPEDRIVE_KEY needs to be set.')
                
        return os.environ.get('API_KEY')


    def url(self):
        if not (
            os.environ.get('PIPEDRIVE_URL')
        ):
            raise RuntimeError('PIPEDRIVE_URL needs to be set.')
                
        return os.environ.get('PIPEDRIVE_URL')

    
    def getActivities(self):
        return get(self._url)