from datetime import datetime
from typing import ClassVar, Dict, Optional

from datarteapi.apiresponse import APIResponse
from datarteapi.typing import COUNTRY_EIC_CODE, DATE_TYPE, SCT, UNAVAILABILITY_STATUS

from .base_client import BaseClient


class UnavailabilityAdditionalInformation(BaseClient):
    """Unavailability Additional Information API.

    `API Reference <https://data.rte-france.com/catalog/-/api/generation/Unavailability-Additional-Information/v4.0>`_
    """

    default_base_url: ClassVar[
        str
    ] = "https://digital.iservices.rte-france.com/open_api/unavailability_additional_information/v4/"
    api_version: ClassVar[tuple[int, int, int]] = (4, 0, 0)

    def get_transmission_network_unavailabilities(
        self,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        status: Optional[SCT[UNAVAILABILITY_STATUS]] = None,
        country_eic_code: Optional[SCT[COUNTRY_EIC_CODE]] = None,
        date_type: Optional[DATE_TYPE] = None,
        last_version: Optional[bool] = None,
    ) -> APIResponse:
        params: Dict[str, str] = {}

        if start_date is not None:
            start_date = start_date.replace(microsecond=0)
            params["start_date"] = start_date.isoformat()
        if end_date is not None:
            end_date = end_date.replace(microsecond=0)
            params["end_date"] = end_date.isoformat()
        if status is not None:
            params["status"] = status if isinstance(status, str) else ",".join(status)
        if country_eic_code is not None:
            params["country_eic_code"] = (
                country_eic_code if isinstance(country_eic_code, str) else ",".join(country_eic_code)
            )
        if date_type is not None:
            params["date_type"] = date_type
        if last_version is not None:
            params["last_version"] = str(last_version).lower()

        return self._get("transmission_network_unavailabilities", params=params)

    def get_transmission_network_unavailabilities_versions(self, identifier: str) -> APIResponse:
        return self._get(f"transmission_network_unavailabilities/{identifier}/versions")

    def get_generation_unavailabilities(
        self,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        status: Optional[SCT[UNAVAILABILITY_STATUS]] = None,
        date_type: Optional[DATE_TYPE] = None,
        last_version: Optional[bool] = None,
    ) -> APIResponse:
        params: Dict[str, str] = {}

        if start_date is not None:
            start_date = start_date.replace(microsecond=0)
            params["start_date"] = start_date.isoformat()
        if end_date is not None:
            end_date = end_date.replace(microsecond=0)
            params["end_date"] = end_date.isoformat()
        if status is not None:
            params["status"] = status if isinstance(status, str) else ",".join(status)
        if date_type is not None:
            params["date_type"] = date_type
        if last_version is not None:
            params["last_version"] = str(last_version).lower()

        return self._get("generation_unavailabilities", params=params)

    def get_generation_unavailabilities_versions(self, identifier: str) -> APIResponse:
        return self._get(f"generation_unavailabilities/{identifier}/versions")

    def get_additional_informations(self, start_date: datetime, end_date: datetime) -> APIResponse:
        params = {
            "start_date": start_date.isoformat(),
            "end_date": end_date.isoformat(),
        }

        return self._get("additional_informations", params=params)
