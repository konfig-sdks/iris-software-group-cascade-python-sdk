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


class RequiredUpdateAbsenceCommand(TypedDict):
    pass

class OptionalUpdateAbsenceCommand(TypedDict, total=False):
    # The Narrative relating to the Attendance. <br />  Cascade Source: [EmployeeAttendance].[Narrative]
    Narrative: typing.Optional[str]

    # The Start Date of the Attendance. <br />  Cascade Source: [EmployeeAttendance].[StartDate]
    StartDate: typing.Optional[datetime]

    # The End Date of the Attendance. <br />  Cascade Source: [EmployeeAttendance].[EndDate]  Null if Opened Ended - Cascade Source: [EmployeeAttendance].[OpenEnded]
    EndDate: typing.Optional[datetime]

    # The ID of the Absence. <br />  Must exist in the Attendance Absences Service.
    Id: typing.Optional[str]

class UpdateAbsenceCommand(RequiredUpdateAbsenceCommand, OptionalUpdateAbsenceCommand):
    pass
