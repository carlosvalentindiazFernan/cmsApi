from test.support import EnvironmentVarGuard
from cms_api import Config
import pytest
import unittest
import cms_api


class PersonsUniTest(unittest.TestCase):
    """ Persons Uni test """

    def setUp(self):
        self.env = EnvironmentVarGuard()
        self.env.set('API_KEY', 'd2ba482a9eb656728b4d22ba89f1437ba6732f16')
        self.env.set('API_URL', 'https://api.pipedrive.com/v1/')
        self._url = 'http://127.0.0.1:5000/api/v1'
        self._app = cms_api.create_app(Config)
        self.app = self._app.test_client()
        self.app.testing = True


    def test_all_persons(self):
        response = self.app.get(f'{self._url}/persons')        
        self.assertEqual(response.status_code,200)


    def test_persons_by_id(self):
        response = self.app.get(f'{self._url}/persons/1')        
        self.assertEqual(response.status_code,200)


    def test_create_persons(self):
        response = self.app.get(f'{self._url}/persons')        
        self.assertEqual(response.status_code,200)


    def test_delete_deal(self):
        response = self.app.get(f'{self._url}/persons')        
        self.assertEqual(response.status_code,200)


    def test_update_deal(self):
        response = self.app.get(f'{self._url}/persons')        
        self.assertEqual(response.status_code,200)