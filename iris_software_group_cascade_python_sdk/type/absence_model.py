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


class RequiredAbsenceModel(TypedDict):
    pass

class OptionalAbsenceModel(TypedDict, total=False):
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

    # Source HR System Id. <br />   Cascade Source: [EmployeeAttendance].[RUID] <br />
    SourceSystemId: typing.Optional[str]

    # The date when the Absence was created in the Source HR System. <br />  Cascade Source: [EmployeeAttendance].[SYS_EffectiveDate] <br />
    SourceSystemCreatedOn: typing.Optional[datetime]

    # The date when the Absence was created or last updated in the Source HR System. <br />  Cascade Source: [EmployeeAttendance].[SYS_ModifiedDate] <br />
    SourceSystemLastModifiedOn: typing.Optional[datetime]

    # This ID is generated by the Iris HR platform and does not relate to the Cascade ID.
    Id: typing.Optional[str]

    # The date when the Absence was created in the Iris HR platform.
    CreatedOn: datetime

    # Not used as the Iris HR platform has no concept of users.
    CreatedBy: typing.Optional[str]

    # The date when the Absence was created or last updated.
    LastModifiedOn: typing.Optional[datetime]

    # Not used as the Iris HR platform has no concept of users.
    LastModifiedBy: typing.Optional[str]

class AbsenceModel(RequiredAbsenceModel, OptionalAbsenceModel):
    pass
