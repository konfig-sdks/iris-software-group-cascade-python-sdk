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

from iris_software_group_cascade_python_sdk.model.job_query_model import JobQueryModel as JobQueryModelSchema

from iris_software_group_cascade_python_sdk.type.job_query_model import JobQueryModel

from ...api_client import Dictionary
from iris_software_group_cascade_python_sdk.pydantic.job_query_model import JobQueryModel as JobQueryModelPydantic

# Query params


class TopSchema(
    schemas.IntSchema
):
    pass


class SkipSchema(
    schemas.IntSchema
):
    pass
FilterSchema = schemas.StrSchema


class SelectSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'SelectSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class OrderbySchema(
    schemas.StrSchema
):
    pass
CountSchema = schemas.BoolSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        '$top': typing.Union[TopSchema, decimal.Decimal, int, ],
        '$skip': typing.Union[SkipSchema, decimal.Decimal, int, ],
        '$filter': typing.Union[FilterSchema, str, ],
        '$select': typing.Union[SelectSchema, list, tuple, ],
        '$orderby': typing.Union[OrderbySchema, str, ],
        '$count': typing.Union[CountSchema, bool, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_top = api_client.QueryParameter(
    name="$top",
    style=api_client.ParameterStyle.FORM,
    schema=TopSchema,
    explode=True,
)
request_query_skip = api_client.QueryParameter(
    name="$skip",
    style=api_client.ParameterStyle.FORM,
    schema=SkipSchema,
    explode=True,
)
request_query_filter = api_client.QueryParameter(
    name="$filter",
    style=api_client.ParameterStyle.FORM,
    schema=FilterSchema,
    explode=True,
)
request_query_select = api_client.QueryParameter(
    name="$select",
    style=api_client.ParameterStyle.FORM,
    schema=SelectSchema,
)
request_query_orderby = api_client.QueryParameter(
    name="$orderby",
    style=api_client.ParameterStyle.FORM,
    schema=OrderbySchema,
)
request_query_count = api_client.QueryParameter(
    name="$count",
    style=api_client.ParameterStyle.FORM,
    schema=CountSchema,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJsonodataMetadataminimalodataStreamingtrueVersion2 = JobQueryModelSchema
SchemaFor200ResponseBodyApplicationJsonodataMetadataminimalodataStreamingfalseVersion2 = JobQueryModelSchema
SchemaFor200ResponseBodyApplicationJsonodataMetadataminimalVersion2 = JobQueryModelSchema
SchemaFor200ResponseBodyApplicationJsonodataMetadatafullodataStreamingtrueVersion2 = JobQueryModelSchema
SchemaFor200ResponseBodyApplicationJsonodataMetadatafullodataStreamingfalseVersion2 = JobQueryModelSchema
SchemaFor200ResponseBodyApplicationJsonodataMetadatafullVersion2 = JobQueryModelSchema
SchemaFor200ResponseBodyApplicationJsonodataMetadatanoneodataStreamingtrueVersion2 = JobQueryModelSchema
SchemaFor200ResponseBodyApplicationJsonodataMetadatanoneodataStreamingfalseVersion2 = JobQueryModelSchema
SchemaFor200ResponseBodyApplicationJsonodataMetadatanoneVersion2 = JobQueryModelSchema
SchemaFor200ResponseBodyApplicationJsonodataStreamingtrueVersion2 = JobQueryModelSchema
SchemaFor200ResponseBodyApplicationJsonodataStreamingfalseVersion2 = JobQueryModelSchema
SchemaFor200ResponseBodyApplicationJsonVersion2 = JobQueryModelSchema
SchemaFor200ResponseBodyApplicationXmlVersion2 = JobQueryModelSchema
SchemaFor200ResponseBodyApplicationPrsOdatatestxxOdataVersion2 = JobQueryModelSchema
SchemaFor200ResponseBodyTextPlainVersion2 = JobQueryModelSchema
SchemaFor200ResponseBodyTextJsonVersion2 = JobQueryModelSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: JobQueryModel


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: JobQueryModel


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

    def _get_list_mapped_args(
        self,
        top: typing.Optional[int] = None,
        skip: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        select: typing.Optional[typing.List[str]] = None,
        orderby: typing.Optional[str] = None,
        count: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if top is not None:
            _query_params["$top"] = top
        if skip is not None:
            _query_params["$skip"] = skip
        if filter is not None:
            _query_params["$filter"] = filter
        if select is not None:
            _query_params["$select"] = select
        if orderby is not None:
            _query_params["$orderby"] = orderby
        if count is not None:
            _query_params["$count"] = count
        args.query = _query_params
        return args

    async def _aget_list_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Gets a list of Jobs.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_top,
            request_query_skip,
            request_query_filter,
            request_query_select,
            request_query_orderby,
            request_query_count,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/jobs',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
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


    def _get_list_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Gets a list of Jobs.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_top,
            request_query_skip,
            request_query_filter,
            request_query_select,
            request_query_orderby,
            request_query_count,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/jobs',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
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


class GetListRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_list(
        self,
        top: typing.Optional[int] = None,
        skip: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        select: typing.Optional[typing.List[str]] = None,
        orderby: typing.Optional[str] = None,
        count: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_list_mapped_args(
            top=top,
            skip=skip,
            filter=filter,
            select=select,
            orderby=orderby,
            count=count,
        )
        return await self._aget_list_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get_list(
        self,
        top: typing.Optional[int] = None,
        skip: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        select: typing.Optional[typing.List[str]] = None,
        orderby: typing.Optional[str] = None,
        count: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_list_mapped_args(
            top=top,
            skip=skip,
            filter=filter,
            select=select,
            orderby=orderby,
            count=count,
        )
        return self._get_list_oapg(
            query_params=args.query,
        )

class GetList(BaseApi):

    async def aget_list(
        self,
        top: typing.Optional[int] = None,
        skip: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        select: typing.Optional[typing.List[str]] = None,
        orderby: typing.Optional[str] = None,
        count: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> JobQueryModelPydantic:
        raw_response = await self.raw.aget_list(
            top=top,
            skip=skip,
            filter=filter,
            select=select,
            orderby=orderby,
            count=count,
            **kwargs,
        )
        if validate:
            return JobQueryModelPydantic(**raw_response.body)
        return api_client.construct_model_instance(JobQueryModelPydantic, raw_response.body)
    
    
    def get_list(
        self,
        top: typing.Optional[int] = None,
        skip: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        select: typing.Optional[typing.List[str]] = None,
        orderby: typing.Optional[str] = None,
        count: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> JobQueryModelPydantic:
        raw_response = self.raw.get_list(
            top=top,
            skip=skip,
            filter=filter,
            select=select,
            orderby=orderby,
            count=count,
        )
        if validate:
            return JobQueryModelPydantic(**raw_response.body)
        return api_client.construct_model_instance(JobQueryModelPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        top: typing.Optional[int] = None,
        skip: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        select: typing.Optional[typing.List[str]] = None,
        orderby: typing.Optional[str] = None,
        count: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_list_mapped_args(
            top=top,
            skip=skip,
            filter=filter,
            select=select,
            orderby=orderby,
            count=count,
        )
        return await self._aget_list_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        top: typing.Optional[int] = None,
        skip: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        select: typing.Optional[typing.List[str]] = None,
        orderby: typing.Optional[str] = None,
        count: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_list_mapped_args(
            top=top,
            skip=skip,
            filter=filter,
            select=select,
            orderby=orderby,
            count=count,
        )
        return self._get_list_oapg(
            query_params=args.query,
        )

