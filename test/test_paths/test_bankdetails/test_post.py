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
from iris_software_group_cascade_python_sdk.paths.bankdetails import post
from iris_software_group_cascade_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestBankdetails(ApiTestMixin, unittest.TestCase):
    """
    Bankdetails unit test stubs
        Creates a Bank Details.
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200


































if __name__ == '__main__':
    unittest.main()
