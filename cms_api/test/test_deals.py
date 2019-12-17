from test.support import EnvironmentVarGuard
from cms_api import Config
import pytest
import unittest
import cms_api
import json

class DealsUniTest(unittest.TestCase):
    """ deals Uni test """

    def setUp(self):
        self.env = EnvironmentVarGuard()
        self.env.set('API_KEY', 'd2ba482a9eb656728b4d22ba89f1437ba6732f16')
        self.env.set('API_URL', 'https://api.pipedrive.com/v1/')
        self._url = 'http://127.0.0.1:5000/api/v1'
        self._app = cms_api.create_app(Config)
        self.app = self._app.test_client()
        self.app.testing = True


    def test_all_deals(self):
        response = self.app.get(f'{self._url}/deals')        
        self.assertEqual(response.status_code,200)


    def test_deals_by_id(self):
        response = self.app.get(f'{self._url}/deals/1')        
        self.assertEqual(response.status_code,200)


    def test_create_deals_error(self):
        item = {"demo": "some_item"}
        response = self.app.post(f'{self._url}/deals',
                                 data=json.dumps(item),
                                 content_type='application/json')
    
        data = json.loads(response.get_data())
        self.assertEqual(data['status'], False)
        self.assertEqual(response.status_code, 400)


    def test_create_deals(self):
        item = {"title": "some_activity"}
        response = self.app.post(f'{self._url}/deals',
                                 data=json.dumps(item),
                                 content_type='application/json')
    
        data = json.loads(response.get_data())
        self.assertEqual(data['status'], True)
        self.assertEqual(response.status_code, 201)


    def test_update_deal(self):
        item = {
            "title": "demo_update",
            "user_id": "1"
        }
        response = self.app.put(f'{self._url}/deals/1',
                                 data=json.dumps(item),
                                 content_type='application/json')
        data = json.loads(response.get_data())
        self.assertEqual(data['status'], True)
        self.assertEqual(response.status_code,200)


    def test_delete_deal(self):
        response = self.app.delete(f'{self._url}/deals/1')        
        data = json.loads(response.get_data())
        self.assertEqual(data['status'], True)
        self.assertEqual(response.status_code,200)

