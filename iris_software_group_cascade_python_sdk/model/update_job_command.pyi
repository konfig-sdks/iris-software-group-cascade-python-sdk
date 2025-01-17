# coding: utf-8

"""
    HR API

    <a href='swaggerv2.json'>Download Swagger Json in OAS2 Format.</a>

    The version of the OpenAPI document: 2
    Contact: hrapi@iris.co.uk
    Created by: https://help.iris.co.uk/hr/cascade/api/
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from iris_software_group_cascade_python_sdk import schemas  # noqa: F401


class UpdateJobCommand(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class JobTitle(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'JobTitle':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class Classification(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Classification':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            StartDate = schemas.DateTimeSchema
            
            
            class EndDate(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'EndDate':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class WorkingCalendar(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'WorkingCalendar':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class LineManagerId(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'LineManagerId':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class HierarchyNodeId(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'HierarchyNodeId':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            Active = schemas.BoolSchema
            
            
            class Salary(
                schemas.Float64Base,
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'double'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Salary':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class Contract(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Contract':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class PayFrequency(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'PayFrequency':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class PayBasis(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'PayBasis':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class FullTimeEquivalent(
                schemas.Float64Base,
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'double'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'FullTimeEquivalent':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class ChangeReason(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ChangeReason':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class NextIncrementDate(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'NextIncrementDate':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class TimesheetLocation(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'TimesheetLocation':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class TimesheetLunchDuration(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'TimesheetLunchDuration':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class ExpenseSubmissionFrequency(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ExpenseSubmissionFrequency':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class CostCentre(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'CostCentre':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class JobFamily(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'JobFamily':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class ApprenticeUnder25(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ApprenticeUnder25':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class ApprenticeshipEndDate(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ApprenticeshipEndDate':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class ContractEndDate(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ContractEndDate':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class NormalHours(
                schemas.Float64Base,
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'double'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'NormalHours':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class RealTimeInformationIrregularFrequency(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'RealTimeInformationIrregularFrequency':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class NoticePeriod(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'NoticePeriod':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class Id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "JobTitle": JobTitle,
                "Classification": Classification,
                "StartDate": StartDate,
                "EndDate": EndDate,
                "WorkingCalendar": WorkingCalendar,
                "LineManagerId": LineManagerId,
                "HierarchyNodeId": HierarchyNodeId,
                "Active": Active,
                "Salary": Salary,
                "Contract": Contract,
                "PayFrequency": PayFrequency,
                "PayBasis": PayBasis,
                "FullTimeEquivalent": FullTimeEquivalent,
                "ChangeReason": ChangeReason,
                "NextIncrementDate": NextIncrementDate,
                "TimesheetLocation": TimesheetLocation,
                "TimesheetLunchDuration": TimesheetLunchDuration,
                "ExpenseSubmissionFrequency": ExpenseSubmissionFrequency,
                "CostCentre": CostCentre,
                "JobFamily": JobFamily,
                "ApprenticeUnder25": ApprenticeUnder25,
                "ApprenticeshipEndDate": ApprenticeshipEndDate,
                "ContractEndDate": ContractEndDate,
                "NormalHours": NormalHours,
                "RealTimeInformationIrregularFrequency": RealTimeInformationIrregularFrequency,
                "NoticePeriod": NoticePeriod,
                "Id": Id,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["JobTitle"]) -> MetaOapg.properties.JobTitle: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Classification"]) -> MetaOapg.properties.Classification: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["StartDate"]) -> MetaOapg.properties.StartDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EndDate"]) -> MetaOapg.properties.EndDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["WorkingCalendar"]) -> MetaOapg.properties.WorkingCalendar: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LineManagerId"]) -> MetaOapg.properties.LineManagerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["HierarchyNodeId"]) -> MetaOapg.properties.HierarchyNodeId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Active"]) -> MetaOapg.properties.Active: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Salary"]) -> MetaOapg.properties.Salary: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Contract"]) -> MetaOapg.properties.Contract: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PayFrequency"]) -> MetaOapg.properties.PayFrequency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PayBasis"]) -> MetaOapg.properties.PayBasis: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FullTimeEquivalent"]) -> MetaOapg.properties.FullTimeEquivalent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ChangeReason"]) -> MetaOapg.properties.ChangeReason: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["NextIncrementDate"]) -> MetaOapg.properties.NextIncrementDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TimesheetLocation"]) -> MetaOapg.properties.TimesheetLocation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TimesheetLunchDuration"]) -> MetaOapg.properties.TimesheetLunchDuration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ExpenseSubmissionFrequency"]) -> MetaOapg.properties.ExpenseSubmissionFrequency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CostCentre"]) -> MetaOapg.properties.CostCentre: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["JobFamily"]) -> MetaOapg.properties.JobFamily: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ApprenticeUnder25"]) -> MetaOapg.properties.ApprenticeUnder25: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ApprenticeshipEndDate"]) -> MetaOapg.properties.ApprenticeshipEndDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ContractEndDate"]) -> MetaOapg.properties.ContractEndDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["NormalHours"]) -> MetaOapg.properties.NormalHours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["RealTimeInformationIrregularFrequency"]) -> MetaOapg.properties.RealTimeInformationIrregularFrequency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["NoticePeriod"]) -> MetaOapg.properties.NoticePeriod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Id"]) -> MetaOapg.properties.Id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["JobTitle", "Classification", "StartDate", "EndDate", "WorkingCalendar", "LineManagerId", "HierarchyNodeId", "Active", "Salary", "Contract", "PayFrequency", "PayBasis", "FullTimeEquivalent", "ChangeReason", "NextIncrementDate", "TimesheetLocation", "TimesheetLunchDuration", "ExpenseSubmissionFrequency", "CostCentre", "JobFamily", "ApprenticeUnder25", "ApprenticeshipEndDate", "ContractEndDate", "NormalHours", "RealTimeInformationIrregularFrequency", "NoticePeriod", "Id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["JobTitle"]) -> typing.Union[MetaOapg.properties.JobTitle, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Classification"]) -> typing.Union[MetaOapg.properties.Classification, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["StartDate"]) -> typing.Union[MetaOapg.properties.StartDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EndDate"]) -> typing.Union[MetaOapg.properties.EndDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["WorkingCalendar"]) -> typing.Union[MetaOapg.properties.WorkingCalendar, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LineManagerId"]) -> typing.Union[MetaOapg.properties.LineManagerId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["HierarchyNodeId"]) -> typing.Union[MetaOapg.properties.HierarchyNodeId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Active"]) -> typing.Union[MetaOapg.properties.Active, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Salary"]) -> typing.Union[MetaOapg.properties.Salary, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Contract"]) -> typing.Union[MetaOapg.properties.Contract, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PayFrequency"]) -> typing.Union[MetaOapg.properties.PayFrequency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PayBasis"]) -> typing.Union[MetaOapg.properties.PayBasis, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FullTimeEquivalent"]) -> typing.Union[MetaOapg.properties.FullTimeEquivalent, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ChangeReason"]) -> typing.Union[MetaOapg.properties.ChangeReason, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["NextIncrementDate"]) -> typing.Union[MetaOapg.properties.NextIncrementDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TimesheetLocation"]) -> typing.Union[MetaOapg.properties.TimesheetLocation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TimesheetLunchDuration"]) -> typing.Union[MetaOapg.properties.TimesheetLunchDuration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ExpenseSubmissionFrequency"]) -> typing.Union[MetaOapg.properties.ExpenseSubmissionFrequency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CostCentre"]) -> typing.Union[MetaOapg.properties.CostCentre, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["JobFamily"]) -> typing.Union[MetaOapg.properties.JobFamily, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ApprenticeUnder25"]) -> typing.Union[MetaOapg.properties.ApprenticeUnder25, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ApprenticeshipEndDate"]) -> typing.Union[MetaOapg.properties.ApprenticeshipEndDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ContractEndDate"]) -> typing.Union[MetaOapg.properties.ContractEndDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["NormalHours"]) -> typing.Union[MetaOapg.properties.NormalHours, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["RealTimeInformationIrregularFrequency"]) -> typing.Union[MetaOapg.properties.RealTimeInformationIrregularFrequency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["NoticePeriod"]) -> typing.Union[MetaOapg.properties.NoticePeriod, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Id"]) -> typing.Union[MetaOapg.properties.Id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["JobTitle", "Classification", "StartDate", "EndDate", "WorkingCalendar", "LineManagerId", "HierarchyNodeId", "Active", "Salary", "Contract", "PayFrequency", "PayBasis", "FullTimeEquivalent", "ChangeReason", "NextIncrementDate", "TimesheetLocation", "TimesheetLunchDuration", "ExpenseSubmissionFrequency", "CostCentre", "JobFamily", "ApprenticeUnder25", "ApprenticeshipEndDate", "ContractEndDate", "NormalHours", "RealTimeInformationIrregularFrequency", "NoticePeriod", "Id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        JobTitle: typing.Union[MetaOapg.properties.JobTitle, None, str, schemas.Unset] = schemas.unset,
        Classification: typing.Union[MetaOapg.properties.Classification, None, str, schemas.Unset] = schemas.unset,
        StartDate: typing.Union[MetaOapg.properties.StartDate, str, datetime, schemas.Unset] = schemas.unset,
        EndDate: typing.Union[MetaOapg.properties.EndDate, None, str, datetime, schemas.Unset] = schemas.unset,
        WorkingCalendar: typing.Union[MetaOapg.properties.WorkingCalendar, None, str, schemas.Unset] = schemas.unset,
        LineManagerId: typing.Union[MetaOapg.properties.LineManagerId, None, str, schemas.Unset] = schemas.unset,
        HierarchyNodeId: typing.Union[MetaOapg.properties.HierarchyNodeId, None, str, schemas.Unset] = schemas.unset,
        Active: typing.Union[MetaOapg.properties.Active, bool, schemas.Unset] = schemas.unset,
        Salary: typing.Union[MetaOapg.properties.Salary, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        Contract: typing.Union[MetaOapg.properties.Contract, None, str, schemas.Unset] = schemas.unset,
        PayFrequency: typing.Union[MetaOapg.properties.PayFrequency, None, str, schemas.Unset] = schemas.unset,
        PayBasis: typing.Union[MetaOapg.properties.PayBasis, None, str, schemas.Unset] = schemas.unset,
        FullTimeEquivalent: typing.Union[MetaOapg.properties.FullTimeEquivalent, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        ChangeReason: typing.Union[MetaOapg.properties.ChangeReason, None, str, schemas.Unset] = schemas.unset,
        NextIncrementDate: typing.Union[MetaOapg.properties.NextIncrementDate, None, str, datetime, schemas.Unset] = schemas.unset,
        TimesheetLocation: typing.Union[MetaOapg.properties.TimesheetLocation, None, str, schemas.Unset] = schemas.unset,
        TimesheetLunchDuration: typing.Union[MetaOapg.properties.TimesheetLunchDuration, None, str, schemas.Unset] = schemas.unset,
        ExpenseSubmissionFrequency: typing.Union[MetaOapg.properties.ExpenseSubmissionFrequency, None, str, schemas.Unset] = schemas.unset,
        CostCentre: typing.Union[MetaOapg.properties.CostCentre, None, str, schemas.Unset] = schemas.unset,
        JobFamily: typing.Union[MetaOapg.properties.JobFamily, None, str, schemas.Unset] = schemas.unset,
        ApprenticeUnder25: typing.Union[MetaOapg.properties.ApprenticeUnder25, None, bool, schemas.Unset] = schemas.unset,
        ApprenticeshipEndDate: typing.Union[MetaOapg.properties.ApprenticeshipEndDate, None, str, datetime, schemas.Unset] = schemas.unset,
        ContractEndDate: typing.Union[MetaOapg.properties.ContractEndDate, None, str, datetime, schemas.Unset] = schemas.unset,
        NormalHours: typing.Union[MetaOapg.properties.NormalHours, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        RealTimeInformationIrregularFrequency: typing.Union[MetaOapg.properties.RealTimeInformationIrregularFrequency, None, str, schemas.Unset] = schemas.unset,
        NoticePeriod: typing.Union[MetaOapg.properties.NoticePeriod, None, str, schemas.Unset] = schemas.unset,
        Id: typing.Union[MetaOapg.properties.Id, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UpdateJobCommand':
        return super().__new__(
            cls,
            *args,
            JobTitle=JobTitle,
            Classification=Classification,
            StartDate=StartDate,
            EndDate=EndDate,
            WorkingCalendar=WorkingCalendar,
            LineManagerId=LineManagerId,
            HierarchyNodeId=HierarchyNodeId,
            Active=Active,
            Salary=Salary,
            Contract=Contract,
            PayFrequency=PayFrequency,
            PayBasis=PayBasis,
            FullTimeEquivalent=FullTimeEquivalent,
            ChangeReason=ChangeReason,
            NextIncrementDate=NextIncrementDate,
            TimesheetLocation=TimesheetLocation,
            TimesheetLunchDuration=TimesheetLunchDuration,
            ExpenseSubmissionFrequency=ExpenseSubmissionFrequency,
            CostCentre=CostCentre,
            JobFamily=JobFamily,
            ApprenticeUnder25=ApprenticeUnder25,
            ApprenticeshipEndDate=ApprenticeshipEndDate,
            ContractEndDate=ContractEndDate,
            NormalHours=NormalHours,
            RealTimeInformationIrregularFrequency=RealTimeInformationIrregularFrequency,
            NoticePeriod=NoticePeriod,
            Id=Id,
            _configuration=_configuration,
            **kwargs,
        )
