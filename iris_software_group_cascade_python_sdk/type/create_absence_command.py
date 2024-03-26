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


class RequiredCreateAbsenceCommand(TypedDict):
    pass

class OptionalCreateAbsenceCommand(TypedDict, total=False):
    # The ID of the Employee. <br />  Must exist in the Employees Service. <br />  Cannot be updated once Absence created.
    EmployeeId: typing.Optional[str]

    # The Absence Reason ID. <br />  Must exist in the Attendance Absence Reasons Service. <br />  Cannot be updated once Absence created.
    AbsenceReasonId: typing.Optional[str]

    # The Narrative relating to the Attendance. <br />  Cascade Source: [EmployeeAttendance].[Narrative]
    Narrative: typing.Optional[str]

    # The Start Date of the Attendance. <br />  Cascade Source: [EmployeeAttendance].[StartDate]
    StartDate: typing.Optional[datetime]

    # The End Date of the Attendance. <br />  Cascade Source: [EmployeeAttendance].[EndDate]  Null if Opened Ended - Cascade Source: [EmployeeAttendance].[OpenEnded]
    EndDate: typing.Optional[datetime]

class CreateAbsenceCommand(RequiredCreateAbsenceCommand, OptionalCreateAbsenceCommand):
    pass
