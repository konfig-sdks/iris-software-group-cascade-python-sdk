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

from iris_software_group_cascade_python_sdk.type.ownership import Ownership

class RequiredAddress(TypedDict):
    pass

class OptionalAddress(TypedDict, total=False):
    Ownership: Ownership

    # Address Line 1 <br />  Cascade Source: [EmployeeHomeAddress].[Address1]
    Address1: typing.Optional[str]

    # Address Line 2 <br />  Cascade Source: [EmployeeHomeAddress].[Address2]
    Address2: typing.Optional[str]

    # Address Line 3 <br />  Cascade Source: [EmployeeHomeAddress].[Address3]
    Address3: typing.Optional[str]

    # Address Line 4 <br />  Cascade Source: [EmployeeHomeAddress].[Address4]
    Address4: typing.Optional[str]

    # Address Line 5 <br />  Cascade Source: [EmployeeHomeAddress].[Address5]
    Address5: typing.Optional[str]

    # Address UK Post Code <br />  Cascade Source: [EmployeeHomeAddress].[Postcode]
    PostCode: typing.Optional[str]

class Address(RequiredAddress, OptionalAddress):
    pass
