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


class AbsenceDayModel(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    An Attendance Absence Day
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
            
            
            class SourceSystemId(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'SourceSystemId':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class Id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            CreatedOn = schemas.DateTimeSchema
            
            
            class CreatedBy(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'CreatedBy':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class LastModifiedOn(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'LastModifiedOn':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class LastModifiedBy(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'LastModifiedBy':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "AbsenceId": AbsenceId,
                "EmployeeId": EmployeeId,
                "Date": Date,
                "DurationDays": DurationDays,
                "DurationMinutes": DurationMinutes,
                "DayPart": DayPart,
                "SourceSystemId": SourceSystemId,
                "Id": Id,
                "CreatedOn": CreatedOn,
                "CreatedBy": CreatedBy,
                "LastModifiedOn": LastModifiedOn,
                "LastModifiedBy": LastModifiedBy,
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
    def __getitem__(self, name: typing_extensions.Literal["SourceSystemId"]) -> MetaOapg.properties.SourceSystemId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Id"]) -> MetaOapg.properties.Id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CreatedOn"]) -> MetaOapg.properties.CreatedOn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CreatedBy"]) -> MetaOapg.properties.CreatedBy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LastModifiedOn"]) -> MetaOapg.properties.LastModifiedOn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LastModifiedBy"]) -> MetaOapg.properties.LastModifiedBy: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["AbsenceId", "EmployeeId", "Date", "DurationDays", "DurationMinutes", "DayPart", "SourceSystemId", "Id", "CreatedOn", "CreatedBy", "LastModifiedOn", "LastModifiedBy", ], str]):
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
    def get_item_oapg(self, name: typing_extensions.Literal["SourceSystemId"]) -> typing.Union[MetaOapg.properties.SourceSystemId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Id"]) -> typing.Union[MetaOapg.properties.Id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CreatedOn"]) -> typing.Union[MetaOapg.properties.CreatedOn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CreatedBy"]) -> typing.Union[MetaOapg.properties.CreatedBy, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LastModifiedOn"]) -> typing.Union[MetaOapg.properties.LastModifiedOn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LastModifiedBy"]) -> typing.Union[MetaOapg.properties.LastModifiedBy, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["AbsenceId", "EmployeeId", "Date", "DurationDays", "DurationMinutes", "DayPart", "SourceSystemId", "Id", "CreatedOn", "CreatedBy", "LastModifiedOn", "LastModifiedBy", ], str]):
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
        SourceSystemId: typing.Union[MetaOapg.properties.SourceSystemId, None, str, schemas.Unset] = schemas.unset,
        Id: typing.Union[MetaOapg.properties.Id, None, str, schemas.Unset] = schemas.unset,
        CreatedOn: typing.Union[MetaOapg.properties.CreatedOn, str, datetime, schemas.Unset] = schemas.unset,
        CreatedBy: typing.Union[MetaOapg.properties.CreatedBy, None, str, schemas.Unset] = schemas.unset,
        LastModifiedOn: typing.Union[MetaOapg.properties.LastModifiedOn, None, str, datetime, schemas.Unset] = schemas.unset,
        LastModifiedBy: typing.Union[MetaOapg.properties.LastModifiedBy, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AbsenceDayModel':
        return super().__new__(
            cls,
            *args,
            AbsenceId=AbsenceId,
            EmployeeId=EmployeeId,
            Date=Date,
            DurationDays=DurationDays,
            DurationMinutes=DurationMinutes,
            DayPart=DayPart,
            SourceSystemId=SourceSystemId,
            Id=Id,
            CreatedOn=CreatedOn,
            CreatedBy=CreatedBy,
            LastModifiedOn=LastModifiedOn,
            LastModifiedBy=LastModifiedBy,
            _configuration=_configuration,
            **kwargs,
        )

from iris_software_group_cascade_python_sdk.model.day_part import DayPart
