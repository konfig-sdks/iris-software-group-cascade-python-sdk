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


class CreateAbsenceDayCommand(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class AbsenceId(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'AbsenceId':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class EmployeeId(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'EmployeeId':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            Date = schemas.DateTimeSchema
            DurationDays = schemas.Float64Schema
            
            
            class DurationMinutes(
                schemas.Int32Base,
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'int32'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'DurationMinutes':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def DayPart() -> typing.Type['DayPart']:
                return DayPart
            __annotations__ = {
                "AbsenceId": AbsenceId,
                "EmployeeId": EmployeeId,
                "Date": Date,
                "DurationDays": DurationDays,
                "DurationMinutes": DurationMinutes,
                "DayPart": DayPart,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AbsenceId"]) -> MetaOapg.properties.AbsenceId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EmployeeId"]) -> MetaOapg.properties.EmployeeId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Date"]) -> MetaOapg.properties.Date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DurationDays"]) -> MetaOapg.properties.DurationDays: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DurationMinutes"]) -> MetaOapg.properties.DurationMinutes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DayPart"]) -> 'DayPart': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["AbsenceId", "EmployeeId", "Date", "DurationDays", "DurationMinutes", "DayPart", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AbsenceId"]) -> typing.Union[MetaOapg.properties.AbsenceId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EmployeeId"]) -> typing.Union[MetaOapg.properties.EmployeeId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Date"]) -> typing.Union[MetaOapg.properties.Date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DurationDays"]) -> typing.Union[MetaOapg.properties.DurationDays, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DurationMinutes"]) -> typing.Union[MetaOapg.properties.DurationMinutes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DayPart"]) -> typing.Union['DayPart', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["AbsenceId", "EmployeeId", "Date", "DurationDays", "DurationMinutes", "DayPart", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        AbsenceId: typing.Union[MetaOapg.properties.AbsenceId, None, str, schemas.Unset] = schemas.unset,
        EmployeeId: typing.Union[MetaOapg.properties.EmployeeId, None, str, schemas.Unset] = schemas.unset,
        Date: typing.Union[MetaOapg.properties.Date, str, datetime, schemas.Unset] = schemas.unset,
        DurationDays: typing.Union[MetaOapg.properties.DurationDays, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        DurationMinutes: typing.Union[MetaOapg.properties.DurationMinutes, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        DayPart: typing.Union['DayPart', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateAbsenceDayCommand':
        return super().__new__(
            cls,
            *args,
            AbsenceId=AbsenceId,
            EmployeeId=EmployeeId,
            Date=Date,
            DurationDays=DurationDays,
            DurationMinutes=DurationMinutes,
            DayPart=DayPart,
            _configuration=_configuration,
            **kwargs,
        )

from iris_software_group_cascade_python_sdk.model.day_part import DayPart