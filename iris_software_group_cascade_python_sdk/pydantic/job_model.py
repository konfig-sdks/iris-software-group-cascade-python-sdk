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


class JobModel(BaseModel):
    # The title of the Job. <br />  Cascade Source: [EmployeeJobs].[JobTitle]
    job_title: typing.Optional[typing.Optional[str]] = Field(None, alias='JobTitle')

    # The classification of the Job e.g. Technical, Professional, Managerial. <br />  Cascade Source: [EmployeeJobs].[Classification] translated through the JOBCLASSIFICATION system list.
    classification: typing.Optional[typing.Optional[str]] = Field(None, alias='Classification')

    # The start date of the Job. <br />  Required. <br />  Cascade Source: [EmployeeJobs].[SYS_EffectiveDate]
    start_date: typing.Optional[datetime] = Field(None, alias='StartDate')

    # The end date of the Job. <br />  Automatically Calculated. <br />  Cascade Source: [EmployeeJobs].[SYS_CalculatedEndDate]
    end_date: typing.Optional[typing.Optional[datetime]] = Field(None, alias='EndDate')

    # The name of the working calendar of the Job. <br />  Cascade Source: [EmployeeJobs].[CalendarName] which comes from [ValidWorkingCalendar].[CalendarName]
    working_calendar: typing.Optional[typing.Optional[str]] = Field(None, alias='WorkingCalendar')

    # The ID of the Employee that is the line manager for this Job. <br />  Must exist in Employees Service. <br />  Cascade Source: [EmployeeJobs].[WorksForEmployeeId]
    line_manager_id: typing.Optional[typing.Optional[str]] = Field(None, alias='LineManagerId')

    # The ID of the Employee's Hierarchy node of the Job. <br />  Must exist in Hierarchy Service.
    hierarchy_node_id: typing.Optional[typing.Optional[str]] = Field(None, alias='HierarchyNodeId')

    # The Job is currently active. <br />  Automatically Calculated. <br />  Cascade Source: [EmployeeJobs].[sys_ActiveJob]
    active: typing.Optional[bool] = Field(None, alias='Active')

    # The salary of the Job. <br />  Cascade Source: [EmployeeJobs].[BasicPay]
    salary: typing.Optional[typing.Optional[typing.Union[int, float]]] = Field(None, alias='Salary')

    # The ID of the Employee of the Job. <br />  Must exist in Employee Service.
    employee_id: typing.Optional[typing.Optional[str]] = Field(None, alias='EmployeeId')

    # The contract of the Job e.g. Full Time, Part Time. <br />  Cascade Source: [EmployeeJobs].[ContractType] translated through the EMPLOYMENTTYPES system list.
    contract: typing.Optional[typing.Optional[str]] = Field(None, alias='Contract')

    # How often the Job's salary will be paid e.g. Monthly, Weekly. <br />  Cascade Source: [EmployeeJobs].[PayFrequency] translated through the PAY FREQ system list.
    pay_frequency: typing.Optional[typing.Optional[str]] = Field(None, alias='PayFrequency')

    # The unit of measurement the salary is specified against e.g. Yearly, Hourly. <br />  Cascade Source: [EmployeeJobs].[PayBasis] translated through the PAY BASIS system list.
    pay_basis: typing.Optional[typing.Optional[str]] = Field(None, alias='PayBasis')

    # The full-time equivalent to a full time employee's hours e.g. 1 = Full Time, 0.5 = Half Hours. <br />  Cascade Source: [EmployeeJobs].[FTE].
    full_time_equivalent: typing.Optional[typing.Optional[typing.Union[int, float]]] = Field(None, alias='FullTimeEquivalent')

    # The readonly property of employee position. <br />  Cascade Source: [EmployeeJobs].[Postid].
    position: typing.Optional[typing.Optional[str]] = Field(None, alias='Position')

    # The reason for the change. <br />  Cascade Source: [EmployeeJobs].[Reason].
    change_reason: typing.Optional[typing.Optional[str]] = Field(None, alias='ChangeReason')

    # The readonly property of public holiday. <br />  Cascade Soruce: [EmployeeJobs].[HolidayLocation].
    public_holiday: typing.Optional[typing.Optional[str]] = Field(None, alias='PublicHoliday')

    # The readonly property of pay grade.  <br />  Cascade Source: [EmployeeJobs].[PayGrade].
    pay_grade: typing.Optional[typing.Optional[str]] = Field(None, alias='PayGrade')

    # The readonly property of pay spinal point. <br />  Cascade Source: [EmployeeJobs].[SpinalPoint].
    spinal_point: typing.Optional[typing.Optional[int]] = Field(None, alias='SpinalPoint')

    # The next increment date.  <br />  Cascade Source: [EmployeeJobs].[IncrementDate].
    next_increment_date: typing.Optional[typing.Optional[datetime]] = Field(None, alias='NextIncrementDate')

    # The timesheet location. <br />  Cascade Source: [EmployeeJobs].[TimesheetLocation].
    timesheet_location: typing.Optional[typing.Optional[str]] = Field(None, alias='TimesheetLocation')

    # The readonly property of time sheet rule set. <br />  Cascade Source: [EmployeeJobs].[TimesheetRuleSetID].
    timesheet_rule_set: typing.Optional[typing.Optional[str]] = Field(None, alias='TimesheetRuleSet')

    # The time set lunch duration. <br />  Cascade Source: [EmployeeJobs].[LunchDuration].
    timesheet_lunch_duration: typing.Optional[typing.Optional[str]] = Field(None, alias='TimesheetLunchDuration')

    # The readonly property of automatic enrolment profiles. <br />  Cascade Source: [EmployeeJobs].[AutoEnrolmentProfile].
    auto_enrolment_profile: typing.Optional[typing.Optional[str]] = Field(None, alias='AutoEnrolmentProfile')

    # The expense submission frequency. <br />  Cascade Source: [EmployeeJobs].[ExpenseSubmissionFrequency].
    expense_submission_frequency: typing.Optional[typing.Optional[str]] = Field(None, alias='ExpenseSubmissionFrequency')

    # The cost centre. <br />  Cascade Source: [EmployeeJobs].[CostCentre].
    cost_centre: typing.Optional[typing.Optional[str]] = Field(None, alias='CostCentre')

    # The job family. <br />  Cascade Source: [EmployeeJobs].[JobFamily].
    job_family: typing.Optional[typing.Optional[str]] = Field(None, alias='JobFamily')

    # The flag to indicate if the employee is an apprentice under 25. <br />  Cascade Source: [EmployeeJobs].[ApprenticeUnder25].
    apprentice_under25: typing.Optional[typing.Optional[bool]] = Field(None, alias='ApprenticeUnder25')

    # The end date of the apprenticeship. <br />  Cascade Source: [EmployeeJobs].[ApprenticeshipEndDate].
    apprenticeship_end_date: typing.Optional[typing.Optional[datetime]] = Field(None, alias='ApprenticeshipEndDate')

    # The end date of the contract. <br />  Cascade Source: [EmployeeJobs].[ContractEndDate].
    contract_end_date: typing.Optional[typing.Optional[datetime]] = Field(None, alias='ContractEndDate')

    # The readonly property of reports to post. <br />  Cascade Source: [EmployeeJobs].[ReportsToPost].
    reports_to_post: typing.Optional[typing.Optional[str]] = Field(None, alias='ReportsToPost')

    # Normal hours. <br />  Cascade Source: [EmployeeJobs].[NormalHours].
    normal_hours: typing.Optional[typing.Optional[typing.Union[int, float]]] = Field(None, alias='NormalHours')

    # The real time information of irregular frequency. <br />  Cascade Source: [EmployeeJobs].[RTIIrregularFrequency].
    real_time_information_irregular_frequency: typing.Optional[typing.Optional[str]] = Field(None, alias='RealTimeInformationIrregularFrequency')

    # The notice period. <br />  Cascade Source: [EmployeeJobs].[NoticePeriod].
    notice_period: typing.Optional[typing.Optional[str]] = Field(None, alias='NoticePeriod')

    # This ID is generated by the Iris Hr platform and does not relate to the Cascade ID.
    id: typing.Optional[typing.Optional[str]] = Field(None, alias='Id')

    # Source HR System Id. <br />  Cascade Source: [EmployeeJobs].[Ruid] <br />  Read Only
    source_system_id: typing.Optional[typing.Optional[str]] = Field(None, alias='SourceSystemId')

    # The date when the Job was created in the Iris Hr platform.
    created_on: typing.Optional[datetime] = Field(None, alias='CreatedOn')

    # The date when the Job was created in the Source HR System. <br />  Cascade Source: [EmployeeJobs].[SYS_EffectiveDate] <br />  Note: In Cascade this value is also the Start Date of the Job and can changed at any time. <br />  Read Only
    source_system_created_on: typing.Optional[typing.Optional[datetime]] = Field(None, alias='SourceSystemCreatedOn')

    # Not used as the Iris Hr platform has no concept of users at the moment.
    created_by: typing.Optional[typing.Optional[str]] = Field(None, alias='CreatedBy')

    # The date when the Job was created or last updated.
    last_modified_on: typing.Optional[typing.Optional[datetime]] = Field(None, alias='LastModifiedOn')

    # The date when the Job was created or last updated in the Source HR System. <br />  Cascade Source: [EmployeeJobs].[SYS_ModifiedDate] <br />  Read Only
    source_system_last_modified_on: typing.Optional[typing.Optional[datetime]] = Field(None, alias='SourceSystemLastModifiedOn')

    # Not used as Iris Hr platform has no concept of users at the moment.
    last_modified_by: typing.Optional[typing.Optional[str]] = Field(None, alias='LastModifiedBy')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
