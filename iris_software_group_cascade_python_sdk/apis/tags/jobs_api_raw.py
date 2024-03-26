# coding: utf-8

"""
    HR API

    <a href='swaggerv2.json'>Download Swagger Json in OAS2 Format.</a>

    The version of the OpenAPI document: 2
    Contact: hrapi@iris.co.uk
    Created by: https://help.iris.co.uk/hr/cascade/api/
"""

from iris_software_group_cascade_python_sdk.paths.jobs.post import CreateNewJobRaw
from iris_software_group_cascade_python_sdk.paths.jobs_id.get import GetByIdRaw
from iris_software_group_cascade_python_sdk.paths.jobs.get import GetListRaw
from iris_software_group_cascade_python_sdk.paths.jobs_id.put import UpdateByIdRaw


class JobsApiRaw(
    CreateNewJobRaw,
    GetByIdRaw,
    GetListRaw,
    UpdateByIdRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass