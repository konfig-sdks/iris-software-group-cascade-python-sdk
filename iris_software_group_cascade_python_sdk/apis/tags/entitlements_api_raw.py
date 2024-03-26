# coding: utf-8

"""
    HR API

    <a href='swaggerv2.json'>Download Swagger Json in OAS2 Format.</a>

    The version of the OpenAPI document: 2
    Contact: hrapi@iris.co.uk
    Created by: https://help.iris.co.uk/hr/cascade/api/
"""

from iris_software_group_cascade_python_sdk.paths.attendance_entitlements_id.get import GetByIdRaw
from iris_software_group_cascade_python_sdk.paths.attendance_entitlements.get import GetListRaw


class EntitlementsApiRaw(
    GetByIdRaw,
    GetListRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass