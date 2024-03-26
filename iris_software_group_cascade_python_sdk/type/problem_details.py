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


class RequiredProblemDetails(TypedDict):
    pass

class OptionalProblemDetails(TypedDict, total=False):
    title: typing.Optional[str]

    type: typing.Optional[str]

    status: typing.Optional[int]

    detail: typing.Optional[str]

    instance: typing.Optional[str]

class ProblemDetails(RequiredProblemDetails, OptionalProblemDetails):
    pass
