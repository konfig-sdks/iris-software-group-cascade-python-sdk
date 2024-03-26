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


class RequiredEntitlementModel(TypedDict):
    pass

class OptionalEntitlementModel(TypedDict, total=False):
    # The ID of the HR Employee. <br />  Must exist in the Employee Service.
    EmployeeId: typing.Optional[str]

    # The Absence Reason ID. <br />  Must exist in the Absence Reason Service.
    AbsenceReasonId: typing.Optional[str]

    # The Entitlement Year Name. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[EntitlementYearName]
    EntitlementYearName: typing.Optional[str]

    # The status of Open indicates whether the entitlement is active. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[Open]
    Open: bool

    # The Start Date of this Entitlement. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[StartDate]
    StartDate: datetime

    # The End Date of this Entitlement. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[EndDate]
    EndDate: datetime

    # The optional description of this Entitlement. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[Narrative]
    Narrative: typing.Optional[str]

    # The number of Base Entitlement Days. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[BaseEntitlementDays]
    BaseDays: typing.Union[int, float]

    # The number of Base Entitlement Minutes. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[BaseEntitlement]
    BaseMinutes: typing.Optional[int]

    # The number of Carry Days allowed. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[CarryDays]
    CarryDays: typing.Union[int, float]

    # The number of Carry Minutes allowed. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[Carry]
    CarryMinutes: typing.Optional[int]

    # The date when Carry Days should be used by. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[CarryUsebyDays]
    CarryUseByDate: typing.Optional[datetime]

    # The number of Carry Days lost. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[CarryLostDays]
    CarryLostDays: typing.Optional[typing.Union[int, float]]

    # The number of Carry Minutes lost. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[CarryLost]
    CarryLostMinutes: typing.Optional[int]

    # The number of Manual Adjustment Days. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[ManualAdjustmentDays]
    ManualAdjustmentDays: typing.Union[int, float]

    # The number of Manual Adjustment Minutes. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[ManualAdjustment]
    ManualAdjustmentMinutes: typing.Optional[int]

    # The number of Adjustment Days due to service length. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[ServiceLengthAdjustmentDays]
    ServiceLengthAdjustmentDays: typing.Union[int, float]

    # The number of Adjustment Minutes due to service length. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[ServiceLengthAdjustment]
    ServiceLengthAdjustmentMinutes: typing.Optional[int]

    # The number of New Starter Adjustment Days. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[NewStarterAdjustmentDays]
    NewStarterAdjustmentDays: typing.Union[int, float]

    # The number of New Starter Adjustment Minutes. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[NewStarterAdjustment]
    NewStarterAdjustmentMinutes: typing.Optional[int]

    # [Obsolete] The number of Leaver Adjustment Days. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[LeaverAdjustmentDays]
    LeaverAdjusmentDays: typing.Union[int, float]

    # [Obsolete] The number of Leaver Adjustment Minutes. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[LeaverAdjustment]
    LeaverAdjusmentMinutes: typing.Optional[int]

    # The number of Leaver Adjustment Days. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[LeaverAdjustmentDays]
    LeaverAdjustmentDays: typing.Optional[typing.Union[int, float]]

    # The number of Leaver Adjustment Minutes. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[LeaverAdjustment]
    LeaverAdjustmentMinutes: typing.Optional[int]

    # The number of Part Time Adjustment Days. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[PTProrataDays]
    PartTimeAdjustmentDays: typing.Union[int, float]

    # The number of Part Time Adjustment Minutes. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[PTProrata]
    PartTimeAdjustmentMinutes: typing.Optional[int]

    # The number of Bank Holiday Adjustment Day. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[BHProrataDays]
    BankHolidayAdjustmentDays: typing.Union[int, float]

    # The number of Bank Holiday Adjustment Minutes. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[BHProrata]
    BankHolidayAdjustmentMinutes: typing.Optional[int]

    # The number of Buy Sell Days. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[BuySellDays]
    BuySellDays: typing.Union[int, float]

    # The number of Buy Sell Minutes. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[BuySell]
    BuySellMinutes: typing.Optional[int]

    # The total Entitlement in days. <br />  = BaseDays <br />      + ServiceLengthAdjustmentDays <br />      + NewStarterAdjustmentDays <br />      + ManualAdjustmentDays <br />      + CarryDays <br />      + PartTimeAdjustmentDays <br />      + BankHolidayAdjustmentDays <br />      + BuySellDays <br />      - CarryLostDays <br />      + LeaverAdjustmentDays
    TotalEntitlementDays: typing.Optional[typing.Union[int, float]]

    # The total Entitlement in minutes. <br />  = BaseMinutes <br />      + ServiceLengthAdjustmentMinutes <br />      + NewStarterAdjustmentMinutes <br />      + ManualAdjustmentMinutes <br />      + CarryMinutes <br />      + PartTimeAdjustmentMinutes <br />      + BankHolidayAdjustmentMinutes <br />      + BuySellMinutes <br />      - CarryLostMinutes <br />      + LeaverAdjustmentMinutes
    TotalEntitlementMinutes: typing.Optional[int]

    # The Internal ID of the Source HR Product. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[Key]
    SourceSystemId: typing.Optional[str]

    # The date when the Entitlement record was created in the Source HR System. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[SYS_EffectiveDate]
    SourceSystemCreatedOn: typing.Optional[datetime]

    # The date when the Entitlement record was created or last updated in the Source HR System. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[SYS_ModifiedDate]
    SourceSystemLastModifiedOn: typing.Optional[datetime]

    # This ID is generated by the Iris HR platform and does not relate to the Cascade Employee Entitlement ID.
    Id: typing.Optional[str]

    # The date when the Entitlement was created in the Iris HR platform.
    CreatedOn: datetime

    # Not used as the Iris HR platform has no concept of users at the moment.
    CreatedBy: typing.Optional[str]

    # The date when the Entitlement was created or last updated.
    LastModifiedOn: typing.Optional[datetime]

    # Not used as the Iris HR platform has no concept of users at the moment.
    LastModifiedBy: typing.Optional[str]

class EntitlementModel(RequiredEntitlementModel, OptionalEntitlementModel):
    pass
