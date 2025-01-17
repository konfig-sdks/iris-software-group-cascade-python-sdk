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


class BenefitModel(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    An HR Employee's Benefits.
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
            
            
            class Type(
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
                ) -> 'Type':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class Description(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Description':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class Value(
                schemas.Float64Base,
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'double'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Value':
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
            
            
            class P11DValue(
                schemas.Float64Base,
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'double'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'P11DValue':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            Suspended = schemas.BoolSchema
            
            
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
                "EmployeeId": EmployeeId,
                "Type": Type,
                "Description": Description,
                "Value": Value,
                "StartDate": StartDate,
                "EndDate": EndDate,
                "P11DValue": P11DValue,
                "Suspended": Suspended,
                "Id": Id,
                "SourceSystemId": SourceSystemId,
                "CreatedOn": CreatedOn,
                "CreatedBy": CreatedBy,
                "LastModifiedOn": LastModifiedOn,
                "LastModifiedBy": LastModifiedBy,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EmployeeId"]) -> MetaOapg.properties.EmployeeId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Type"]) -> MetaOapg.properties.Type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Description"]) -> MetaOapg.properties.Description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Value"]) -> MetaOapg.properties.Value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["StartDate"]) -> MetaOapg.properties.StartDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EndDate"]) -> MetaOapg.properties.EndDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["P11DValue"]) -> MetaOapg.properties.P11DValue: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Suspended"]) -> MetaOapg.properties.Suspended: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Id"]) -> MetaOapg.properties.Id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SourceSystemId"]) -> MetaOapg.properties.SourceSystemId: ...
    
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
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["EmployeeId", "Type", "Description", "Value", "StartDate", "EndDate", "P11DValue", "Suspended", "Id", "SourceSystemId", "CreatedOn", "CreatedBy", "LastModifiedOn", "LastModifiedBy", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EmployeeId"]) -> typing.Union[MetaOapg.properties.EmployeeId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Type"]) -> typing.Union[MetaOapg.properties.Type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Description"]) -> typing.Union[MetaOapg.properties.Description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Value"]) -> typing.Union[MetaOapg.properties.Value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["StartDate"]) -> typing.Union[MetaOapg.properties.StartDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EndDate"]) -> typing.Union[MetaOapg.properties.EndDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["P11DValue"]) -> typing.Union[MetaOapg.properties.P11DValue, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Suspended"]) -> typing.Union[MetaOapg.properties.Suspended, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Id"]) -> typing.Union[MetaOapg.properties.Id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SourceSystemId"]) -> typing.Union[MetaOapg.properties.SourceSystemId, schemas.Unset]: ...
    
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
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["EmployeeId", "Type", "Description", "Value", "StartDate", "EndDate", "P11DValue", "Suspended", "Id", "SourceSystemId", "CreatedOn", "CreatedBy", "LastModifiedOn", "LastModifiedBy", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        EmployeeId: typing.Union[MetaOapg.properties.EmployeeId, None, str, schemas.Unset] = schemas.unset,
        Type: typing.Union[MetaOapg.properties.Type, None, str, schemas.Unset] = schemas.unset,
        Description: typing.Union[MetaOapg.properties.Description, None, str, schemas.Unset] = schemas.unset,
        Value: typing.Union[MetaOapg.properties.Value, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        StartDate: typing.Union[MetaOapg.properties.StartDate, None, str, datetime, schemas.Unset] = schemas.unset,
        EndDate: typing.Union[MetaOapg.properties.EndDate, None, str, datetime, schemas.Unset] = schemas.unset,
        P11DValue: typing.Union[MetaOapg.properties.P11DValue, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        Suspended: typing.Union[MetaOapg.properties.Suspended, bool, schemas.Unset] = schemas.unset,
        Id: typing.Union[MetaOapg.properties.Id, None, str, schemas.Unset] = schemas.unset,
        SourceSystemId: typing.Union[MetaOapg.properties.SourceSystemId, None, str, schemas.Unset] = schemas.unset,
        CreatedOn: typing.Union[MetaOapg.properties.CreatedOn, str, datetime, schemas.Unset] = schemas.unset,
        CreatedBy: typing.Union[MetaOapg.properties.CreatedBy, None, str, schemas.Unset] = schemas.unset,
        LastModifiedOn: typing.Union[MetaOapg.properties.LastModifiedOn, None, str, datetime, schemas.Unset] = schemas.unset,
        LastModifiedBy: typing.Union[MetaOapg.properties.LastModifiedBy, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BenefitModel':
        return super().__new__(
            cls,
            *args,
            EmployeeId=EmployeeId,
            Type=Type,
            Description=Description,
            Value=Value,
            StartDate=StartDate,
            EndDate=EndDate,
            P11DValue=P11DValue,
            Suspended=Suspended,
            Id=Id,
            SourceSystemId=SourceSystemId,
            CreatedOn=CreatedOn,
            CreatedBy=CreatedBy,
            LastModifiedOn=LastModifiedOn,
            LastModifiedBy=LastModifiedBy,
            _configuration=_configuration,
            **kwargs,
        )
