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

from iris_software_group_cascade_python_sdk.type.address import Address
from iris_software_group_cascade_python_sdk.type.email import Email
from iris_software_group_cascade_python_sdk.type.phone import Phone

class RequiredUpdateEmployeeCommand(TypedDict):
    pass

class OptionalUpdateEmployeeCommand(TypedDict, total=False):
    # The Display ID of the Employee. <br />  If provided must be unqiue, If null then it will automatically be generated. <br />  Cascade Source: [Employee].[DisplayEmployeeId]
    DisplayId: typing.Optional[str]

    # The Title of the Employee. E.g. Mr, Mrs, Miss. <br />  Cascade Source: [Employee].[Title] translated through the TITLE system list.
    TitleHonorific: typing.Optional[str]

    # The First Name of the Employee. <br />  Required. <br />  Cascade Source: [Employee].[Forename]
    FirstName: typing.Optional[str]

    # The name the Employee is commonly known as. <br />  Cascade Source: [Employee].[KnownAs]
    KnownAs: typing.Optional[str]

    # Any other name that the Employee has. <br />  Cascade Source: [Employee].[OtherName]
    OtherName: typing.Optional[str]

    # The Last Name, Surname or Family Name of the Employee. <br />  Required. <br />  Cascade Source: [Employee].[Surname]
    LastName: typing.Optional[str]

    # The Cost Centre assigned to the Employee. <br />  Cascade Source: [Employee].[CostCentre]
    CostCentre: typing.Optional[str]

    # The Status of the Employee E.g. On Holiday, Sick. <br />  Automatically Calculated. <br />  Cascade Source: [Sysview_Employee_Status].[StatusDescription]
    WorkingStatus: typing.Optional[str]

    # Indicates if the Employee is a Manager. <br />  True if any other Employee's active <see cref=\"T:Iris.Api.Hr.Employee.Domain.Entities.V1.Job\">Job</see> has this Employee as their Line Manager. <br />  Automaticaly Calculated.
    IsManager: typing.Optional[bool]

    # The National Insurance Number of the Employee. <br />  Cascade Source: [Employee].[NationalInsuranceNo]
    NationalInsuranceNumber: typing.Optional[str]

    # The Payroll ID of the Employee. <br />  Cascade Source: [Employee].[PayrollId]
    PayrollId: typing.Optional[str]

    # The Tax Code of the Employee. <br />  Cascade Source: [Employee].[TaxCode]
    TaxCode: typing.Optional[str]

    # Indicates if the Employee should be included in Payroll. <br />  Cascade Source: [Employee].[IncludeInPayroll]
    IncludeInPayroll: typing.Optional[bool]

    # The date the Employee started with their current Employer. <br />  Cascade Source: [Employee].[EmployeeStartDate]
    EmploymentStartDate: typing.Optional[datetime]

    # The date the Employee left their current Employer. <br />  Cascade Source: [Employee].[EmployementLeftDate]
    EmploymentLeftDate: typing.Optional[datetime]

    # The date the Employee's continuous service should be applied from. <br />  Cascade Source: [Employee].[ContServiceDate]
    ContinuousServiceDate: typing.Optional[datetime]

    # The Date of Birth of the Employee. <br />  Cascade Source: [Employee].[DateOfBirth]
    DateOfBirth: typing.Optional[datetime]

    # The date of the last working date of the Employee. <br />  Cascade Source: [Employee].[LeaverLastWorkDate]
    LastWorkingDate: typing.Optional[datetime]

    # The Gender of the Employee. <br />  Cascade Source: [Employee].[Sex] translated through the GENDER system list.
    Gender: typing.Optional[str]

    # The Ethnicity of the Employee. <br />  Cascade Source: [Employee].[EthnicOrigin] translated through the ETHNICTORIGIN system list.
    Ethnicity: typing.Optional[str]

    # The Nationality of the Employee. <br />  Cascade Source: [Employee].[Nationality] translated through the NATIONALITY system list.
    Nationality: typing.Optional[str]

    # The Religion of the Employee. <br />  Cascade Source: [Employee].[Religion] transalated through the RELIGION system list.
    Religion: typing.Optional[str]

    # The reason for the Employee to Leave. <br />  Cascade Source: [Employee].[LeaverReason]
    LeaverReason: typing.Optional[str]

    # The marrital status of the Employee. <br />  Cascade Source: [Employee.[MaritalStatus] translated through the MARITALSTATUS system list.
    MaritalStatus: typing.Optional[str]

    # The <see cref=\"T:Iris.Api.Hr.Employee.Domain.Entities.V1.Phone\">Phone Numbers</see> belonging to the Employee.
    Phones: typing.Optional[typing.List[Phone]]

    # The <see cref=\"T:Iris.Api.Hr.Employee.Domain.Entities.V1.Email\">Email Addresses</see> belonging to the Employee.
    Emails: typing.Optional[typing.List[Email]]

    # The <see cref=\"T:Iris.Api.Hr.Employee.Domain.Entities.V1.Address\">Addresses</see> belonging to the Employee.
    Addresses: typing.Optional[typing.List[Address]]

    # The Gender Identity of the Employee. <br />  Cascade Source: [Employee].[GenderIdentity] translated through the GenderIdentity system list.
    GenderIdentity: typing.Optional[str]

    # The Windows Username of the Employee. <br />  Cascade Source: [Employee].[WindowsUsername]
    WindowsUsername: typing.Optional[str]

    # The ID of the Employee. <br />  Must exist in the Employee Service.
    Id: typing.Optional[str]

class UpdateEmployeeCommand(RequiredUpdateEmployeeCommand, OptionalUpdateEmployeeCommand):
    pass
