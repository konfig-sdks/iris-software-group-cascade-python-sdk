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


class RequiredCreateJobCommand(TypedDict):
    pass

class OptionalCreateJobCommand(TypedDict, total=False):
    # The title of the Job. <br />  Cascade Source: [EmployeeJobs].[JobTitle]
    JobTitle: typing.Optional[str]

    # The classification of the Job e.g. Technical, Professional, Managerial. <br />  Cascade Source: [EmployeeJobs].[Classification] translated through the JOBCLASSIFICATION system list.
    Classification: typing.Optional[str]

    # The start date of the Job. <br />  Required. <br />  Cascade Source: [EmployeeJobs].[SYS_EffectiveDate]
    StartDate: datetime

    # The end date of the Job. <br />  Automatically Calculated. <br />  Cascade Source: [EmployeeJobs].[SYS_CalculatedEndDate]
    EndDate: typing.Optional[datetime]

    # The name of the working calendar of the Job. <br />  Cascade Source: [EmployeeJobs].[CalendarName] which comes from [ValidWorkingCalendar].[CalendarName]
    WorkingCalendar: typing.Optional[str]

    # The ID of the Employee that is the line manager for this Job. <br />  Must exist in Employees Service. <br />  Cascade Source: [EmployeeJobs].[WorksForEmployeeId]
    LineManagerId: typing.Optional[str]

    # The ID of the Employee's Hierarchy node of the Job. <br />  Must exist in Hierarchy Service.
    HierarchyNodeId: typing.Optional[str]

    # The Job is currently active. <br />  Automatically Calculated. <br />  Cascade Source: [EmployeeJobs].[sys_ActiveJob]
    Active: bool

    # The salary of the Job. <br />  Cascade Source: [EmployeeJobs].[BasicPay]
    Salary: typing.Optional[typing.Union[int, float]]

    # The ID of the Employee of the Job. <br />  Must exist in Employee Service.
    EmployeeId: typing.Optional[str]

    # The contract of the Job e.g. Full Time, Part Time. <br />  Cascade Source: [EmployeeJobs].[ContractType] translated through the EMPLOYMENTTYPES system list.
    Contract: typing.Optional[str]

    # How often the Job's salary will be paid e.g. Monthly, Weekly. <br />  Cascade Source: [EmployeeJobs].[PayFrequency] translated through the PAY FREQ system list.
    PayFrequency: typing.Optional[str]

    # The unit of measurement the salary is specified against e.g. Yearly, Hourly. <br />  Cascade Source: [EmployeeJobs].[PayBasis] translated through the PAY BASIS system list.
    PayBasis: typing.Optional[str]

    # The full-time equivalent to a full time employee's hours e.g. 1 = Full Time, 0.5 = Half Hours. <br />  Cascade Source: [EmployeeJobs].[FTE].
    FullTimeEquivalent: typing.Optional[typing.Union[int, float]]

    # The reason for the change. <br />  Cascade Source: [EmployeeJobs].[Reason].
    ChangeReason: typing.Optional[str]

    # The next increment date.  <br />  Cascade Source: [EmployeeJobs].[IncrementDate].
    NextIncrementDate: typing.Optional[datetime]

    # The timesheet location. <br />  Cascade Source: [EmployeeJobs].[TimesheetLocation].
    TimesheetLocation: typing.Optional[str]

    # The time set lunch duration. <br />  Cascade Source: [EmployeeJobs].[LunchDuration].
    TimesheetLunchDuration: typing.Optional[str]

    # The expense submission frequency. <br />  Cascade Source: [EmployeeJobs].[ExpenseSubmissionFrequency].
    ExpenseSubmissionFrequency: typing.Optional[str]

    # The cost centre. <br />  Cascade Source: [EmployeeJobs].[CostCentre].
    CostCentre: typing.Optional[str]

    # The job family. <br />  Cascade Source: [EmployeeJobs].[JobFamily].
    JobFamily: typing.Optional[str]

    # The flag to indicate if the employee is an apprentice under 25. <br />  Cascade Source: [EmployeeJobs].[ApprenticeUnder25].
    ApprenticeUnder25: typing.Optional[bool]

    # The end date of the apprenticeship. <br />  Cascade Source: [EmployeeJobs].[ApprenticeshipEndDate].
    ApprenticeshipEndDate: typing.Optional[datetime]

    # The end date of the contract. <br />  Cascade Source: [EmployeeJobs].[ContractEndDate].
    ContractEndDate: typing.Optional[datetime]

    # Normal hours. <br />  Cascade Source: [EmployeeJobs].[NormalHours].
    NormalHours: typing.Optional[typing.Union[int, float]]

    # The real time information of irregular frequency. <br />  Cascade Source: [EmployeeJobs].[RTIIrregularFrequency].
    RealTimeInformationIrregularFrequency: typing.Optional[str]

    # The notice period. <br />  Cascade Source: [EmployeeJobs].[NoticePeriod].
    NoticePeriod: typing.Optional[str]

class CreateJobCommand(RequiredCreateJobCommand, OptionalCreateJobCommand):
    pass
