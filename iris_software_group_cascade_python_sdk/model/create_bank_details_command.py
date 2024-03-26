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


class CreateBankDetailsCommand(
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
            
            
            class BankName(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 50
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'BankName':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def BankAddress() -> typing.Type['BankAddress']:
                return BankAddress
            
            
            class AccountName(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 50
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'AccountName':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class AccountNumber(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 50
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'AccountNumber':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class SortCode(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 50
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'SortCode':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class RollNumber(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 50
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'RollNumber':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "EmployeeId": EmployeeId,
                "BankName": BankName,
                "BankAddress": BankAddress,
                "AccountName": AccountName,
                "AccountNumber": AccountNumber,
                "SortCode": SortCode,
                "RollNumber": RollNumber,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EmployeeId"]) -> MetaOapg.properties.EmployeeId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["BankName"]) -> MetaOapg.properties.BankName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["BankAddress"]) -> 'BankAddress': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AccountName"]) -> MetaOapg.properties.AccountName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AccountNumber"]) -> MetaOapg.properties.AccountNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SortCode"]) -> MetaOapg.properties.SortCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["RollNumber"]) -> MetaOapg.properties.RollNumber: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["EmployeeId", "BankName", "BankAddress", "AccountName", "AccountNumber", "SortCode", "RollNumber", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EmployeeId"]) -> typing.Union[MetaOapg.properties.EmployeeId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["BankName"]) -> typing.Union[MetaOapg.properties.BankName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["BankAddress"]) -> typing.Union['BankAddress', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AccountName"]) -> typing.Union[MetaOapg.properties.AccountName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AccountNumber"]) -> typing.Union[MetaOapg.properties.AccountNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SortCode"]) -> typing.Union[MetaOapg.properties.SortCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["RollNumber"]) -> typing.Union[MetaOapg.properties.RollNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["EmployeeId", "BankName", "BankAddress", "AccountName", "AccountNumber", "SortCode", "RollNumber", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        EmployeeId: typing.Union[MetaOapg.properties.EmployeeId, None, str, schemas.Unset] = schemas.unset,
        BankName: typing.Union[MetaOapg.properties.BankName, None, str, schemas.Unset] = schemas.unset,
        BankAddress: typing.Union['BankAddress', schemas.Unset] = schemas.unset,
        AccountName: typing.Union[MetaOapg.properties.AccountName, None, str, schemas.Unset] = schemas.unset,
        AccountNumber: typing.Union[MetaOapg.properties.AccountNumber, None, str, schemas.Unset] = schemas.unset,
        SortCode: typing.Union[MetaOapg.properties.SortCode, None, str, schemas.Unset] = schemas.unset,
        RollNumber: typing.Union[MetaOapg.properties.RollNumber, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateBankDetailsCommand':
        return super().__new__(
            cls,
            *args,
            EmployeeId=EmployeeId,
            BankName=BankName,
            BankAddress=BankAddress,
            AccountName=AccountName,
            AccountNumber=AccountNumber,
            SortCode=SortCode,
            RollNumber=RollNumber,
            _configuration=_configuration,
            **kwargs,
        )

from iris_software_group_cascade_python_sdk.model.bank_address import BankAddress
