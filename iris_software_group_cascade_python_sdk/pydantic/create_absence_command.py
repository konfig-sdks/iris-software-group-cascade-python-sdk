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


class CreateAbsenceCommand(BaseModel):
    # The ID of the Employee. <br />  Must exist in the Employees Service. <br />  Cannot be updated once Absence created.
    employee_id: typing.Optional[typing.Optional[str]] = Field(None, alias='EmployeeId')

    # The Absence Reason ID. <br />  Must exist in the Attendance Absence Reasons Service. <br />  Cannot be updated once Absence created.
    absence_reason_id: typing.Optional[typing.Optional[str]] = Field(None, alias='AbsenceReasonId')

    # The Narrative relating to the Attendance. <br />  Cascade Source: [EmployeeAttendance].[Narrative]
    narrative: typing.Optional[typing.Optional[str]] = Field(None, alias='Narrative')

    # The Start Date of the Attendance. <br />  Cascade Source: [EmployeeAttendance].[StartDate]
    start_date: typing.Optional[typing.Optional[datetime]] = Field(None, alias='StartDate')

    # The End Date of the Attendance. <br />  Cascade Source: [EmployeeAttendance].[EndDate]  Null if Opened Ended - Cascade Source: [EmployeeAttendance].[OpenEnded]
    end_date: typing.Optional[typing.Optional[datetime]] = Field(None, alias='EndDate')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
