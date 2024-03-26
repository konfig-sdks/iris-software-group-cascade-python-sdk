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


class EntitlementModel(BaseModel):
    # The ID of the HR Employee. <br />  Must exist in the Employee Service.
    employee_id: typing.Optional[typing.Optional[str]] = Field(None, alias='EmployeeId')

    # The Absence Reason ID. <br />  Must exist in the Absence Reason Service.
    absence_reason_id: typing.Optional[typing.Optional[str]] = Field(None, alias='AbsenceReasonId')

    # The Entitlement Year Name. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[EntitlementYearName]
    entitlement_year_name: typing.Optional[typing.Optional[str]] = Field(None, alias='EntitlementYearName')

    # The status of Open indicates whether the entitlement is active. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[Open]
    open: typing.Optional[bool] = Field(None, alias='Open')

    # The Start Date of this Entitlement. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[StartDate]
    start_date: typing.Optional[datetime] = Field(None, alias='StartDate')

    # The End Date of this Entitlement. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[EndDate]
    end_date: typing.Optional[datetime] = Field(None, alias='EndDate')

    # The optional description of this Entitlement. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[Narrative]
    narrative: typing.Optional[typing.Optional[str]] = Field(None, alias='Narrative')

    # The number of Base Entitlement Days. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[BaseEntitlementDays]
    base_days: typing.Optional[typing.Union[int, float]] = Field(None, alias='BaseDays')

    # The number of Base Entitlement Minutes. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[BaseEntitlement]
    base_minutes: typing.Optional[typing.Optional[int]] = Field(None, alias='BaseMinutes')

    # The number of Carry Days allowed. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[CarryDays]
    carry_days: typing.Optional[typing.Union[int, float]] = Field(None, alias='CarryDays')

    # The number of Carry Minutes allowed. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[Carry]
    carry_minutes: typing.Optional[typing.Optional[int]] = Field(None, alias='CarryMinutes')

    # The date when Carry Days should be used by. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[CarryUsebyDays]
    carry_use_by_date: typing.Optional[typing.Optional[datetime]] = Field(None, alias='CarryUseByDate')

    # The number of Carry Days lost. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[CarryLostDays]
    carry_lost_days: typing.Optional[typing.Optional[typing.Union[int, float]]] = Field(None, alias='CarryLostDays')

    # The number of Carry Minutes lost. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[CarryLost]
    carry_lost_minutes: typing.Optional[typing.Optional[int]] = Field(None, alias='CarryLostMinutes')

    # The number of Manual Adjustment Days. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[ManualAdjustmentDays]
    manual_adjustment_days: typing.Optional[typing.Union[int, float]] = Field(None, alias='ManualAdjustmentDays')

    # The number of Manual Adjustment Minutes. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[ManualAdjustment]
    manual_adjustment_minutes: typing.Optional[typing.Optional[int]] = Field(None, alias='ManualAdjustmentMinutes')

    # The number of Adjustment Days due to service length. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[ServiceLengthAdjustmentDays]
    service_length_adjustment_days: typing.Optional[typing.Union[int, float]] = Field(None, alias='ServiceLengthAdjustmentDays')

    # The number of Adjustment Minutes due to service length. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[ServiceLengthAdjustment]
    service_length_adjustment_minutes: typing.Optional[typing.Optional[int]] = Field(None, alias='ServiceLengthAdjustmentMinutes')

    # The number of New Starter Adjustment Days. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[NewStarterAdjustmentDays]
    new_starter_adjustment_days: typing.Optional[typing.Union[int, float]] = Field(None, alias='NewStarterAdjustmentDays')

    # The number of New Starter Adjustment Minutes. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[NewStarterAdjustment]
    new_starter_adjustment_minutes: typing.Optional[typing.Optional[int]] = Field(None, alias='NewStarterAdjustmentMinutes')

    # [Obsolete] The number of Leaver Adjustment Days. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[LeaverAdjustmentDays]
    leaver_adjusment_days: typing.Optional[typing.Union[int, float]] = Field(None, alias='LeaverAdjusmentDays')

    # [Obsolete] The number of Leaver Adjustment Minutes. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[LeaverAdjustment]
    leaver_adjusment_minutes: typing.Optional[typing.Optional[int]] = Field(None, alias='LeaverAdjusmentMinutes')

    # The number of Leaver Adjustment Days. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[LeaverAdjustmentDays]
    leaver_adjustment_days: typing.Optional[typing.Optional[typing.Union[int, float]]] = Field(None, alias='LeaverAdjustmentDays')

    # The number of Leaver Adjustment Minutes. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[LeaverAdjustment]
    leaver_adjustment_minutes: typing.Optional[typing.Optional[int]] = Field(None, alias='LeaverAdjustmentMinutes')

    # The number of Part Time Adjustment Days. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[PTProrataDays]
    part_time_adjustment_days: typing.Optional[typing.Union[int, float]] = Field(None, alias='PartTimeAdjustmentDays')

    # The number of Part Time Adjustment Minutes. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[PTProrata]
    part_time_adjustment_minutes: typing.Optional[typing.Optional[int]] = Field(None, alias='PartTimeAdjustmentMinutes')

    # The number of Bank Holiday Adjustment Day. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[BHProrataDays]
    bank_holiday_adjustment_days: typing.Optional[typing.Union[int, float]] = Field(None, alias='BankHolidayAdjustmentDays')

    # The number of Bank Holiday Adjustment Minutes. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[BHProrata]
    bank_holiday_adjustment_minutes: typing.Optional[typing.Optional[int]] = Field(None, alias='BankHolidayAdjustmentMinutes')

    # The number of Buy Sell Days. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[BuySellDays]
    buy_sell_days: typing.Optional[typing.Union[int, float]] = Field(None, alias='BuySellDays')

    # The number of Buy Sell Minutes. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[BuySell]
    buy_sell_minutes: typing.Optional[typing.Optional[int]] = Field(None, alias='BuySellMinutes')

    # The total Entitlement in days. <br />  = BaseDays <br />      + ServiceLengthAdjustmentDays <br />      + NewStarterAdjustmentDays <br />      + ManualAdjustmentDays <br />      + CarryDays <br />      + PartTimeAdjustmentDays <br />      + BankHolidayAdjustmentDays <br />      + BuySellDays <br />      - CarryLostDays <br />      + LeaverAdjustmentDays
    total_entitlement_days: typing.Optional[typing.Optional[typing.Union[int, float]]] = Field(None, alias='TotalEntitlementDays')

    # The total Entitlement in minutes. <br />  = BaseMinutes <br />      + ServiceLengthAdjustmentMinutes <br />      + NewStarterAdjustmentMinutes <br />      + ManualAdjustmentMinutes <br />      + CarryMinutes <br />      + PartTimeAdjustmentMinutes <br />      + BankHolidayAdjustmentMinutes <br />      + BuySellMinutes <br />      - CarryLostMinutes <br />      + LeaverAdjustmentMinutes
    total_entitlement_minutes: typing.Optional[typing.Optional[int]] = Field(None, alias='TotalEntitlementMinutes')

    # The Internal ID of the Source HR Product. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[Key]
    source_system_id: typing.Optional[typing.Optional[str]] = Field(None, alias='SourceSystemId')

    # The date when the Entitlement record was created in the Source HR System. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[SYS_EffectiveDate]
    source_system_created_on: typing.Optional[typing.Optional[datetime]] = Field(None, alias='SourceSystemCreatedOn')

    # The date when the Entitlement record was created or last updated in the Source HR System. <br />  Cascade Source: [EmployeeAttendanceEntitlementYear].[SYS_ModifiedDate]
    source_system_last_modified_on: typing.Optional[typing.Optional[datetime]] = Field(None, alias='SourceSystemLastModifiedOn')

    # This ID is generated by the Iris HR platform and does not relate to the Cascade Employee Entitlement ID.
    id: typing.Optional[typing.Optional[str]] = Field(None, alias='Id')

    # The date when the Entitlement was created in the Iris HR platform.
    created_on: typing.Optional[datetime] = Field(None, alias='CreatedOn')

    # Not used as the Iris HR platform has no concept of users at the moment.
    created_by: typing.Optional[typing.Optional[str]] = Field(None, alias='CreatedBy')

    # The date when the Entitlement was created or last updated.
    last_modified_on: typing.Optional[typing.Optional[datetime]] = Field(None, alias='LastModifiedOn')

    # Not used as the Iris HR platform has no concept of users at the moment.
    last_modified_by: typing.Optional[typing.Optional[str]] = Field(None, alias='LastModifiedBy')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
