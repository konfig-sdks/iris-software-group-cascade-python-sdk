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


class UpdateAbsenceCommand(BaseModel):
    # The Narrative relating to the Attendance. <br />  Cascade Source: [EmployeeAttendance].[Narrative]
    narrative: typing.Optional[typing.Optional[str]] = Field(None, alias='Narrative')

    # The Start Date of the Attendance. <br />  Cascade Source: [EmployeeAttendance].[StartDate]
    start_date: typing.Optional[typing.Optional[datetime]] = Field(None, alias='StartDate')

    # The End Date of the Attendance. <br />  Cascade Source: [EmployeeAttendance].[EndDate]  Null if Opened Ended - Cascade Source: [EmployeeAttendance].[OpenEnded]
    end_date: typing.Optional[typing.Optional[datetime]] = Field(None, alias='EndDate')

    # The ID of the Absence. <br />  Must exist in the Attendance Absences Service.
    id: typing.Optional[typing.Optional[str]] = Field(None, alias='Id')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
