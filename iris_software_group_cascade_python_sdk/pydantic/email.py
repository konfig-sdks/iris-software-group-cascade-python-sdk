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

class Email(BaseModel):
    ownership: typing.Optional[Ownership] = Field(None, alias='Ownership')

    # The Email Address. <br />  Cascade Source: <br />  Ownership = Organization then [Employee].[WorkEmail], Maximum Length: 320<br />  Ownership = Personal then [EmployeeHomeAddress].[HomeEmail], Maximum Length: 50.
    value: typing.Optional[typing.Optional[str]] = Field(None, alias='Value')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )