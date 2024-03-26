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
from pydantic import BaseModel, Field, RootModel, ConfigDict


class ProblemDetails(BaseModel):
    title: typing.Optional[typing.Optional[str]] = Field(None, alias='title')

    type: typing.Optional[typing.Optional[str]] = Field(None, alias='type')

    status: typing.Optional[typing.Optional[int]] = Field(None, alias='status')

    detail: typing.Optional[typing.Optional[str]] = Field(None, alias='detail')

    instance: typing.Optional[typing.Optional[str]] = Field(None, alias='instance')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
