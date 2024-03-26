# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from iris_software_group_cascade_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    ABSENCES = "Absences"
    ABSENCE_DAYS = "AbsenceDays"
    EMPLOYEES = "Employees"
    JOBS = "Jobs"
    BANK_DETAILS = "BankDetails"
    HIERARCHY = "Hierarchy"
    ABSENCE_REASONS = "AbsenceReasons"
    ENTITLEMENTS = "Entitlements"
    BENEFITS = "Benefits"
    PUBLIC_HOLIDAYS = "PublicHolidays"
