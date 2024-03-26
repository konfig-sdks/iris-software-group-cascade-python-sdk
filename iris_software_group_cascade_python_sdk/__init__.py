# coding: utf-8

# flake8: noqa

"""
    HR API

    <a href='swaggerv2.json'>Download Swagger Json in OAS2 Format.</a>

    The version of the OpenAPI document: 2
    Contact: hrapi@iris.co.uk
    Created by: https://help.iris.co.uk/hr/cascade/api/
"""

__version__ = "2"

# import ApiClient
from iris_software_group_cascade_python_sdk.api_client import ApiClient

# import Configuration
from iris_software_group_cascade_python_sdk.configuration import Configuration

# import exceptions
from iris_software_group_cascade_python_sdk.exceptions import OpenApiException
from iris_software_group_cascade_python_sdk.exceptions import ApiAttributeError
from iris_software_group_cascade_python_sdk.exceptions import ApiTypeError
from iris_software_group_cascade_python_sdk.exceptions import ApiValueError
from iris_software_group_cascade_python_sdk.exceptions import ApiKeyError
from iris_software_group_cascade_python_sdk.exceptions import ApiException

from iris_software_group_cascade_python_sdk.client import IrisSoftwareGroupCascade
