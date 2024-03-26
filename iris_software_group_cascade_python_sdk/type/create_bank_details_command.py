# coding: utf-8

"""
    HR API

    <a href='swaggerv2.json'>Download Swagger Json in OAS2 Format.</a>

    The version of the OpenAPI document: 2
    Contact: hrapi@iris.co.uk
    Created by: https://help.iris.co.uk/hr/cascade/api/
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from iris_software_group_cascade_python_sdk.type.bank_address import BankAddress

class RequiredCreateBankDetailsCommand(TypedDict):
    pass

class OptionalCreateBankDetailsCommand(TypedDict, total=False):
    # The ID of the HR Employee. <br />  Must exist in the Employee Service.
    EmployeeId: typing.Optional[str]

    # Bank Name. <br />  Cascade Source: [EmployeeBank].[BankName]
    BankName: typing.Optional[str]

    BankAddress: BankAddress

    # Account Name. <br />  Cascade Source: [EmployeeBank].[AccountName]
    AccountName: typing.Optional[str]

    # Account Number. <br />  Cascade Source: [EmployeeBank].[AccountNumber]
    AccountNumber: typing.Optional[str]

    # Sort Code. <br />  Cascade Source: [EmployeeBank].[SortCode]
    SortCode: typing.Optional[str]

    # Roll Number. <br />  Cascade Source: [EmployeeBank].[RollNumber]
    RollNumber: typing.Optional[str]

class CreateBankDetailsCommand(RequiredCreateBankDetailsCommand, OptionalCreateBankDetailsCommand):
    pass
