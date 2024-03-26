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

from iris_software_group_cascade_python_sdk.type.day_part import DayPart

class RequiredUpdateAbsenceDayCommand(TypedDict):
    pass

class OptionalUpdateAbsenceDayCommand(TypedDict, total=False):
    # The date of the Absence Day. <br />  Cascade Source: [EmployeeAttendanceDates].[StartDate]
    Date: datetime

    # The duration in days for this Absence Day. <br />  Cascade Source: [EmployeeAttendanceDates].[DurationDays]
    DurationDays: typing.Union[int, float]

    # The duration in minutes for this Absence Day. <br />  Cascade Source: [EmployeeAttendanceDates].[Duration]
    DurationMinutes: typing.Optional[int]

    DayPart: DayPart

    # The ID of the Absence Day. <br />  Must exist in the Attendance Absence Day Service.
    Id: typing.Optional[str]

class UpdateAbsenceDayCommand(RequiredUpdateAbsenceDayCommand, OptionalUpdateAbsenceDayCommand):
    pass
