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

from iris_software_group_cascade_python_sdk.model.create_job_command import CreateJobCommand as CreateJobCommandSchema

from iris_software_group_cascade_python_sdk.type.create_job_command import CreateJobCommand

from ...api_client import Dictionary
from iris_software_group_cascade_python_sdk.pydantic.create_job_command import CreateJobCommand as CreateJobCommandPydantic

# body param
SchemaForRequestBodyApplicationJsonodataMetadataminimalodataStreamingtrueVersion2 = CreateJobCommandSchema
SchemaForRequestBodyApplicationJsonodataMetadataminimalodataStreamingfalseVersion2 = CreateJobCommandSchema
SchemaForRequestBodyApplicationJsonodataMetadataminimalVersion2 = CreateJobCommandSchema
SchemaForRequestBodyApplicationJsonodataMetadatafullodataStreamingtrueVersion2 = CreateJobCommandSchema
SchemaForRequestBodyApplicationJsonodataMetadatafullodataStreamingfalseVersion2 = CreateJobCommandSchema
SchemaForRequestBodyApplicationJsonodataMetadatafullVersion2 = CreateJobCommandSchema
SchemaForRequestBodyApplicationJsonodataMetadatanoneodataStreamingtrueVersion2 = CreateJobCommandSchema
SchemaForRequestBodyApplicationJsonodataMetadatanoneodataStreamingfalseVersion2 = CreateJobCommandSchema
SchemaForRequestBodyApplicationJsonodataMetadatanoneVersion2 = CreateJobCommandSchema
SchemaForRequestBodyApplicationJsonodataStreamingtrueVersion2 = CreateJobCommandSchema
SchemaForRequestBodyApplicationJsonodataStreamingfalseVersion2 = CreateJobCommandSchema
SchemaForRequestBodyApplicationJsonVersion2 = CreateJobCommandSchema
SchemaForRequestBodyApplicationXmlVersion2 = CreateJobCommandSchema
SchemaForRequestBodyApplicationPrsOdatatestxxOdataVersion2 = CreateJobCommandSchema
SchemaForRequestBodyTextJsonVersion2 = CreateJobCommandSchema
SchemaForRequestBodyApplicationJsonVersion2 = CreateJobCommandSchema


request_body_create_job_command = api_client.RequestBody(
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

    def _create_new_job_mapped_args(
        self,
        job_title: typing.Optional[typing.Optional[str]] = None,
        classification: typing.Optional[typing.Optional[str]] = None,
        start_date: typing.Optional[datetime] = None,
        end_date: typing.Optional[typing.Optional[datetime]] = None,
        working_calendar: typing.Optional[typing.Optional[str]] = None,
        line_manager_id: typing.Optional[typing.Optional[str]] = None,
        hierarchy_node_id: typing.Optional[typing.Optional[str]] = None,
        active: typing.Optional[bool] = None,
        salary: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        employee_id: typing.Optional[typing.Optional[str]] = None,
        contract: typing.Optional[typing.Optional[str]] = None,
        pay_frequency: typing.Optional[typing.Optional[str]] = None,
        pay_basis: typing.Optional[typing.Optional[str]] = None,
        full_time_equivalent: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        change_reason: typing.Optional[typing.Optional[str]] = None,
        next_increment_date: typing.Optional[typing.Optional[datetime]] = None,
        timesheet_location: typing.Optional[typing.Optional[str]] = None,
        timesheet_lunch_duration: typing.Optional[typing.Optional[str]] = None,
        expense_submission_frequency: typing.Optional[typing.Optional[str]] = None,
        cost_centre: typing.Optional[typing.Optional[str]] = None,
        job_family: typing.Optional[typing.Optional[str]] = None,
        apprentice_under25: typing.Optional[typing.Optional[bool]] = None,
        apprenticeship_end_date: typing.Optional[typing.Optional[datetime]] = None,
        contract_end_date: typing.Optional[typing.Optional[datetime]] = None,
        normal_hours: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        real_time_information_irregular_frequency: typing.Optional[typing.Optional[str]] = None,
        notice_period: typing.Optional[typing.Optional[str]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if job_title is not None:
            _body["JobTitle"] = job_title
        if classification is not None:
            _body["Classification"] = classification
        if start_date is not None:
            _body["StartDate"] = start_date
        if end_date is not None:
            _body["EndDate"] = end_date
        if working_calendar is not None:
            _body["WorkingCalendar"] = working_calendar
        if line_manager_id is not None:
            _body["LineManagerId"] = line_manager_id
        if hierarchy_node_id is not None:
            _body["HierarchyNodeId"] = hierarchy_node_id
        if active is not None:
            _body["Active"] = active
        if salary is not None:
            _body["Salary"] = salary
        if employee_id is not None:
            _body["EmployeeId"] = employee_id
        if contract is not None:
            _body["Contract"] = contract
        if pay_frequency is not None:
            _body["PayFrequency"] = pay_frequency
        if pay_basis is not None:
            _body["PayBasis"] = pay_basis
        if full_time_equivalent is not None:
            _body["FullTimeEquivalent"] = full_time_equivalent
        if change_reason is not None:
            _body["ChangeReason"] = change_reason
        if next_increment_date is not None:
            _body["NextIncrementDate"] = next_increment_date
        if timesheet_location is not None:
            _body["TimesheetLocation"] = timesheet_location
        if timesheet_lunch_duration is not None:
            _body["TimesheetLunchDuration"] = timesheet_lunch_duration
        if expense_submission_frequency is not None:
            _body["ExpenseSubmissionFrequency"] = expense_submission_frequency
        if cost_centre is not None:
            _body["CostCentre"] = cost_centre
        if job_family is not None:
            _body["JobFamily"] = job_family
        if apprentice_under25 is not None:
            _body["ApprenticeUnder25"] = apprentice_under25
        if apprenticeship_end_date is not None:
            _body["ApprenticeshipEndDate"] = apprenticeship_end_date
        if contract_end_date is not None:
            _body["ContractEndDate"] = contract_end_date
        if normal_hours is not None:
            _body["NormalHours"] = normal_hours
        if real_time_information_irregular_frequency is not None:
            _body["RealTimeInformationIrregularFrequency"] = real_time_information_irregular_frequency
        if notice_period is not None:
            _body["NoticePeriod"] = notice_period
        args.body = _body
        return args

    async def _acreate_new_job_oapg(
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
        Creates a new Job.
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
            path_template='/jobs',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_create_job_command.serialize(body, content_type)
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


    def _create_new_job_oapg(
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
        Creates a new Job.
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
            path_template='/jobs',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_create_job_command.serialize(body, content_type)
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


class CreateNewJobRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_new_job(
        self,
        job_title: typing.Optional[typing.Optional[str]] = None,
        classification: typing.Optional[typing.Optional[str]] = None,
        start_date: typing.Optional[datetime] = None,
        end_date: typing.Optional[typing.Optional[datetime]] = None,
        working_calendar: typing.Optional[typing.Optional[str]] = None,
        line_manager_id: typing.Optional[typing.Optional[str]] = None,
        hierarchy_node_id: typing.Optional[typing.Optional[str]] = None,
        active: typing.Optional[bool] = None,
        salary: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        employee_id: typing.Optional[typing.Optional[str]] = None,
        contract: typing.Optional[typing.Optional[str]] = None,
        pay_frequency: typing.Optional[typing.Optional[str]] = None,
        pay_basis: typing.Optional[typing.Optional[str]] = None,
        full_time_equivalent: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        change_reason: typing.Optional[typing.Optional[str]] = None,
        next_increment_date: typing.Optional[typing.Optional[datetime]] = None,
        timesheet_location: typing.Optional[typing.Optional[str]] = None,
        timesheet_lunch_duration: typing.Optional[typing.Optional[str]] = None,
        expense_submission_frequency: typing.Optional[typing.Optional[str]] = None,
        cost_centre: typing.Optional[typing.Optional[str]] = None,
        job_family: typing.Optional[typing.Optional[str]] = None,
        apprentice_under25: typing.Optional[typing.Optional[bool]] = None,
        apprenticeship_end_date: typing.Optional[typing.Optional[datetime]] = None,
        contract_end_date: typing.Optional[typing.Optional[datetime]] = None,
        normal_hours: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        real_time_information_irregular_frequency: typing.Optional[typing.Optional[str]] = None,
        notice_period: typing.Optional[typing.Optional[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_job_mapped_args(
            job_title=job_title,
            classification=classification,
            start_date=start_date,
            end_date=end_date,
            working_calendar=working_calendar,
            line_manager_id=line_manager_id,
            hierarchy_node_id=hierarchy_node_id,
            active=active,
            salary=salary,
            employee_id=employee_id,
            contract=contract,
            pay_frequency=pay_frequency,
            pay_basis=pay_basis,
            full_time_equivalent=full_time_equivalent,
            change_reason=change_reason,
            next_increment_date=next_increment_date,
            timesheet_location=timesheet_location,
            timesheet_lunch_duration=timesheet_lunch_duration,
            expense_submission_frequency=expense_submission_frequency,
            cost_centre=cost_centre,
            job_family=job_family,
            apprentice_under25=apprentice_under25,
            apprenticeship_end_date=apprenticeship_end_date,
            contract_end_date=contract_end_date,
            normal_hours=normal_hours,
            real_time_information_irregular_frequency=real_time_information_irregular_frequency,
            notice_period=notice_period,
        )
        return await self._acreate_new_job_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_new_job(
        self,
        job_title: typing.Optional[typing.Optional[str]] = None,
        classification: typing.Optional[typing.Optional[str]] = None,
        start_date: typing.Optional[datetime] = None,
        end_date: typing.Optional[typing.Optional[datetime]] = None,
        working_calendar: typing.Optional[typing.Optional[str]] = None,
        line_manager_id: typing.Optional[typing.Optional[str]] = None,
        hierarchy_node_id: typing.Optional[typing.Optional[str]] = None,
        active: typing.Optional[bool] = None,
        salary: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        employee_id: typing.Optional[typing.Optional[str]] = None,
        contract: typing.Optional[typing.Optional[str]] = None,
        pay_frequency: typing.Optional[typing.Optional[str]] = None,
        pay_basis: typing.Optional[typing.Optional[str]] = None,
        full_time_equivalent: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        change_reason: typing.Optional[typing.Optional[str]] = None,
        next_increment_date: typing.Optional[typing.Optional[datetime]] = None,
        timesheet_location: typing.Optional[typing.Optional[str]] = None,
        timesheet_lunch_duration: typing.Optional[typing.Optional[str]] = None,
        expense_submission_frequency: typing.Optional[typing.Optional[str]] = None,
        cost_centre: typing.Optional[typing.Optional[str]] = None,
        job_family: typing.Optional[typing.Optional[str]] = None,
        apprentice_under25: typing.Optional[typing.Optional[bool]] = None,
        apprenticeship_end_date: typing.Optional[typing.Optional[datetime]] = None,
        contract_end_date: typing.Optional[typing.Optional[datetime]] = None,
        normal_hours: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        real_time_information_irregular_frequency: typing.Optional[typing.Optional[str]] = None,
        notice_period: typing.Optional[typing.Optional[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_job_mapped_args(
            job_title=job_title,
            classification=classification,
            start_date=start_date,
            end_date=end_date,
            working_calendar=working_calendar,
            line_manager_id=line_manager_id,
            hierarchy_node_id=hierarchy_node_id,
            active=active,
            salary=salary,
            employee_id=employee_id,
            contract=contract,
            pay_frequency=pay_frequency,
            pay_basis=pay_basis,
            full_time_equivalent=full_time_equivalent,
            change_reason=change_reason,
            next_increment_date=next_increment_date,
            timesheet_location=timesheet_location,
            timesheet_lunch_duration=timesheet_lunch_duration,
            expense_submission_frequency=expense_submission_frequency,
            cost_centre=cost_centre,
            job_family=job_family,
            apprentice_under25=apprentice_under25,
            apprenticeship_end_date=apprenticeship_end_date,
            contract_end_date=contract_end_date,
            normal_hours=normal_hours,
            real_time_information_irregular_frequency=real_time_information_irregular_frequency,
            notice_period=notice_period,
        )
        return self._create_new_job_oapg(
            body=args.body,
        )

class CreateNewJob(BaseApi):

    async def acreate_new_job(
        self,
        job_title: typing.Optional[typing.Optional[str]] = None,
        classification: typing.Optional[typing.Optional[str]] = None,
        start_date: typing.Optional[datetime] = None,
        end_date: typing.Optional[typing.Optional[datetime]] = None,
        working_calendar: typing.Optional[typing.Optional[str]] = None,
        line_manager_id: typing.Optional[typing.Optional[str]] = None,
        hierarchy_node_id: typing.Optional[typing.Optional[str]] = None,
        active: typing.Optional[bool] = None,
        salary: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        employee_id: typing.Optional[typing.Optional[str]] = None,
        contract: typing.Optional[typing.Optional[str]] = None,
        pay_frequency: typing.Optional[typing.Optional[str]] = None,
        pay_basis: typing.Optional[typing.Optional[str]] = None,
        full_time_equivalent: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        change_reason: typing.Optional[typing.Optional[str]] = None,
        next_increment_date: typing.Optional[typing.Optional[datetime]] = None,
        timesheet_location: typing.Optional[typing.Optional[str]] = None,
        timesheet_lunch_duration: typing.Optional[typing.Optional[str]] = None,
        expense_submission_frequency: typing.Optional[typing.Optional[str]] = None,
        cost_centre: typing.Optional[typing.Optional[str]] = None,
        job_family: typing.Optional[typing.Optional[str]] = None,
        apprentice_under25: typing.Optional[typing.Optional[bool]] = None,
        apprenticeship_end_date: typing.Optional[typing.Optional[datetime]] = None,
        contract_end_date: typing.Optional[typing.Optional[datetime]] = None,
        normal_hours: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        real_time_information_irregular_frequency: typing.Optional[typing.Optional[str]] = None,
        notice_period: typing.Optional[typing.Optional[str]] = None,
        validate: bool = False,
        **kwargs,
    ) -> str:
        raw_response = await self.raw.acreate_new_job(
            job_title=job_title,
            classification=classification,
            start_date=start_date,
            end_date=end_date,
            working_calendar=working_calendar,
            line_manager_id=line_manager_id,
            hierarchy_node_id=hierarchy_node_id,
            active=active,
            salary=salary,
            employee_id=employee_id,
            contract=contract,
            pay_frequency=pay_frequency,
            pay_basis=pay_basis,
            full_time_equivalent=full_time_equivalent,
            change_reason=change_reason,
            next_increment_date=next_increment_date,
            timesheet_location=timesheet_location,
            timesheet_lunch_duration=timesheet_lunch_duration,
            expense_submission_frequency=expense_submission_frequency,
            cost_centre=cost_centre,
            job_family=job_family,
            apprentice_under25=apprentice_under25,
            apprenticeship_end_date=apprenticeship_end_date,
            contract_end_date=contract_end_date,
            normal_hours=normal_hours,
            real_time_information_irregular_frequency=real_time_information_irregular_frequency,
            notice_period=notice_period,
            **kwargs,
        )
        if validate:
            return RootModel[str](raw_response.body).root
        return raw_response.body
    
    
    def create_new_job(
        self,
        job_title: typing.Optional[typing.Optional[str]] = None,
        classification: typing.Optional[typing.Optional[str]] = None,
        start_date: typing.Optional[datetime] = None,
        end_date: typing.Optional[typing.Optional[datetime]] = None,
        working_calendar: typing.Optional[typing.Optional[str]] = None,
        line_manager_id: typing.Optional[typing.Optional[str]] = None,
        hierarchy_node_id: typing.Optional[typing.Optional[str]] = None,
        active: typing.Optional[bool] = None,
        salary: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        employee_id: typing.Optional[typing.Optional[str]] = None,
        contract: typing.Optional[typing.Optional[str]] = None,
        pay_frequency: typing.Optional[typing.Optional[str]] = None,
        pay_basis: typing.Optional[typing.Optional[str]] = None,
        full_time_equivalent: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        change_reason: typing.Optional[typing.Optional[str]] = None,
        next_increment_date: typing.Optional[typing.Optional[datetime]] = None,
        timesheet_location: typing.Optional[typing.Optional[str]] = None,
        timesheet_lunch_duration: typing.Optional[typing.Optional[str]] = None,
        expense_submission_frequency: typing.Optional[typing.Optional[str]] = None,
        cost_centre: typing.Optional[typing.Optional[str]] = None,
        job_family: typing.Optional[typing.Optional[str]] = None,
        apprentice_under25: typing.Optional[typing.Optional[bool]] = None,
        apprenticeship_end_date: typing.Optional[typing.Optional[datetime]] = None,
        contract_end_date: typing.Optional[typing.Optional[datetime]] = None,
        normal_hours: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        real_time_information_irregular_frequency: typing.Optional[typing.Optional[str]] = None,
        notice_period: typing.Optional[typing.Optional[str]] = None,
        validate: bool = False,
    ) -> str:
        raw_response = self.raw.create_new_job(
            job_title=job_title,
            classification=classification,
            start_date=start_date,
            end_date=end_date,
            working_calendar=working_calendar,
            line_manager_id=line_manager_id,
            hierarchy_node_id=hierarchy_node_id,
            active=active,
            salary=salary,
            employee_id=employee_id,
            contract=contract,
            pay_frequency=pay_frequency,
            pay_basis=pay_basis,
            full_time_equivalent=full_time_equivalent,
            change_reason=change_reason,
            next_increment_date=next_increment_date,
            timesheet_location=timesheet_location,
            timesheet_lunch_duration=timesheet_lunch_duration,
            expense_submission_frequency=expense_submission_frequency,
            cost_centre=cost_centre,
            job_family=job_family,
            apprentice_under25=apprentice_under25,
            apprenticeship_end_date=apprenticeship_end_date,
            contract_end_date=contract_end_date,
            normal_hours=normal_hours,
            real_time_information_irregular_frequency=real_time_information_irregular_frequency,
            notice_period=notice_period,
        )
        if validate:
            return RootModel[str](raw_response.body).root
        return raw_response.body


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        job_title: typing.Optional[typing.Optional[str]] = None,
        classification: typing.Optional[typing.Optional[str]] = None,
        start_date: typing.Optional[datetime] = None,
        end_date: typing.Optional[typing.Optional[datetime]] = None,
        working_calendar: typing.Optional[typing.Optional[str]] = None,
        line_manager_id: typing.Optional[typing.Optional[str]] = None,
        hierarchy_node_id: typing.Optional[typing.Optional[str]] = None,
        active: typing.Optional[bool] = None,
        salary: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        employee_id: typing.Optional[typing.Optional[str]] = None,
        contract: typing.Optional[typing.Optional[str]] = None,
        pay_frequency: typing.Optional[typing.Optional[str]] = None,
        pay_basis: typing.Optional[typing.Optional[str]] = None,
        full_time_equivalent: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        change_reason: typing.Optional[typing.Optional[str]] = None,
        next_increment_date: typing.Optional[typing.Optional[datetime]] = None,
        timesheet_location: typing.Optional[typing.Optional[str]] = None,
        timesheet_lunch_duration: typing.Optional[typing.Optional[str]] = None,
        expense_submission_frequency: typing.Optional[typing.Optional[str]] = None,
        cost_centre: typing.Optional[typing.Optional[str]] = None,
        job_family: typing.Optional[typing.Optional[str]] = None,
        apprentice_under25: typing.Optional[typing.Optional[bool]] = None,
        apprenticeship_end_date: typing.Optional[typing.Optional[datetime]] = None,
        contract_end_date: typing.Optional[typing.Optional[datetime]] = None,
        normal_hours: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        real_time_information_irregular_frequency: typing.Optional[typing.Optional[str]] = None,
        notice_period: typing.Optional[typing.Optional[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_job_mapped_args(
            job_title=job_title,
            classification=classification,
            start_date=start_date,
            end_date=end_date,
            working_calendar=working_calendar,
            line_manager_id=line_manager_id,
            hierarchy_node_id=hierarchy_node_id,
            active=active,
            salary=salary,
            employee_id=employee_id,
            contract=contract,
            pay_frequency=pay_frequency,
            pay_basis=pay_basis,
            full_time_equivalent=full_time_equivalent,
            change_reason=change_reason,
            next_increment_date=next_increment_date,
            timesheet_location=timesheet_location,
            timesheet_lunch_duration=timesheet_lunch_duration,
            expense_submission_frequency=expense_submission_frequency,
            cost_centre=cost_centre,
            job_family=job_family,
            apprentice_under25=apprentice_under25,
            apprenticeship_end_date=apprenticeship_end_date,
            contract_end_date=contract_end_date,
            normal_hours=normal_hours,
            real_time_information_irregular_frequency=real_time_information_irregular_frequency,
            notice_period=notice_period,
        )
        return await self._acreate_new_job_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        job_title: typing.Optional[typing.Optional[str]] = None,
        classification: typing.Optional[typing.Optional[str]] = None,
        start_date: typing.Optional[datetime] = None,
        end_date: typing.Optional[typing.Optional[datetime]] = None,
        working_calendar: typing.Optional[typing.Optional[str]] = None,
        line_manager_id: typing.Optional[typing.Optional[str]] = None,
        hierarchy_node_id: typing.Optional[typing.Optional[str]] = None,
        active: typing.Optional[bool] = None,
        salary: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        employee_id: typing.Optional[typing.Optional[str]] = None,
        contract: typing.Optional[typing.Optional[str]] = None,
        pay_frequency: typing.Optional[typing.Optional[str]] = None,
        pay_basis: typing.Optional[typing.Optional[str]] = None,
        full_time_equivalent: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        change_reason: typing.Optional[typing.Optional[str]] = None,
        next_increment_date: typing.Optional[typing.Optional[datetime]] = None,
        timesheet_location: typing.Optional[typing.Optional[str]] = None,
        timesheet_lunch_duration: typing.Optional[typing.Optional[str]] = None,
        expense_submission_frequency: typing.Optional[typing.Optional[str]] = None,
        cost_centre: typing.Optional[typing.Optional[str]] = None,
        job_family: typing.Optional[typing.Optional[str]] = None,
        apprentice_under25: typing.Optional[typing.Optional[bool]] = None,
        apprenticeship_end_date: typing.Optional[typing.Optional[datetime]] = None,
        contract_end_date: typing.Optional[typing.Optional[datetime]] = None,
        normal_hours: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        real_time_information_irregular_frequency: typing.Optional[typing.Optional[str]] = None,
        notice_period: typing.Optional[typing.Optional[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_job_mapped_args(
            job_title=job_title,
            classification=classification,
            start_date=start_date,
            end_date=end_date,
            working_calendar=working_calendar,
            line_manager_id=line_manager_id,
            hierarchy_node_id=hierarchy_node_id,
            active=active,
            salary=salary,
            employee_id=employee_id,
            contract=contract,
            pay_frequency=pay_frequency,
            pay_basis=pay_basis,
            full_time_equivalent=full_time_equivalent,
            change_reason=change_reason,
            next_increment_date=next_increment_date,
            timesheet_location=timesheet_location,
            timesheet_lunch_duration=timesheet_lunch_duration,
            expense_submission_frequency=expense_submission_frequency,
            cost_centre=cost_centre,
            job_family=job_family,
            apprentice_under25=apprentice_under25,
            apprenticeship_end_date=apprenticeship_end_date,
            contract_end_date=contract_end_date,
            normal_hours=normal_hours,
            real_time_information_irregular_frequency=real_time_information_irregular_frequency,
            notice_period=notice_period,
        )
        return self._create_new_job_oapg(
            body=args.body,
        )

