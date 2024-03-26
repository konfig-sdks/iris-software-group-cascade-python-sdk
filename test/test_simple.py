# coding: utf-8

"""
    HR API

    <a href='swaggerv2.json'>Download Swagger Json in OAS2 Format.</a>

    The version of the OpenAPI document: 2
    Contact: hrapi@iris.co.uk
    Created by: https://help.iris.co.uk/hr/cascade/api/
"""

import unittest

import os
from pprint import pprint
from iris_software_group_cascade_python_sdk import IrisSoftwareGroupCascade

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        irissoftwaregroupcascade = IrisSoftwareGroupCascade(
        
            client_id = 'YOUR_CLIENT_ID',
            client_secret = 'YOUR_CLIENT_SECRET',
        )
        self.assertIsNotNone(irissoftwaregroupcascade)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
