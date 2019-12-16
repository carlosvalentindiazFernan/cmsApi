from .connect_pipedrive import Pipedrive
from cms_api.utils.connect_api import get,post,delete,put

class Activities(Pipedrive):
    """
        PipeDrive Activities Operations
    """

    def get_activities(self,params):
        """ 
            Get Activities
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
        return self.parse_status_ok(status,result)           



    def details_activities(self,id):
        """
            Details activity
        """
        url = f'{self._url()}activities/{id}?api_token={self._key()}'
        result,status = get(url)
        return self.parse_status_ok(status,result)           
        
        


    def post_activities(self,data):
        """
            Post Activities
        """
        url = f'{self._url()}activities?api_token={self._key()}'
        result,status = post(url,data)
        return self.parse_status_created(status,result)



    def put_activies(self,id,data):
        """
            Put activities
        """
        url = f'{self._url()}activities/{id}?api_token={self._key()}'
        result,status = put(url,data)
        return self.parse_status_ok(status,result)



    def delete_activies(self,id):
        """
            delete activities
        """
        url = f'{self._url()}activities?ids={id}&api_token={self._key()}'
        result,status = delete(url)
        return self.parse_status_ok(status,result)           
  