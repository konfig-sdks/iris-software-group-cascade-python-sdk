import typing_extensions

from iris_software_group_cascade_python_sdk.apis.tags import TagValues
from iris_software_group_cascade_python_sdk.apis.tags.absences_api import AbsencesApi
from iris_software_group_cascade_python_sdk.apis.tags.absence_days_api import AbsenceDaysApi
from iris_software_group_cascade_python_sdk.apis.tags.employees_api import EmployeesApi
from iris_software_group_cascade_python_sdk.apis.tags.jobs_api import JobsApi
from iris_software_group_cascade_python_sdk.apis.tags.bank_details_api import BankDetailsApi
from iris_software_group_cascade_python_sdk.apis.tags.hierarchy_api import HierarchyApi
from iris_software_group_cascade_python_sdk.apis.tags.absence_reasons_api import AbsenceReasonsApi
from iris_software_group_cascade_python_sdk.apis.tags.entitlements_api import EntitlementsApi
from iris_software_group_cascade_python_sdk.apis.tags.benefits_api import BenefitsApi
from iris_software_group_cascade_python_sdk.apis.tags.public_holidays_api import PublicHolidaysApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ABSENCES: AbsencesApi,
        TagValues.ABSENCE_DAYS: AbsenceDaysApi,
        TagValues.EMPLOYEES: EmployeesApi,
        TagValues.JOBS: JobsApi,
        TagValues.BANK_DETAILS: BankDetailsApi,
        TagValues.HIERARCHY: HierarchyApi,
        TagValues.ABSENCE_REASONS: AbsenceReasonsApi,
        TagValues.ENTITLEMENTS: EntitlementsApi,
        TagValues.BENEFITS: BenefitsApi,
        TagValues.PUBLIC_HOLIDAYS: PublicHolidaysApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ABSENCES: AbsencesApi,
        TagValues.ABSENCE_DAYS: AbsenceDaysApi,
        TagValues.EMPLOYEES: EmployeesApi,
        TagValues.JOBS: JobsApi,
        TagValues.BANK_DETAILS: BankDetailsApi,
        TagValues.HIERARCHY: HierarchyApi,
        TagValues.ABSENCE_REASONS: AbsenceReasonsApi,
        TagValues.ENTITLEMENTS: EntitlementsApi,
        TagValues.BENEFITS: BenefitsApi,
        TagValues.PUBLIC_HOLIDAYS: PublicHolidaysApi,
    }
)
