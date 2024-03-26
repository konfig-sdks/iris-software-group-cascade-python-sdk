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


class EmployeeAbsenceReasonModel(BaseModel):
    # The Parent ID of this Absence Reason. <br />  Cascade Source: [ValidAttendanceTypes].[Key].
    employee_id: typing.Optional[typing.Optional[str]] = Field(None, alias='EmployeeId')

    # The Name of this Absence Reason. <br />  Cascade Source: <br />  [ValidAttendanceCategory].[Category] when ParentID is null; <br />  [ValidAttendanceTypes].[Type] when ParentID is not null.
    absence_reason_id: typing.Optional[typing.Optional[str]] = Field(None, alias='AbsenceReasonId')

    # The Absence Reason For The Employee should be recorded in Days or not.
    show_in_days: typing.Optional[bool] = Field(None, alias='ShowInDays')

    # The ID of the Employee Absence Reason.
    id: typing.Optional[typing.Optional[str]] = Field(None, alias='Id')

    # The date time when the Employee Absence Reason was created in the Iris HR platform.
    created_on: typing.Optional[datetime] = Field(None, alias='CreatedOn')

    # Not used as the Iris HR platform has no concept of users at the moment.
    created_by: typing.Optional[typing.Optional[str]] = Field(None, alias='CreatedBy')

    # The date time when the Employee Absence Reason was created or last updated.
    last_modified_on: typing.Optional[typing.Optional[datetime]] = Field(None, alias='LastModifiedOn')

    # Not used as the Iris HR platform has no concept of users at the moment.
    last_modified_by: typing.Optional[typing.Optional[str]] = Field(None, alias='LastModifiedBy')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
