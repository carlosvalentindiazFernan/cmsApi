from test.support import EnvironmentVarGuard
from cms_api import Config
import pytest
import unittest
import cms_api


class ActivitiesUniTest(unittest.TestCase):
    def setUp(self):
        self.env = EnvironmentVarGuard()
        self.env.set('API_KEY', 'value')
        self.env.set('API_URL', 'value')
        self.env.set('VAR', 'value')

        self._app = cms_api.create_app(Config)


    def test_hello_world(self):
        print(self._app)
        self.assertEqual(200, 200)
