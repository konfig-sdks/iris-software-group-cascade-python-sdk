# coding: utf-8

"""
    HR API

    <a href='swaggerv2.json'>Download Swagger Json in OAS2 Format.</a>

    The version of the OpenAPI document: 2
    Contact: hrapi@iris.co.uk
    Created by: https://help.iris.co.uk/hr/cascade/api/
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from iris_software_group_cascade_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from iris_software_group_cascade_python_sdk.api_response import AsyncGeneratorResponse
from iris_software_group_cascade_python_sdk import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from iris_software_group_cascade_python_sdk import schemas  # noqa: F401

from iris_software_group_cascade_python_sdk.model.email import Email as EmailSchema
from iris_software_group_cascade_python_sdk.model.address import Address as AddressSchema
from iris_software_group_cascade_python_sdk.model.create_employee_command import CreateEmployeeCommand as CreateEmployeeCommandSchema
from iris_software_group_cascade_python_sdk.model.phone import Phone as PhoneSchema

from iris_software_group_cascade_python_sdk.type.address import Address
from iris_software_group_cascade_python_sdk.type.create_employee_command import CreateEmployeeCommand
from iris_software_group_cascade_python_sdk.type.email import Email
from iris_software_group_cascade_python_sdk.type.phone import Phone

from ...api_client import Dictionary
from iris_software_group_cascade_python_sdk.pydantic.email import Email as EmailPydantic
from iris_software_group_cascade_python_sdk.pydantic.address import Address as AddressPydantic
from iris_software_group_cascade_python_sdk.pydantic.phone import Phone as PhonePydantic
from iris_software_group_cascade_python_sdk.pydantic.create_employee_command import CreateEmployeeCommand as CreateEmployeeCommandPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJsonodataMetadataminimalodataStreamingtrueVersion2 = CreateEmployeeCommandSchema
SchemaForRequestBodyApplicationJsonodataMetadataminimalodataStreamingfalseVersion2 = CreateEmployeeCommandSchema
SchemaForRequestBodyApplicationJsonodataMetadataminimalVersion2 = CreateEmployeeCommandSchema
SchemaForRequestBodyApplicationJsonodataMetadatafullodataStreamingtrueVersion2 = CreateEmployeeCommandSchema
SchemaForRequestBodyApplicationJsonodataMetadatafullodataStreamingfalseVersion2 = CreateEmployeeCommandSchema
SchemaForRequestBodyApplicationJsonodataMetadatafullVersion2 = CreateEmployeeCommandSchema
SchemaForRequestBodyApplicationJsonodataMetadatanoneodataStreamingtrueVersion2 = CreateEmployeeCommandSchema
SchemaForRequestBodyApplicationJsonodataMetadatanoneodataStreamingfalseVersion2 = CreateEmployeeCommandSchema
SchemaForRequestBodyApplicationJsonodataMetadatanoneVersion2 = CreateEmployeeCommandSchema
SchemaForRequestBodyApplicationJsonodataStreamingtrueVersion2 = CreateEmployeeCommandSchema
SchemaForRequestBodyApplicationJsonodataStreamingfalseVersion2 = CreateEmployeeCommandSchema
SchemaForRequestBodyApplicationJsonVersion2 = CreateEmployeeCommandSchema
SchemaForRequestBodyApplicationXmlVersion2 = CreateEmployeeCommandSchema
SchemaForRequestBodyApplicationPrsOdatatestxxOdataVersion2 = CreateEmployeeCommandSchema
SchemaForRequestBodyTextJsonVersion2 = CreateEmployeeCommandSchema
SchemaForRequestBodyApplicationJsonVersion2 = CreateEmployeeCommandSchema


request_body_create_employee_command = api_client.RequestBody(
    content={
        'application/json;odata.metadata=minimal;odata.streaming=true; version=2': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJsonodataMetadataminimalodataStreamingtrueVersion2),
        'application/json;odata.metadata=minimal;odata.streaming=false; version=2': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJsonodataMetadataminimalodataStreamingfalseVersion2),
        'application/json;odata.metadata=minimal; version=2': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJsonodataMetadataminimalVersion2),
        'application/json;odata.metadata=full;odata.streaming=true; version=2': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJsonodataMetadatafullodataStreamingtrueVersion2),
        'application/json;odata.metadata=full;odata.streaming=false; version=2': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJsonodataMetadatafullodataStreamingfalseVersion2),
        'application/json;odata.metadata=full; version=2': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJsonodataMetadatafullVersion2),
        'application/json;odata.metadata=none;odata.streaming=true; version=2': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJsonodataMetadatanoneodataStreamingtrueVersion2),
        'application/json;odata.metadata=none;odata.streaming=false; version=2': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJsonodataMetadatanoneodataStreamingfalseVersion2),
        'application/json;odata.metadata=none; version=2': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJsonodataMetadatanoneVersion2),
        'application/json;odata.streaming=true; version=2': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJsonodataStreamingtrueVersion2),
        'application/json;odata.streaming=false; version=2': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJsonodataStreamingfalseVersion2),
        'application/json; version=2': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJsonVersion2),
        'application/xml; version=2': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationXmlVersion2),
        'application/prs.odatatestxx-odata; version=2': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationPrsOdatatestxxOdataVersion2),
        'text/json; version=2': api_client.MediaType(
            schema=SchemaForRequestBodyTextJsonVersion2),
        'application/*+json; version=2': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJsonVersion2),
    },
)
_auth = [
    'Bearer',
]
SchemaFor200ResponseBodyApplicationJsonodataMetadataminimalodataStreamingtrueVersion2 = schemas.StrSchema
SchemaFor200ResponseBodyApplicationJsonodataMetadataminimalodataStreamingfalseVersion2 = schemas.StrSchema
SchemaFor200ResponseBodyApplicationJsonodataMetadataminimalVersion2 = schemas.StrSchema
SchemaFor200ResponseBodyApplicationJsonodataMetadatafullodataStreamingtrueVersion2 = schemas.StrSchema
SchemaFor200ResponseBodyApplicationJsonodataMetadatafullodataStreamingfalseVersion2 = schemas.StrSchema
SchemaFor200ResponseBodyApplicationJsonodataMetadatafullVersion2 = schemas.StrSchema
SchemaFor200ResponseBodyApplicationJsonodataMetadatanoneodataStreamingtrueVersion2 = schemas.StrSchema
SchemaFor200ResponseBodyApplicationJsonodataMetadatanoneodataStreamingfalseVersion2 = schemas.StrSchema
SchemaFor200ResponseBodyApplicationJsonodataMetadatanoneVersion2 = schemas.StrSchema
SchemaFor200ResponseBodyApplicationJsonodataStreamingtrueVersion2 = schemas.StrSchema
SchemaFor200ResponseBodyApplicationJsonodataStreamingfalseVersion2 = schemas.StrSchema
SchemaFor200ResponseBodyApplicationJsonVersion2 = schemas.StrSchema
SchemaFor200ResponseBodyApplicationXmlVersion2 = schemas.StrSchema
SchemaFor200ResponseBodyApplicationPrsOdatatestxxOdataVersion2 = schemas.StrSchema
SchemaFor200ResponseBodyTextPlainVersion2 = schemas.StrSchema
SchemaFor200ResponseBodyTextJsonVersion2 = schemas.StrSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: str


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: str


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json;odata.metadata=minimal;odata.streaming=true; version=2': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJsonodataMetadataminimalodataStreamingtrueVersion2),
        'application/json;odata.metadata=minimal;odata.streaming=false; version=2': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJsonodataMetadataminimalodataStreamingfalseVersion2),
        'application/json;odata.metadata=minimal; version=2': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJsonodataMetadataminimalVersion2),
        'application/json;odata.metadata=full;odata.streaming=true; version=2': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJsonodataMetadatafullodataStreamingtrueVersion2),
        'application/json;odata.metadata=full;odata.streaming=false; version=2': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJsonodataMetadatafullodataStreamingfalseVersion2),
        'application/json;odata.metadata=full; version=2': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJsonodataMetadatafullVersion2),
        'application/json;odata.metadata=none;odata.streaming=true; version=2': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJsonodataMetadatanoneodataStreamingtrueVersion2),
        'application/json;odata.metadata=none;odata.streaming=false; version=2': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJsonodataMetadatanoneodataStreamingfalseVersion2),
        'application/json;odata.metadata=none; version=2': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJsonodataMetadatanoneVersion2),
        'application/json;odata.streaming=true; version=2': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJsonodataStreamingtrueVersion2),
        'application/json;odata.streaming=false; version=2': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJsonodataStreamingfalseVersion2),
        'application/json; version=2': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJsonVersion2),
        'application/xml; version=2': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationXmlVersion2),
        'application/prs.odatatestxx-odata; version=2': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationPrsOdatatestxxOdataVersion2),
        'text/plain; version=2': api_client.MediaType(
            schema=SchemaFor200ResponseBodyTextPlainVersion2),
        'text/json; version=2': api_client.MediaType(
            schema=SchemaFor200ResponseBodyTextJsonVersion2),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
}
_all_accept_content_types = (
    'application/json;odata.metadata=minimal;odata.streaming=true; version=2',
    'application/json;odata.metadata=minimal;odata.streaming=false; version=2',
    'application/json;odata.metadata=minimal; version=2',
    'application/json;odata.metadata=full;odata.streaming=true; version=2',
    'application/json;odata.metadata=full;odata.streaming=false; version=2',
    'application/json;odata.metadata=full; version=2',
    'application/json;odata.metadata=none;odata.streaming=true; version=2',
    'application/json;odata.metadata=none;odata.streaming=false; version=2',
    'application/json;odata.metadata=none; version=2',
    'application/json;odata.streaming=true; version=2',
    'application/json;odata.streaming=false; version=2',
    'application/json; version=2',
    'application/xml; version=2',
    'application/prs.odatatestxx-odata; version=2',
    'text/plain; version=2',
    'text/json; version=2',
)


class BaseApi(api_client.Api):

    def _create_new_employee_mapped_args(
        self,
        display_id: typing.Optional[typing.Optional[str]] = None,
        title_honorific: typing.Optional[typing.Optional[str]] = None,
        first_name: typing.Optional[typing.Optional[str]] = None,
        known_as: typing.Optional[typing.Optional[str]] = None,
        other_name: typing.Optional[typing.Optional[str]] = None,
        last_name: typing.Optional[typing.Optional[str]] = None,
        cost_centre: typing.Optional[typing.Optional[str]] = None,
        working_status: typing.Optional[typing.Optional[str]] = None,
        is_manager: typing.Optional[typing.Optional[bool]] = None,
        national_insurance_number: typing.Optional[typing.Optional[str]] = None,
        payroll_id: typing.Optional[typing.Optional[str]] = None,
        tax_code: typing.Optional[typing.Optional[str]] = None,
        include_in_payroll: typing.Optional[typing.Optional[bool]] = None,
        employment_start_date: typing.Optional[typing.Optional[datetime]] = None,
        employment_left_date: typing.Optional[typing.Optional[datetime]] = None,
        continuous_service_date: typing.Optional[typing.Optional[datetime]] = None,
        date_of_birth: typing.Optional[typing.Optional[datetime]] = None,
        last_working_date: typing.Optional[typing.Optional[datetime]] = None,
        gender: typing.Optional[typing.Optional[str]] = None,
        ethnicity: typing.Optional[typing.Optional[str]] = None,
        nationality: typing.Optional[typing.Optional[str]] = None,
        religion: typing.Optional[typing.Optional[str]] = None,
        leaver_reason: typing.Optional[typing.Optional[str]] = None,
        marital_status: typing.Optional[typing.Optional[str]] = None,
        phones: typing.Optional[typing.Optional[typing.List[Phone]]] = None,
        emails: typing.Optional[typing.Optional[typing.List[Email]]] = None,
        addresses: typing.Optional[typing.Optional[typing.List[Address]]] = None,
        gender_identity: typing.Optional[typing.Optional[str]] = None,
        windows_username: typing.Optional[typing.Optional[str]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if display_id is not None:
            _body["DisplayId"] = display_id
        if title_honorific is not None:
            _body["TitleHonorific"] = title_honorific
        if first_name is not None:
            _body["FirstName"] = first_name
        if known_as is not None:
            _body["KnownAs"] = known_as
        if other_name is not None:
            _body["OtherName"] = other_name
        if last_name is not None:
            _body["LastName"] = last_name
        if cost_centre is not None:
            _body["CostCentre"] = cost_centre
        if working_status is not None:
            _body["WorkingStatus"] = working_status
        if is_manager is not None:
            _body["IsManager"] = is_manager
        if national_insurance_number is not None:
            _body["NationalInsuranceNumber"] = national_insurance_number
        if payroll_id is not None:
            _body["PayrollId"] = payroll_id
        if tax_code is not None:
            _body["TaxCode"] = tax_code
        if include_in_payroll is not None:
            _body["IncludeInPayroll"] = include_in_payroll
        if employment_start_date is not None:
            _body["EmploymentStartDate"] = employment_start_date
        if employment_left_date is not None:
            _body["EmploymentLeftDate"] = employment_left_date
        if continuous_service_date is not None:
            _body["ContinuousServiceDate"] = continuous_service_date
        if date_of_birth is not None:
            _body["DateOfBirth"] = date_of_birth
        if last_working_date is not None:
            _body["LastWorkingDate"] = last_working_date
        if gender is not None:
            _body["Gender"] = gender
        if ethnicity is not None:
            _body["Ethnicity"] = ethnicity
        if nationality is not None:
            _body["Nationality"] = nationality
        if religion is not None:
            _body["Religion"] = religion
        if leaver_reason is not None:
            _body["LeaverReason"] = leaver_reason
        if marital_status is not None:
            _body["MaritalStatus"] = marital_status
        if phones is not None:
            _body["Phones"] = phones
        if emails is not None:
            _body["Emails"] = emails
        if addresses is not None:
            _body["Addresses"] = addresses
        if gender_identity is not None:
            _body["GenderIdentity"] = gender_identity
        if windows_username is not None:
            _body["WindowsUsername"] = windows_username
        args.body = _body
        return args

    async def _acreate_new_employee_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json;odata.metadata=minimal;odata.streaming=true; version=2',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Creates a new Employee.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/employees',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_create_employee_command.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _create_new_employee_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json;odata.metadata=minimal;odata.streaming=true; version=2',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Creates a new Employee.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/employees',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_create_employee_command.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class CreateNewEmployeeRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_new_employee(
        self,
        display_id: typing.Optional[typing.Optional[str]] = None,
        title_honorific: typing.Optional[typing.Optional[str]] = None,
        first_name: typing.Optional[typing.Optional[str]] = None,
        known_as: typing.Optional[typing.Optional[str]] = None,
        other_name: typing.Optional[typing.Optional[str]] = None,
        last_name: typing.Optional[typing.Optional[str]] = None,
        cost_centre: typing.Optional[typing.Optional[str]] = None,
        working_status: typing.Optional[typing.Optional[str]] = None,
        is_manager: typing.Optional[typing.Optional[bool]] = None,
        national_insurance_number: typing.Optional[typing.Optional[str]] = None,
        payroll_id: typing.Optional[typing.Optional[str]] = None,
        tax_code: typing.Optional[typing.Optional[str]] = None,
        include_in_payroll: typing.Optional[typing.Optional[bool]] = None,
        employment_start_date: typing.Optional[typing.Optional[datetime]] = None,
        employment_left_date: typing.Optional[typing.Optional[datetime]] = None,
        continuous_service_date: typing.Optional[typing.Optional[datetime]] = None,
        date_of_birth: typing.Optional[typing.Optional[datetime]] = None,
        last_working_date: typing.Optional[typing.Optional[datetime]] = None,
        gender: typing.Optional[typing.Optional[str]] = None,
        ethnicity: typing.Optional[typing.Optional[str]] = None,
        nationality: typing.Optional[typing.Optional[str]] = None,
        religion: typing.Optional[typing.Optional[str]] = None,
        leaver_reason: typing.Optional[typing.Optional[str]] = None,
        marital_status: typing.Optional[typing.Optional[str]] = None,
        phones: typing.Optional[typing.Optional[typing.List[Phone]]] = None,
        emails: typing.Optional[typing.Optional[typing.List[Email]]] = None,
        addresses: typing.Optional[typing.Optional[typing.List[Address]]] = None,
        gender_identity: typing.Optional[typing.Optional[str]] = None,
        windows_username: typing.Optional[typing.Optional[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_employee_mapped_args(
            display_id=display_id,
            title_honorific=title_honorific,
            first_name=first_name,
            known_as=known_as,
            other_name=other_name,
            last_name=last_name,
            cost_centre=cost_centre,
            working_status=working_status,
            is_manager=is_manager,
            national_insurance_number=national_insurance_number,
            payroll_id=payroll_id,
            tax_code=tax_code,
            include_in_payroll=include_in_payroll,
            employment_start_date=employment_start_date,
            employment_left_date=employment_left_date,
            continuous_service_date=continuous_service_date,
            date_of_birth=date_of_birth,
            last_working_date=last_working_date,
            gender=gender,
            ethnicity=ethnicity,
            nationality=nationality,
            religion=religion,
            leaver_reason=leaver_reason,
            marital_status=marital_status,
            phones=phones,
            emails=emails,
            addresses=addresses,
            gender_identity=gender_identity,
            windows_username=windows_username,
        )
        return await self._acreate_new_employee_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_new_employee(
        self,
        display_id: typing.Optional[typing.Optional[str]] = None,
        title_honorific: typing.Optional[typing.Optional[str]] = None,
        first_name: typing.Optional[typing.Optional[str]] = None,
        known_as: typing.Optional[typing.Optional[str]] = None,
        other_name: typing.Optional[typing.Optional[str]] = None,
        last_name: typing.Optional[typing.Optional[str]] = None,
        cost_centre: typing.Optional[typing.Optional[str]] = None,
        working_status: typing.Optional[typing.Optional[str]] = None,
        is_manager: typing.Optional[typing.Optional[bool]] = None,
        national_insurance_number: typing.Optional[typing.Optional[str]] = None,
        payroll_id: typing.Optional[typing.Optional[str]] = None,
        tax_code: typing.Optional[typing.Optional[str]] = None,
        include_in_payroll: typing.Optional[typing.Optional[bool]] = None,
        employment_start_date: typing.Optional[typing.Optional[datetime]] = None,
        employment_left_date: typing.Optional[typing.Optional[datetime]] = None,
        continuous_service_date: typing.Optional[typing.Optional[datetime]] = None,
        date_of_birth: typing.Optional[typing.Optional[datetime]] = None,
        last_working_date: typing.Optional[typing.Optional[datetime]] = None,
        gender: typing.Optional[typing.Optional[str]] = None,
        ethnicity: typing.Optional[typing.Optional[str]] = None,
        nationality: typing.Optional[typing.Optional[str]] = None,
        religion: typing.Optional[typing.Optional[str]] = None,
        leaver_reason: typing.Optional[typing.Optional[str]] = None,
        marital_status: typing.Optional[typing.Optional[str]] = None,
        phones: typing.Optional[typing.Optional[typing.List[Phone]]] = None,
        emails: typing.Optional[typing.Optional[typing.List[Email]]] = None,
        addresses: typing.Optional[typing.Optional[typing.List[Address]]] = None,
        gender_identity: typing.Optional[typing.Optional[str]] = None,
        windows_username: typing.Optional[typing.Optional[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_employee_mapped_args(
            display_id=display_id,
            title_honorific=title_honorific,
            first_name=first_name,
            known_as=known_as,
            other_name=other_name,
            last_name=last_name,
            cost_centre=cost_centre,
            working_status=working_status,
            is_manager=is_manager,
            national_insurance_number=national_insurance_number,
            payroll_id=payroll_id,
            tax_code=tax_code,
            include_in_payroll=include_in_payroll,
            employment_start_date=employment_start_date,
            employment_left_date=employment_left_date,
            continuous_service_date=continuous_service_date,
            date_of_birth=date_of_birth,
            last_working_date=last_working_date,
            gender=gender,
            ethnicity=ethnicity,
            nationality=nationality,
            religion=religion,
            leaver_reason=leaver_reason,
            marital_status=marital_status,
            phones=phones,
            emails=emails,
            addresses=addresses,
            gender_identity=gender_identity,
            windows_username=windows_username,
        )
        return self._create_new_employee_oapg(
            body=args.body,
        )

class CreateNewEmployee(BaseApi):

    async def acreate_new_employee(
        self,
        display_id: typing.Optional[typing.Optional[str]] = None,
        title_honorific: typing.Optional[typing.Optional[str]] = None,
        first_name: typing.Optional[typing.Optional[str]] = None,
        known_as: typing.Optional[typing.Optional[str]] = None,
        other_name: typing.Optional[typing.Optional[str]] = None,
        last_name: typing.Optional[typing.Optional[str]] = None,
        cost_centre: typing.Optional[typing.Optional[str]] = None,
        working_status: typing.Optional[typing.Optional[str]] = None,
        is_manager: typing.Optional[typing.Optional[bool]] = None,
        national_insurance_number: typing.Optional[typing.Optional[str]] = None,
        payroll_id: typing.Optional[typing.Optional[str]] = None,
        tax_code: typing.Optional[typing.Optional[str]] = None,
        include_in_payroll: typing.Optional[typing.Optional[bool]] = None,
        employment_start_date: typing.Optional[typing.Optional[datetime]] = None,
        employment_left_date: typing.Optional[typing.Optional[datetime]] = None,
        continuous_service_date: typing.Optional[typing.Optional[datetime]] = None,
        date_of_birth: typing.Optional[typing.Optional[datetime]] = None,
        last_working_date: typing.Optional[typing.Optional[datetime]] = None,
        gender: typing.Optional[typing.Optional[str]] = None,
        ethnicity: typing.Optional[typing.Optional[str]] = None,
        nationality: typing.Optional[typing.Optional[str]] = None,
        religion: typing.Optional[typing.Optional[str]] = None,
        leaver_reason: typing.Optional[typing.Optional[str]] = None,
        marital_status: typing.Optional[typing.Optional[str]] = None,
        phones: typing.Optional[typing.Optional[typing.List[Phone]]] = None,
        emails: typing.Optional[typing.Optional[typing.List[Email]]] = None,
        addresses: typing.Optional[typing.Optional[typing.List[Address]]] = None,
        gender_identity: typing.Optional[typing.Optional[str]] = None,
        windows_username: typing.Optional[typing.Optional[str]] = None,
        validate: bool = False,
        **kwargs,
    ) -> str:
        raw_response = await self.raw.acreate_new_employee(
            display_id=display_id,
            title_honorific=title_honorific,
            first_name=first_name,
            known_as=known_as,
            other_name=other_name,
            last_name=last_name,
            cost_centre=cost_centre,
            working_status=working_status,
            is_manager=is_manager,
            national_insurance_number=national_insurance_number,
            payroll_id=payroll_id,
            tax_code=tax_code,
            include_in_payroll=include_in_payroll,
            employment_start_date=employment_start_date,
            employment_left_date=employment_left_date,
            continuous_service_date=continuous_service_date,
            date_of_birth=date_of_birth,
            last_working_date=last_working_date,
            gender=gender,
            ethnicity=ethnicity,
            nationality=nationality,
            religion=religion,
            leaver_reason=leaver_reason,
            marital_status=marital_status,
            phones=phones,
            emails=emails,
            addresses=addresses,
            gender_identity=gender_identity,
            windows_username=windows_username,
            **kwargs,
        )
        if validate:
            return RootModel[str](raw_response.body).root
        return raw_response.body
    
    
    def create_new_employee(
        self,
        display_id: typing.Optional[typing.Optional[str]] = None,
        title_honorific: typing.Optional[typing.Optional[str]] = None,
        first_name: typing.Optional[typing.Optional[str]] = None,
        known_as: typing.Optional[typing.Optional[str]] = None,
        other_name: typing.Optional[typing.Optional[str]] = None,
        last_name: typing.Optional[typing.Optional[str]] = None,
        cost_centre: typing.Optional[typing.Optional[str]] = None,
        working_status: typing.Optional[typing.Optional[str]] = None,
        is_manager: typing.Optional[typing.Optional[bool]] = None,
        national_insurance_number: typing.Optional[typing.Optional[str]] = None,
        payroll_id: typing.Optional[typing.Optional[str]] = None,
        tax_code: typing.Optional[typing.Optional[str]] = None,
        include_in_payroll: typing.Optional[typing.Optional[bool]] = None,
        employment_start_date: typing.Optional[typing.Optional[datetime]] = None,
        employment_left_date: typing.Optional[typing.Optional[datetime]] = None,
        continuous_service_date: typing.Optional[typing.Optional[datetime]] = None,
        date_of_birth: typing.Optional[typing.Optional[datetime]] = None,
        last_working_date: typing.Optional[typing.Optional[datetime]] = None,
        gender: typing.Optional[typing.Optional[str]] = None,
        ethnicity: typing.Optional[typing.Optional[str]] = None,
        nationality: typing.Optional[typing.Optional[str]] = None,
        religion: typing.Optional[typing.Optional[str]] = None,
        leaver_reason: typing.Optional[typing.Optional[str]] = None,
        marital_status: typing.Optional[typing.Optional[str]] = None,
        phones: typing.Optional[typing.Optional[typing.List[Phone]]] = None,
        emails: typing.Optional[typing.Optional[typing.List[Email]]] = None,
        addresses: typing.Optional[typing.Optional[typing.List[Address]]] = None,
        gender_identity: typing.Optional[typing.Optional[str]] = None,
        windows_username: typing.Optional[typing.Optional[str]] = None,
        validate: bool = False,
    ) -> str:
        raw_response = self.raw.create_new_employee(
            display_id=display_id,
            title_honorific=title_honorific,
            first_name=first_name,
            known_as=known_as,
            other_name=other_name,
            last_name=last_name,
            cost_centre=cost_centre,
            working_status=working_status,
            is_manager=is_manager,
            national_insurance_number=national_insurance_number,
            payroll_id=payroll_id,
            tax_code=tax_code,
            include_in_payroll=include_in_payroll,
            employment_start_date=employment_start_date,
            employment_left_date=employment_left_date,
            continuous_service_date=continuous_service_date,
            date_of_birth=date_of_birth,
            last_working_date=last_working_date,
            gender=gender,
            ethnicity=ethnicity,
            nationality=nationality,
            religion=religion,
            leaver_reason=leaver_reason,
            marital_status=marital_status,
            phones=phones,
            emails=emails,
            addresses=addresses,
            gender_identity=gender_identity,
            windows_username=windows_username,
        )
        if validate:
            return RootModel[str](raw_response.body).root
        return raw_response.body


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        display_id: typing.Optional[typing.Optional[str]] = None,
        title_honorific: typing.Optional[typing.Optional[str]] = None,
        first_name: typing.Optional[typing.Optional[str]] = None,
        known_as: typing.Optional[typing.Optional[str]] = None,
        other_name: typing.Optional[typing.Optional[str]] = None,
        last_name: typing.Optional[typing.Optional[str]] = None,
        cost_centre: typing.Optional[typing.Optional[str]] = None,
        working_status: typing.Optional[typing.Optional[str]] = None,
        is_manager: typing.Optional[typing.Optional[bool]] = None,
        national_insurance_number: typing.Optional[typing.Optional[str]] = None,
        payroll_id: typing.Optional[typing.Optional[str]] = None,
        tax_code: typing.Optional[typing.Optional[str]] = None,
        include_in_payroll: typing.Optional[typing.Optional[bool]] = None,
        employment_start_date: typing.Optional[typing.Optional[datetime]] = None,
        employment_left_date: typing.Optional[typing.Optional[datetime]] = None,
        continuous_service_date: typing.Optional[typing.Optional[datetime]] = None,
        date_of_birth: typing.Optional[typing.Optional[datetime]] = None,
        last_working_date: typing.Optional[typing.Optional[datetime]] = None,
        gender: typing.Optional[typing.Optional[str]] = None,
        ethnicity: typing.Optional[typing.Optional[str]] = None,
        nationality: typing.Optional[typing.Optional[str]] = None,
        religion: typing.Optional[typing.Optional[str]] = None,
        leaver_reason: typing.Optional[typing.Optional[str]] = None,
        marital_status: typing.Optional[typing.Optional[str]] = None,
        phones: typing.Optional[typing.Optional[typing.List[Phone]]] = None,
        emails: typing.Optional[typing.Optional[typing.List[Email]]] = None,
        addresses: typing.Optional[typing.Optional[typing.List[Address]]] = None,
        gender_identity: typing.Optional[typing.Optional[str]] = None,
        windows_username: typing.Optional[typing.Optional[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_employee_mapped_args(
            display_id=display_id,
            title_honorific=title_honorific,
            first_name=first_name,
            known_as=known_as,
            other_name=other_name,
            last_name=last_name,
            cost_centre=cost_centre,
            working_status=working_status,
            is_manager=is_manager,
            national_insurance_number=national_insurance_number,
            payroll_id=payroll_id,
            tax_code=tax_code,
            include_in_payroll=include_in_payroll,
            employment_start_date=employment_start_date,
            employment_left_date=employment_left_date,
            continuous_service_date=continuous_service_date,
            date_of_birth=date_of_birth,
            last_working_date=last_working_date,
            gender=gender,
            ethnicity=ethnicity,
            nationality=nationality,
            religion=religion,
            leaver_reason=leaver_reason,
            marital_status=marital_status,
            phones=phones,
            emails=emails,
            addresses=addresses,
            gender_identity=gender_identity,
            windows_username=windows_username,
        )
        return await self._acreate_new_employee_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        display_id: typing.Optional[typing.Optional[str]] = None,
        title_honorific: typing.Optional[typing.Optional[str]] = None,
        first_name: typing.Optional[typing.Optional[str]] = None,
        known_as: typing.Optional[typing.Optional[str]] = None,
        other_name: typing.Optional[typing.Optional[str]] = None,
        last_name: typing.Optional[typing.Optional[str]] = None,
        cost_centre: typing.Optional[typing.Optional[str]] = None,
        working_status: typing.Optional[typing.Optional[str]] = None,
        is_manager: typing.Optional[typing.Optional[bool]] = None,
        national_insurance_number: typing.Optional[typing.Optional[str]] = None,
        payroll_id: typing.Optional[typing.Optional[str]] = None,
        tax_code: typing.Optional[typing.Optional[str]] = None,
        include_in_payroll: typing.Optional[typing.Optional[bool]] = None,
        employment_start_date: typing.Optional[typing.Optional[datetime]] = None,
        employment_left_date: typing.Optional[typing.Optional[datetime]] = None,
        continuous_service_date: typing.Optional[typing.Optional[datetime]] = None,
        date_of_birth: typing.Optional[typing.Optional[datetime]] = None,
        last_working_date: typing.Optional[typing.Optional[datetime]] = None,
        gender: typing.Optional[typing.Optional[str]] = None,
        ethnicity: typing.Optional[typing.Optional[str]] = None,
        nationality: typing.Optional[typing.Optional[str]] = None,
        religion: typing.Optional[typing.Optional[str]] = None,
        leaver_reason: typing.Optional[typing.Optional[str]] = None,
        marital_status: typing.Optional[typing.Optional[str]] = None,
        phones: typing.Optional[typing.Optional[typing.List[Phone]]] = None,
        emails: typing.Optional[typing.Optional[typing.List[Email]]] = None,
        addresses: typing.Optional[typing.Optional[typing.List[Address]]] = None,
        gender_identity: typing.Optional[typing.Optional[str]] = None,
        windows_username: typing.Optional[typing.Optional[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_employee_mapped_args(
            display_id=display_id,
            title_honorific=title_honorific,
            first_name=first_name,
            known_as=known_as,
            other_name=other_name,
            last_name=last_name,
            cost_centre=cost_centre,
            working_status=working_status,
            is_manager=is_manager,
            national_insurance_number=national_insurance_number,
            payroll_id=payroll_id,
            tax_code=tax_code,
            include_in_payroll=include_in_payroll,
            employment_start_date=employment_start_date,
            employment_left_date=employment_left_date,
            continuous_service_date=continuous_service_date,
            date_of_birth=date_of_birth,
            last_working_date=last_working_date,
            gender=gender,
            ethnicity=ethnicity,
            nationality=nationality,
            religion=religion,
            leaver_reason=leaver_reason,
            marital_status=marital_status,
            phones=phones,
            emails=emails,
            addresses=addresses,
            gender_identity=gender_identity,
            windows_username=windows_username,
        )
        return self._create_new_employee_oapg(
            body=args.body,
        )

