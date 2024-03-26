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


class CreateEmployeeCommand(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class DisplayId(
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
                ) -> 'DisplayId':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class TitleHonorific(
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
                ) -> 'TitleHonorific':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class FirstName(
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
                ) -> 'FirstName':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class KnownAs(
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
                ) -> 'KnownAs':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class OtherName(
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
                ) -> 'OtherName':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class LastName(
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
                ) -> 'LastName':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class CostCentre(
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
                ) -> 'CostCentre':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class WorkingStatus(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'WorkingStatus':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class IsManager(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'IsManager':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class NationalInsuranceNumber(
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
                ) -> 'NationalInsuranceNumber':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class PayrollId(
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
                ) -> 'PayrollId':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class TaxCode(
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
                ) -> 'TaxCode':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class IncludeInPayroll(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'IncludeInPayroll':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class EmploymentStartDate(
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
                ) -> 'EmploymentStartDate':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class EmploymentLeftDate(
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
                ) -> 'EmploymentLeftDate':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class ContinuousServiceDate(
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
                ) -> 'ContinuousServiceDate':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class DateOfBirth(
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
                ) -> 'DateOfBirth':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class LastWorkingDate(
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
                ) -> 'LastWorkingDate':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class Gender(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Gender':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class Ethnicity(
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
                ) -> 'Ethnicity':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class Nationality(
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
                ) -> 'Nationality':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class Religion(
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
                ) -> 'Religion':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class LeaverReason(
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
                ) -> 'LeaverReason':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class MaritalStatus(
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
                ) -> 'MaritalStatus':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class Phones(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Phone']:
                        return Phone
            
            
                def __new__(
                    cls,
                    *args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Phones':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class Emails(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Email']:
                        return Email
            
            
                def __new__(
                    cls,
                    *args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Emails':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class Addresses(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Address']:
                        return Address
            
            
                def __new__(
                    cls,
                    *args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Addresses':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class GenderIdentity(
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
                ) -> 'GenderIdentity':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class WindowsUsername(
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
                ) -> 'WindowsUsername':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "DisplayId": DisplayId,
                "TitleHonorific": TitleHonorific,
                "FirstName": FirstName,
                "KnownAs": KnownAs,
                "OtherName": OtherName,
                "LastName": LastName,
                "CostCentre": CostCentre,
                "WorkingStatus": WorkingStatus,
                "IsManager": IsManager,
                "NationalInsuranceNumber": NationalInsuranceNumber,
                "PayrollId": PayrollId,
                "TaxCode": TaxCode,
                "IncludeInPayroll": IncludeInPayroll,
                "EmploymentStartDate": EmploymentStartDate,
                "EmploymentLeftDate": EmploymentLeftDate,
                "ContinuousServiceDate": ContinuousServiceDate,
                "DateOfBirth": DateOfBirth,
                "LastWorkingDate": LastWorkingDate,
                "Gender": Gender,
                "Ethnicity": Ethnicity,
                "Nationality": Nationality,
                "Religion": Religion,
                "LeaverReason": LeaverReason,
                "MaritalStatus": MaritalStatus,
                "Phones": Phones,
                "Emails": Emails,
                "Addresses": Addresses,
                "GenderIdentity": GenderIdentity,
                "WindowsUsername": WindowsUsername,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DisplayId"]) -> MetaOapg.properties.DisplayId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TitleHonorific"]) -> MetaOapg.properties.TitleHonorific: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FirstName"]) -> MetaOapg.properties.FirstName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["KnownAs"]) -> MetaOapg.properties.KnownAs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OtherName"]) -> MetaOapg.properties.OtherName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LastName"]) -> MetaOapg.properties.LastName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CostCentre"]) -> MetaOapg.properties.CostCentre: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["WorkingStatus"]) -> MetaOapg.properties.WorkingStatus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["IsManager"]) -> MetaOapg.properties.IsManager: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["NationalInsuranceNumber"]) -> MetaOapg.properties.NationalInsuranceNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PayrollId"]) -> MetaOapg.properties.PayrollId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TaxCode"]) -> MetaOapg.properties.TaxCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["IncludeInPayroll"]) -> MetaOapg.properties.IncludeInPayroll: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EmploymentStartDate"]) -> MetaOapg.properties.EmploymentStartDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EmploymentLeftDate"]) -> MetaOapg.properties.EmploymentLeftDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ContinuousServiceDate"]) -> MetaOapg.properties.ContinuousServiceDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DateOfBirth"]) -> MetaOapg.properties.DateOfBirth: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LastWorkingDate"]) -> MetaOapg.properties.LastWorkingDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Gender"]) -> MetaOapg.properties.Gender: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Ethnicity"]) -> MetaOapg.properties.Ethnicity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Nationality"]) -> MetaOapg.properties.Nationality: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Religion"]) -> MetaOapg.properties.Religion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LeaverReason"]) -> MetaOapg.properties.LeaverReason: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["MaritalStatus"]) -> MetaOapg.properties.MaritalStatus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Phones"]) -> MetaOapg.properties.Phones: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Emails"]) -> MetaOapg.properties.Emails: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Addresses"]) -> MetaOapg.properties.Addresses: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["GenderIdentity"]) -> MetaOapg.properties.GenderIdentity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["WindowsUsername"]) -> MetaOapg.properties.WindowsUsername: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["DisplayId", "TitleHonorific", "FirstName", "KnownAs", "OtherName", "LastName", "CostCentre", "WorkingStatus", "IsManager", "NationalInsuranceNumber", "PayrollId", "TaxCode", "IncludeInPayroll", "EmploymentStartDate", "EmploymentLeftDate", "ContinuousServiceDate", "DateOfBirth", "LastWorkingDate", "Gender", "Ethnicity", "Nationality", "Religion", "LeaverReason", "MaritalStatus", "Phones", "Emails", "Addresses", "GenderIdentity", "WindowsUsername", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DisplayId"]) -> typing.Union[MetaOapg.properties.DisplayId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TitleHonorific"]) -> typing.Union[MetaOapg.properties.TitleHonorific, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FirstName"]) -> typing.Union[MetaOapg.properties.FirstName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["KnownAs"]) -> typing.Union[MetaOapg.properties.KnownAs, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OtherName"]) -> typing.Union[MetaOapg.properties.OtherName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LastName"]) -> typing.Union[MetaOapg.properties.LastName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CostCentre"]) -> typing.Union[MetaOapg.properties.CostCentre, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["WorkingStatus"]) -> typing.Union[MetaOapg.properties.WorkingStatus, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["IsManager"]) -> typing.Union[MetaOapg.properties.IsManager, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["NationalInsuranceNumber"]) -> typing.Union[MetaOapg.properties.NationalInsuranceNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PayrollId"]) -> typing.Union[MetaOapg.properties.PayrollId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TaxCode"]) -> typing.Union[MetaOapg.properties.TaxCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["IncludeInPayroll"]) -> typing.Union[MetaOapg.properties.IncludeInPayroll, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EmploymentStartDate"]) -> typing.Union[MetaOapg.properties.EmploymentStartDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EmploymentLeftDate"]) -> typing.Union[MetaOapg.properties.EmploymentLeftDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ContinuousServiceDate"]) -> typing.Union[MetaOapg.properties.ContinuousServiceDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DateOfBirth"]) -> typing.Union[MetaOapg.properties.DateOfBirth, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LastWorkingDate"]) -> typing.Union[MetaOapg.properties.LastWorkingDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Gender"]) -> typing.Union[MetaOapg.properties.Gender, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Ethnicity"]) -> typing.Union[MetaOapg.properties.Ethnicity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Nationality"]) -> typing.Union[MetaOapg.properties.Nationality, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Religion"]) -> typing.Union[MetaOapg.properties.Religion, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LeaverReason"]) -> typing.Union[MetaOapg.properties.LeaverReason, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["MaritalStatus"]) -> typing.Union[MetaOapg.properties.MaritalStatus, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Phones"]) -> typing.Union[MetaOapg.properties.Phones, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Emails"]) -> typing.Union[MetaOapg.properties.Emails, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Addresses"]) -> typing.Union[MetaOapg.properties.Addresses, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["GenderIdentity"]) -> typing.Union[MetaOapg.properties.GenderIdentity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["WindowsUsername"]) -> typing.Union[MetaOapg.properties.WindowsUsername, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["DisplayId", "TitleHonorific", "FirstName", "KnownAs", "OtherName", "LastName", "CostCentre", "WorkingStatus", "IsManager", "NationalInsuranceNumber", "PayrollId", "TaxCode", "IncludeInPayroll", "EmploymentStartDate", "EmploymentLeftDate", "ContinuousServiceDate", "DateOfBirth", "LastWorkingDate", "Gender", "Ethnicity", "Nationality", "Religion", "LeaverReason", "MaritalStatus", "Phones", "Emails", "Addresses", "GenderIdentity", "WindowsUsername", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        DisplayId: typing.Union[MetaOapg.properties.DisplayId, None, str, schemas.Unset] = schemas.unset,
        TitleHonorific: typing.Union[MetaOapg.properties.TitleHonorific, None, str, schemas.Unset] = schemas.unset,
        FirstName: typing.Union[MetaOapg.properties.FirstName, None, str, schemas.Unset] = schemas.unset,
        KnownAs: typing.Union[MetaOapg.properties.KnownAs, None, str, schemas.Unset] = schemas.unset,
        OtherName: typing.Union[MetaOapg.properties.OtherName, None, str, schemas.Unset] = schemas.unset,
        LastName: typing.Union[MetaOapg.properties.LastName, None, str, schemas.Unset] = schemas.unset,
        CostCentre: typing.Union[MetaOapg.properties.CostCentre, None, str, schemas.Unset] = schemas.unset,
        WorkingStatus: typing.Union[MetaOapg.properties.WorkingStatus, None, str, schemas.Unset] = schemas.unset,
        IsManager: typing.Union[MetaOapg.properties.IsManager, None, bool, schemas.Unset] = schemas.unset,
        NationalInsuranceNumber: typing.Union[MetaOapg.properties.NationalInsuranceNumber, None, str, schemas.Unset] = schemas.unset,
        PayrollId: typing.Union[MetaOapg.properties.PayrollId, None, str, schemas.Unset] = schemas.unset,
        TaxCode: typing.Union[MetaOapg.properties.TaxCode, None, str, schemas.Unset] = schemas.unset,
        IncludeInPayroll: typing.Union[MetaOapg.properties.IncludeInPayroll, None, bool, schemas.Unset] = schemas.unset,
        EmploymentStartDate: typing.Union[MetaOapg.properties.EmploymentStartDate, None, str, datetime, schemas.Unset] = schemas.unset,
        EmploymentLeftDate: typing.Union[MetaOapg.properties.EmploymentLeftDate, None, str, datetime, schemas.Unset] = schemas.unset,
        ContinuousServiceDate: typing.Union[MetaOapg.properties.ContinuousServiceDate, None, str, datetime, schemas.Unset] = schemas.unset,
        DateOfBirth: typing.Union[MetaOapg.properties.DateOfBirth, None, str, datetime, schemas.Unset] = schemas.unset,
        LastWorkingDate: typing.Union[MetaOapg.properties.LastWorkingDate, None, str, datetime, schemas.Unset] = schemas.unset,
        Gender: typing.Union[MetaOapg.properties.Gender, None, str, schemas.Unset] = schemas.unset,
        Ethnicity: typing.Union[MetaOapg.properties.Ethnicity, None, str, schemas.Unset] = schemas.unset,
        Nationality: typing.Union[MetaOapg.properties.Nationality, None, str, schemas.Unset] = schemas.unset,
        Religion: typing.Union[MetaOapg.properties.Religion, None, str, schemas.Unset] = schemas.unset,
        LeaverReason: typing.Union[MetaOapg.properties.LeaverReason, None, str, schemas.Unset] = schemas.unset,
        MaritalStatus: typing.Union[MetaOapg.properties.MaritalStatus, None, str, schemas.Unset] = schemas.unset,
        Phones: typing.Union[MetaOapg.properties.Phones, list, tuple, None, schemas.Unset] = schemas.unset,
        Emails: typing.Union[MetaOapg.properties.Emails, list, tuple, None, schemas.Unset] = schemas.unset,
        Addresses: typing.Union[MetaOapg.properties.Addresses, list, tuple, None, schemas.Unset] = schemas.unset,
        GenderIdentity: typing.Union[MetaOapg.properties.GenderIdentity, None, str, schemas.Unset] = schemas.unset,
        WindowsUsername: typing.Union[MetaOapg.properties.WindowsUsername, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateEmployeeCommand':
        return super().__new__(
            cls,
            *args,
            DisplayId=DisplayId,
            TitleHonorific=TitleHonorific,
            FirstName=FirstName,
            KnownAs=KnownAs,
            OtherName=OtherName,
            LastName=LastName,
            CostCentre=CostCentre,
            WorkingStatus=WorkingStatus,
            IsManager=IsManager,
            NationalInsuranceNumber=NationalInsuranceNumber,
            PayrollId=PayrollId,
            TaxCode=TaxCode,
            IncludeInPayroll=IncludeInPayroll,
            EmploymentStartDate=EmploymentStartDate,
            EmploymentLeftDate=EmploymentLeftDate,
            ContinuousServiceDate=ContinuousServiceDate,
            DateOfBirth=DateOfBirth,
            LastWorkingDate=LastWorkingDate,
            Gender=Gender,
            Ethnicity=Ethnicity,
            Nationality=Nationality,
            Religion=Religion,
            LeaverReason=LeaverReason,
            MaritalStatus=MaritalStatus,
            Phones=Phones,
            Emails=Emails,
            Addresses=Addresses,
            GenderIdentity=GenderIdentity,
            WindowsUsername=WindowsUsername,
            _configuration=_configuration,
            **kwargs,
        )

from iris_software_group_cascade_python_sdk.model.address import Address
from iris_software_group_cascade_python_sdk.model.email import Email
from iris_software_group_cascade_python_sdk.model.phone import Phone
