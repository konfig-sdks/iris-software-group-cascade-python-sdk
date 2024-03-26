# coding: utf-8

"""
    HR API

    <a href='swaggerv2.json'>Download Swagger Json in OAS2 Format.</a>

    The version of the OpenAPI document: 2
    Contact: hrapi@iris.co.uk
    Created by: https://help.iris.co.uk/hr/cascade/api/
"""

import unittest
from unittest.mock import patch

import urllib3

import iris_software_group_cascade_python_sdk
from iris_software_group_cascade_python_sdk.paths.publicholidays import get
from iris_software_group_cascade_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestPublicholidays(ApiTestMixin, unittest.TestCase):
    """
    Publicholidays unit test stubs
        Gets a set of Public Holidays with locations.
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200


































if __name__ == '__main__':
    unittest.main()
