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


class AbsenceReasonModel(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    An HR Attendance Absence Reason.
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
            
            
            class Name(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Name':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class Holiday(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Holiday':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class Absent(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Absent':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class Sick(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Sick':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class StatutoryMaternityPayApplicable(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'StatutoryMaternityPayApplicable':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class StudyExam(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'StudyExam':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class FlexiLeave(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'FlexiLeave':
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
                "Name": Name,
                "Holiday": Holiday,
                "Absent": Absent,
                "Sick": Sick,
                "StatutoryMaternityPayApplicable": StatutoryMaternityPayApplicable,
                "StudyExam": StudyExam,
                "FlexiLeave": FlexiLeave,
                "Id": Id,
                "CreatedOn": CreatedOn,
                "CreatedBy": CreatedBy,
                "LastModifiedOn": LastModifiedOn,
                "LastModifiedBy": LastModifiedBy,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ParentId"]) -> MetaOapg.properties.ParentId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Name"]) -> MetaOapg.properties.Name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Holiday"]) -> MetaOapg.properties.Holiday: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Absent"]) -> MetaOapg.properties.Absent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Sick"]) -> MetaOapg.properties.Sick: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["StatutoryMaternityPayApplicable"]) -> MetaOapg.properties.StatutoryMaternityPayApplicable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["StudyExam"]) -> MetaOapg.properties.StudyExam: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FlexiLeave"]) -> MetaOapg.properties.FlexiLeave: ...
    
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
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["ParentId", "Name", "Holiday", "Absent", "Sick", "StatutoryMaternityPayApplicable", "StudyExam", "FlexiLeave", "Id", "CreatedOn", "CreatedBy", "LastModifiedOn", "LastModifiedBy", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ParentId"]) -> typing.Union[MetaOapg.properties.ParentId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Name"]) -> typing.Union[MetaOapg.properties.Name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Holiday"]) -> typing.Union[MetaOapg.properties.Holiday, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Absent"]) -> typing.Union[MetaOapg.properties.Absent, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Sick"]) -> typing.Union[MetaOapg.properties.Sick, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["StatutoryMaternityPayApplicable"]) -> typing.Union[MetaOapg.properties.StatutoryMaternityPayApplicable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["StudyExam"]) -> typing.Union[MetaOapg.properties.StudyExam, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FlexiLeave"]) -> typing.Union[MetaOapg.properties.FlexiLeave, schemas.Unset]: ...
    
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
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ParentId", "Name", "Holiday", "Absent", "Sick", "StatutoryMaternityPayApplicable", "StudyExam", "FlexiLeave", "Id", "CreatedOn", "CreatedBy", "LastModifiedOn", "LastModifiedBy", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        ParentId: typing.Union[MetaOapg.properties.ParentId, None, str, schemas.Unset] = schemas.unset,
        Name: typing.Union[MetaOapg.properties.Name, None, str, schemas.Unset] = schemas.unset,
        Holiday: typing.Union[MetaOapg.properties.Holiday, None, bool, schemas.Unset] = schemas.unset,
        Absent: typing.Union[MetaOapg.properties.Absent, None, bool, schemas.Unset] = schemas.unset,
        Sick: typing.Union[MetaOapg.properties.Sick, None, bool, schemas.Unset] = schemas.unset,
        StatutoryMaternityPayApplicable: typing.Union[MetaOapg.properties.StatutoryMaternityPayApplicable, None, bool, schemas.Unset] = schemas.unset,
        StudyExam: typing.Union[MetaOapg.properties.StudyExam, None, bool, schemas.Unset] = schemas.unset,
        FlexiLeave: typing.Union[MetaOapg.properties.FlexiLeave, None, bool, schemas.Unset] = schemas.unset,
        Id: typing.Union[MetaOapg.properties.Id, None, str, schemas.Unset] = schemas.unset,
        CreatedOn: typing.Union[MetaOapg.properties.CreatedOn, str, datetime, schemas.Unset] = schemas.unset,
        CreatedBy: typing.Union[MetaOapg.properties.CreatedBy, None, str, schemas.Unset] = schemas.unset,
        LastModifiedOn: typing.Union[MetaOapg.properties.LastModifiedOn, None, str, datetime, schemas.Unset] = schemas.unset,
        LastModifiedBy: typing.Union[MetaOapg.properties.LastModifiedBy, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AbsenceReasonModel':
        return super().__new__(
            cls,
            *args,
            ParentId=ParentId,
            Name=Name,
            Holiday=Holiday,
            Absent=Absent,
            Sick=Sick,
            StatutoryMaternityPayApplicable=StatutoryMaternityPayApplicable,
            StudyExam=StudyExam,
            FlexiLeave=FlexiLeave,
            Id=Id,
            CreatedOn=CreatedOn,
            CreatedBy=CreatedBy,
            LastModifiedOn=LastModifiedOn,
            LastModifiedBy=LastModifiedBy,
            _configuration=_configuration,
            **kwargs,
        )
