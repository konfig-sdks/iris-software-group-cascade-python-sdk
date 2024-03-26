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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from iris_software_group_cascade_python_sdk.pydantic.bank_address import BankAddress

class UpdateBankDetailsCommand(BaseModel):
    # Bank Name. <br />  Cascade Source: [EmployeeBank].[BankName]
    bank_name: typing.Optional[typing.Optional[str]] = Field(None, alias='BankName')

    bank_address: typing.Optional[BankAddress] = Field(None, alias='BankAddress')

    # Account Name. <br />  Cascade Source: [EmployeeBank].[AccountName]
    account_name: typing.Optional[typing.Optional[str]] = Field(None, alias='AccountName')

    # Account Number. <br />  Cascade Source: [EmployeeBank].[AccountNumber]
    account_number: typing.Optional[typing.Optional[str]] = Field(None, alias='AccountNumber')

    # Sort Code. <br />  Cascade Source: [EmployeeBank].[SortCode]
    sort_code: typing.Optional[typing.Optional[str]] = Field(None, alias='SortCode')

    # Roll Number. <br />  Cascade Source: [EmployeeBank].[RollNumber]
    roll_number: typing.Optional[typing.Optional[str]] = Field(None, alias='RollNumber')

    # The ID of Bank Details to update. <br />  Must exist in Bank Details Service.
    id: typing.Optional[typing.Optional[str]] = Field(None, alias='Id')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
