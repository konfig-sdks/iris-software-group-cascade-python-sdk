<div align="center">

[![Visit Iris software group](./header.png)](https://www.iris.co.uk&#x2F;products&#x2F;iris-cascade&#x2F;)

# Iris software group<a id="iris-software-group"></a>

<a href='swaggerv2.json'>Download Swagger Json in OAS2 Format.</a>


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`irissoftwaregroupcascade.absence_days.create_absence_day`](#irissoftwaregroupcascadeabsence_dayscreate_absence_day)
  * [`irissoftwaregroupcascade.absence_days.delete_by_id`](#irissoftwaregroupcascadeabsence_daysdelete_by_id)
  * [`irissoftwaregroupcascade.absence_days.get_by_id`](#irissoftwaregroupcascadeabsence_daysget_by_id)
  * [`irissoftwaregroupcascade.absence_days.get_list`](#irissoftwaregroupcascadeabsence_daysget_list)
  * [`irissoftwaregroupcascade.absence_days.update_absence_day`](#irissoftwaregroupcascadeabsence_daysupdate_absence_day)
  * [`irissoftwaregroupcascade.absence_reasons.get_by_id`](#irissoftwaregroupcascadeabsence_reasonsget_by_id)
  * [`irissoftwaregroupcascade.absence_reasons.get_employee_by_id`](#irissoftwaregroupcascadeabsence_reasonsget_employee_by_id)
  * [`irissoftwaregroupcascade.absence_reasons.list`](#irissoftwaregroupcascadeabsence_reasonslist)
  * [`irissoftwaregroupcascade.absences.create_new_absence`](#irissoftwaregroupcascadeabsencescreate_new_absence)
  * [`irissoftwaregroupcascade.absences.delete_by_id`](#irissoftwaregroupcascadeabsencesdelete_by_id)
  * [`irissoftwaregroupcascade.absences.get_by_id`](#irissoftwaregroupcascadeabsencesget_by_id)
  * [`irissoftwaregroupcascade.absences.get_list`](#irissoftwaregroupcascadeabsencesget_list)
  * [`irissoftwaregroupcascade.absences.update_by_id`](#irissoftwaregroupcascadeabsencesupdate_by_id)
  * [`irissoftwaregroupcascade.bank_details.create_bank_detail`](#irissoftwaregroupcascadebank_detailscreate_bank_detail)
  * [`irissoftwaregroupcascade.bank_details.get_by_id`](#irissoftwaregroupcascadebank_detailsget_by_id)
  * [`irissoftwaregroupcascade.bank_details.get_list`](#irissoftwaregroupcascadebank_detailsget_list)
  * [`irissoftwaregroupcascade.bank_details.update_bank_detail`](#irissoftwaregroupcascadebank_detailsupdate_bank_detail)
  * [`irissoftwaregroupcascade.benefits.get_by_id`](#irissoftwaregroupcascadebenefitsget_by_id)
  * [`irissoftwaregroupcascade.benefits.get_list`](#irissoftwaregroupcascadebenefitsget_list)
  * [`irissoftwaregroupcascade.employees.create_new_employee`](#irissoftwaregroupcascadeemployeescreate_new_employee)
  * [`irissoftwaregroupcascade.employees.get_by_id`](#irissoftwaregroupcascadeemployeesget_by_id)
  * [`irissoftwaregroupcascade.employees.get_list`](#irissoftwaregroupcascadeemployeesget_list)
  * [`irissoftwaregroupcascade.employees.update_by_id`](#irissoftwaregroupcascadeemployeesupdate_by_id)
  * [`irissoftwaregroupcascade.entitlements.get_by_id`](#irissoftwaregroupcascadeentitlementsget_by_id)
  * [`irissoftwaregroupcascade.entitlements.get_list`](#irissoftwaregroupcascadeentitlementsget_list)
  * [`irissoftwaregroupcascade.hierarchy.get_list`](#irissoftwaregroupcascadehierarchyget_list)
  * [`irissoftwaregroupcascade.hierarchy.get_node_by_id`](#irissoftwaregroupcascadehierarchyget_node_by_id)
  * [`irissoftwaregroupcascade.hierarchy.get_path_by_id`](#irissoftwaregroupcascadehierarchyget_path_by_id)
  * [`irissoftwaregroupcascade.jobs.create_new_job`](#irissoftwaregroupcascadejobscreate_new_job)
  * [`irissoftwaregroupcascade.jobs.get_by_id`](#irissoftwaregroupcascadejobsget_by_id)
  * [`irissoftwaregroupcascade.jobs.get_list`](#irissoftwaregroupcascadejobsget_list)
  * [`irissoftwaregroupcascade.jobs.update_by_id`](#irissoftwaregroupcascadejobsupdate_by_id)
  * [`irissoftwaregroupcascade.public_holidays.get_location_list_by_id`](#irissoftwaregroupcascadepublic_holidaysget_location_list_by_id)
  * [`irissoftwaregroupcascade.public_holidays.get_locations`](#irissoftwaregroupcascadepublic_holidaysget_locations)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=IRIS%20Software%20Group&serviceName=Cascade&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from iris_software_group_cascade_python_sdk import IrisSoftwareGroupCascade, ApiException

irissoftwaregroupcascade = IrisSoftwareGroupCascade(

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

try:
    # Creates an Absence Day.
    create_absence_day_response = irissoftwaregroupcascade.absence_days.create_absence_day(
        absence_id="string_example",
        employee_id="string_example",
        date="1970-01-01T00:00:00.00Z",
        duration_days=3.14,
        duration_minutes=1,
        day_part="AM",
    )
except ApiException as e:
    print("Exception when calling AbsenceDaysApi.create_absence_day: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from iris_software_group_cascade_python_sdk import IrisSoftwareGroupCascade, ApiException

irissoftwaregroupcascade = IrisSoftwareGroupCascade(

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

async def main():
    try:
        # Creates an Absence Day.
        create_absence_day_response = await irissoftwaregroupcascade.absence_days.acreate_absence_day(
            absence_id="string_example",
            employee_id="string_example",
            date="1970-01-01T00:00:00.00Z",
            duration_days=3.14,
            duration_minutes=1,
            day_part="AM",
        )
    except ApiException as e:
        print("Exception when calling AbsenceDaysApi.create_absence_day: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from iris_software_group_cascade_python_sdk import IrisSoftwareGroupCascade, ApiException

irissoftwaregroupcascade = IrisSoftwareGroupCascade(

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

try:
    # Creates an Absence Day.
    create_absence_day_response = irissoftwaregroupcascade.absence_days.raw.create_absence_day(
        absence_id="string_example",
        employee_id="string_example",
        date="1970-01-01T00:00:00.00Z",
        duration_days=3.14,
        duration_minutes=1,
        day_part="AM",
    )
    pprint(create_absence_day_response.headers)
    pprint(create_absence_day_response.status)
    pprint(create_absence_day_response.round_trip_time)
except ApiException as e:
    print("Exception when calling AbsenceDaysApi.create_absence_day: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `irissoftwaregroupcascade.absence_days.create_absence_day`<a id="irissoftwaregroupcascadeabsence_dayscreate_absence_day"></a>

![Beta](https://img.shields.io/badge/Status-Beta-yellow) <b>This API request method is currently in beta testing.</b> To gain access to use this method, please contact <a href='mailto:hrapi@iris.co.uk'>hrapi@iris.co.uk.</a>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_absence_day_response = irissoftwaregroupcascade.absence_days.create_absence_day(
    absence_id="string_example",
    employee_id="string_example",
    date="1970-01-01T00:00:00.00Z",
    duration_days=3.14,
    duration_minutes=1,
    day_part="AM",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### absence_id: `Optional[str]`<a id="absence_id-optionalstr"></a>

The ID of the parent Absence. <br />  Must exist in the Attendance Absence Service.

##### employee_id: `Optional[str]`<a id="employee_id-optionalstr"></a>

The ID of the Employee. <br />  Must exist in the Employees Service.

##### date: `datetime`<a id="date-datetime"></a>

The date of the Absence Day. <br />  Cascade Source: [EmployeeAttendanceDates].[StartDate]

##### duration_days: `Union[int, float]`<a id="duration_days-unionint-float"></a>

The duration in days for this Absence Day. <br />  Cascade Source: [EmployeeAttendanceDates].[DurationDays]

##### duration_minutes: `Optional[int]`<a id="duration_minutes-optionalint"></a>

The duration in minutes for this Absence Day. <br />  Cascade Source: [EmployeeAttendanceDates].[Duration]

##### day_part: [`DayPart`](./iris_software_group_cascade_python_sdk/type/day_part.py)<a id="day_part-daypartiris_software_group_cascade_python_sdktypeday_partpy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateAbsenceDayCommand`](./iris_software_group_cascade_python_sdk/type/create_absence_day_command.py)
The values for an Absence Day.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/attendance/absencedays` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `irissoftwaregroupcascade.absence_days.delete_by_id`<a id="irissoftwaregroupcascadeabsence_daysdelete_by_id"></a>

![Beta](https://img.shields.io/badge/Status-Beta-yellow) <b>This API request method is currently in beta testing.</b> To gain access to use this method, please contact <a href='mailto:hrapi@iris.co.uk'>hrapi@iris.co.uk.</a>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
irissoftwaregroupcascade.absence_days.delete_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID of the Absence Day to delete.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/attendance/absencedays/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `irissoftwaregroupcascade.absence_days.get_by_id`<a id="irissoftwaregroupcascadeabsence_daysget_by_id"></a>

Gets a single Absence Day based on ID given.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = irissoftwaregroupcascade.absence_days.get_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Absence Day ID.

#### 🔄 Return<a id="🔄-return"></a>

[`AbsenceDayModel`](./iris_software_group_cascade_python_sdk/pydantic/absence_day_model.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/attendance/absencedays/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `irissoftwaregroupcascade.absence_days.get_list`<a id="irissoftwaregroupcascadeabsence_daysget_list"></a>

Gets a list of all Absence Days.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = irissoftwaregroupcascade.absence_days.get_list(
    top=0,
    skip=0,
    filter="string_example",
    select=[
        "string_example"
    ],
    orderby="string_example",
    count=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### top: `int`<a id="top-int"></a>

Show only the first n items, maximum of 250, see [Paging - Top](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptiontop)

##### skip: `int`<a id="skip-int"></a>

Skip the first n items, see [Paging - Skip](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptionskip)

##### filter: `str`<a id="filter-str"></a>

Filter items by property values, see [Filtering](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptionfilter)

##### select: List[`str`]<a id="select-liststr"></a>

Select properties to be returned, see [Select](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptionselect)

##### orderby: `str`<a id="orderby-str"></a>

Order items by property values, see [Sorting](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptionorderby)

##### count: `bool`<a id="count-bool"></a>

Include count of items, see [Count](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptioncount)

#### 🔄 Return<a id="🔄-return"></a>

[`AbsenceDayQueryModel`](./iris_software_group_cascade_python_sdk/pydantic/absence_day_query_model.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/attendance/absencedays` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `irissoftwaregroupcascade.absence_days.update_absence_day`<a id="irissoftwaregroupcascadeabsence_daysupdate_absence_day"></a>

![Beta](https://img.shields.io/badge/Status-Beta-yellow) <b>This API request method is currently in beta testing.</b> To gain access to use this method, please contact <a href='mailto:hrapi@iris.co.uk'>hrapi@iris.co.uk.</a>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
irissoftwaregroupcascade.absence_days.update_absence_day(
    id="id_example",
    date="1970-01-01T00:00:00.00Z",
    duration_days=3.14,
    duration_minutes=1,
    day_part="AM",
    id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID of the Absence Day to update.

##### date: `datetime`<a id="date-datetime"></a>

The date of the Absence Day. <br />  Cascade Source: [EmployeeAttendanceDates].[StartDate]

##### duration_days: `Union[int, float]`<a id="duration_days-unionint-float"></a>

The duration in days for this Absence Day. <br />  Cascade Source: [EmployeeAttendanceDates].[DurationDays]

##### duration_minutes: `Optional[int]`<a id="duration_minutes-optionalint"></a>

The duration in minutes for this Absence Day. <br />  Cascade Source: [EmployeeAttendanceDates].[Duration]

##### day_part: [`DayPart`](./iris_software_group_cascade_python_sdk/type/day_part.py)<a id="day_part-daypartiris_software_group_cascade_python_sdktypeday_partpy"></a>

##### id: `Optional[str]`<a id="id-optionalstr"></a>

The ID of the Absence Day. <br />  Must exist in the Attendance Absence Day Service.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateAbsenceDayCommand`](./iris_software_group_cascade_python_sdk/type/update_absence_day_command.py)
The value of an Absence Day.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/attendance/absencedays/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `irissoftwaregroupcascade.absence_reasons.get_by_id`<a id="irissoftwaregroupcascadeabsence_reasonsget_by_id"></a>

Gets a single Absence Reason referenced by ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = irissoftwaregroupcascade.absence_reasons.get_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Absence Reason ID.

#### 🔄 Return<a id="🔄-return"></a>

[`AbsenceReasonModel`](./iris_software_group_cascade_python_sdk/pydantic/absence_reason_model.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/attendance/absencereasons/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `irissoftwaregroupcascade.absence_reasons.get_employee_by_id`<a id="irissoftwaregroupcascadeabsence_reasonsget_employee_by_id"></a>

Gets a single Employee Absence Reason referenced by ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_employee_by_id_response = irissoftwaregroupcascade.absence_reasons.get_employee_by_id(
    id="id_example",
    employee_id="employeeId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Absence Reason ID.

##### employee_id: `str`<a id="employee_id-str"></a>

Employee ID.

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeAbsenceReasonModel`](./iris_software_group_cascade_python_sdk/pydantic/employee_absence_reason_model.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/attendance/absencereasons/{id}/employees/{employeeId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `irissoftwaregroupcascade.absence_reasons.list`<a id="irissoftwaregroupcascadeabsence_reasonslist"></a>

Gets a list of Absence Reasons

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = irissoftwaregroupcascade.absence_reasons.list(
    top=0,
    skip=0,
    filter="string_example",
    select=[
        "string_example"
    ],
    orderby="string_example",
    count=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### top: `int`<a id="top-int"></a>

Show only the first n items, maximum of 250, see [Paging - Top](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptiontop)

##### skip: `int`<a id="skip-int"></a>

Skip the first n items, see [Paging - Skip](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptionskip)

##### filter: `str`<a id="filter-str"></a>

Filter items by property values, see [Filtering](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptionfilter)

##### select: List[`str`]<a id="select-liststr"></a>

Select properties to be returned, see [Select](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptionselect)

##### orderby: `str`<a id="orderby-str"></a>

Order items by property values, see [Sorting](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptionorderby)

##### count: `bool`<a id="count-bool"></a>

Include count of items, see [Count](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptioncount)

#### 🔄 Return<a id="🔄-return"></a>

[`AbsenceReasonQueryModel`](./iris_software_group_cascade_python_sdk/pydantic/absence_reason_query_model.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/attendance/absencereasons` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `irissoftwaregroupcascade.absences.create_new_absence`<a id="irissoftwaregroupcascadeabsencescreate_new_absence"></a>

![Beta](https://img.shields.io/badge/Status-Beta-yellow) <b>This API request method is currently in beta testing.</b> To gain access to use this method, please contact <a href='mailto:hrapi@iris.co.uk'>hrapi@iris.co.uk.</a>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_absence_response = irissoftwaregroupcascade.absences.create_new_absence(
    employee_id="string_example",
    absence_reason_id="string_example",
    narrative="string_example",
    start_date="1970-01-01T00:00:00.00Z",
    end_date="1970-01-01T00:00:00.00Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `Optional[str]`<a id="employee_id-optionalstr"></a>

The ID of the Employee. <br />  Must exist in the Employees Service. <br />  Cannot be updated once Absence created.

##### absence_reason_id: `Optional[str]`<a id="absence_reason_id-optionalstr"></a>

The Absence Reason ID. <br />  Must exist in the Attendance Absence Reasons Service. <br />  Cannot be updated once Absence created.

##### narrative: `Optional[str]`<a id="narrative-optionalstr"></a>

The Narrative relating to the Attendance. <br />  Cascade Source: [EmployeeAttendance].[Narrative]

##### start_date: `Optional[datetime]`<a id="start_date-optionaldatetime"></a>

The Start Date of the Attendance. <br />  Cascade Source: [EmployeeAttendance].[StartDate]

##### end_date: `Optional[datetime]`<a id="end_date-optionaldatetime"></a>

The End Date of the Attendance. <br />  Cascade Source: [EmployeeAttendance].[EndDate]  Null if Opened Ended - Cascade Source: [EmployeeAttendance].[OpenEnded]

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateAbsenceCommand`](./iris_software_group_cascade_python_sdk/type/create_absence_command.py)
New Absence.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/attendance/absences` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `irissoftwaregroupcascade.absences.delete_by_id`<a id="irissoftwaregroupcascadeabsencesdelete_by_id"></a>

![Beta](https://img.shields.io/badge/Status-Beta-yellow) <b>This API request method is currently in beta testing.</b> To gain access to use this method, please contact <a href='mailto:hrapi@iris.co.uk'>hrapi@iris.co.uk.</a>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
irissoftwaregroupcascade.absences.delete_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID of the Absence to delete.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/attendance/absences/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `irissoftwaregroupcascade.absences.get_by_id`<a id="irissoftwaregroupcascadeabsencesget_by_id"></a>

Gets a single Absence referenced by ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = irissoftwaregroupcascade.absences.get_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Absence ID.

#### 🔄 Return<a id="🔄-return"></a>

[`AbsenceModel`](./iris_software_group_cascade_python_sdk/pydantic/absence_model.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/attendance/absences/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `irissoftwaregroupcascade.absences.get_list`<a id="irissoftwaregroupcascadeabsencesget_list"></a>

Gets a list of Absences.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = irissoftwaregroupcascade.absences.get_list(
    top=0,
    skip=0,
    filter="string_example",
    select=[
        "string_example"
    ],
    orderby="string_example",
    count=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### top: `int`<a id="top-int"></a>

Show only the first n items, maximum of 250, see [Paging - Top](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptiontop)

##### skip: `int`<a id="skip-int"></a>

Skip the first n items, see [Paging - Skip](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptionskip)

##### filter: `str`<a id="filter-str"></a>

Filter items by property values, see [Filtering](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptionfilter)

##### select: List[`str`]<a id="select-liststr"></a>

Select properties to be returned, see [Select](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptionselect)

##### orderby: `str`<a id="orderby-str"></a>

Order items by property values, see [Sorting](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptionorderby)

##### count: `bool`<a id="count-bool"></a>

Include count of items, see [Count](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptioncount)

#### 🔄 Return<a id="🔄-return"></a>

[`AbsenceQueryModel`](./iris_software_group_cascade_python_sdk/pydantic/absence_query_model.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/attendance/absences` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `irissoftwaregroupcascade.absences.update_by_id`<a id="irissoftwaregroupcascadeabsencesupdate_by_id"></a>

![Beta](https://img.shields.io/badge/Status-Beta-yellow) <b>This API request method is currently in beta testing.</b> To gain access to use this method, please contact <a href='mailto:hrapi@iris.co.uk'>hrapi@iris.co.uk.</a>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
irissoftwaregroupcascade.absences.update_by_id(
    id="id_example",
    narrative="string_example",
    start_date="1970-01-01T00:00:00.00Z",
    end_date="1970-01-01T00:00:00.00Z",
    id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID of the Absence to update.

##### narrative: `Optional[str]`<a id="narrative-optionalstr"></a>

The Narrative relating to the Attendance. <br />  Cascade Source: [EmployeeAttendance].[Narrative]

##### start_date: `Optional[datetime]`<a id="start_date-optionaldatetime"></a>

The Start Date of the Attendance. <br />  Cascade Source: [EmployeeAttendance].[StartDate]

##### end_date: `Optional[datetime]`<a id="end_date-optionaldatetime"></a>

The End Date of the Attendance. <br />  Cascade Source: [EmployeeAttendance].[EndDate]  Null if Opened Ended - Cascade Source: [EmployeeAttendance].[OpenEnded]

##### id: `Optional[str]`<a id="id-optionalstr"></a>

The ID of the Absence. <br />  Must exist in the Attendance Absences Service.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateAbsenceCommand`](./iris_software_group_cascade_python_sdk/type/update_absence_command.py)
The new state of the Absence.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/attendance/absences/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `irissoftwaregroupcascade.bank_details.create_bank_detail`<a id="irissoftwaregroupcascadebank_detailscreate_bank_detail"></a>

Creates a Bank Details.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_bank_detail_response = irissoftwaregroupcascade.bank_details.create_bank_detail(
    employee_id="string_example",
    bank_name="string_example",
    bank_address={
    },
    account_name="string_example",
    account_number="string_example",
    sort_code="string_example",
    roll_number="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `Optional[str]`<a id="employee_id-optionalstr"></a>

The ID of the HR Employee. <br />  Must exist in the Employee Service.

##### bank_name: `Optional[str]`<a id="bank_name-optionalstr"></a>

Bank Name. <br />  Cascade Source: [EmployeeBank].[BankName]

##### bank_address: [`BankAddress`](./iris_software_group_cascade_python_sdk/type/bank_address.py)<a id="bank_address-bankaddressiris_software_group_cascade_python_sdktypebank_addresspy"></a>


##### account_name: `Optional[str]`<a id="account_name-optionalstr"></a>

Account Name. <br />  Cascade Source: [EmployeeBank].[AccountName]

##### account_number: `Optional[str]`<a id="account_number-optionalstr"></a>

Account Number. <br />  Cascade Source: [EmployeeBank].[AccountNumber]

##### sort_code: `Optional[str]`<a id="sort_code-optionalstr"></a>

Sort Code. <br />  Cascade Source: [EmployeeBank].[SortCode]

##### roll_number: `Optional[str]`<a id="roll_number-optionalstr"></a>

Roll Number. <br />  Cascade Source: [EmployeeBank].[RollNumber]

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateBankDetailsCommand`](./iris_software_group_cascade_python_sdk/type/create_bank_details_command.py)
The value of Bank Details.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/bankdetails` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `irissoftwaregroupcascade.bank_details.get_by_id`<a id="irissoftwaregroupcascadebank_detailsget_by_id"></a>

Gets a single Bank Details by an ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = irissoftwaregroupcascade.bank_details.get_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Bank Details ID.

#### 🔄 Return<a id="🔄-return"></a>

[`BankDetailsModel`](./iris_software_group_cascade_python_sdk/pydantic/bank_details_model.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/bankdetails/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `irissoftwaregroupcascade.bank_details.get_list`<a id="irissoftwaregroupcascadebank_detailsget_list"></a>

Gets a list of Bank Details.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = irissoftwaregroupcascade.bank_details.get_list(
    top=0,
    skip=0,
    filter="string_example",
    select=[
        "string_example"
    ],
    orderby="string_example",
    count=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### top: `int`<a id="top-int"></a>

Show only the first n items, maximum of 250, see [Paging - Top](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptiontop)

##### skip: `int`<a id="skip-int"></a>

Skip the first n items, see [Paging - Skip](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptionskip)

##### filter: `str`<a id="filter-str"></a>

Filter items by property values, see [Filtering](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptionfilter)

##### select: List[`str`]<a id="select-liststr"></a>

Select properties to be returned, see [Select](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptionselect)

##### orderby: `str`<a id="orderby-str"></a>

Order items by property values, see [Sorting](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptionorderby)

##### count: `bool`<a id="count-bool"></a>

Include count of items, see [Count](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptioncount)

#### 🔄 Return<a id="🔄-return"></a>

[`BankDetailsQueryModel`](./iris_software_group_cascade_python_sdk/pydantic/bank_details_query_model.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/bankdetails` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `irissoftwaregroupcascade.bank_details.update_bank_detail`<a id="irissoftwaregroupcascadebank_detailsupdate_bank_detail"></a>

Updates Bank Details.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
irissoftwaregroupcascade.bank_details.update_bank_detail(
    id="id_example",
    bank_name="string_example",
    bank_address={
    },
    account_name="string_example",
    account_number="string_example",
    sort_code="string_example",
    roll_number="string_example",
    id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID of Bank Details to update.

##### bank_name: `Optional[str]`<a id="bank_name-optionalstr"></a>

Bank Name. <br />  Cascade Source: [EmployeeBank].[BankName]

##### bank_address: [`BankAddress`](./iris_software_group_cascade_python_sdk/type/bank_address.py)<a id="bank_address-bankaddressiris_software_group_cascade_python_sdktypebank_addresspy"></a>


##### account_name: `Optional[str]`<a id="account_name-optionalstr"></a>

Account Name. <br />  Cascade Source: [EmployeeBank].[AccountName]

##### account_number: `Optional[str]`<a id="account_number-optionalstr"></a>

Account Number. <br />  Cascade Source: [EmployeeBank].[AccountNumber]

##### sort_code: `Optional[str]`<a id="sort_code-optionalstr"></a>

Sort Code. <br />  Cascade Source: [EmployeeBank].[SortCode]

##### roll_number: `Optional[str]`<a id="roll_number-optionalstr"></a>

Roll Number. <br />  Cascade Source: [EmployeeBank].[RollNumber]

##### id: `Optional[str]`<a id="id-optionalstr"></a>

The ID of Bank Details to update. <br />  Must exist in Bank Details Service.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateBankDetailsCommand`](./iris_software_group_cascade_python_sdk/type/update_bank_details_command.py)
The value of Bank Details.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/bankdetails/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `irissoftwaregroupcascade.benefits.get_by_id`<a id="irissoftwaregroupcascadebenefitsget_by_id"></a>

Gets a single Benefit referenced by ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = irissoftwaregroupcascade.benefits.get_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Benefit ID.

#### 🔄 Return<a id="🔄-return"></a>

[`BenefitModel`](./iris_software_group_cascade_python_sdk/pydantic/benefit_model.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/benefits/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `irissoftwaregroupcascade.benefits.get_list`<a id="irissoftwaregroupcascadebenefitsget_list"></a>

Gets a list of Benefits.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = irissoftwaregroupcascade.benefits.get_list(
    top=0,
    skip=0,
    filter="string_example",
    select=[
        "string_example"
    ],
    orderby="string_example",
    count=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### top: `int`<a id="top-int"></a>

Show only the first n items, maximum of 250, see [Paging - Top](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptiontop)

##### skip: `int`<a id="skip-int"></a>

Skip the first n items, see [Paging - Skip](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptionskip)

##### filter: `str`<a id="filter-str"></a>

Filter items by property values, see [Filtering](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptionfilter)

##### select: List[`str`]<a id="select-liststr"></a>

Select properties to be returned, see [Select](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptionselect)

##### orderby: `str`<a id="orderby-str"></a>

Order items by property values, see [Sorting](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptionorderby)

##### count: `bool`<a id="count-bool"></a>

Include count of items, see [Count](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptioncount)

#### 🔄 Return<a id="🔄-return"></a>

[`BenefitQueryModel`](./iris_software_group_cascade_python_sdk/pydantic/benefit_query_model.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/benefits` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `irissoftwaregroupcascade.employees.create_new_employee`<a id="irissoftwaregroupcascadeemployeescreate_new_employee"></a>

Creates a new Employee.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_employee_response = irissoftwaregroupcascade.employees.create_new_employee(
    display_id="string_example",
    title_honorific="string_example",
    first_name="string_example",
    known_as="string_example",
    other_name="string_example",
    last_name="string_example",
    cost_centre="string_example",
    working_status="string_example",
    is_manager=True,
    national_insurance_number="string_example",
    payroll_id="string_example",
    tax_code="string_example",
    include_in_payroll=True,
    employment_start_date="1970-01-01T00:00:00.00Z",
    employment_left_date="1970-01-01T00:00:00.00Z",
    continuous_service_date="1970-01-01T00:00:00.00Z",
    date_of_birth="1970-01-01T00:00:00.00Z",
    last_working_date="1970-01-01T00:00:00.00Z",
    gender="string_example",
    ethnicity="string_example",
    nationality="string_example",
    religion="string_example",
    leaver_reason="string_example",
    marital_status="string_example",
    phones=[
        {
            "ownership": "Personal",
            "type": "Mobile",
        }
    ],
    emails=[
        {
            "ownership": "Personal",
        }
    ],
    addresses=[
        {
            "ownership": "Personal",
        }
    ],
    gender_identity="string_example",
    windows_username="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### display_id: `Optional[str]`<a id="display_id-optionalstr"></a>

The Display ID of the Employee. <br />  If provided must be unqiue, If null then it will automatically be generated. <br />  Cascade Source: [Employee].[DisplayEmployeeId]

##### title_honorific: `Optional[str]`<a id="title_honorific-optionalstr"></a>

The Title of the Employee. E.g. Mr, Mrs, Miss. <br />  Cascade Source: [Employee].[Title] translated through the TITLE system list.

##### first_name: `Optional[str]`<a id="first_name-optionalstr"></a>

The First Name of the Employee. <br />  Required. <br />  Cascade Source: [Employee].[Forename]

##### known_as: `Optional[str]`<a id="known_as-optionalstr"></a>

The name the Employee is commonly known as. <br />  Cascade Source: [Employee].[KnownAs]

##### other_name: `Optional[str]`<a id="other_name-optionalstr"></a>

Any other name that the Employee has. <br />  Cascade Source: [Employee].[OtherName]

##### last_name: `Optional[str]`<a id="last_name-optionalstr"></a>

The Last Name, Surname or Family Name of the Employee. <br />  Required. <br />  Cascade Source: [Employee].[Surname]

##### cost_centre: `Optional[str]`<a id="cost_centre-optionalstr"></a>

The Cost Centre assigned to the Employee. <br />  Cascade Source: [Employee].[CostCentre]

##### working_status: `Optional[str]`<a id="working_status-optionalstr"></a>

The Status of the Employee E.g. On Holiday, Sick. <br />  Automatically Calculated. <br />  Cascade Source: [Sysview_Employee_Status].[StatusDescription]

##### is_manager: `Optional[bool]`<a id="is_manager-optionalbool"></a>

Indicates if the Employee is a Manager. <br />  True if any other Employee's active <see cref=\\\"T:Iris.Api.Hr.Employee.Domain.Entities.V1.Job\\\">Job</see> has this Employee as their Line Manager. <br />  Automaticaly Calculated.

##### national_insurance_number: `Optional[str]`<a id="national_insurance_number-optionalstr"></a>

The National Insurance Number of the Employee. <br />  Cascade Source: [Employee].[NationalInsuranceNo]

##### payroll_id: `Optional[str]`<a id="payroll_id-optionalstr"></a>

The Payroll ID of the Employee. <br />  Cascade Source: [Employee].[PayrollId]

##### tax_code: `Optional[str]`<a id="tax_code-optionalstr"></a>

The Tax Code of the Employee. <br />  Cascade Source: [Employee].[TaxCode]

##### include_in_payroll: `Optional[bool]`<a id="include_in_payroll-optionalbool"></a>

Indicates if the Employee should be included in Payroll. <br />  Cascade Source: [Employee].[IncludeInPayroll]

##### employment_start_date: `Optional[datetime]`<a id="employment_start_date-optionaldatetime"></a>

The date the Employee started with their current Employer. <br />  Cascade Source: [Employee].[EmployeeStartDate]

##### employment_left_date: `Optional[datetime]`<a id="employment_left_date-optionaldatetime"></a>

The date the Employee left their current Employer. <br />  Cascade Source: [Employee].[EmployementLeftDate]

##### continuous_service_date: `Optional[datetime]`<a id="continuous_service_date-optionaldatetime"></a>

The date the Employee's continuous service should be applied from. <br />  Cascade Source: [Employee].[ContServiceDate]

##### date_of_birth: `Optional[datetime]`<a id="date_of_birth-optionaldatetime"></a>

The Date of Birth of the Employee. <br />  Cascade Source: [Employee].[DateOfBirth]

##### last_working_date: `Optional[datetime]`<a id="last_working_date-optionaldatetime"></a>

The date of the last working date of the Employee. <br />  Cascade Source: [Employee].[LeaverLastWorkDate]

##### gender: `Optional[str]`<a id="gender-optionalstr"></a>

The Gender of the Employee. <br />  Cascade Source: [Employee].[Sex] translated through the GENDER system list.

##### ethnicity: `Optional[str]`<a id="ethnicity-optionalstr"></a>

The Ethnicity of the Employee. <br />  Cascade Source: [Employee].[EthnicOrigin] translated through the ETHNICTORIGIN system list.

##### nationality: `Optional[str]`<a id="nationality-optionalstr"></a>

The Nationality of the Employee. <br />  Cascade Source: [Employee].[Nationality] translated through the NATIONALITY system list.

##### religion: `Optional[str]`<a id="religion-optionalstr"></a>

The Religion of the Employee. <br />  Cascade Source: [Employee].[Religion] transalated through the RELIGION system list.

##### leaver_reason: `Optional[str]`<a id="leaver_reason-optionalstr"></a>

The reason for the Employee to Leave. <br />  Cascade Source: [Employee].[LeaverReason]

##### marital_status: `Optional[str]`<a id="marital_status-optionalstr"></a>

The marrital status of the Employee. <br />  Cascade Source: [Employee.[MaritalStatus] translated through the MARITALSTATUS system list.

##### phones: List[`Phone`]<a id="phones-listphone"></a>

The <see cref=\\\"T:Iris.Api.Hr.Employee.Domain.Entities.V1.Phone\\\">Phone Numbers</see> belonging to the Employee.

##### emails: List[`Email`]<a id="emails-listemail"></a>

The <see cref=\\\"T:Iris.Api.Hr.Employee.Domain.Entities.V1.Email\\\">Email Addresses</see> belonging to the Employee.

##### addresses: List[`Address`]<a id="addresses-listaddress"></a>

The <see cref=\\\"T:Iris.Api.Hr.Employee.Domain.Entities.V1.Address\\\">Addresses</see> belonging to the Employee.

##### gender_identity: `Optional[str]`<a id="gender_identity-optionalstr"></a>

The Gender Identity of the Employee. <br />  Cascade Source: [Employee].[GenderIdentity] translated through the GenderIdentity system list.

##### windows_username: `Optional[str]`<a id="windows_username-optionalstr"></a>

The Windows Username of the Employee. <br />  Cascade Source: [Employee].[WindowsUsername]

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateEmployeeCommand`](./iris_software_group_cascade_python_sdk/type/create_employee_command.py)
New Employee.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employees` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `irissoftwaregroupcascade.employees.get_by_id`<a id="irissoftwaregroupcascadeemployeesget_by_id"></a>

Gets a single Employee referenced by ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = irissoftwaregroupcascade.employees.get_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Employee ID.

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeModel`](./iris_software_group_cascade_python_sdk/pydantic/employee_model.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employees/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `irissoftwaregroupcascade.employees.get_list`<a id="irissoftwaregroupcascadeemployeesget_list"></a>

Gets a list of Employees.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = irissoftwaregroupcascade.employees.get_list(
    top=0,
    skip=0,
    filter="string_example",
    select=[
        "string_example"
    ],
    orderby="string_example",
    count=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### top: `int`<a id="top-int"></a>

Show only the first n items, maximum of 250, see [Paging - Top](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptiontop)

##### skip: `int`<a id="skip-int"></a>

Skip the first n items, see [Paging - Skip](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptionskip)

##### filter: `str`<a id="filter-str"></a>

Filter items by property values, see [Filtering](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptionfilter)

##### select: List[`str`]<a id="select-liststr"></a>

Select properties to be returned, see [Select](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptionselect)

##### orderby: `str`<a id="orderby-str"></a>

Order items by property values, see [Sorting](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptionorderby)

##### count: `bool`<a id="count-bool"></a>

Include count of items, see [Count](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptioncount)

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeQueryModel`](./iris_software_group_cascade_python_sdk/pydantic/employee_query_model.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employees` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `irissoftwaregroupcascade.employees.update_by_id`<a id="irissoftwaregroupcascadeemployeesupdate_by_id"></a>

Update an Employee referenced by ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
irissoftwaregroupcascade.employees.update_by_id(
    id="id_example",
    display_id="string_example",
    title_honorific="string_example",
    first_name="string_example",
    known_as="string_example",
    other_name="string_example",
    last_name="string_example",
    cost_centre="string_example",
    working_status="string_example",
    is_manager=True,
    national_insurance_number="string_example",
    payroll_id="string_example",
    tax_code="string_example",
    include_in_payroll=True,
    employment_start_date="1970-01-01T00:00:00.00Z",
    employment_left_date="1970-01-01T00:00:00.00Z",
    continuous_service_date="1970-01-01T00:00:00.00Z",
    date_of_birth="1970-01-01T00:00:00.00Z",
    last_working_date="1970-01-01T00:00:00.00Z",
    gender="string_example",
    ethnicity="string_example",
    nationality="string_example",
    religion="string_example",
    leaver_reason="string_example",
    marital_status="string_example",
    phones=[
        {
            "ownership": "Personal",
            "type": "Mobile",
        }
    ],
    emails=[
        {
            "ownership": "Personal",
        }
    ],
    addresses=[
        {
            "ownership": "Personal",
        }
    ],
    gender_identity="string_example",
    windows_username="string_example",
    id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID of Employee to update.

##### display_id: `Optional[str]`<a id="display_id-optionalstr"></a>

The Display ID of the Employee. <br />  If provided must be unqiue, If null then it will automatically be generated. <br />  Cascade Source: [Employee].[DisplayEmployeeId]

##### title_honorific: `Optional[str]`<a id="title_honorific-optionalstr"></a>

The Title of the Employee. E.g. Mr, Mrs, Miss. <br />  Cascade Source: [Employee].[Title] translated through the TITLE system list.

##### first_name: `Optional[str]`<a id="first_name-optionalstr"></a>

The First Name of the Employee. <br />  Required. <br />  Cascade Source: [Employee].[Forename]

##### known_as: `Optional[str]`<a id="known_as-optionalstr"></a>

The name the Employee is commonly known as. <br />  Cascade Source: [Employee].[KnownAs]

##### other_name: `Optional[str]`<a id="other_name-optionalstr"></a>

Any other name that the Employee has. <br />  Cascade Source: [Employee].[OtherName]

##### last_name: `Optional[str]`<a id="last_name-optionalstr"></a>

The Last Name, Surname or Family Name of the Employee. <br />  Required. <br />  Cascade Source: [Employee].[Surname]

##### cost_centre: `Optional[str]`<a id="cost_centre-optionalstr"></a>

The Cost Centre assigned to the Employee. <br />  Cascade Source: [Employee].[CostCentre]

##### working_status: `Optional[str]`<a id="working_status-optionalstr"></a>

The Status of the Employee E.g. On Holiday, Sick. <br />  Automatically Calculated. <br />  Cascade Source: [Sysview_Employee_Status].[StatusDescription]

##### is_manager: `Optional[bool]`<a id="is_manager-optionalbool"></a>

Indicates if the Employee is a Manager. <br />  True if any other Employee's active <see cref=\\\"T:Iris.Api.Hr.Employee.Domain.Entities.V1.Job\\\">Job</see> has this Employee as their Line Manager. <br />  Automaticaly Calculated.

##### national_insurance_number: `Optional[str]`<a id="national_insurance_number-optionalstr"></a>

The National Insurance Number of the Employee. <br />  Cascade Source: [Employee].[NationalInsuranceNo]

##### payroll_id: `Optional[str]`<a id="payroll_id-optionalstr"></a>

The Payroll ID of the Employee. <br />  Cascade Source: [Employee].[PayrollId]

##### tax_code: `Optional[str]`<a id="tax_code-optionalstr"></a>

The Tax Code of the Employee. <br />  Cascade Source: [Employee].[TaxCode]

##### include_in_payroll: `Optional[bool]`<a id="include_in_payroll-optionalbool"></a>

Indicates if the Employee should be included in Payroll. <br />  Cascade Source: [Employee].[IncludeInPayroll]

##### employment_start_date: `Optional[datetime]`<a id="employment_start_date-optionaldatetime"></a>

The date the Employee started with their current Employer. <br />  Cascade Source: [Employee].[EmployeeStartDate]

##### employment_left_date: `Optional[datetime]`<a id="employment_left_date-optionaldatetime"></a>

The date the Employee left their current Employer. <br />  Cascade Source: [Employee].[EmployementLeftDate]

##### continuous_service_date: `Optional[datetime]`<a id="continuous_service_date-optionaldatetime"></a>

The date the Employee's continuous service should be applied from. <br />  Cascade Source: [Employee].[ContServiceDate]

##### date_of_birth: `Optional[datetime]`<a id="date_of_birth-optionaldatetime"></a>

The Date of Birth of the Employee. <br />  Cascade Source: [Employee].[DateOfBirth]

##### last_working_date: `Optional[datetime]`<a id="last_working_date-optionaldatetime"></a>

The date of the last working date of the Employee. <br />  Cascade Source: [Employee].[LeaverLastWorkDate]

##### gender: `Optional[str]`<a id="gender-optionalstr"></a>

The Gender of the Employee. <br />  Cascade Source: [Employee].[Sex] translated through the GENDER system list.

##### ethnicity: `Optional[str]`<a id="ethnicity-optionalstr"></a>

The Ethnicity of the Employee. <br />  Cascade Source: [Employee].[EthnicOrigin] translated through the ETHNICTORIGIN system list.

##### nationality: `Optional[str]`<a id="nationality-optionalstr"></a>

The Nationality of the Employee. <br />  Cascade Source: [Employee].[Nationality] translated through the NATIONALITY system list.

##### religion: `Optional[str]`<a id="religion-optionalstr"></a>

The Religion of the Employee. <br />  Cascade Source: [Employee].[Religion] transalated through the RELIGION system list.

##### leaver_reason: `Optional[str]`<a id="leaver_reason-optionalstr"></a>

The reason for the Employee to Leave. <br />  Cascade Source: [Employee].[LeaverReason]

##### marital_status: `Optional[str]`<a id="marital_status-optionalstr"></a>

The marrital status of the Employee. <br />  Cascade Source: [Employee.[MaritalStatus] translated through the MARITALSTATUS system list.

##### phones: List[`Phone`]<a id="phones-listphone"></a>

The <see cref=\\\"T:Iris.Api.Hr.Employee.Domain.Entities.V1.Phone\\\">Phone Numbers</see> belonging to the Employee.

##### emails: List[`Email`]<a id="emails-listemail"></a>

The <see cref=\\\"T:Iris.Api.Hr.Employee.Domain.Entities.V1.Email\\\">Email Addresses</see> belonging to the Employee.

##### addresses: List[`Address`]<a id="addresses-listaddress"></a>

The <see cref=\\\"T:Iris.Api.Hr.Employee.Domain.Entities.V1.Address\\\">Addresses</see> belonging to the Employee.

##### gender_identity: `Optional[str]`<a id="gender_identity-optionalstr"></a>

The Gender Identity of the Employee. <br />  Cascade Source: [Employee].[GenderIdentity] translated through the GenderIdentity system list.

##### windows_username: `Optional[str]`<a id="windows_username-optionalstr"></a>

The Windows Username of the Employee. <br />  Cascade Source: [Employee].[WindowsUsername]

##### id: `Optional[str]`<a id="id-optionalstr"></a>

The ID of the Employee. <br />  Must exist in the Employee Service.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateEmployeeCommand`](./iris_software_group_cascade_python_sdk/type/update_employee_command.py)
The new state of the Employee.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/employees/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `irissoftwaregroupcascade.entitlements.get_by_id`<a id="irissoftwaregroupcascadeentitlementsget_by_id"></a>

Gets an Entitlement by ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = irissoftwaregroupcascade.entitlements.get_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Entitlement ID.

#### 🔄 Return<a id="🔄-return"></a>

[`EntitlementModel`](./iris_software_group_cascade_python_sdk/pydantic/entitlement_model.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/attendance/entitlements/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `irissoftwaregroupcascade.entitlements.get_list`<a id="irissoftwaregroupcascadeentitlementsget_list"></a>

Gets a list of Entitlements.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = irissoftwaregroupcascade.entitlements.get_list(
    top=0,
    skip=0,
    filter="string_example",
    select=[
        "string_example"
    ],
    orderby="string_example",
    count=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### top: `int`<a id="top-int"></a>

Show only the first n items, maximum of 250, see [Paging - Top](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptiontop)

##### skip: `int`<a id="skip-int"></a>

Skip the first n items, see [Paging - Skip](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptionskip)

##### filter: `str`<a id="filter-str"></a>

Filter items by property values, see [Filtering](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptionfilter)

##### select: List[`str`]<a id="select-liststr"></a>

Select properties to be returned, see [Select](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptionselect)

##### orderby: `str`<a id="orderby-str"></a>

Order items by property values, see [Sorting](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptionorderby)

##### count: `bool`<a id="count-bool"></a>

Include count of items, see [Count](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptioncount)

#### 🔄 Return<a id="🔄-return"></a>

[`EntitlementQueryModel`](./iris_software_group_cascade_python_sdk/pydantic/entitlement_query_model.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/attendance/entitlements` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `irissoftwaregroupcascade.hierarchy.get_list`<a id="irissoftwaregroupcascadehierarchyget_list"></a>

Gets a list of Hierarchy Nodes.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = irissoftwaregroupcascade.hierarchy.get_list(
    top=0,
    skip=0,
    filter="string_example",
    select=[
        "string_example"
    ],
    orderby="string_example",
    count=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### top: `int`<a id="top-int"></a>

Show only the first n items, maximum of 250, see [Paging - Top](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptiontop)

##### skip: `int`<a id="skip-int"></a>

Skip the first n items, see [Paging - Skip](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptionskip)

##### filter: `str`<a id="filter-str"></a>

Filter items by property values, see [Filtering](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptionfilter)

##### select: List[`str`]<a id="select-liststr"></a>

Select properties to be returned, see [Select](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptionselect)

##### orderby: `str`<a id="orderby-str"></a>

Order items by property values, see [Sorting](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptionorderby)

##### count: `bool`<a id="count-bool"></a>

Include count of items, see [Count](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptioncount)

#### 🔄 Return<a id="🔄-return"></a>

[`HierarchyNodeQueryModel`](./iris_software_group_cascade_python_sdk/pydantic/hierarchy_node_query_model.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/hierarchy` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `irissoftwaregroupcascade.hierarchy.get_node_by_id`<a id="irissoftwaregroupcascadehierarchyget_node_by_id"></a>

Gets a single Hierarchy Node by ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_node_by_id_response = irissoftwaregroupcascade.hierarchy.get_node_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Hierarchy Node ID.

#### 🔄 Return<a id="🔄-return"></a>

[`HierarchyNodeModel`](./iris_software_group_cascade_python_sdk/pydantic/hierarchy_node_model.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/hierarchy/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `irissoftwaregroupcascade.hierarchy.get_path_by_id`<a id="irissoftwaregroupcascadehierarchyget_path_by_id"></a>

Gets a Hierarchy Path by ID. The path is an array of nodes traversed from the root to the node specified.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_path_by_id_response = irissoftwaregroupcascade.hierarchy.get_path_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Hierarchy Node ID.

#### 🔄 Return<a id="🔄-return"></a>

[`HierarchyNodeModel`](./iris_software_group_cascade_python_sdk/pydantic/hierarchy_node_model.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/hierarchy/{id}/path` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `irissoftwaregroupcascade.jobs.create_new_job`<a id="irissoftwaregroupcascadejobscreate_new_job"></a>

Creates a new Job.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_job_response = irissoftwaregroupcascade.jobs.create_new_job(
    job_title="string_example",
    classification="string_example",
    start_date="1970-01-01T00:00:00.00Z",
    end_date="1970-01-01T00:00:00.00Z",
    working_calendar="string_example",
    line_manager_id="string_example",
    hierarchy_node_id="string_example",
    active=True,
    salary=3.14,
    employee_id="string_example",
    contract="string_example",
    pay_frequency="string_example",
    pay_basis="string_example",
    full_time_equivalent=3.14,
    change_reason="string_example",
    next_increment_date="1970-01-01T00:00:00.00Z",
    timesheet_location="string_example",
    timesheet_lunch_duration="string_example",
    expense_submission_frequency="string_example",
    cost_centre="string_example",
    job_family="string_example",
    apprentice_under25=True,
    apprenticeship_end_date="1970-01-01T00:00:00.00Z",
    contract_end_date="1970-01-01T00:00:00.00Z",
    normal_hours=3.14,
    real_time_information_irregular_frequency="string_example",
    notice_period="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### job_title: `Optional[str]`<a id="job_title-optionalstr"></a>

The title of the Job. <br />  Cascade Source: [EmployeeJobs].[JobTitle]

##### classification: `Optional[str]`<a id="classification-optionalstr"></a>

The classification of the Job e.g. Technical, Professional, Managerial. <br />  Cascade Source: [EmployeeJobs].[Classification] translated through the JOBCLASSIFICATION system list.

##### start_date: `datetime`<a id="start_date-datetime"></a>

The start date of the Job. <br />  Required. <br />  Cascade Source: [EmployeeJobs].[SYS_EffectiveDate]

##### end_date: `Optional[datetime]`<a id="end_date-optionaldatetime"></a>

The end date of the Job. <br />  Automatically Calculated. <br />  Cascade Source: [EmployeeJobs].[SYS_CalculatedEndDate]

##### working_calendar: `Optional[str]`<a id="working_calendar-optionalstr"></a>

The name of the working calendar of the Job. <br />  Cascade Source: [EmployeeJobs].[CalendarName] which comes from [ValidWorkingCalendar].[CalendarName]

##### line_manager_id: `Optional[str]`<a id="line_manager_id-optionalstr"></a>

The ID of the Employee that is the line manager for this Job. <br />  Must exist in Employees Service. <br />  Cascade Source: [EmployeeJobs].[WorksForEmployeeId]

##### hierarchy_node_id: `Optional[str]`<a id="hierarchy_node_id-optionalstr"></a>

The ID of the Employee's Hierarchy node of the Job. <br />  Must exist in Hierarchy Service.

##### active: `bool`<a id="active-bool"></a>

The Job is currently active. <br />  Automatically Calculated. <br />  Cascade Source: [EmployeeJobs].[sys_ActiveJob]

##### salary: `Optional[Union[int, float]]`<a id="salary-optionalunionint-float"></a>

The salary of the Job. <br />  Cascade Source: [EmployeeJobs].[BasicPay]

##### employee_id: `Optional[str]`<a id="employee_id-optionalstr"></a>

The ID of the Employee of the Job. <br />  Must exist in Employee Service.

##### contract: `Optional[str]`<a id="contract-optionalstr"></a>

The contract of the Job e.g. Full Time, Part Time. <br />  Cascade Source: [EmployeeJobs].[ContractType] translated through the EMPLOYMENTTYPES system list.

##### pay_frequency: `Optional[str]`<a id="pay_frequency-optionalstr"></a>

How often the Job's salary will be paid e.g. Monthly, Weekly. <br />  Cascade Source: [EmployeeJobs].[PayFrequency] translated through the PAY FREQ system list.

##### pay_basis: `Optional[str]`<a id="pay_basis-optionalstr"></a>

The unit of measurement the salary is specified against e.g. Yearly, Hourly. <br />  Cascade Source: [EmployeeJobs].[PayBasis] translated through the PAY BASIS system list.

##### full_time_equivalent: `Optional[Union[int, float]]`<a id="full_time_equivalent-optionalunionint-float"></a>

The full-time equivalent to a full time employee's hours e.g. 1 = Full Time, 0.5 = Half Hours. <br />  Cascade Source: [EmployeeJobs].[FTE].

##### change_reason: `Optional[str]`<a id="change_reason-optionalstr"></a>

The reason for the change. <br />  Cascade Source: [EmployeeJobs].[Reason].

##### next_increment_date: `Optional[datetime]`<a id="next_increment_date-optionaldatetime"></a>

The next increment date.  <br />  Cascade Source: [EmployeeJobs].[IncrementDate].

##### timesheet_location: `Optional[str]`<a id="timesheet_location-optionalstr"></a>

The timesheet location. <br />  Cascade Source: [EmployeeJobs].[TimesheetLocation].

##### timesheet_lunch_duration: `Optional[str]`<a id="timesheet_lunch_duration-optionalstr"></a>

The time set lunch duration. <br />  Cascade Source: [EmployeeJobs].[LunchDuration].

##### expense_submission_frequency: `Optional[str]`<a id="expense_submission_frequency-optionalstr"></a>

The expense submission frequency. <br />  Cascade Source: [EmployeeJobs].[ExpenseSubmissionFrequency].

##### cost_centre: `Optional[str]`<a id="cost_centre-optionalstr"></a>

The cost centre. <br />  Cascade Source: [EmployeeJobs].[CostCentre].

##### job_family: `Optional[str]`<a id="job_family-optionalstr"></a>

The job family. <br />  Cascade Source: [EmployeeJobs].[JobFamily].

##### apprentice_under25: `Optional[bool]`<a id="apprentice_under25-optionalbool"></a>

The flag to indicate if the employee is an apprentice under 25. <br />  Cascade Source: [EmployeeJobs].[ApprenticeUnder25].

##### apprenticeship_end_date: `Optional[datetime]`<a id="apprenticeship_end_date-optionaldatetime"></a>

The end date of the apprenticeship. <br />  Cascade Source: [EmployeeJobs].[ApprenticeshipEndDate].

##### contract_end_date: `Optional[datetime]`<a id="contract_end_date-optionaldatetime"></a>

The end date of the contract. <br />  Cascade Source: [EmployeeJobs].[ContractEndDate].

##### normal_hours: `Optional[Union[int, float]]`<a id="normal_hours-optionalunionint-float"></a>

Normal hours. <br />  Cascade Source: [EmployeeJobs].[NormalHours].

##### real_time_information_irregular_frequency: `Optional[str]`<a id="real_time_information_irregular_frequency-optionalstr"></a>

The real time information of irregular frequency. <br />  Cascade Source: [EmployeeJobs].[RTIIrregularFrequency].

##### notice_period: `Optional[str]`<a id="notice_period-optionalstr"></a>

The notice period. <br />  Cascade Source: [EmployeeJobs].[NoticePeriod].

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateJobCommand`](./iris_software_group_cascade_python_sdk/type/create_job_command.py)
New Job.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobs` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `irissoftwaregroupcascade.jobs.get_by_id`<a id="irissoftwaregroupcascadejobsget_by_id"></a>

Gets a single Job referenced by an ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = irissoftwaregroupcascade.jobs.get_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Job ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobs/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `irissoftwaregroupcascade.jobs.get_list`<a id="irissoftwaregroupcascadejobsget_list"></a>

Gets a list of Jobs.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = irissoftwaregroupcascade.jobs.get_list(
    top=0,
    skip=0,
    filter="string_example",
    select=[
        "string_example"
    ],
    orderby="string_example",
    count=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### top: `int`<a id="top-int"></a>

Show only the first n items, maximum of 250, see [Paging - Top](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptiontop)

##### skip: `int`<a id="skip-int"></a>

Skip the first n items, see [Paging - Skip](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptionskip)

##### filter: `str`<a id="filter-str"></a>

Filter items by property values, see [Filtering](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptionfilter)

##### select: List[`str`]<a id="select-liststr"></a>

Select properties to be returned, see [Select](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptionselect)

##### orderby: `str`<a id="orderby-str"></a>

Order items by property values, see [Sorting](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptionorderby)

##### count: `bool`<a id="count-bool"></a>

Include count of items, see [Count](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptioncount)

#### 🔄 Return<a id="🔄-return"></a>

[`JobQueryModel`](./iris_software_group_cascade_python_sdk/pydantic/job_query_model.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `irissoftwaregroupcascade.jobs.update_by_id`<a id="irissoftwaregroupcascadejobsupdate_by_id"></a>

Update a Job referenced by an ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
irissoftwaregroupcascade.jobs.update_by_id(
    id="id_example",
    job_title="string_example",
    classification="string_example",
    start_date="1970-01-01T00:00:00.00Z",
    end_date="1970-01-01T00:00:00.00Z",
    working_calendar="string_example",
    line_manager_id="string_example",
    hierarchy_node_id="string_example",
    active=True,
    salary=3.14,
    contract="string_example",
    pay_frequency="string_example",
    pay_basis="string_example",
    full_time_equivalent=3.14,
    change_reason="string_example",
    next_increment_date="1970-01-01T00:00:00.00Z",
    timesheet_location="string_example",
    timesheet_lunch_duration="string_example",
    expense_submission_frequency="string_example",
    cost_centre="string_example",
    job_family="string_example",
    apprentice_under25=True,
    apprenticeship_end_date="1970-01-01T00:00:00.00Z",
    contract_end_date="1970-01-01T00:00:00.00Z",
    normal_hours=3.14,
    real_time_information_irregular_frequency="string_example",
    notice_period="string_example",
    id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID of the Job to update.

##### job_title: `Optional[str]`<a id="job_title-optionalstr"></a>

The title of the Job. <br />  Cascade Source: [EmployeeJobs].[JobTitle]

##### classification: `Optional[str]`<a id="classification-optionalstr"></a>

The classification of the Job e.g. Technical, Professional, Managerial. <br />  Cascade Source: [EmployeeJobs].[Classification] translated through the JOBCLASSIFICATION system list.

##### start_date: `datetime`<a id="start_date-datetime"></a>

The start date of the Job. <br />  Required. <br />  Cascade Source: [EmployeeJobs].[SYS_EffectiveDate]

##### end_date: `Optional[datetime]`<a id="end_date-optionaldatetime"></a>

The end date of the Job. <br />  Automatically Calculated. <br />  Cascade Source: [EmployeeJobs].[SYS_CalculatedEndDate]

##### working_calendar: `Optional[str]`<a id="working_calendar-optionalstr"></a>

The name of the working calendar of the Job. <br />  Cascade Source: [EmployeeJobs].[CalendarName] which comes from [ValidWorkingCalendar].[CalendarName]

##### line_manager_id: `Optional[str]`<a id="line_manager_id-optionalstr"></a>

The ID of the Employee that is the line manager for this Job. <br />  Must exist in Employees Service. <br />  Cascade Source: [EmployeeJobs].[WorksForEmployeeId]

##### hierarchy_node_id: `Optional[str]`<a id="hierarchy_node_id-optionalstr"></a>

The ID of the Employee's Hierarchy node of the Job. <br />  Must exist in Hierarchy Service.

##### active: `bool`<a id="active-bool"></a>

The Job is currently active. <br />  Automatically Calculated. <br />  Cascade Source: [EmployeeJobs].[sys_ActiveJob]

##### salary: `Optional[Union[int, float]]`<a id="salary-optionalunionint-float"></a>

The salary of the Job. <br />  Cascade Source: [EmployeeJobs].[BasicPay]

##### contract: `Optional[str]`<a id="contract-optionalstr"></a>

The contract of the Job e.g. Full Time, Part Time. <br />  Cascade Source: [EmployeeJobs].[ContractType] translated through the EMPLOYMENTTYPES system list.

##### pay_frequency: `Optional[str]`<a id="pay_frequency-optionalstr"></a>

How often the Job's salary will be paid e.g. Monthly, Weekly. <br />  Cascade Source: [EmployeeJobs].[PayFrequency] translated through the PAY FREQ system list.

##### pay_basis: `Optional[str]`<a id="pay_basis-optionalstr"></a>

The unit of measurement the salary is specified against e.g. Yearly, Hourly. <br />  Cascade Source: [EmployeeJobs].[PayBasis] translated through the PAY BASIS system list.

##### full_time_equivalent: `Optional[Union[int, float]]`<a id="full_time_equivalent-optionalunionint-float"></a>

The full-time equivalent to a full time employee's hours e.g. 1 = Full Time, 0.5 = Half Hours. <br />  Cascade Source: [EmployeeJobs].[FTE].

##### change_reason: `Optional[str]`<a id="change_reason-optionalstr"></a>

The reason for the change. <br />  Cascade Source: [EmployeeJobs].[Reason].

##### next_increment_date: `Optional[datetime]`<a id="next_increment_date-optionaldatetime"></a>

The next increment date.  <br />  Cascade Source: [EmployeeJobs].[IncrementDate].

##### timesheet_location: `Optional[str]`<a id="timesheet_location-optionalstr"></a>

The timesheet location. <br />  Cascade Source: [EmployeeJobs].[TimesheetLocation].

##### timesheet_lunch_duration: `Optional[str]`<a id="timesheet_lunch_duration-optionalstr"></a>

The time set lunch duration. <br />  Cascade Source: [EmployeeJobs].[LunchDuration].

##### expense_submission_frequency: `Optional[str]`<a id="expense_submission_frequency-optionalstr"></a>

The expense submission frequency. <br />  Cascade Source: [EmployeeJobs].[ExpenseSubmissionFrequency].

##### cost_centre: `Optional[str]`<a id="cost_centre-optionalstr"></a>

The cost centre. <br />  Cascade Source: [EmployeeJobs].[CostCentre].

##### job_family: `Optional[str]`<a id="job_family-optionalstr"></a>

The job family. <br />  Cascade Source: [EmployeeJobs].[JobFamily].

##### apprentice_under25: `Optional[bool]`<a id="apprentice_under25-optionalbool"></a>

The flag to indicate if the employee is an apprentice under 25. <br />  Cascade Source: [EmployeeJobs].[ApprenticeUnder25].

##### apprenticeship_end_date: `Optional[datetime]`<a id="apprenticeship_end_date-optionaldatetime"></a>

The end date of the apprenticeship. <br />  Cascade Source: [EmployeeJobs].[ApprenticeshipEndDate].

##### contract_end_date: `Optional[datetime]`<a id="contract_end_date-optionaldatetime"></a>

The end date of the contract. <br />  Cascade Source: [EmployeeJobs].[ContractEndDate].

##### normal_hours: `Optional[Union[int, float]]`<a id="normal_hours-optionalunionint-float"></a>

Normal hours. <br />  Cascade Source: [EmployeeJobs].[NormalHours].

##### real_time_information_irregular_frequency: `Optional[str]`<a id="real_time_information_irregular_frequency-optionalstr"></a>

The real time information of irregular frequency. <br />  Cascade Source: [EmployeeJobs].[RTIIrregularFrequency].

##### notice_period: `Optional[str]`<a id="notice_period-optionalstr"></a>

The notice period. <br />  Cascade Source: [EmployeeJobs].[NoticePeriod].

##### id: `Optional[str]`<a id="id-optionalstr"></a>

The ID of the Job to update. <br />  Must exist in the Jobs Service.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateJobCommand`](./iris_software_group_cascade_python_sdk/type/update_job_command.py)
The new state of the Job.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/jobs/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `irissoftwaregroupcascade.public_holidays.get_location_list_by_id`<a id="irissoftwaregroupcascadepublic_holidaysget_location_list_by_id"></a>

Gets a location based Public Holiday list by ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_location_list_by_id_response = irissoftwaregroupcascade.public_holidays.get_location_list_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

Public Holiday ID.

#### 🔄 Return<a id="🔄-return"></a>

[`PublicHolidayModel`](./iris_software_group_cascade_python_sdk/pydantic/public_holiday_model.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/publicholidays/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `irissoftwaregroupcascade.public_holidays.get_locations`<a id="irissoftwaregroupcascadepublic_holidaysget_locations"></a>

Gets a set of Public Holidays with locations.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_locations_response = irissoftwaregroupcascade.public_holidays.get_locations(
    top=0,
    skip=0,
    filter="string_example",
    select=[
        "string_example"
    ],
    orderby="string_example",
    count=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### top: `int`<a id="top-int"></a>

Show only the first n items, maximum of 250, see [Paging - Top](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptiontop)

##### skip: `int`<a id="skip-int"></a>

Skip the first n items, see [Paging - Skip](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptionskip)

##### filter: `str`<a id="filter-str"></a>

Filter items by property values, see [Filtering](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptionfilter)

##### select: List[`str`]<a id="select-liststr"></a>

Select properties to be returned, see [Select](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptionselect)

##### orderby: `str`<a id="orderby-str"></a>

Order items by property values, see [Sorting](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptionorderby)

##### count: `bool`<a id="count-bool"></a>

Include count of items, see [Count](https://docs.oasis-open.org/odata/odata/v4.01/odata-v4.01-part1-protocol.html#sec_SystemQueryOptioncount)

#### 🔄 Return<a id="🔄-return"></a>

[`PublicHolidayQueryModel`](./iris_software_group_cascade_python_sdk/pydantic/public_holiday_query_model.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/publicholidays` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
