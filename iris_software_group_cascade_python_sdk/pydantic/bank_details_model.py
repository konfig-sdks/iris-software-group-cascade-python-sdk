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

class BankDetailsModel(BaseModel):
    # The ID of the HR Employee. <br />  Must exist in the Employee Service.
    employee_id: typing.Optional[typing.Optional[str]] = Field(None, alias='EmployeeId')

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

    # The Internal ID for the source HR Product. <br />  Cascade Source: [EmployeeBank].[RUID]
    source_system_id: typing.Optional[typing.Optional[str]] = Field(None, alias='SourceSystemId')

    # The date when the Bank details record was created in the Source HR System. <br />  Cascade Source: [EmployeeBank].[SYS_EffectiveDate]
    source_system_created_on: typing.Optional[typing.Optional[datetime]] = Field(None, alias='SourceSystemCreatedOn')

    # The latest date when the Bank details record was created or last updated in the Source HR System. <br />  Cascade Source: Latest of [EmployeeBank].[SYS_ModifiedDate]
    source_system_last_modified_on: typing.Optional[typing.Optional[datetime]] = Field(None, alias='SourceSystemLastModifiedOn')

    # The ID of Bank Details. <br />  This field is generated by Iris HR platform and not related to the Cascade ID.
    id: typing.Optional[typing.Optional[str]] = Field(None, alias='Id')

    # The date time when the Bank Details was created in the Iris HR platform.
    created_on: typing.Optional[datetime] = Field(None, alias='CreatedOn')

    # Not used as the Iris HR platform has no concept of users at the moment.
    created_by: typing.Optional[typing.Optional[str]] = Field(None, alias='CreatedBy')

    # The date time when the Bank Details was created or last updated.
    last_modified_on: typing.Optional[typing.Optional[datetime]] = Field(None, alias='LastModifiedOn')

    # Not used as the Iris HR platform has no concept of users at the moment.
    last_modified_by: typing.Optional[typing.Optional[str]] = Field(None, alias='LastModifiedBy')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
