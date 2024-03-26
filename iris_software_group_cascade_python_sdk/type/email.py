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

class RequiredEmail(TypedDict):
    pass

class OptionalEmail(TypedDict, total=False):
    Ownership: Ownership

    # The Email Address. <br />  Cascade Source: <br />  Ownership = Organization then [Employee].[WorkEmail], Maximum Length: 320<br />  Ownership = Personal then [EmployeeHomeAddress].[HomeEmail], Maximum Length: 50.
    Value: typing.Optional[str]

class Email(RequiredEmail, OptionalEmail):
    pass
