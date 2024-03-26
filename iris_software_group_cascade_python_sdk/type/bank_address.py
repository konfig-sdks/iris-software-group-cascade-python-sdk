# coding: utf-8

"""
    HR API

    <a href='swaggerv2.json'>Download Swagger Json in OAS2 Format.</a>

    The version of the OpenAPI document: 2
    Contact: hrapi@iris.co.uk
    Created by: https://help.iris.co.uk/hr/cascade/api/
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


class RequiredBankAddress(TypedDict):
    pass

class OptionalBankAddress(TypedDict, total=False):
    # The first line of Bank Address <br />  Cascade Source: [EmployeeBank].[Address1]
    Address1: typing.Optional[str]

    # The second line of Bank Address <br />  Cascade Source: [EmployeeBank].[Address2]
    Address2: typing.Optional[str]

    # The third line of Bank Address <br />  Cascade Source: [EmployeeBank].[Address3]
    Address3: typing.Optional[str]

    # The fourth line of Bank Address <br />  Cascade Source: [EmployeeBank].[Address4]
    Address4: typing.Optional[str]

    # Post Code of the Bank <br />  Cascade Source: [EmployeeBank].[Postcode]
    PostCode: typing.Optional[str]

class BankAddress(RequiredBankAddress, OptionalBankAddress):
    pass
