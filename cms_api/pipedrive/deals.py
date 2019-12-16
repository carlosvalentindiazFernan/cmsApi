from .connect_pipedrive import Pipedrive
from cms_api.utils.connect_api import get,post,delete,put

class Deals(Pipedrive):
    """
        PipeDrive Deals Operations
    """

    def get_deals(self,params):
        """ 
            Get deals
        """

        url = f'{self._url()}activities?limit=10' 

        if params.__contains__('user_id'):
            url += f'&user_id={params.get("user_id")}'

        if params.__contains__('filter_id'):
            url += f'&filter_id={params.get("filter_id")}'

        if params.__contains__('type'):
            url += f'&type={params.get("type")}'

        if params.__contains__('done'):
            url += f'&done={params.get("done")}'
        
        if params.__contains__('start'):
            url += f'&start={params.get("start")}'
        else:
            url += f'&start={self._start}'


        url += f'&api_token={self._key()}'

        result,status = get(url)

        data_request = {}

        if status != 200:
           data_request = {
               'success':result.get('success'),
               'menssage': {
                 'error': result.get('error')                               
               }                 
           }
        else:

           data_request = {
               'success':result.get('success'),
               'menssage': result['data']                 
           }
           
        return data_request


    def details_deals(self,id):
        url = f'{self._url()}activities/{id}?api_token={self._key()}'
        


    def post_deals(self):
        """
            Post deals
        """
        return post(f'{self._url()}',None)



    def put_deals(self):
        """
            Put deals
        """
        return put(f'{self._url()}',None,None)



    def delete_deals(self):
        """
            delete deals
        """
        return delete(f'{self._url()}',None,None)



    