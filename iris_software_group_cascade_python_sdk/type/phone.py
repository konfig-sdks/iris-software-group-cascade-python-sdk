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
from iris_software_group_cascade_python_sdk.type.phone_type import PhoneType

class RequiredPhone(TypedDict):
    pass

class OptionalPhone(TypedDict, total=False):
    Ownership: Ownership

    Type: PhoneType

    # The Phone Number value. <br />  Cascade Source:  <br />  Ownership = Organization, Type = Landline Then [Employee].[WorkPhone] <br />  Ownership = Organization, Type = Mobile Then [Employee].[WorkMobilePhoneNumber] <br />  Ownership = Personal, Type = Landline Then [EmployeeHomeAddress].[Phone] <br />  Ownership = Personal, Type = Mobile Then [EmployeeHomeAddress].[MobilePhone]
    Value: typing.Optional[str]

class Phone(RequiredPhone, OptionalPhone):
    pass
