# coding: utf-8

"""
    HR API

    <a href='swaggerv2.json'>Download Swagger Json in OAS2 Format.</a>

    The version of the OpenAPI document: 2
    Contact: hrapi@iris.co.uk
    Created by: https://help.iris.co.uk/hr/cascade/api/
"""

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


class Phone(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A Phone Number with Ownership and Type properties
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def Ownership() -> typing.Type['Ownership']:
                return Ownership
        
            @staticmethod
            def Type() -> typing.Type['PhoneType']:
                return PhoneType
            
            
            class Value(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Value':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "Ownership": Ownership,
                "Type": Type,
                "Value": Value,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Ownership"]) -> 'Ownership': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Type"]) -> 'PhoneType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Value"]) -> MetaOapg.properties.Value: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Ownership", "Type", "Value", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Ownership"]) -> typing.Union['Ownership', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Type"]) -> typing.Union['PhoneType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Value"]) -> typing.Union[MetaOapg.properties.Value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Ownership", "Type", "Value", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Ownership: typing.Union['Ownership', schemas.Unset] = schemas.unset,
        Type: typing.Union['PhoneType', schemas.Unset] = schemas.unset,
        Value: typing.Union[MetaOapg.properties.Value, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Phone':
        return super().__new__(
            cls,
            *args,
            Ownership=Ownership,
            Type=Type,
            Value=Value,
            _configuration=_configuration,
            **kwargs,
        )

from iris_software_group_cascade_python_sdk.model.ownership import Ownership
from iris_software_group_cascade_python_sdk.model.phone_type import PhoneType
