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


class HierarchyNodeModel(BaseModel):
    # The Parent ID of this Hierarchy node. <br />  Must exist in the Hierarchy Service.
    parent_id: typing.Optional[typing.Optional[str]] = Field(None, alias='ParentId')

    # The Level of the Hierarchy node. <br />  Cascade Source: [ValidHierarchyX].[level]
    level: typing.Optional[int] = Field(None, alias='Level')

    # The Title of this Hierarchy node. <br />  Cascade Source: [ValidHierarchyX].[name]
    title: typing.Optional[typing.Optional[str]] = Field(None, alias='Title')

    # Hierarchy node is disabled. <br />  Cascade Source: [ValidHierarchyX].[disabled]
    disabled: typing.Optional[bool] = Field(None, alias='Disabled')

    # Source HR System Id. <br />  Cascade Source: [ValidHierarchyX].[HierarchyNode] <br />  Read Only
    source_system_id: typing.Optional[typing.Optional[str]] = Field(None, alias='SourceSystemId')

    # The date when the Hierarchy node record was created in the Source HR System. <br />  Cascade Source: [ValidHierarchyX].[createdon]
    source_system_created_on: typing.Optional[typing.Optional[datetime]] = Field(None, alias='SourceSystemCreatedOn')

    # The date when the Hierarchy node record was created or last updated in the Source HR System. <br />  Cascade Source: [ValidHierarchyX].[disabledon] if exists else [ValidHierachyX].[createdon]
    source_system_last_modified_on: typing.Optional[typing.Optional[datetime]] = Field(None, alias='SourceSystemLastModifiedOn')

    # This ID of the Hierarchy node. <br />  This field is generated by Iris HR platform and not related to the Cascade ID.
    id: typing.Optional[typing.Optional[str]] = Field(None, alias='Id')

    # The date time when the Hierarchy node was created in the Iris HR platform.
    created_on: typing.Optional[datetime] = Field(None, alias='CreatedOn')

    # Not used as the Iris HR platform has no concept of users at the moment.
    created_by: typing.Optional[typing.Optional[str]] = Field(None, alias='CreatedBy')

    # The date time when the Hierarchy node was created or last updated.
    last_modified_on: typing.Optional[typing.Optional[datetime]] = Field(None, alias='LastModifiedOn')

    # Not used as the Iris HR platform has no concept of users at the moment.
    last_modified_by: typing.Optional[typing.Optional[str]] = Field(None, alias='LastModifiedBy')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )