from datetime import date
from typing import Any, ClassVar, Dict, Optional, Union

from typing_extensions import Literal

from datarteapi.apiresponse import APIResponse
from datarteapi.typing import PLIC_TYPE, SCT

from .base_client import BaseClient


class Tariff(BaseClient):
    """Tariff API.

    `API Reference <https://data.rte-france.com/catalog/-/api/partners/Tariff/v1.3>`_
    """

    default_base_url: ClassVar[str] = "https://digital.iservices.rte-france.com/private_api/tariff/v1/"
    api_version: ClassVar[tuple[int, int]] = (1, 3)

    def get_plics_eligibility(
        self,
        request_type: Literal["P", "V", "D"],
        permanent_contextual_eligibility: Literal["PE", "CO", "PC"],
        plic_type: PLIC_TYPE,
        plics: SCT[str],
        application_date: Optional[date] = None,
        max_return: Optional[int] = None,
        superior_at: Optional[int] = None,
    ) -> APIResponse:
        json: Dict[str, Any] = {
            "request_type": request_type,
            "permanent_contextual_eligibility": permanent_contextual_eligibility,
            "plic_type": plic_type,
            "plics": [plics] if isinstance(plics, str) else list(plics),
        }
        if application_date is not None:
            json["application_date"] = application_date.strftime("%Y%m%d")

        params: Dict[str, int] = {}
        if max_return is not None:
            params["max_return"] = max_return
        if superior_at is not None:
            params["superior_at"] = superior_at

        return self._post("plics/eligibility", params=params, json=json)

    def get_plics_state(
        self,
        plic_type: PLIC_TYPE,
        plics: SCT[str],
        max_return: Optional[int] = None,
        superior_at: Optional[int] = None,
        order_by: Optional[str] = None,
    ) -> APIResponse:
        json: Dict[str, Any] = {"plic_type": plic_type, "plics": [plics] if isinstance(plics, str) else list(plics)}

        params: Dict[str, Union[str, int]] = {}
        if max_return is not None:
            params["max_return"] = max_return
        if superior_at is not None:
            params["superior_at"] = superior_at
        if order_by is not None:
            params["order_by"] = order_by

        return self._post("plics/state", params=params, json=json)

    def get_plics_ps_historic(
        self,
        plic_type: PLIC_TYPE,
        plic_id: str,
        max_return: Optional[int] = None,
        superior_at: Optional[int] = None,
    ) -> APIResponse:
        json: Dict[str, Any] = {"plic_type": plic_type, "plic_id": plic_id}

        params: Dict[str, int] = {}
        if max_return is not None:
            params["max_return"] = max_return
        if superior_at is not None:
            params["superior_at"] = superior_at

        return self._post("plics/ps/historic", params=params, json=json)

    def get_plics_vt_historic(
        self,
        plic_type: PLIC_TYPE,
        plic_id: str,
        max_return: Optional[int] = None,
        superior_at: Optional[int] = None,
    ) -> APIResponse:
        json: Dict[str, Any] = {"plic_type": plic_type, "plic_id": plic_id}

        params: Dict[str, int] = {}
        if max_return is not None:
            params["max_return"] = max_return
        if superior_at is not None:
            params["superior_at"] = superior_at

        return self._post("plics/vt/historic", params=params, json=json)

    def get_ps_requests_status(
        self,
        establishment_ref_id: str,
        request_number: SCT[str],
        max_return: Optional[int] = None,
        superior_at: Optional[int] = None,
    ) -> APIResponse:
        json: Dict[str, Any] = {
            "establishment_ref_id": establishment_ref_id,
            "request_number": [request_number] if isinstance(request_number, str) else list(request_number),
        }

        params: Dict[str, int] = {}
        if max_return is not None:
            params["max_return"] = max_return
        if superior_at is not None:
            params["superior_at"] = superior_at

        return self._post("ps_requests/status", params=params, json=json)

    def get_ps_requests_historic(
        self,
        plic_type: PLIC_TYPE,
        plics: SCT[str],
        status: SCT[str],
        request_number: Optional[str] = None,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        max_return: Optional[int] = None,
        superior_at: Optional[int] = None,
        order_by: Optional[str] = None,
    ) -> APIResponse:
        json: Dict[str, Any] = {
            "plic_type": plic_type,
            "plics": [plics] if isinstance(plics, str) else list(plics),
            "status": [status] if isinstance(status, str) else list(status),
        }
        if request_number is not None:
            json["request_number"] = request_number
        if start_date is not None:
            json["start_date"] = start_date.strftime("%Y%m%d")
        if end_date is not None:
            json["end_date"] = end_date.strftime("%Y%m%d")

        params: Dict[str, Union[str, int]] = {}
        if max_return is not None:
            params["max_return"] = max_return
        if superior_at is not None:
            params["superior_at"] = superior_at
        if order_by is not None:
            params["order_by"] = order_by

        return self._post("ps_requests/historic", params=params, json=json)

    def get_dpp_requests_status(
        self,
        establishment_ref_id: str,
        request_number: SCT[str],
        max_return: Optional[int] = None,
        superior_at: Optional[int] = None,
    ) -> APIResponse:
        json: Dict[str, Any] = {
            "establishment_ref_id": establishment_ref_id,
            "request_number": [request_number] if isinstance(request_number, str) else list(request_number),
        }

        params: Dict[str, int] = {}
        if max_return is not None:
            params["max_return"] = max_return
        if superior_at is not None:
            params["superior_at"] = superior_at

        return self._post("dpp_requests/status", params=params, json=json)

    def get_dpp_requests_historic(
        self,
        plic_type: PLIC_TYPE,
        plics: SCT[str],
        status: SCT[str],
        request_number: Optional[str] = None,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        max_return: Optional[int] = None,
        superior_at: Optional[int] = None,
        order_by: Optional[str] = None,
    ) -> APIResponse:
        json: Dict[str, Any] = {
            "plic_type": plic_type,
            "plics": [plics] if isinstance(plics, str) else list(plics),
            "status": [status] if isinstance(status, str) else list(status),
        }
        if request_number is not None:
            json["request_number"] = request_number
        if start_date is not None:
            json["start_date"] = start_date.strftime("%Y%m%d")
        if end_date is not None:
            json["end_date"] = end_date.strftime("%Y%m%d")

        params: Dict[str, Union[str, int]] = {}
        if max_return is not None:
            params["max_return"] = max_return
        if superior_at is not None:
            params["superior_at"] = superior_at
        if order_by is not None:
            params["order_by"] = order_by

        return self._post("dpp_requests/historic", params=params, json=json)

    def get_vt_requests_status(
        self,
        establishment_ref_id: str,
        request_number: SCT[str],
        max_return: Optional[int] = None,
        superior_at: Optional[int] = None,
    ) -> APIResponse:
        json: Dict[str, Any] = {
            "establishment_ref_id": establishment_ref_id,
            "request_number": [request_number] if isinstance(request_number, str) else list(request_number),
        }

        params: Dict[str, int] = {}
        if max_return is not None:
            params["max_return"] = max_return
        if superior_at is not None:
            params["superior_at"] = superior_at

        return self._post("vt_requests/status", params=params, json=json)

    def get_vt_requests_historic(
        self,
        plic_type: PLIC_TYPE,
        plics: SCT[str],
        status: SCT[str],
        request_number: Optional[str] = None,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        max_return: Optional[int] = None,
        superior_at: Optional[int] = None,
        order_by: Optional[str] = None,
    ) -> APIResponse:
        json: Dict[str, Any] = {
            "plic_type": plic_type,
            "plics": [plics] if isinstance(plics, str) else list(plics),
            "status": [status] if isinstance(status, str) else list(status),
        }
        if request_number is not None:
            json["request_number"] = request_number
        if start_date is not None:
            json["start_date"] = start_date.strftime("%Y%m%d")
        if end_date is not None:
            json["end_date"] = end_date.strftime("%Y%m%d")

        params: Dict[str, Union[str, int]] = {}
        if max_return is not None:
            params["max_return"] = max_return
        if superior_at is not None:
            params["superior_at"] = superior_at
        if order_by is not None:
            params["order_by"] = order_by

        return self._post("vt_requests/historic", params=params, json=json)
