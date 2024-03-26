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

from iris_software_group_cascade_python_sdk.type.public_holiday_model import PublicHolidayModel

class RequiredPublicHolidayQueryModel(TypedDict):
    pass

class OptionalPublicHolidayQueryModel(TypedDict, total=False):
    ODataContext: typing.Optional[str]

    ODataCount: typing.Optional[int]

    ODataNextLink: typing.Optional[str]

    Value: typing.Optional[typing.List[PublicHolidayModel]]

class PublicHolidayQueryModel(RequiredPublicHolidayQueryModel, OptionalPublicHolidayQueryModel):
    pass
