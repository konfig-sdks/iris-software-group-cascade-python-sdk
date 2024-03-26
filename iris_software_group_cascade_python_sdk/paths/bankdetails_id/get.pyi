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

from iris_software_group_cascade_python_sdk.model.bank_details_model import BankDetailsModel as BankDetailsModelSchema

from iris_software_group_cascade_python_sdk.type.bank_details_model import BankDetailsModel

from ...api_client import Dictionary
from iris_software_group_cascade_python_sdk.pydantic.bank_details_model import BankDetailsModel as BankDetailsModelPydantic

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
SchemaFor200ResponseBodyApplicationJsonodataMetadataminimalodataStreamingtrueVersion1 = BankDetailsModelSchema
SchemaFor200ResponseBodyApplicationJsonodataMetadataminimalodataStreamingfalseVersion1 = BankDetailsModelSchema
SchemaFor200ResponseBodyApplicationJsonodataMetadataminimalVersion1 = BankDetailsModelSchema
SchemaFor200ResponseBodyApplicationJsonodataMetadatafullodataStreamingtrueVersion1 = BankDetailsModelSchema
SchemaFor200ResponseBodyApplicationJsonodataMetadatafullodataStreamingfalseVersion1 = BankDetailsModelSchema
SchemaFor200ResponseBodyApplicationJsonodataMetadatafullVersion1 = BankDetailsModelSchema
SchemaFor200ResponseBodyApplicationJsonodataMetadatanoneodataStreamingtrueVersion1 = BankDetailsModelSchema
SchemaFor200ResponseBodyApplicationJsonodataMetadatanoneodataStreamingfalseVersion1 = BankDetailsModelSchema
SchemaFor200ResponseBodyApplicationJsonodataMetadatanoneVersion1 = BankDetailsModelSchema
SchemaFor200ResponseBodyApplicationJsonodataStreamingtrueVersion1 = BankDetailsModelSchema
SchemaFor200ResponseBodyApplicationJsonodataStreamingfalseVersion1 = BankDetailsModelSchema
SchemaFor200ResponseBodyApplicationJsonVersion1 = BankDetailsModelSchema
SchemaFor200ResponseBodyApplicationXmlVersion1 = BankDetailsModelSchema
SchemaFor200ResponseBodyApplicationPrsOdatatestxxOdataVersion1 = BankDetailsModelSchema
SchemaFor200ResponseBodyTextPlainVersion1 = BankDetailsModelSchema
SchemaFor200ResponseBodyTextJsonVersion1 = BankDetailsModelSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: BankDetailsModel


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: BankDetailsModel


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json;odata.metadata=minimal;odata.streaming=true; version=1': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJsonodataMetadataminimalodataStreamingtrueVersion1),
        'application/json;odata.metadata=minimal;odata.streaming=false; version=1': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJsonodataMetadataminimalodataStreamingfalseVersion1),
        'application/json;odata.metadata=minimal; version=1': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJsonodataMetadataminimalVersion1),
        'application/json;odata.metadata=full;odata.streaming=true; version=1': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJsonodataMetadatafullodataStreamingtrueVersion1),
        'application/json;odata.metadata=full;odata.streaming=false; version=1': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJsonodataMetadatafullodataStreamingfalseVersion1),
        'application/json;odata.metadata=full; version=1': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJsonodataMetadatafullVersion1),
        'application/json;odata.metadata=none;odata.streaming=true; version=1': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJsonodataMetadatanoneodataStreamingtrueVersion1),
        'application/json;odata.metadata=none;odata.streaming=false; version=1': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJsonodataMetadatanoneodataStreamingfalseVersion1),
        'application/json;odata.metadata=none; version=1': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJsonodataMetadatanoneVersion1),
        'application/json;odata.streaming=true; version=1': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJsonodataStreamingtrueVersion1),
        'application/json;odata.streaming=false; version=1': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJsonodataStreamingfalseVersion1),
        'application/json; version=1': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJsonVersion1),
        'application/xml; version=1': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationXmlVersion1),
        'application/prs.odatatestxx-odata; version=1': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationPrsOdatatestxxOdataVersion1),
        'text/plain; version=1': api_client.MediaType(
            schema=SchemaFor200ResponseBodyTextPlainVersion1),
        'text/json; version=1': api_client.MediaType(
            schema=SchemaFor200ResponseBodyTextJsonVersion1),
    },
)
_all_accept_content_types = (
    'application/json;odata.metadata=minimal;odata.streaming=true; version=1',
    'application/json;odata.metadata=minimal;odata.streaming=false; version=1',
    'application/json;odata.metadata=minimal; version=1',
    'application/json;odata.metadata=full;odata.streaming=true; version=1',
    'application/json;odata.metadata=full;odata.streaming=false; version=1',
    'application/json;odata.metadata=full; version=1',
    'application/json;odata.metadata=none;odata.streaming=true; version=1',
    'application/json;odata.metadata=none;odata.streaming=false; version=1',
    'application/json;odata.metadata=none; version=1',
    'application/json;odata.streaming=true; version=1',
    'application/json;odata.streaming=false; version=1',
    'application/json; version=1',
    'application/xml; version=1',
    'application/prs.odatatestxx-odata; version=1',
    'text/plain; version=1',
    'text/json; version=1',
)


class BaseApi(api_client.Api):

    def _get_by_id_mapped_args(
        self,
        id: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        if id is not None:
            _path_params["id"] = id
        args.path = _path_params
        return args

    async def _aget_by_id_oapg(
        self,
            path_params: typing.Optional[dict] = {},
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
        Gets a single Bank Details by an ID.
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
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/bankdetails/{id}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


    def _get_by_id_oapg(
        self,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Gets a single Bank Details by an ID.
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
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/bankdetails/{id}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


class GetByIdRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_by_id(
        self,
        id: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_by_id_mapped_args(
            id=id,
        )
        return await self._aget_by_id_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def get_by_id(
        self,
        id: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_by_id_mapped_args(
            id=id,
        )
        return self._get_by_id_oapg(
            path_params=args.path,
        )

class GetById(BaseApi):

    async def aget_by_id(
        self,
        id: str,
        validate: bool = False,
        **kwargs,
    ) -> BankDetailsModelPydantic:
        raw_response = await self.raw.aget_by_id(
            id=id,
            **kwargs,
        )
        if validate:
            return BankDetailsModelPydantic(**raw_response.body)
        return api_client.construct_model_instance(BankDetailsModelPydantic, raw_response.body)
    
    
    def get_by_id(
        self,
        id: str,
        validate: bool = False,
    ) -> BankDetailsModelPydantic:
        raw_response = self.raw.get_by_id(
            id=id,
        )
        if validate:
            return BankDetailsModelPydantic(**raw_response.body)
        return api_client.construct_model_instance(BankDetailsModelPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        id: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_by_id_mapped_args(
            id=id,
        )
        return await self._aget_by_id_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        id: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_by_id_mapped_args(
            id=id,
        )
        return self._get_by_id_oapg(
            path_params=args.path,
        )

