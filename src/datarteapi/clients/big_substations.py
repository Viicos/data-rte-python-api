from datetime import datetime
from typing import Any, ClassVar, Dict, Literal, Optional, Union

from datarteapi.typing import EXCHANGE_DATA_DATA_TYPE, PDS_DATA_DATA_TYPE, PDS_DATA_RAW_DATA_TYPE, SCT
from datarteapi.utils import to_utc_datetime

from .base_client import BaseClient

datetime.fromisoformat("2017-09-01T12:00:00Z")

class BigSubstations(BaseClient):
    """Big Substations API.

    `API Reference <https://data.rte-france.com/catalog/-/api/partners/Big-Substations/v1.1>`_
    """

    default_base_url: ClassVar[str] = "https://digital.iservices.rte-france.com/private_api/big_substations/v1/"
    api_version: ClassVar[tuple[int, int, int]] = (1, 1, 1)

    def _get_data(
        self,
        endpoint: str,
        resolution: str,
        start_date: datetime,
        end_date: datetime,
        eic_dso: Optional[SCT[str]] = None,
        data_type: Optional[SCT[Union[PDS_DATA_DATA_TYPE, EXCHANGE_DATA_DATA_TYPE, PDS_DATA_RAW_DATA_TYPE]]] = None,
    ) -> Dict[str, Any]:
        params = {
            "start_date": to_utc_datetime(start_date).isoformat().replace("+00:00", "Z"),
            "end_date": to_utc_datetime(end_date).isoformat().replace("+00:00", "Z"),
        }
        if eic_dso is not None:
            params["eic_dso"] = eic_dso if isinstance(eic_dso, str) else ",".join(eic_dso)
        if data_type is not None:
            params["data_type"] = data_type if isinstance(data_type, str) else ",".join(data_type)

        return self._get(f"{endpoint}/{resolution}")

    def get_pds_data(
        self,
        start_date: datetime,
        end_date: datetime,
        eic_dso: Optional[SCT[str]] = None,
        data_type: Optional[SCT[PDS_DATA_DATA_TYPE]] = None,
    ) -> Dict[str, Any]:
        return self._get_data("pds_data", "PT30M", start_date, end_date, eic_dso, data_type)

    def get_exchange_date(
        self,
        start_date: datetime,
        end_date: datetime,
        eic_dso: Optional[SCT[str]] = None,
        data_type: Optional[SCT[EXCHANGE_DATA_DATA_TYPE]] = None,
    ) -> Dict[str, Any]:
        return self._get_data("pds_data", "PT30M", start_date, end_date, eic_dso, data_type)

    def get_pds_data_raw(
        self,
        resolution: Literal["PT15M", "PT30M"],
        start_date: datetime,
        end_date: datetime,
        eic_dso: Optional[SCT[str]] = None,
        data_type: Optional[SCT[PDS_DATA_RAW_DATA_TYPE]] = None,
    ) -> Dict[str, Any]:
        return self._get_data("pds_data_raw", resolution, start_date, end_date, eic_dso, data_type)
