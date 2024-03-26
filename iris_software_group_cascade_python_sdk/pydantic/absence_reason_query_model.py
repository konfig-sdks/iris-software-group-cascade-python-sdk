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

from iris_software_group_cascade_python_sdk.pydantic.absence_reason_model import AbsenceReasonModel

class AbsenceReasonQueryModel(BaseModel):
    o_data_context: typing.Optional[typing.Optional[str]] = Field(None, alias='ODataContext')

    o_data_count: typing.Optional[typing.Optional[int]] = Field(None, alias='ODataCount')

    o_data_next_link: typing.Optional[typing.Optional[str]] = Field(None, alias='ODataNextLink')

    value: typing.Optional[typing.Optional[typing.List[AbsenceReasonModel]]] = Field(None, alias='Value')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
