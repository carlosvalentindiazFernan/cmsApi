from test.support import EnvironmentVarGuard
from cms_api import Config
import pytest
import unittest
import cms_api
import json

class ActivitiesUniTest(unittest.TestCase):
    """ Activities Uni test """

    def setUp(self):
        self.env = EnvironmentVarGuard()
        self.env.set('API_KEY', 'd2ba482a9eb656728b4d22ba89f1437ba6732f16')
        self.env.set('API_URL', 'https://api.pipedrive.com/v1/')
        self._url = 'http://127.0.0.1:5000/api/v1'
        self._app = cms_api.create_app(Config)
        self.app = self._app.test_client()
        self.app.testing = True


    def test_all_activities(self):
        response = self.app.get(f'{self._url}/activities')        
        self.assertEqual(response.status_code,200)


    def test_activities_by_id(self):
        response = self.app.get(f'{self._url}/activities/1')        
        self.assertEqual(response.status_code,200)


    def test_create_activities_error(self):
        item = {"demo": "some_item"}
        response = self.app.post(f'{self._url}/activities',
                                 data=json.dumps(item),
                                 content_type='application/json')
    
        data = json.loads(response.get_data())
        self.assertEqual(data['status'], False)
        self.assertEqual(response.status_code, 400)


    def test_create_activities_success(self):
        item = {
            "subject": "gatoa",
            "type": "call",
            "done": "0"
        }
        response = self.app.post(f'{self._url}/activities',
                                 data=json.dumps(item),
                                 content_type='application/json')
        data = json.loads(response.get_data())
        self.assertEqual(data['status'], True)
        self.assertEqual(response.status_code, 201)



    def test_delete_activity(self):
        response = self.app.delete(f'{self._url}/activities/1')        
        data = json.loads(response.get_data())
        self.assertEqual(data['status'], True)
        self.assertEqual(response.status_code,200)


    def test_update_activity(self):
        item = {
            "subject": "demo",
            "done": "0"
        }
        response = self.app.put(f'{self._url}/activities/1',
                                 data=json.dumps(item),
                                 content_type='application/json')
        data = json.loads(response.get_data())
        self.assertEqual(data['status'], True)
        self.assertEqual(response.status_code,200)
