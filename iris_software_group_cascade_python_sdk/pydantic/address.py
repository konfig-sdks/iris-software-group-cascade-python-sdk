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

from iris_software_group_cascade_python_sdk.pydantic.ownership import Ownership

class Address(BaseModel):
    ownership: typing.Optional[Ownership] = Field(None, alias='Ownership')

    # Address Line 1 <br />  Cascade Source: [EmployeeHomeAddress].[Address1]
    address1: typing.Optional[typing.Optional[str]] = Field(None, alias='Address1')

    # Address Line 2 <br />  Cascade Source: [EmployeeHomeAddress].[Address2]
    address2: typing.Optional[typing.Optional[str]] = Field(None, alias='Address2')

    # Address Line 3 <br />  Cascade Source: [EmployeeHomeAddress].[Address3]
    address3: typing.Optional[typing.Optional[str]] = Field(None, alias='Address3')

    # Address Line 4 <br />  Cascade Source: [EmployeeHomeAddress].[Address4]
    address4: typing.Optional[typing.Optional[str]] = Field(None, alias='Address4')

    # Address Line 5 <br />  Cascade Source: [EmployeeHomeAddress].[Address5]
    address5: typing.Optional[typing.Optional[str]] = Field(None, alias='Address5')

    # Address UK Post Code <br />  Cascade Source: [EmployeeHomeAddress].[Postcode]
    post_code: typing.Optional[typing.Optional[str]] = Field(None, alias='PostCode')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
