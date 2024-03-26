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


class BankAddress(BaseModel):
    # The first line of Bank Address <br />  Cascade Source: [EmployeeBank].[Address1]
    address1: typing.Optional[typing.Optional[str]] = Field(None, alias='Address1')

    # The second line of Bank Address <br />  Cascade Source: [EmployeeBank].[Address2]
    address2: typing.Optional[typing.Optional[str]] = Field(None, alias='Address2')

    # The third line of Bank Address <br />  Cascade Source: [EmployeeBank].[Address3]
    address3: typing.Optional[typing.Optional[str]] = Field(None, alias='Address3')

    # The fourth line of Bank Address <br />  Cascade Source: [EmployeeBank].[Address4]
    address4: typing.Optional[typing.Optional[str]] = Field(None, alias='Address4')

    # Post Code of the Bank <br />  Cascade Source: [EmployeeBank].[Postcode]
    post_code: typing.Optional[typing.Optional[str]] = Field(None, alias='PostCode')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
