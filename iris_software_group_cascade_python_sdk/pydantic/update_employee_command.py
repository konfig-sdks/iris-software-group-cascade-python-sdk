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

from iris_software_group_cascade_python_sdk.pydantic.address import Address
from iris_software_group_cascade_python_sdk.pydantic.email import Email
from iris_software_group_cascade_python_sdk.pydantic.phone import Phone

class UpdateEmployeeCommand(BaseModel):
    # The Display ID of the Employee. <br />  If provided must be unqiue, If null then it will automatically be generated. <br />  Cascade Source: [Employee].[DisplayEmployeeId]
    display_id: typing.Optional[typing.Optional[str]] = Field(None, alias='DisplayId')

    # The Title of the Employee. E.g. Mr, Mrs, Miss. <br />  Cascade Source: [Employee].[Title] translated through the TITLE system list.
    title_honorific: typing.Optional[typing.Optional[str]] = Field(None, alias='TitleHonorific')

    # The First Name of the Employee. <br />  Required. <br />  Cascade Source: [Employee].[Forename]
    first_name: typing.Optional[typing.Optional[str]] = Field(None, alias='FirstName')

    # The name the Employee is commonly known as. <br />  Cascade Source: [Employee].[KnownAs]
    known_as: typing.Optional[typing.Optional[str]] = Field(None, alias='KnownAs')

    # Any other name that the Employee has. <br />  Cascade Source: [Employee].[OtherName]
    other_name: typing.Optional[typing.Optional[str]] = Field(None, alias='OtherName')

    # The Last Name, Surname or Family Name of the Employee. <br />  Required. <br />  Cascade Source: [Employee].[Surname]
    last_name: typing.Optional[typing.Optional[str]] = Field(None, alias='LastName')

    # The Cost Centre assigned to the Employee. <br />  Cascade Source: [Employee].[CostCentre]
    cost_centre: typing.Optional[typing.Optional[str]] = Field(None, alias='CostCentre')

    # The Status of the Employee E.g. On Holiday, Sick. <br />  Automatically Calculated. <br />  Cascade Source: [Sysview_Employee_Status].[StatusDescription]
    working_status: typing.Optional[typing.Optional[str]] = Field(None, alias='WorkingStatus')

    # Indicates if the Employee is a Manager. <br />  True if any other Employee's active <see cref=\"T:Iris.Api.Hr.Employee.Domain.Entities.V1.Job\">Job</see> has this Employee as their Line Manager. <br />  Automaticaly Calculated.
    is_manager: typing.Optional[typing.Optional[bool]] = Field(None, alias='IsManager')

    # The National Insurance Number of the Employee. <br />  Cascade Source: [Employee].[NationalInsuranceNo]
    national_insurance_number: typing.Optional[typing.Optional[str]] = Field(None, alias='NationalInsuranceNumber')

    # The Payroll ID of the Employee. <br />  Cascade Source: [Employee].[PayrollId]
    payroll_id: typing.Optional[typing.Optional[str]] = Field(None, alias='PayrollId')

    # The Tax Code of the Employee. <br />  Cascade Source: [Employee].[TaxCode]
    tax_code: typing.Optional[typing.Optional[str]] = Field(None, alias='TaxCode')

    # Indicates if the Employee should be included in Payroll. <br />  Cascade Source: [Employee].[IncludeInPayroll]
    include_in_payroll: typing.Optional[typing.Optional[bool]] = Field(None, alias='IncludeInPayroll')

    # The date the Employee started with their current Employer. <br />  Cascade Source: [Employee].[EmployeeStartDate]
    employment_start_date: typing.Optional[typing.Optional[datetime]] = Field(None, alias='EmploymentStartDate')

    # The date the Employee left their current Employer. <br />  Cascade Source: [Employee].[EmployementLeftDate]
    employment_left_date: typing.Optional[typing.Optional[datetime]] = Field(None, alias='EmploymentLeftDate')

    # The date the Employee's continuous service should be applied from. <br />  Cascade Source: [Employee].[ContServiceDate]
    continuous_service_date: typing.Optional[typing.Optional[datetime]] = Field(None, alias='ContinuousServiceDate')

    # The Date of Birth of the Employee. <br />  Cascade Source: [Employee].[DateOfBirth]
    date_of_birth: typing.Optional[typing.Optional[datetime]] = Field(None, alias='DateOfBirth')

    # The date of the last working date of the Employee. <br />  Cascade Source: [Employee].[LeaverLastWorkDate]
    last_working_date: typing.Optional[typing.Optional[datetime]] = Field(None, alias='LastWorkingDate')

    # The Gender of the Employee. <br />  Cascade Source: [Employee].[Sex] translated through the GENDER system list.
    gender: typing.Optional[typing.Optional[str]] = Field(None, alias='Gender')

    # The Ethnicity of the Employee. <br />  Cascade Source: [Employee].[EthnicOrigin] translated through the ETHNICTORIGIN system list.
    ethnicity: typing.Optional[typing.Optional[str]] = Field(None, alias='Ethnicity')

    # The Nationality of the Employee. <br />  Cascade Source: [Employee].[Nationality] translated through the NATIONALITY system list.
    nationality: typing.Optional[typing.Optional[str]] = Field(None, alias='Nationality')

    # The Religion of the Employee. <br />  Cascade Source: [Employee].[Religion] transalated through the RELIGION system list.
    religion: typing.Optional[typing.Optional[str]] = Field(None, alias='Religion')

    # The reason for the Employee to Leave. <br />  Cascade Source: [Employee].[LeaverReason]
    leaver_reason: typing.Optional[typing.Optional[str]] = Field(None, alias='LeaverReason')

    # The marrital status of the Employee. <br />  Cascade Source: [Employee.[MaritalStatus] translated through the MARITALSTATUS system list.
    marital_status: typing.Optional[typing.Optional[str]] = Field(None, alias='MaritalStatus')

    # The <see cref=\"T:Iris.Api.Hr.Employee.Domain.Entities.V1.Phone\">Phone Numbers</see> belonging to the Employee.
    phones: typing.Optional[typing.Optional[typing.List[Phone]]] = Field(None, alias='Phones')

    # The <see cref=\"T:Iris.Api.Hr.Employee.Domain.Entities.V1.Email\">Email Addresses</see> belonging to the Employee.
    emails: typing.Optional[typing.Optional[typing.List[Email]]] = Field(None, alias='Emails')

    # The <see cref=\"T:Iris.Api.Hr.Employee.Domain.Entities.V1.Address\">Addresses</see> belonging to the Employee.
    addresses: typing.Optional[typing.Optional[typing.List[Address]]] = Field(None, alias='Addresses')

    # The Gender Identity of the Employee. <br />  Cascade Source: [Employee].[GenderIdentity] translated through the GenderIdentity system list.
    gender_identity: typing.Optional[typing.Optional[str]] = Field(None, alias='GenderIdentity')

    # The Windows Username of the Employee. <br />  Cascade Source: [Employee].[WindowsUsername]
    windows_username: typing.Optional[typing.Optional[str]] = Field(None, alias='WindowsUsername')

    # The ID of the Employee. <br />  Must exist in the Employee Service.
    id: typing.Optional[typing.Optional[str]] = Field(None, alias='Id')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
