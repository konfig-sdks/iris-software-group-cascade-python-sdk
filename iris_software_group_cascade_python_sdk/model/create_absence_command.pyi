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


class CreateAbsenceCommand(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
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
            
            
            class AbsenceReasonId(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'AbsenceReasonId':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class Narrative(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Narrative':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class StartDate(
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
                ) -> 'StartDate':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class EndDate(
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
                ) -> 'EndDate':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "EmployeeId": EmployeeId,
                "AbsenceReasonId": AbsenceReasonId,
                "Narrative": Narrative,
                "StartDate": StartDate,
                "EndDate": EndDate,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EmployeeId"]) -> MetaOapg.properties.EmployeeId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AbsenceReasonId"]) -> MetaOapg.properties.AbsenceReasonId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Narrative"]) -> MetaOapg.properties.Narrative: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["StartDate"]) -> MetaOapg.properties.StartDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EndDate"]) -> MetaOapg.properties.EndDate: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["EmployeeId", "AbsenceReasonId", "Narrative", "StartDate", "EndDate", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EmployeeId"]) -> typing.Union[MetaOapg.properties.EmployeeId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AbsenceReasonId"]) -> typing.Union[MetaOapg.properties.AbsenceReasonId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Narrative"]) -> typing.Union[MetaOapg.properties.Narrative, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["StartDate"]) -> typing.Union[MetaOapg.properties.StartDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EndDate"]) -> typing.Union[MetaOapg.properties.EndDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["EmployeeId", "AbsenceReasonId", "Narrative", "StartDate", "EndDate", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        EmployeeId: typing.Union[MetaOapg.properties.EmployeeId, None, str, schemas.Unset] = schemas.unset,
        AbsenceReasonId: typing.Union[MetaOapg.properties.AbsenceReasonId, None, str, schemas.Unset] = schemas.unset,
        Narrative: typing.Union[MetaOapg.properties.Narrative, None, str, schemas.Unset] = schemas.unset,
        StartDate: typing.Union[MetaOapg.properties.StartDate, None, str, datetime, schemas.Unset] = schemas.unset,
        EndDate: typing.Union[MetaOapg.properties.EndDate, None, str, datetime, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateAbsenceCommand':
        return super().__new__(
            cls,
            *args,
            EmployeeId=EmployeeId,
            AbsenceReasonId=AbsenceReasonId,
            Narrative=Narrative,
            StartDate=StartDate,
            EndDate=EndDate,
            _configuration=_configuration,
            **kwargs,
        )
