# coding: utf-8

"""
    HR API

    <a href='swaggerv2.json'>Download Swagger Json in OAS2 Format.</a>

    The version of the OpenAPI document: 2
    Contact: hrapi@iris.co.uk
    Created by: https://help.iris.co.uk/hr/cascade/api/
"""

from iris_software_group_cascade_python_sdk.paths.bankdetails.post import CreateBankDetail
from iris_software_group_cascade_python_sdk.paths.bankdetails_id.get import GetById
from iris_software_group_cascade_python_sdk.paths.bankdetails.get import GetList
from iris_software_group_cascade_python_sdk.paths.bankdetails_id.put import UpdateBankDetail
from iris_software_group_cascade_python_sdk.apis.tags.bank_details_api_raw import BankDetailsApiRaw


class BankDetailsApi(
    CreateBankDetail,
    GetById,
    GetList,
    UpdateBankDetail,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: BankDetailsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = BankDetailsApiRaw(api_client)
