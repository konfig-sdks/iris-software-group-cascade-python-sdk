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

from iris_software_group_cascade_python_sdk.pydantic.day_part import DayPart

class AbsenceDayModel(BaseModel):
    # The ID of the parent Absence. <br />  Must exist in the Attendance Absence Service.
    absence_id: typing.Optional[typing.Optional[str]] = Field(None, alias='AbsenceId')

    # The ID of the Employee. <br />  Must exist in the Employees Service.
    employee_id: typing.Optional[typing.Optional[str]] = Field(None, alias='EmployeeId')

    # The date of the Absence Day. <br />  Cascade Source: [EmployeeAttendanceDates].[StartDate]
    date: typing.Optional[datetime] = Field(None, alias='Date')

    # The duration in days for this Absence Day. <br />  Cascade Source: [EmployeeAttendanceDates].[DurationDays]
    duration_days: typing.Optional[typing.Union[int, float]] = Field(None, alias='DurationDays')

    # The duration in minutes for this Absence Day. <br />  Cascade Source: [EmployeeAttendanceDates].[Duration]
    duration_minutes: typing.Optional[typing.Optional[int]] = Field(None, alias='DurationMinutes')

    day_part: typing.Optional[DayPart] = Field(None, alias='DayPart')

    # Source HR System Id. <br />  Cascade Source: [EmployeeAttendanceDates].[Sequence] <br />  Read Only
    source_system_id: typing.Optional[typing.Optional[str]] = Field(None, alias='SourceSystemId')

    # The ID of the Absence Day. <br />  This field is generated by Iris HR platform and not related to the Cascade ID.
    id: typing.Optional[typing.Optional[str]] = Field(None, alias='Id')

    # The date time when the Absence Day was created in the Iris HR platform.
    created_on: typing.Optional[datetime] = Field(None, alias='CreatedOn')

    # Not used as the Iris HR platform has no concept of users at the moment.
    created_by: typing.Optional[typing.Optional[str]] = Field(None, alias='CreatedBy')

    # The date time when the Absence Day was created or last updated.
    last_modified_on: typing.Optional[typing.Optional[datetime]] = Field(None, alias='LastModifiedOn')

    last_modified_by: typing.Optional[typing.Optional[str]] = Field(None, alias='LastModifiedBy')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )