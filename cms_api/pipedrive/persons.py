from .connect_pipedrive import Pipedrive
from cms_api.utils.connect_api import get,post,delete,put

class Persons(Pipedrive):
    """ 
        Persons Pipedriv Operations
    """

    def get_persons(self,params):
        """ Get persons """
        url = f'{self._url()}persons?limit=10' 

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


    def details_persons(self,id):
        """ 
            Get details persons 
        """
        url = f'{self._url()}persons/{id}?api_token={self._key()}'
        result,status = get(url)
        return self.parse_status_ok(status,result)           
                


    def post_persons(self,payload):
        """ 
            Post persons 
        """
        url = f'{self._url()}persons?api_token={self._key()}'
        result,status = post(url,payload,{
            'Content-Type': 'application/json'
        })
        return self.parse_status_created(status,result)


    def put_persons(self):
        """
            Put persons
        """
        return put(f'{self._url()}',None,None)



    def delete_persons(self,id):
        """
            delete persons
        """
        url = f'{self._url()}persons?ids={id}&api_token={self._key()}'
        result,status = delete(url,{
            'Content-Type': 'application/json'
        })
        return self.parse_status_ok(status,result)           
  

    def get_persons_activities(self,id,params):
        """
            List activities associated with a person
        """

        url = f'{self._url()}persons/{id}/activities?limit=20&done=0&api_token={self._key()}'
        if params.__contains__('start'):
            url += f'$start={params.get("start")}'
        else:
            url += f'&start={self._start}'
        

        result,status = get(url)
        return self.parse_status_ok(status,result)           


    def get_persons_deals(self,id,params):
        """
            List deals associated with a person
        """

        url = f'{self._url()}persons/{id}/deals?limit=20&done=0&api_token={self._key()}'

        if params.__contains__('start'):
            url += f'$start={params.get("start")}'
        else:
            url += f'&start={self._start}'
        
        result,status = get(url)
        return self.parse_status_ok(status,result)           
