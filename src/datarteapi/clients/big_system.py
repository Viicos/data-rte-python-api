from datetime import datetime
from typing import ClassVar, Dict, Literal, Optional, Tuple, Union

from datarteapi.apiresponse import APIResponse
from datarteapi.typing import SCT
from datarteapi.utils import to_utc_datetime

from .base_client import BaseClient


class BigSystem(BaseClient):
    """Big System API.

    `API Reference <https://data.rte-france.com/catalog/-/api/partners/Big-System/v1.2>`_
    """

    default_base_url: ClassVar[str] = "https://digital.iservices.rte-france.com/private_api/validated_system_data/v1/"
    api_version: ClassVar[tuple[int, int, int]] = (1, 2, 2)

    def get_updated_data(
        self,
        update_date: datetime,
        update_time_slot: Optional[Literal[1, 2, 3]] = None,
        range: Optional[Tuple[int, int]] = None,
    ) -> APIResponse:
        params: Dict[str, Union[str, int]] = {
            "update_date": to_utc_datetime(update_date).isoformat().replace("+00:00", "Z")
        }
        if update_time_slot is not None:
            params["update_time_slot"] = update_time_slot
        if range is not None:
            params["range"] = f"{range[0]}-{range[1]}"
        return self._get("updated_data", params=params)

    def get_validated_points(
        self,
        start_date: datetime,
        end_date: datetime,
        market_evaluation_point_id: SCT[str],
        product: Optional[SCT[str]] = None,
        values_status: Optional[str] = None,
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
        if product is not None:
            params["product"] = product if isinstance(product, str) else ",".join(product)
        if values_status is not None:
            params["values_status"] = values_status

        return self._get("validated_points/PT10M", params=params)

    def create_applied_ps(
        self,
        company_eic_code: str,
        start_date: datetime,
        end_date: datetime,
        market_evaluation_point_id: SCT[str],
        max_return: Optional[int] = None,
        superior_at: Optional[int] = None,
    ) -> APIResponse:
        json = {
            "company_eic_code": company_eic_code,
            "start_date": to_utc_datetime(start_date).isoformat().replace("+00:00", "Z"),
            "end_date": to_utc_datetime(end_date).isoformat().replace("+00:00", "Z"),
            "market_evaluation_point_id": [market_evaluation_point_id]
            if isinstance(market_evaluation_point_id, str)
            else list(market_evaluation_point_id),
        }
        params: Dict[str, int] = {}
        if max_return is not None:
            params["max_return"] = max_return
        if superior_at is not None:
            params["superior_at"] = superior_at

        return self._post("applied_ps", params=params, json=json)
