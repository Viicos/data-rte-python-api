from typing import Any, ClassVar, Dict

from .base_client import BaseClient


class BalancingImbalancesAccount(BaseClient):
    """Balancing Imbalances Account API.

    `API Reference <https://data.rte-france.com/catalog/-/api/market/Balancing-Imbalances-Account/v1.0>`_
    """

    default_base_url: ClassVar[
        str
    ] = "https://digital.iservices.rte-france.com/open_api/balancing_imbalances_account/v1/"
    api_version: ClassVar[tuple[int, int, int]] = (1, 0, 1)

    def get_coefficient_k(self, application_month: str) -> Dict[str, Any]:
        params = {"application_month": application_month}
        return self._get("coefficient_k", params=params)
