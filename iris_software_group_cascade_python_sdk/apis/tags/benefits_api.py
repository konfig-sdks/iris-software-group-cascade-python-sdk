# coding: utf-8

"""
    HR API

    <a href='swaggerv2.json'>Download Swagger Json in OAS2 Format.</a>

    The version of the OpenAPI document: 2
    Contact: hrapi@iris.co.uk
    Created by: https://help.iris.co.uk/hr/cascade/api/
"""

from iris_software_group_cascade_python_sdk.paths.benefits_id.get import GetById
from iris_software_group_cascade_python_sdk.paths.benefits.get import GetList
from iris_software_group_cascade_python_sdk.apis.tags.benefits_api_raw import BenefitsApiRaw


class BenefitsApi(
    GetById,
    GetList,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: BenefitsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = BenefitsApiRaw(api_client)