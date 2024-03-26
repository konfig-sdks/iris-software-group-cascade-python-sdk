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

class RequiredCreateAbsenceDayCommand(TypedDict):
    pass

class OptionalCreateAbsenceDayCommand(TypedDict, total=False):
    # The ID of the parent Absence. <br />  Must exist in the Attendance Absence Service.
    AbsenceId: typing.Optional[str]

    # The ID of the Employee. <br />  Must exist in the Employees Service.
    EmployeeId: typing.Optional[str]

    # The date of the Absence Day. <br />  Cascade Source: [EmployeeAttendanceDates].[StartDate]
    Date: datetime

    # The duration in days for this Absence Day. <br />  Cascade Source: [EmployeeAttendanceDates].[DurationDays]
    DurationDays: typing.Union[int, float]

    # The duration in minutes for this Absence Day. <br />  Cascade Source: [EmployeeAttendanceDates].[Duration]
    DurationMinutes: typing.Optional[int]

    DayPart: DayPart

class CreateAbsenceDayCommand(RequiredCreateAbsenceDayCommand, OptionalCreateAbsenceDayCommand):
    pass
