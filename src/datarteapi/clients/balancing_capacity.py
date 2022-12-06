from datetime import datetime
from typing import Any, ClassVar, Dict, Literal, Optional

from datarteapi.typing import MARGE_TYPE, SCT
from datarteapi.utils import to_utc_datetime

from .base_client import BaseClient


class BalancingCapacity(BaseClient):
    """Balancing Capacity API.

    `API Reference <https://data.rte-france.com/catalog/-/api/market/Balancing-Capacity/v4.1>`_
    """

    default_base_url: ClassVar[str] = "https://digital.iservices.rte-france.com/open_api/balancing_capacity/v4/"
    api_version: ClassVar[tuple[int, int, int]] = (4, 1, 1)

    def _get_data_date(
        self, endpoint: str, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None
    ) -> Dict[str, Any]:
        params: Dict[str, str] = {}
        if start_date is not None:
            start_date = start_date.replace(microsecond=0)
            params["start_date"] = start_date.isoformat()
        if end_date is not None:
            end_date = end_date.replace(microsecond=0)
            params["end_date"] = end_date.isoformat()

        return self._get(endpoint, params=params)

    def get_procured_reserves(
        self, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None
    ) -> Dict[str, Any]:
        return self._get_data_date("procured_reserves", start_date, end_date)

    def get_accepted_offers(
        self, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None
    ) -> Dict[str, Any]:
        return self._get_data_date("accepted_offers", start_date, end_date)

    def get_peak_daily_margins(
        self, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None
    ) -> Dict[str, Any]:
        return self._get_data_date("peak_daily_margins", start_date, end_date)

    def get_insufficients_offers(
        self, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None
    ) -> Dict[str, Any]:
        return self._get_data_date("insufficients_offers", start_date, end_date)

    def get_imbalance(
        self, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None
    ) -> Dict[str, Any]:
        return self._get_data_date("imbalance", start_date, end_date)

    def get_individualoffers_energybids(
        self, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None
    ) -> Dict[str, Any]:
        if not (start_date is not None and end_date is not None):
            raise ValueError("'start_date' and 'end_date' must be specified if one of them is not None")
        return self._get_data_date("individualoffers_energybids", start_date, end_date)

    def get_aggregatedoffers_energybids(
        self, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None
    ) -> Dict[str, Any]:
        if not (start_date is not None and end_date is not None):
            raise ValueError("'start_date' and 'end_date' must be specified if one of them is not None")
        return self._get_data_date("aggregatedoffers_energybids", start_date, end_date)

    def get_daily_procured_reserves(
        self, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None
    ) -> Dict[str, Any]:
        return self._get_data_date("daily_procured_reserves", start_date, end_date)

    def get_tso_need_for_procured_reserves(
        self, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None
    ) -> Dict[str, Any]:
        return self._get_data_date("tso_need_for_procured_reserves", start_date, end_date)

    def get_aggregatedoffers_afrr_energybids(
        self, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None
    ) -> Dict[str, Any]:
        if not (start_date is not None and end_date is not None):
            raise ValueError("'start_date' and 'end_date' must be specified if one of them is not None")
        return self._get_data_date("aggregatedoffers_afrr_energybids", start_date, end_date)

    def get_margins_data(
        self,
        date: datetime,
        sens: Optional[Literal["Up", "Down", "Up&Down"]] = None,
        marge_type: Optional[SCT[MARGE_TYPE]] = None,
    ) -> Dict[str, Any]:
        params = {"date": to_utc_datetime(date).isoformat()}
        if sens is not None:
            params["sens"] = sens
        if marge_type is not None:
            params["type"] = marge_type if isinstance(marge_type, str) else ",".join(marge_type)

        return self._get("margins_data", params=params)
