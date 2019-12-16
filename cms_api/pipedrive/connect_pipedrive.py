from cms_api.utils.connect_api import get, post, delete, put
import requests
import os


class Pipedrive:
    """ 
        Pipedrive Connection 
    """    
    
    def __init__(self):
        self.app = None
        self._limit = 20
        self._start = 0


    def init_api(self,app):
        self.app = app
        if not (
            app.config.get('PIPEDRIVE_URL')
            or app.config.get('PIPEDRIVE_KEY')
        ):
            raise RuntimeError('Either PIPEDRIVE_URL '
                               'or PIPEDRIVE_KEY needs to be set.')

    def _key(self):
        if not (
            os.environ.get('API_KEY')
        ):
            raise RuntimeError('PIPEDRIVE_KEY needs to be set.')
                
        return os.environ.get('API_KEY')


    def _url(self):
        if not (
            os.environ.get('API_URL')
        ):
            raise RuntimeError('API_URL needs to be set.')
                
        return os.environ.get('API_URL')

    
    def parse_status_ok(self,status,result):
        """
            Pase status ok 200
        """
        if status != 200:
           return {
               'success':result.get('success'),
               'menssage': {
                 'error': result.get('error')                               
               }                 
           }
        else:
           return {
               'success':result.get('success'),
               'menssage': result['data']                 
           }
        
    
    def parse_status_created(self,status,result):
        """
            Pase status created 201
        """
        if status != 201:
           return {
               'success':result.get('success'),
               'menssage': {
                 'error': result.get('error')                               
               }                 
           }
        else:
           return {
               'success':result.get('success'),
               'menssage': result['data']                 
           }
           
