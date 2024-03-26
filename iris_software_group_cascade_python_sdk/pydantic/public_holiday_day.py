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


class PublicHolidayDay(BaseModel):
    # The description of the Public Holiday Day. <br />  Cascade Source: [ValidBankHolidays].[Description]
    description: typing.Optional[typing.Optional[str]] = Field(None, alias='Description')

    # The date of the Public Holiday Day. <br />  Cascade Source: [ValidBankHolidays].[Date]
    date: typing.Optional[datetime] = Field(None, alias='Date')

    # Source HR System Id. <br />  Cascade Source: [ValidBankHolidays].[key] <br />  Read Only
    source_system_id: typing.Optional[typing.Optional[str]] = Field(None, alias='SourceSystemId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
