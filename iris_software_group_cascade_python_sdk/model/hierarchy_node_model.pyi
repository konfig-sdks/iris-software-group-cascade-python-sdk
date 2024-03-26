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


class HierarchyNodeModel(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The Hierarchy node.
    """


    class MetaOapg:
        
        class properties:
            
            
            class ParentId(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ParentId':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            Level = schemas.Int32Schema
            
            
            class Title(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Title':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            Disabled = schemas.BoolSchema
            
            
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
            
            
            class SourceSystemCreatedOn(
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
                ) -> 'SourceSystemCreatedOn':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class SourceSystemLastModifiedOn(
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
                ) -> 'SourceSystemLastModifiedOn':
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
                "ParentId": ParentId,
                "Level": Level,
                "Title": Title,
                "Disabled": Disabled,
                "SourceSystemId": SourceSystemId,
                "SourceSystemCreatedOn": SourceSystemCreatedOn,
                "SourceSystemLastModifiedOn": SourceSystemLastModifiedOn,
                "Id": Id,
                "CreatedOn": CreatedOn,
                "CreatedBy": CreatedBy,
                "LastModifiedOn": LastModifiedOn,
                "LastModifiedBy": LastModifiedBy,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ParentId"]) -> MetaOapg.properties.ParentId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Level"]) -> MetaOapg.properties.Level: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Title"]) -> MetaOapg.properties.Title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Disabled"]) -> MetaOapg.properties.Disabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SourceSystemId"]) -> MetaOapg.properties.SourceSystemId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SourceSystemCreatedOn"]) -> MetaOapg.properties.SourceSystemCreatedOn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SourceSystemLastModifiedOn"]) -> MetaOapg.properties.SourceSystemLastModifiedOn: ...
    
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
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["ParentId", "Level", "Title", "Disabled", "SourceSystemId", "SourceSystemCreatedOn", "SourceSystemLastModifiedOn", "Id", "CreatedOn", "CreatedBy", "LastModifiedOn", "LastModifiedBy", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ParentId"]) -> typing.Union[MetaOapg.properties.ParentId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Level"]) -> typing.Union[MetaOapg.properties.Level, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Title"]) -> typing.Union[MetaOapg.properties.Title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Disabled"]) -> typing.Union[MetaOapg.properties.Disabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SourceSystemId"]) -> typing.Union[MetaOapg.properties.SourceSystemId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SourceSystemCreatedOn"]) -> typing.Union[MetaOapg.properties.SourceSystemCreatedOn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SourceSystemLastModifiedOn"]) -> typing.Union[MetaOapg.properties.SourceSystemLastModifiedOn, schemas.Unset]: ...
    
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
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ParentId", "Level", "Title", "Disabled", "SourceSystemId", "SourceSystemCreatedOn", "SourceSystemLastModifiedOn", "Id", "CreatedOn", "CreatedBy", "LastModifiedOn", "LastModifiedBy", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        ParentId: typing.Union[MetaOapg.properties.ParentId, None, str, schemas.Unset] = schemas.unset,
        Level: typing.Union[MetaOapg.properties.Level, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        Title: typing.Union[MetaOapg.properties.Title, None, str, schemas.Unset] = schemas.unset,
        Disabled: typing.Union[MetaOapg.properties.Disabled, bool, schemas.Unset] = schemas.unset,
        SourceSystemId: typing.Union[MetaOapg.properties.SourceSystemId, None, str, schemas.Unset] = schemas.unset,
        SourceSystemCreatedOn: typing.Union[MetaOapg.properties.SourceSystemCreatedOn, None, str, datetime, schemas.Unset] = schemas.unset,
        SourceSystemLastModifiedOn: typing.Union[MetaOapg.properties.SourceSystemLastModifiedOn, None, str, datetime, schemas.Unset] = schemas.unset,
        Id: typing.Union[MetaOapg.properties.Id, None, str, schemas.Unset] = schemas.unset,
        CreatedOn: typing.Union[MetaOapg.properties.CreatedOn, str, datetime, schemas.Unset] = schemas.unset,
        CreatedBy: typing.Union[MetaOapg.properties.CreatedBy, None, str, schemas.Unset] = schemas.unset,
        LastModifiedOn: typing.Union[MetaOapg.properties.LastModifiedOn, None, str, datetime, schemas.Unset] = schemas.unset,
        LastModifiedBy: typing.Union[MetaOapg.properties.LastModifiedBy, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'HierarchyNodeModel':
        return super().__new__(
            cls,
            *args,
            ParentId=ParentId,
            Level=Level,
            Title=Title,
            Disabled=Disabled,
            SourceSystemId=SourceSystemId,
            SourceSystemCreatedOn=SourceSystemCreatedOn,
            SourceSystemLastModifiedOn=SourceSystemLastModifiedOn,
            Id=Id,
            CreatedOn=CreatedOn,
            CreatedBy=CreatedBy,
            LastModifiedOn=LastModifiedOn,
            LastModifiedBy=LastModifiedBy,
            _configuration=_configuration,
            **kwargs,
        )
