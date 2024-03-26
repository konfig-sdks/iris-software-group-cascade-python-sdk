# coding: utf-8

"""
    HR API

    <a href='swaggerv2.json'>Download Swagger Json in OAS2 Format.</a>

    The version of the OpenAPI document: 2
    Contact: hrapi@iris.co.uk
    Created by: https://help.iris.co.uk/hr/cascade/api/
"""

from iris_software_group_cascade_python_sdk.paths.attendance_absences.post import CreateNewAbsence
from iris_software_group_cascade_python_sdk.paths.attendance_absences_id.delete import DeleteById
from iris_software_group_cascade_python_sdk.paths.attendance_absences_id.get import GetById
from iris_software_group_cascade_python_sdk.paths.attendance_absences.get import GetList
from iris_software_group_cascade_python_sdk.paths.attendance_absences_id.put import UpdateById
from iris_software_group_cascade_python_sdk.apis.tags.absences_api_raw import AbsencesApiRaw


class AbsencesApi(
    CreateNewAbsence,
    DeleteById,
    GetById,
    GetList,
    UpdateById,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: AbsencesApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = AbsencesApiRaw(api_client)
