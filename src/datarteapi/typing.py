from typing import Collection, Literal, TypeVar, Union

_CT = TypeVar("_CT")

SCT = Union[_CT, Collection[_CT]]
"""Single instance or collection of instances."""

# BigSubstations

PDS_DATA_DATA_TYPE = Literal["C06", "C06C", "C06P", "C20"]

EXCHANGE_DATA_DATA_TYPE = Literal["C07", "C08"]

PDS_DATA_RAW_DATA_TYPE = Literal["c06_blanc", "c06c_blanc", "c06p_blanc", "c06_brut", "c06c_brut", "c06p_brut"]

# UnavailabilityAdditionalInformation

UNAVAILABILITY_STATUS = Literal["DISMISSED", "ACTIVE", "INACTIVE"]

COUNTRY_EIC_CODE = Literal[
    "10YCB-GERMANY--8",
    "10YGB----------A",
    "10Y1001C--00098F",
    "17Y0000009369493",
    "10YBE----------2",
    "10YIT-GRTN-----B",
    "10YES-REE------0",
    "10YCH-SWISSGRIDZ",
    "11Y0-0000-0265-K",
]

DATE_TYPE = Literal["APPLICATION_DATE", "UPDATED_DATE"]

# BigAdjusted

SERVICE_POINT_TYPE = Literal["SDS", "VIR", "GDP", "AUX"]

# BalancingCapacity

MARGE_TYPE = Literal[
    "forecastedImbalanceRs",
    "availableMarginsComplemantaryDown",
    "availableMarginsComplemantaryUp",
    "availableMarginsNormalDown",
    "availableMarginsNormalUp",
    "availableMarginsReliefDown",
    "availableMarginsReliefUp",
    "requiredMarginsOperationnalDown",
    "requiredMarginsOperationnalUp",
]
