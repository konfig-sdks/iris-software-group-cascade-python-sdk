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

from iris_software_group_cascade_python_sdk.model.bank_address import BankAddress as BankAddressSchema
from iris_software_group_cascade_python_sdk.model.update_bank_details_command import UpdateBankDetailsCommand as UpdateBankDetailsCommandSchema
from iris_software_group_cascade_python_sdk.model.problem_details import ProblemDetails as ProblemDetailsSchema

from iris_software_group_cascade_python_sdk.type.bank_address import BankAddress
from iris_software_group_cascade_python_sdk.type.update_bank_details_command import UpdateBankDetailsCommand
from iris_software_group_cascade_python_sdk.type.problem_details import ProblemDetails

from ...api_client import Dictionary
from iris_software_group_cascade_python_sdk.pydantic.bank_address import BankAddress as BankAddressPydantic
from iris_software_group_cascade_python_sdk.pydantic.problem_details import ProblemDetails as ProblemDetailsPydantic
from iris_software_group_cascade_python_sdk.pydantic.update_bank_details_command import UpdateBankDetailsCommand as UpdateBankDetailsCommandPydantic

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
SchemaForRequestBodyApplicationJsonodataMetadataminimalodataStreamingtrueVersion1 = UpdateBankDetailsCommandSchema
SchemaForRequestBodyApplicationJsonodataMetadataminimalodataStreamingfalseVersion1 = UpdateBankDetailsCommandSchema
SchemaForRequestBodyApplicationJsonodataMetadataminimalVersion1 = UpdateBankDetailsCommandSchema
SchemaForRequestBodyApplicationJsonodataMetadatafullodataStreamingtrueVersion1 = UpdateBankDetailsCommandSchema
SchemaForRequestBodyApplicationJsonodataMetadatafullodataStreamingfalseVersion1 = UpdateBankDetailsCommandSchema
SchemaForRequestBodyApplicationJsonodataMetadatafullVersion1 = UpdateBankDetailsCommandSchema
SchemaForRequestBodyApplicationJsonodataMetadatanoneodataStreamingtrueVersion1 = UpdateBankDetailsCommandSchema
SchemaForRequestBodyApplicationJsonodataMetadatanoneodataStreamingfalseVersion1 = UpdateBankDetailsCommandSchema
SchemaForRequestBodyApplicationJsonodataMetadatanoneVersion1 = UpdateBankDetailsCommandSchema
SchemaForRequestBodyApplicationJsonodataStreamingtrueVersion1 = UpdateBankDetailsCommandSchema
SchemaForRequestBodyApplicationJsonodataStreamingfalseVersion1 = UpdateBankDetailsCommandSchema
SchemaForRequestBodyApplicationJsonVersion1 = UpdateBankDetailsCommandSchema
SchemaForRequestBodyApplicationXmlVersion1 = UpdateBankDetailsCommandSchema
SchemaForRequestBodyApplicationPrsOdatatestxxOdataVersion1 = UpdateBankDetailsCommandSchema
SchemaForRequestBodyTextJsonVersion1 = UpdateBankDetailsCommandSchema
SchemaForRequestBodyApplicationJsonVersion1 = UpdateBankDetailsCommandSchema


request_body_update_bank_details_command = api_client.RequestBody(
    content={
        'application/json;odata.metadata=minimal;odata.streaming=true; version=1': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJsonodataMetadataminimalodataStreamingtrueVersion1),
        'application/json;odata.metadata=minimal;odata.streaming=false; version=1': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJsonodataMetadataminimalodataStreamingfalseVersion1),
        'application/json;odata.metadata=minimal; version=1': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJsonodataMetadataminimalVersion1),
        'application/json;odata.metadata=full;odata.streaming=true; version=1': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJsonodataMetadatafullodataStreamingtrueVersion1),
        'application/json;odata.metadata=full;odata.streaming=false; version=1': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJsonodataMetadatafullodataStreamingfalseVersion1),
        'application/json;odata.metadata=full; version=1': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJsonodataMetadatafullVersion1),
        'application/json;odata.metadata=none;odata.streaming=true; version=1': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJsonodataMetadatanoneodataStreamingtrueVersion1),
        'application/json;odata.metadata=none;odata.streaming=false; version=1': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJsonodataMetadatanoneodataStreamingfalseVersion1),
        'application/json;odata.metadata=none; version=1': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJsonodataMetadatanoneVersion1),
        'application/json;odata.streaming=true; version=1': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJsonodataStreamingtrueVersion1),
        'application/json;odata.streaming=false; version=1': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJsonodataStreamingfalseVersion1),
        'application/json; version=1': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJsonVersion1),
        'application/xml; version=1': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationXmlVersion1),
        'application/prs.odatatestxx-odata; version=1': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationPrsOdatatestxxOdataVersion1),
        'text/json; version=1': api_client.MediaType(
            schema=SchemaForRequestBodyTextJsonVersion1),
        'application/*+json; version=1': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJsonVersion1),
    },
)


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
SchemaFor400ResponseBodyApplicationJsonodataMetadataminimalodataStreamingtrueVersion1 = ProblemDetailsSchema
SchemaFor400ResponseBodyApplicationJsonodataMetadataminimalodataStreamingfalseVersion1 = ProblemDetailsSchema
SchemaFor400ResponseBodyApplicationJsonodataMetadataminimalVersion1 = ProblemDetailsSchema
SchemaFor400ResponseBodyApplicationJsonodataMetadatafullodataStreamingtrueVersion1 = ProblemDetailsSchema
SchemaFor400ResponseBodyApplicationJsonodataMetadatafullodataStreamingfalseVersion1 = ProblemDetailsSchema
SchemaFor400ResponseBodyApplicationJsonodataMetadatafullVersion1 = ProblemDetailsSchema
SchemaFor400ResponseBodyApplicationJsonodataMetadatanoneodataStreamingtrueVersion1 = ProblemDetailsSchema
SchemaFor400ResponseBodyApplicationJsonodataMetadatanoneodataStreamingfalseVersion1 = ProblemDetailsSchema
SchemaFor400ResponseBodyApplicationJsonodataMetadatanoneVersion1 = ProblemDetailsSchema
SchemaFor400ResponseBodyApplicationJsonodataStreamingtrueVersion1 = ProblemDetailsSchema
SchemaFor400ResponseBodyApplicationJsonodataStreamingfalseVersion1 = ProblemDetailsSchema
SchemaFor400ResponseBodyApplicationJsonVersion1 = ProblemDetailsSchema
SchemaFor400ResponseBodyApplicationXmlVersion1 = ProblemDetailsSchema
SchemaFor400ResponseBodyApplicationPrsOdatatestxxOdataVersion1 = ProblemDetailsSchema
SchemaFor400ResponseBodyTextPlainVersion1 = ProblemDetailsSchema
SchemaFor400ResponseBodyTextJsonVersion1 = ProblemDetailsSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: ProblemDetails


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: ProblemDetails


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json;odata.metadata=minimal;odata.streaming=true; version=1': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJsonodataMetadataminimalodataStreamingtrueVersion1),
        'application/json;odata.metadata=minimal;odata.streaming=false; version=1': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJsonodataMetadataminimalodataStreamingfalseVersion1),
        'application/json;odata.metadata=minimal; version=1': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJsonodataMetadataminimalVersion1),
        'application/json;odata.metadata=full;odata.streaming=true; version=1': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJsonodataMetadatafullodataStreamingtrueVersion1),
        'application/json;odata.metadata=full;odata.streaming=false; version=1': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJsonodataMetadatafullodataStreamingfalseVersion1),
        'application/json;odata.metadata=full; version=1': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJsonodataMetadatafullVersion1),
        'application/json;odata.metadata=none;odata.streaming=true; version=1': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJsonodataMetadatanoneodataStreamingtrueVersion1),
        'application/json;odata.metadata=none;odata.streaming=false; version=1': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJsonodataMetadatanoneodataStreamingfalseVersion1),
        'application/json;odata.metadata=none; version=1': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJsonodataMetadatanoneVersion1),
        'application/json;odata.streaming=true; version=1': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJsonodataStreamingtrueVersion1),
        'application/json;odata.streaming=false; version=1': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJsonodataStreamingfalseVersion1),
        'application/json; version=1': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJsonVersion1),
        'application/xml; version=1': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationXmlVersion1),
        'application/prs.odatatestxx-odata; version=1': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationPrsOdatatestxxOdataVersion1),
        'text/plain; version=1': api_client.MediaType(
            schema=SchemaFor400ResponseBodyTextPlainVersion1),
        'text/json; version=1': api_client.MediaType(
            schema=SchemaFor400ResponseBodyTextJsonVersion1),
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

    def _update_bank_detail_mapped_args(
        self,
        id: str,
        bank_name: typing.Optional[typing.Optional[str]] = None,
        bank_address: typing.Optional[BankAddress] = None,
        account_name: typing.Optional[typing.Optional[str]] = None,
        account_number: typing.Optional[typing.Optional[str]] = None,
        sort_code: typing.Optional[typing.Optional[str]] = None,
        roll_number: typing.Optional[typing.Optional[str]] = None,
        id: typing.Optional[typing.Optional[str]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if bank_name is not None:
            _body["BankName"] = bank_name
        if bank_address is not None:
            _body["BankAddress"] = bank_address
        if account_name is not None:
            _body["AccountName"] = account_name
        if account_number is not None:
            _body["AccountNumber"] = account_number
        if sort_code is not None:
            _body["SortCode"] = sort_code
        if roll_number is not None:
            _body["RollNumber"] = roll_number
        if id is not None:
            _body["Id"] = id
        args.body = _body
        if id is not None:
            _path_params["id"] = id
        args.path = _path_params
        return args

    async def _aupdate_bank_detail_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json;odata.metadata=minimal;odata.streaming=true; version=1',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Updates Bank Details.
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
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/bankdetails/{id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_update_bank_details_command.serialize(body, content_type)
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


    def _update_bank_detail_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json;odata.metadata=minimal;odata.streaming=true; version=1',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Updates Bank Details.
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
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/bankdetails/{id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_update_bank_details_command.serialize(body, content_type)
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


class UpdateBankDetailRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_bank_detail(
        self,
        id: str,
        bank_name: typing.Optional[typing.Optional[str]] = None,
        bank_address: typing.Optional[BankAddress] = None,
        account_name: typing.Optional[typing.Optional[str]] = None,
        account_number: typing.Optional[typing.Optional[str]] = None,
        sort_code: typing.Optional[typing.Optional[str]] = None,
        roll_number: typing.Optional[typing.Optional[str]] = None,
        id: typing.Optional[typing.Optional[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_bank_detail_mapped_args(
            id=id,
            bank_name=bank_name,
            bank_address=bank_address,
            account_name=account_name,
            account_number=account_number,
            sort_code=sort_code,
            roll_number=roll_number,
            id=id,
        )
        return await self._aupdate_bank_detail_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update_bank_detail(
        self,
        id: str,
        bank_name: typing.Optional[typing.Optional[str]] = None,
        bank_address: typing.Optional[BankAddress] = None,
        account_name: typing.Optional[typing.Optional[str]] = None,
        account_number: typing.Optional[typing.Optional[str]] = None,
        sort_code: typing.Optional[typing.Optional[str]] = None,
        roll_number: typing.Optional[typing.Optional[str]] = None,
        id: typing.Optional[typing.Optional[str]] = None,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_bank_detail_mapped_args(
            id=id,
            bank_name=bank_name,
            bank_address=bank_address,
            account_name=account_name,
            account_number=account_number,
            sort_code=sort_code,
            roll_number=roll_number,
            id=id,
        )
        return self._update_bank_detail_oapg(
            body=args.body,
            path_params=args.path,
        )

class UpdateBankDetail(BaseApi):

    async def aupdate_bank_detail(
        self,
        id: str,
        bank_name: typing.Optional[typing.Optional[str]] = None,
        bank_address: typing.Optional[BankAddress] = None,
        account_name: typing.Optional[typing.Optional[str]] = None,
        account_number: typing.Optional[typing.Optional[str]] = None,
        sort_code: typing.Optional[typing.Optional[str]] = None,
        roll_number: typing.Optional[typing.Optional[str]] = None,
        id: typing.Optional[typing.Optional[str]] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.aupdate_bank_detail(
            id=id,
            bank_name=bank_name,
            bank_address=bank_address,
            account_name=account_name,
            account_number=account_number,
            sort_code=sort_code,
            roll_number=roll_number,
            id=id,
            **kwargs,
        )
    
    
    def update_bank_detail(
        self,
        id: str,
        bank_name: typing.Optional[typing.Optional[str]] = None,
        bank_address: typing.Optional[BankAddress] = None,
        account_name: typing.Optional[typing.Optional[str]] = None,
        account_number: typing.Optional[typing.Optional[str]] = None,
        sort_code: typing.Optional[typing.Optional[str]] = None,
        roll_number: typing.Optional[typing.Optional[str]] = None,
        id: typing.Optional[typing.Optional[str]] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.update_bank_detail(
            id=id,
            bank_name=bank_name,
            bank_address=bank_address,
            account_name=account_name,
            account_number=account_number,
            sort_code=sort_code,
            roll_number=roll_number,
            id=id,
        )


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        id: str,
        bank_name: typing.Optional[typing.Optional[str]] = None,
        bank_address: typing.Optional[BankAddress] = None,
        account_name: typing.Optional[typing.Optional[str]] = None,
        account_number: typing.Optional[typing.Optional[str]] = None,
        sort_code: typing.Optional[typing.Optional[str]] = None,
        roll_number: typing.Optional[typing.Optional[str]] = None,
        id: typing.Optional[typing.Optional[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_bank_detail_mapped_args(
            id=id,
            bank_name=bank_name,
            bank_address=bank_address,
            account_name=account_name,
            account_number=account_number,
            sort_code=sort_code,
            roll_number=roll_number,
            id=id,
        )
        return await self._aupdate_bank_detail_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        id: str,
        bank_name: typing.Optional[typing.Optional[str]] = None,
        bank_address: typing.Optional[BankAddress] = None,
        account_name: typing.Optional[typing.Optional[str]] = None,
        account_number: typing.Optional[typing.Optional[str]] = None,
        sort_code: typing.Optional[typing.Optional[str]] = None,
        roll_number: typing.Optional[typing.Optional[str]] = None,
        id: typing.Optional[typing.Optional[str]] = None,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_bank_detail_mapped_args(
            id=id,
            bank_name=bank_name,
            bank_address=bank_address,
            account_name=account_name,
            account_number=account_number,
            sort_code=sort_code,
            roll_number=roll_number,
            id=id,
        )
        return self._update_bank_detail_oapg(
            body=args.body,
            path_params=args.path,
        )

