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


class RequiredPublicHolidayDay(TypedDict):
    pass

class OptionalPublicHolidayDay(TypedDict, total=False):
    # The description of the Public Holiday Day. <br />  Cascade Source: [ValidBankHolidays].[Description]
    Description: typing.Optional[str]

    # The date of the Public Holiday Day. <br />  Cascade Source: [ValidBankHolidays].[Date]
    Date: datetime

    # Source HR System Id. <br />  Cascade Source: [ValidBankHolidays].[key] <br />  Read Only
    SourceSystemId: typing.Optional[str]

class PublicHolidayDay(RequiredPublicHolidayDay, OptionalPublicHolidayDay):
    pass
