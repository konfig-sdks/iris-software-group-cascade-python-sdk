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


class RequiredEmployeeAbsenceReasonModel(TypedDict):
    pass

class OptionalEmployeeAbsenceReasonModel(TypedDict, total=False):
    # The Parent ID of this Absence Reason. <br />  Cascade Source: [ValidAttendanceTypes].[Key].
    EmployeeId: typing.Optional[str]

    # The Name of this Absence Reason. <br />  Cascade Source: <br />  [ValidAttendanceCategory].[Category] when ParentID is null; <br />  [ValidAttendanceTypes].[Type] when ParentID is not null.
    AbsenceReasonId: typing.Optional[str]

    # The Absence Reason For The Employee should be recorded in Days or not.
    ShowInDays: bool

    # The ID of the Employee Absence Reason.
    Id: typing.Optional[str]

    # The date time when the Employee Absence Reason was created in the Iris HR platform.
    CreatedOn: datetime

    # Not used as the Iris HR platform has no concept of users at the moment.
    CreatedBy: typing.Optional[str]

    # The date time when the Employee Absence Reason was created or last updated.
    LastModifiedOn: typing.Optional[datetime]

    # Not used as the Iris HR platform has no concept of users at the moment.
    LastModifiedBy: typing.Optional[str]

class EmployeeAbsenceReasonModel(RequiredEmployeeAbsenceReasonModel, OptionalEmployeeAbsenceReasonModel):
    pass
