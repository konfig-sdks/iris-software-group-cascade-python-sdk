import typing_extensions

from iris_software_group_cascade_python_sdk.paths import PathValues
from iris_software_group_cascade_python_sdk.apis.paths.employees import Employees
from iris_software_group_cascade_python_sdk.apis.paths.employees_id import EmployeesId
from iris_software_group_cascade_python_sdk.apis.paths.jobs import Jobs
from iris_software_group_cascade_python_sdk.apis.paths.jobs_id import JobsId
from iris_software_group_cascade_python_sdk.apis.paths.hierarchy import Hierarchy
from iris_software_group_cascade_python_sdk.apis.paths.hierarchy_id import HierarchyId
from iris_software_group_cascade_python_sdk.apis.paths.hierarchy_id_path import HierarchyIdPath
from iris_software_group_cascade_python_sdk.apis.paths.bankdetails import Bankdetails
from iris_software_group_cascade_python_sdk.apis.paths.bankdetails_id import BankdetailsId
from iris_software_group_cascade_python_sdk.apis.paths.attendance_absencereasons import AttendanceAbsencereasons
from iris_software_group_cascade_python_sdk.apis.paths.attendance_absencereasons_id import AttendanceAbsencereasonsId
from iris_software_group_cascade_python_sdk.apis.paths.attendance_absencereasons_id_employees_employee_id import AttendanceAbsencereasonsIdEmployeesEmployeeId
from iris_software_group_cascade_python_sdk.apis.paths.attendance_entitlements import AttendanceEntitlements
from iris_software_group_cascade_python_sdk.apis.paths.attendance_entitlements_id import AttendanceEntitlementsId
from iris_software_group_cascade_python_sdk.apis.paths.attendance_absences import AttendanceAbsences
from iris_software_group_cascade_python_sdk.apis.paths.attendance_absences_id import AttendanceAbsencesId
from iris_software_group_cascade_python_sdk.apis.paths.attendance_absencedays import AttendanceAbsencedays
from iris_software_group_cascade_python_sdk.apis.paths.attendance_absencedays_id import AttendanceAbsencedaysId
from iris_software_group_cascade_python_sdk.apis.paths.benefits import Benefits
from iris_software_group_cascade_python_sdk.apis.paths.benefits_id import BenefitsId
from iris_software_group_cascade_python_sdk.apis.paths.publicholidays import Publicholidays
from iris_software_group_cascade_python_sdk.apis.paths.publicholidays_id import PublicholidaysId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.EMPLOYEES: Employees,
        PathValues.EMPLOYEES_ID: EmployeesId,
        PathValues.JOBS: Jobs,
        PathValues.JOBS_ID: JobsId,
        PathValues.HIERARCHY: Hierarchy,
        PathValues.HIERARCHY_ID: HierarchyId,
        PathValues.HIERARCHY_ID_PATH: HierarchyIdPath,
        PathValues.BANKDETAILS: Bankdetails,
        PathValues.BANKDETAILS_ID: BankdetailsId,
        PathValues.ATTENDANCE_ABSENCEREASONS: AttendanceAbsencereasons,
        PathValues.ATTENDANCE_ABSENCEREASONS_ID: AttendanceAbsencereasonsId,
        PathValues.ATTENDANCE_ABSENCEREASONS_ID_EMPLOYEES_EMPLOYEE_ID: AttendanceAbsencereasonsIdEmployeesEmployeeId,
        PathValues.ATTENDANCE_ENTITLEMENTS: AttendanceEntitlements,
        PathValues.ATTENDANCE_ENTITLEMENTS_ID: AttendanceEntitlementsId,
        PathValues.ATTENDANCE_ABSENCES: AttendanceAbsences,
        PathValues.ATTENDANCE_ABSENCES_ID: AttendanceAbsencesId,
        PathValues.ATTENDANCE_ABSENCEDAYS: AttendanceAbsencedays,
        PathValues.ATTENDANCE_ABSENCEDAYS_ID: AttendanceAbsencedaysId,
        PathValues.BENEFITS: Benefits,
        PathValues.BENEFITS_ID: BenefitsId,
        PathValues.PUBLICHOLIDAYS: Publicholidays,
        PathValues.PUBLICHOLIDAYS_ID: PublicholidaysId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.EMPLOYEES: Employees,
        PathValues.EMPLOYEES_ID: EmployeesId,
        PathValues.JOBS: Jobs,
        PathValues.JOBS_ID: JobsId,
        PathValues.HIERARCHY: Hierarchy,
        PathValues.HIERARCHY_ID: HierarchyId,
        PathValues.HIERARCHY_ID_PATH: HierarchyIdPath,
        PathValues.BANKDETAILS: Bankdetails,
        PathValues.BANKDETAILS_ID: BankdetailsId,
        PathValues.ATTENDANCE_ABSENCEREASONS: AttendanceAbsencereasons,
        PathValues.ATTENDANCE_ABSENCEREASONS_ID: AttendanceAbsencereasonsId,
        PathValues.ATTENDANCE_ABSENCEREASONS_ID_EMPLOYEES_EMPLOYEE_ID: AttendanceAbsencereasonsIdEmployeesEmployeeId,
        PathValues.ATTENDANCE_ENTITLEMENTS: AttendanceEntitlements,
        PathValues.ATTENDANCE_ENTITLEMENTS_ID: AttendanceEntitlementsId,
        PathValues.ATTENDANCE_ABSENCES: AttendanceAbsences,
        PathValues.ATTENDANCE_ABSENCES_ID: AttendanceAbsencesId,
        PathValues.ATTENDANCE_ABSENCEDAYS: AttendanceAbsencedays,
        PathValues.ATTENDANCE_ABSENCEDAYS_ID: AttendanceAbsencedaysId,
        PathValues.BENEFITS: Benefits,
        PathValues.BENEFITS_ID: BenefitsId,
        PathValues.PUBLICHOLIDAYS: Publicholidays,
        PathValues.PUBLICHOLIDAYS_ID: PublicholidaysId,
    }
)
