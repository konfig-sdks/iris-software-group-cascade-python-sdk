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

from iris_software_group_cascade_python_sdk.model.update_job_command import UpdateJobCommand as UpdateJobCommandSchema

from iris_software_group_cascade_python_sdk.type.update_job_command import UpdateJobCommand

from ...api_client import Dictionary
from iris_software_group_cascade_python_sdk.pydantic.update_job_command import UpdateJobCommand as UpdateJobCommandPydantic

from . import path

# Path params
IdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'id': typing.Union[IdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_id = api_client.PathParameter(
    name="id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJsonodataMetadataminimalodataStreamingtrueVersion2 = UpdateJobCommandSchema
SchemaForRequestBodyApplicationJsonodataMetadataminimalodataStreamingfalseVersion2 = UpdateJobCommandSchema
SchemaForRequestBodyApplicationJsonodataMetadataminimalVersion2 = UpdateJobCommandSchema
SchemaForRequestBodyApplicationJsonodataMetadatafullodataStreamingtrueVersion2 = UpdateJobCommandSchema
SchemaForRequestBodyApplicationJsonodataMetadatafullodataStreamingfalseVersion2 = UpdateJobCommandSchema
SchemaForRequestBodyApplicationJsonodataMetadatafullVersion2 = UpdateJobCommandSchema
SchemaForRequestBodyApplicationJsonodataMetadatanoneodataStreamingtrueVersion2 = UpdateJobCommandSchema
SchemaForRequestBodyApplicationJsonodataMetadatanoneodataStreamingfalseVersion2 = UpdateJobCommandSchema
SchemaForRequestBodyApplicationJsonodataMetadatanoneVersion2 = UpdateJobCommandSchema
SchemaForRequestBodyApplicationJsonodataStreamingtrueVersion2 = UpdateJobCommandSchema
SchemaForRequestBodyApplicationJsonodataStreamingfalseVersion2 = UpdateJobCommandSchema
SchemaForRequestBodyApplicationJsonVersion2 = UpdateJobCommandSchema
SchemaForRequestBodyApplicationXmlVersion2 = UpdateJobCommandSchema
SchemaForRequestBodyApplicationPrsOdatatestxxOdataVersion2 = UpdateJobCommandSchema
SchemaForRequestBodyTextJsonVersion2 = UpdateJobCommandSchema
SchemaForRequestBodyApplicationJsonVersion2 = UpdateJobCommandSchema


request_body_update_job_command = api_client.RequestBody(
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


@dataclass
class ApiResponseFor204(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor204Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_204 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor204,
    response_cls_async=ApiResponseFor204Async,
)
_status_code_to_response = {
    '204': _response_for_204,
}


class BaseApi(api_client.Api):

    def _update_by_id_mapped_args(
        self,
        id: str,
        job_title: typing.Optional[typing.Optional[str]] = None,
        classification: typing.Optional[typing.Optional[str]] = None,
        start_date: typing.Optional[datetime] = None,
        end_date: typing.Optional[typing.Optional[datetime]] = None,
        working_calendar: typing.Optional[typing.Optional[str]] = None,
        line_manager_id: typing.Optional[typing.Optional[str]] = None,
        hierarchy_node_id: typing.Optional[typing.Optional[str]] = None,
        active: typing.Optional[bool] = None,
        salary: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
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
        id: typing.Optional[typing.Optional[str]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
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
        if id is not None:
            _body["Id"] = id
        args.body = _body
        if id is not None:
            _path_params["id"] = id
        args.path = _path_params
        return args

    async def _aupdate_by_id_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        content_type: str = 'application/json;odata.metadata=minimal;odata.streaming=true; version=2',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Update a Job referenced by an ID.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/jobs/{id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_update_job_command.serialize(body, content_type)
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


    def _update_by_id_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        content_type: str = 'application/json;odata.metadata=minimal;odata.streaming=true; version=2',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Update a Job referenced by an ID.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/jobs/{id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_update_job_command.serialize(body, content_type)
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


class UpdateByIdRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_by_id(
        self,
        id: str,
        job_title: typing.Optional[typing.Optional[str]] = None,
        classification: typing.Optional[typing.Optional[str]] = None,
        start_date: typing.Optional[datetime] = None,
        end_date: typing.Optional[typing.Optional[datetime]] = None,
        working_calendar: typing.Optional[typing.Optional[str]] = None,
        line_manager_id: typing.Optional[typing.Optional[str]] = None,
        hierarchy_node_id: typing.Optional[typing.Optional[str]] = None,
        active: typing.Optional[bool] = None,
        salary: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
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
        id: typing.Optional[typing.Optional[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_by_id_mapped_args(
            id=id,
            job_title=job_title,
            classification=classification,
            start_date=start_date,
            end_date=end_date,
            working_calendar=working_calendar,
            line_manager_id=line_manager_id,
            hierarchy_node_id=hierarchy_node_id,
            active=active,
            salary=salary,
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
            id=id,
        )
        return await self._aupdate_by_id_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update_by_id(
        self,
        id: str,
        job_title: typing.Optional[typing.Optional[str]] = None,
        classification: typing.Optional[typing.Optional[str]] = None,
        start_date: typing.Optional[datetime] = None,
        end_date: typing.Optional[typing.Optional[datetime]] = None,
        working_calendar: typing.Optional[typing.Optional[str]] = None,
        line_manager_id: typing.Optional[typing.Optional[str]] = None,
        hierarchy_node_id: typing.Optional[typing.Optional[str]] = None,
        active: typing.Optional[bool] = None,
        salary: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
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
        id: typing.Optional[typing.Optional[str]] = None,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_by_id_mapped_args(
            id=id,
            job_title=job_title,
            classification=classification,
            start_date=start_date,
            end_date=end_date,
            working_calendar=working_calendar,
            line_manager_id=line_manager_id,
            hierarchy_node_id=hierarchy_node_id,
            active=active,
            salary=salary,
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
            id=id,
        )
        return self._update_by_id_oapg(
            body=args.body,
            path_params=args.path,
        )

class UpdateById(BaseApi):

    async def aupdate_by_id(
        self,
        id: str,
        job_title: typing.Optional[typing.Optional[str]] = None,
        classification: typing.Optional[typing.Optional[str]] = None,
        start_date: typing.Optional[datetime] = None,
        end_date: typing.Optional[typing.Optional[datetime]] = None,
        working_calendar: typing.Optional[typing.Optional[str]] = None,
        line_manager_id: typing.Optional[typing.Optional[str]] = None,
        hierarchy_node_id: typing.Optional[typing.Optional[str]] = None,
        active: typing.Optional[bool] = None,
        salary: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
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
        id: typing.Optional[typing.Optional[str]] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.aupdate_by_id(
            id=id,
            job_title=job_title,
            classification=classification,
            start_date=start_date,
            end_date=end_date,
            working_calendar=working_calendar,
            line_manager_id=line_manager_id,
            hierarchy_node_id=hierarchy_node_id,
            active=active,
            salary=salary,
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
            id=id,
            **kwargs,
        )
    
    
    def update_by_id(
        self,
        id: str,
        job_title: typing.Optional[typing.Optional[str]] = None,
        classification: typing.Optional[typing.Optional[str]] = None,
        start_date: typing.Optional[datetime] = None,
        end_date: typing.Optional[typing.Optional[datetime]] = None,
        working_calendar: typing.Optional[typing.Optional[str]] = None,
        line_manager_id: typing.Optional[typing.Optional[str]] = None,
        hierarchy_node_id: typing.Optional[typing.Optional[str]] = None,
        active: typing.Optional[bool] = None,
        salary: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
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
        id: typing.Optional[typing.Optional[str]] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.update_by_id(
            id=id,
            job_title=job_title,
            classification=classification,
            start_date=start_date,
            end_date=end_date,
            working_calendar=working_calendar,
            line_manager_id=line_manager_id,
            hierarchy_node_id=hierarchy_node_id,
            active=active,
            salary=salary,
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
            id=id,
        )


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        id: str,
        job_title: typing.Optional[typing.Optional[str]] = None,
        classification: typing.Optional[typing.Optional[str]] = None,
        start_date: typing.Optional[datetime] = None,
        end_date: typing.Optional[typing.Optional[datetime]] = None,
        working_calendar: typing.Optional[typing.Optional[str]] = None,
        line_manager_id: typing.Optional[typing.Optional[str]] = None,
        hierarchy_node_id: typing.Optional[typing.Optional[str]] = None,
        active: typing.Optional[bool] = None,
        salary: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
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
        id: typing.Optional[typing.Optional[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_by_id_mapped_args(
            id=id,
            job_title=job_title,
            classification=classification,
            start_date=start_date,
            end_date=end_date,
            working_calendar=working_calendar,
            line_manager_id=line_manager_id,
            hierarchy_node_id=hierarchy_node_id,
            active=active,
            salary=salary,
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
            id=id,
        )
        return await self._aupdate_by_id_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        id: str,
        job_title: typing.Optional[typing.Optional[str]] = None,
        classification: typing.Optional[typing.Optional[str]] = None,
        start_date: typing.Optional[datetime] = None,
        end_date: typing.Optional[typing.Optional[datetime]] = None,
        working_calendar: typing.Optional[typing.Optional[str]] = None,
        line_manager_id: typing.Optional[typing.Optional[str]] = None,
        hierarchy_node_id: typing.Optional[typing.Optional[str]] = None,
        active: typing.Optional[bool] = None,
        salary: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
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
        id: typing.Optional[typing.Optional[str]] = None,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_by_id_mapped_args(
            id=id,
            job_title=job_title,
            classification=classification,
            start_date=start_date,
            end_date=end_date,
            working_calendar=working_calendar,
            line_manager_id=line_manager_id,
            hierarchy_node_id=hierarchy_node_id,
            active=active,
            salary=salary,
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
            id=id,
        )
        return self._update_by_id_oapg(
            body=args.body,
            path_params=args.path,
        )

