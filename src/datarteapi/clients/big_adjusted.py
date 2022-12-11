from datetime import date, datetime
from typing import ClassVar, Dict, Literal, Optional, Tuple, Union

from datarteapi.apiresponse import APIResponse
from datarteapi.typing import SCT, SERVICE_POINT_TYPE
from datarteapi.utils import to_utc_datetime

from .base_client import BaseClient


class BigAdjusted(BaseClient):
    """Big Adjusted API.

    `API Reference <https://data.rte-france.com/catalog/-/api/partners/Big-Adjusted/v2.0>`_
    """

    default_base_url: ClassVar[str] = "https://digital.iservices.rte-france.com/private_api/adjusted_consumption/v2/"
    api_version: ClassVar[tuple[int, int, int]] = (2, 0, 0)

    def get_updated_data(
        self,
        update_date: date,
        update_time_slot: Optional[Literal[1, 2, 3]] = None,
        range: Optional[Tuple[int, int]] = None,
        service_point_type: Optional[SCT[SERVICE_POINT_TYPE]] = None,
    ) -> APIResponse:
        params: Dict[str, Union[str, int]] = {"update_date": update_date.strftime("%Y-%m-%dT00:00:00Z")}
        if update_time_slot is not None:
            params["update_time_slot"] = update_time_slot
        if range is not None:
            params["range"] = f"{range[0]}-{range[1]}"
        if service_point_type is not None:
            params["service_point_type"] = (
                service_point_type if isinstance(service_point_type, str) else ",".join(service_point_type)
            )
        return self._get("updated_data", params=params)

    def get_detailed(
        self,
        start_date: datetime,
        end_date: datetime,
        market_evaluation_point_id: SCT[str],
        data_type: Optional[SCT[Literal["Z56", "Z53"]]] = None,
    ) -> APIResponse:
        params = {
            "start_date": to_utc_datetime(start_date).isoformat().replace("+00:00", "Z"),
            "end_date": to_utc_datetime(end_date).isoformat().replace("+00:00", "Z"),
        }
        params["market_evaluation_point_id"] = (
            market_evaluation_point_id
            if isinstance(market_evaluation_point_id, str)
            else ",".join(market_evaluation_point_id)
        )
        if data_type is not None:
            params["data_type"] = data_type if isinstance(data_type, str) else ",".join(data_type)

        return self._get("detailed/PT10M", params=params)
