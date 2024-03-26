operation_parameter_map = {
    '/attendance/absencedays-POST': {
        'parameters': [
            {
                'name': 'AbsenceId'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'Date'
            },
            {
                'name': 'DurationDays'
            },
            {
                'name': 'DurationMinutes'
            },
            {
                'name': 'DayPart'
            },
        ]
    },
    '/attendance/absencedays/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/attendance/absencedays/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/attendance/absencedays-GET': {
        'parameters': [
            {
                'name': '$top'
            },
            {
                'name': '$skip'
            },
            {
                'name': '$filter'
            },
            {
                'name': '$select'
            },
            {
                'name': '$orderby'
            },
            {
                'name': '$count'
            },
        ]
    },
    '/attendance/absencedays/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'Date'
            },
            {
                'name': 'DurationDays'
            },
            {
                'name': 'DurationMinutes'
            },
            {
                'name': 'DayPart'
            },
            {
                'name': 'Id'
            },
        ]
    },
    '/attendance/absencereasons/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/attendance/absencereasons/{id}/employees/{employeeId}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'employeeId'
            },
        ]
    },
    '/attendance/absencereasons-GET': {
        'parameters': [
            {
                'name': '$top'
            },
            {
                'name': '$skip'
            },
            {
                'name': '$filter'
            },
            {
                'name': '$select'
            },
            {
                'name': '$orderby'
            },
            {
                'name': '$count'
            },
        ]
    },
    '/attendance/absences-POST': {
        'parameters': [
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'AbsenceReasonId'
            },
            {
                'name': 'Narrative'
            },
            {
                'name': 'StartDate'
            },
            {
                'name': 'EndDate'
            },
        ]
    },
    '/attendance/absences/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/attendance/absences/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/attendance/absences-GET': {
        'parameters': [
            {
                'name': '$top'
            },
            {
                'name': '$skip'
            },
            {
                'name': '$filter'
            },
            {
                'name': '$select'
            },
            {
                'name': '$orderby'
            },
            {
                'name': '$count'
            },
        ]
    },
    '/attendance/absences/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'Narrative'
            },
            {
                'name': 'StartDate'
            },
            {
                'name': 'EndDate'
            },
            {
                'name': 'Id'
            },
        ]
    },
    '/bankdetails-POST': {
        'parameters': [
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'BankName'
            },
            {
                'name': 'BankAddress'
            },
            {
                'name': 'AccountName'
            },
            {
                'name': 'AccountNumber'
            },
            {
                'name': 'SortCode'
            },
            {
                'name': 'RollNumber'
            },
        ]
    },
    '/bankdetails/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/bankdetails-GET': {
        'parameters': [
            {
                'name': '$top'
            },
            {
                'name': '$skip'
            },
            {
                'name': '$filter'
            },
            {
                'name': '$select'
            },
            {
                'name': '$orderby'
            },
            {
                'name': '$count'
            },
        ]
    },
    '/bankdetails/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'BankName'
            },
            {
                'name': 'BankAddress'
            },
            {
                'name': 'AccountName'
            },
            {
                'name': 'AccountNumber'
            },
            {
                'name': 'SortCode'
            },
            {
                'name': 'RollNumber'
            },
            {
                'name': 'Id'
            },
        ]
    },
    '/benefits/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/benefits-GET': {
        'parameters': [
            {
                'name': '$top'
            },
            {
                'name': '$skip'
            },
            {
                'name': '$filter'
            },
            {
                'name': '$select'
            },
            {
                'name': '$orderby'
            },
            {
                'name': '$count'
            },
        ]
    },
    '/employees-POST': {
        'parameters': [
            {
                'name': 'DisplayId'
            },
            {
                'name': 'TitleHonorific'
            },
            {
                'name': 'FirstName'
            },
            {
                'name': 'KnownAs'
            },
            {
                'name': 'OtherName'
            },
            {
                'name': 'LastName'
            },
            {
                'name': 'CostCentre'
            },
            {
                'name': 'WorkingStatus'
            },
            {
                'name': 'IsManager'
            },
            {
                'name': 'NationalInsuranceNumber'
            },
            {
                'name': 'PayrollId'
            },
            {
                'name': 'TaxCode'
            },
            {
                'name': 'IncludeInPayroll'
            },
            {
                'name': 'EmploymentStartDate'
            },
            {
                'name': 'EmploymentLeftDate'
            },
            {
                'name': 'ContinuousServiceDate'
            },
            {
                'name': 'DateOfBirth'
            },
            {
                'name': 'LastWorkingDate'
            },
            {
                'name': 'Gender'
            },
            {
                'name': 'Ethnicity'
            },
            {
                'name': 'Nationality'
            },
            {
                'name': 'Religion'
            },
            {
                'name': 'LeaverReason'
            },
            {
                'name': 'MaritalStatus'
            },
            {
                'name': 'Phones'
            },
            {
                'name': 'Emails'
            },
            {
                'name': 'Addresses'
            },
            {
                'name': 'GenderIdentity'
            },
            {
                'name': 'WindowsUsername'
            },
        ]
    },
    '/employees/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/employees-GET': {
        'parameters': [
            {
                'name': '$top'
            },
            {
                'name': '$skip'
            },
            {
                'name': '$filter'
            },
            {
                'name': '$select'
            },
            {
                'name': '$orderby'
            },
            {
                'name': '$count'
            },
        ]
    },
    '/employees/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'DisplayId'
            },
            {
                'name': 'TitleHonorific'
            },
            {
                'name': 'FirstName'
            },
            {
                'name': 'KnownAs'
            },
            {
                'name': 'OtherName'
            },
            {
                'name': 'LastName'
            },
            {
                'name': 'CostCentre'
            },
            {
                'name': 'WorkingStatus'
            },
            {
                'name': 'IsManager'
            },
            {
                'name': 'NationalInsuranceNumber'
            },
            {
                'name': 'PayrollId'
            },
            {
                'name': 'TaxCode'
            },
            {
                'name': 'IncludeInPayroll'
            },
            {
                'name': 'EmploymentStartDate'
            },
            {
                'name': 'EmploymentLeftDate'
            },
            {
                'name': 'ContinuousServiceDate'
            },
            {
                'name': 'DateOfBirth'
            },
            {
                'name': 'LastWorkingDate'
            },
            {
                'name': 'Gender'
            },
            {
                'name': 'Ethnicity'
            },
            {
                'name': 'Nationality'
            },
            {
                'name': 'Religion'
            },
            {
                'name': 'LeaverReason'
            },
            {
                'name': 'MaritalStatus'
            },
            {
                'name': 'Phones'
            },
            {
                'name': 'Emails'
            },
            {
                'name': 'Addresses'
            },
            {
                'name': 'GenderIdentity'
            },
            {
                'name': 'WindowsUsername'
            },
            {
                'name': 'Id'
            },
        ]
    },
    '/attendance/entitlements/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/attendance/entitlements-GET': {
        'parameters': [
            {
                'name': '$top'
            },
            {
                'name': '$skip'
            },
            {
                'name': '$filter'
            },
            {
                'name': '$select'
            },
            {
                'name': '$orderby'
            },
            {
                'name': '$count'
            },
        ]
    },
    '/hierarchy-GET': {
        'parameters': [
            {
                'name': '$top'
            },
            {
                'name': '$skip'
            },
            {
                'name': '$filter'
            },
            {
                'name': '$select'
            },
            {
                'name': '$orderby'
            },
            {
                'name': '$count'
            },
        ]
    },
    '/hierarchy/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/hierarchy/{id}/path-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/jobs-POST': {
        'parameters': [
            {
                'name': 'JobTitle'
            },
            {
                'name': 'Classification'
            },
            {
                'name': 'StartDate'
            },
            {
                'name': 'EndDate'
            },
            {
                'name': 'WorkingCalendar'
            },
            {
                'name': 'LineManagerId'
            },
            {
                'name': 'HierarchyNodeId'
            },
            {
                'name': 'Active'
            },
            {
                'name': 'Salary'
            },
            {
                'name': 'EmployeeId'
            },
            {
                'name': 'Contract'
            },
            {
                'name': 'PayFrequency'
            },
            {
                'name': 'PayBasis'
            },
            {
                'name': 'FullTimeEquivalent'
            },
            {
                'name': 'ChangeReason'
            },
            {
                'name': 'NextIncrementDate'
            },
            {
                'name': 'TimesheetLocation'
            },
            {
                'name': 'TimesheetLunchDuration'
            },
            {
                'name': 'ExpenseSubmissionFrequency'
            },
            {
                'name': 'CostCentre'
            },
            {
                'name': 'JobFamily'
            },
            {
                'name': 'ApprenticeUnder25'
            },
            {
                'name': 'ApprenticeshipEndDate'
            },
            {
                'name': 'ContractEndDate'
            },
            {
                'name': 'NormalHours'
            },
            {
                'name': 'RealTimeInformationIrregularFrequency'
            },
            {
                'name': 'NoticePeriod'
            },
        ]
    },
    '/jobs/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/jobs-GET': {
        'parameters': [
            {
                'name': '$top'
            },
            {
                'name': '$skip'
            },
            {
                'name': '$filter'
            },
            {
                'name': '$select'
            },
            {
                'name': '$orderby'
            },
            {
                'name': '$count'
            },
        ]
    },
    '/jobs/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'JobTitle'
            },
            {
                'name': 'Classification'
            },
            {
                'name': 'StartDate'
            },
            {
                'name': 'EndDate'
            },
            {
                'name': 'WorkingCalendar'
            },
            {
                'name': 'LineManagerId'
            },
            {
                'name': 'HierarchyNodeId'
            },
            {
                'name': 'Active'
            },
            {
                'name': 'Salary'
            },
            {
                'name': 'Contract'
            },
            {
                'name': 'PayFrequency'
            },
            {
                'name': 'PayBasis'
            },
            {
                'name': 'FullTimeEquivalent'
            },
            {
                'name': 'ChangeReason'
            },
            {
                'name': 'NextIncrementDate'
            },
            {
                'name': 'TimesheetLocation'
            },
            {
                'name': 'TimesheetLunchDuration'
            },
            {
                'name': 'ExpenseSubmissionFrequency'
            },
            {
                'name': 'CostCentre'
            },
            {
                'name': 'JobFamily'
            },
            {
                'name': 'ApprenticeUnder25'
            },
            {
                'name': 'ApprenticeshipEndDate'
            },
            {
                'name': 'ContractEndDate'
            },
            {
                'name': 'NormalHours'
            },
            {
                'name': 'RealTimeInformationIrregularFrequency'
            },
            {
                'name': 'NoticePeriod'
            },
            {
                'name': 'Id'
            },
        ]
    },
    '/publicholidays/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/publicholidays-GET': {
        'parameters': [
            {
                'name': '$top'
            },
            {
                'name': '$skip'
            },
            {
                'name': '$filter'
            },
            {
                'name': '$select'
            },
            {
                'name': '$orderby'
            },
            {
                'name': '$count'
            },
        ]
    },
};