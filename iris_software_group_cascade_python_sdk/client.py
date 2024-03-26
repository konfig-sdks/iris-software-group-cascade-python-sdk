# coding: utf-8
"""
    HR API

    <a href='swaggerv2.json'>Download Swagger Json in OAS2 Format.</a>

    The version of the OpenAPI document: 2
    Contact: hrapi@iris.co.uk
    Created by: https://help.iris.co.uk/hr/cascade/api/
"""

import typing
import inspect
from datetime import date, datetime
from iris_software_group_cascade_python_sdk.client_custom import ClientCustom
from iris_software_group_cascade_python_sdk.configuration import Configuration
from iris_software_group_cascade_python_sdk.api_client import ApiClient
from iris_software_group_cascade_python_sdk.type_util import copy_signature
from iris_software_group_cascade_python_sdk.apis.tags.absence_days_api import AbsenceDaysApi
from iris_software_group_cascade_python_sdk.apis.tags.absence_reasons_api import AbsenceReasonsApi
from iris_software_group_cascade_python_sdk.apis.tags.absences_api import AbsencesApi
from iris_software_group_cascade_python_sdk.apis.tags.bank_details_api import BankDetailsApi
from iris_software_group_cascade_python_sdk.apis.tags.benefits_api import BenefitsApi
from iris_software_group_cascade_python_sdk.apis.tags.employees_api import EmployeesApi
from iris_software_group_cascade_python_sdk.apis.tags.entitlements_api import EntitlementsApi
from iris_software_group_cascade_python_sdk.apis.tags.hierarchy_api import HierarchyApi
from iris_software_group_cascade_python_sdk.apis.tags.jobs_api import JobsApi
from iris_software_group_cascade_python_sdk.apis.tags.public_holidays_api import PublicHolidaysApi



class IrisSoftwareGroupCascade(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.absence_days: AbsenceDaysApi = AbsenceDaysApi(api_client)
        self.absence_reasons: AbsenceReasonsApi = AbsenceReasonsApi(api_client)
        self.absences: AbsencesApi = AbsencesApi(api_client)
        self.bank_details: BankDetailsApi = BankDetailsApi(api_client)
        self.benefits: BenefitsApi = BenefitsApi(api_client)
        self.employees: EmployeesApi = EmployeesApi(api_client)
        self.entitlements: EntitlementsApi = EntitlementsApi(api_client)
        self.hierarchy: HierarchyApi = HierarchyApi(api_client)
        self.jobs: JobsApi = JobsApi(api_client)
        self.public_holidays: PublicHolidaysApi = PublicHolidaysApi(api_client)
