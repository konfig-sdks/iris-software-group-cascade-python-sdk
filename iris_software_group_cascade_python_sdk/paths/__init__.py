# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from iris_software_group_cascade_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    EMPLOYEES = "/employees"
    EMPLOYEES_ID = "/employees/{id}"
    JOBS = "/jobs"
    JOBS_ID = "/jobs/{id}"
    HIERARCHY = "/hierarchy"
    HIERARCHY_ID = "/hierarchy/{id}"
    HIERARCHY_ID_PATH = "/hierarchy/{id}/path"
    BANKDETAILS = "/bankdetails"
    BANKDETAILS_ID = "/bankdetails/{id}"
    ATTENDANCE_ABSENCEREASONS = "/attendance/absencereasons"
    ATTENDANCE_ABSENCEREASONS_ID = "/attendance/absencereasons/{id}"
    ATTENDANCE_ABSENCEREASONS_ID_EMPLOYEES_EMPLOYEE_ID = "/attendance/absencereasons/{id}/employees/{employeeId}"
    ATTENDANCE_ENTITLEMENTS = "/attendance/entitlements"
    ATTENDANCE_ENTITLEMENTS_ID = "/attendance/entitlements/{id}"
    ATTENDANCE_ABSENCES = "/attendance/absences"
    ATTENDANCE_ABSENCES_ID = "/attendance/absences/{id}"
    ATTENDANCE_ABSENCEDAYS = "/attendance/absencedays"
    ATTENDANCE_ABSENCEDAYS_ID = "/attendance/absencedays/{id}"
    BENEFITS = "/benefits"
    BENEFITS_ID = "/benefits/{id}"
    PUBLICHOLIDAYS = "/publicholidays"
    PUBLICHOLIDAYS_ID = "/publicholidays/{id}"
