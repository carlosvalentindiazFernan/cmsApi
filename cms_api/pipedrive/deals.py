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

        url = f'{self._url()}deals?limit=10' 

        if params.__contains__('user_id'):
            url += f'&user_id={params.get("user_id")}'

        if params.__contains__('filter_id'):
            url += f'&filter_id={params.get("filter_id")}'
        
        if params.__contains__('start'):
            url += f'&start={params.get("start")}'
        else:
            url += f'&start={self._start}'


        url += f'&api_token={self._key()}'
        result,status = get(url)
        return self.parse_status_ok(status,result)    


    def details_deals(self,id):
        url = f'{self._url()}deals/{id}?api_token={self._key()}'
        result,status = get(url)
        return self.parse_status_ok(status,result)           
        


    def post_deals(self,params):
        """
            Post deals
        """
        url = f'{self._url()}deals?api_token={self._key()}'
        result,status = post(url,params,{
            'Content-Type': 'application/json'
        })
        return self.parse_status_created(status,result)



    def put_deals(self,id,payload):
        """
            Put deals
        """
        url = f'{self._url()}deals/{id}?api_token={self._key()}'
        result,status = put(url,payload,{
            "Content-Type": "application/json",
            "Content-Type": "application/x-www-form-urlencoded"
        })
        return self.parse_status_ok(status,result)



    def delete_deals(self,id):
        """
            delete deals
        """
        url = f'{self._url()}deals/{id}?api_token={self._key()}'
        print(url)
        result,status = delete(url,{
            'Content-Type': 'application/json'
        })
        return self.parse_status_ok(status,result)           



    