from typing import ClassVar

from datarteapi.apiresponse import APIResponse

from .base_client import BaseClient


class Ecowatt(BaseClient):
    """Ecowatt API.

    `API Reference <https://data.rte-france.com/catalog/-/api/consumption/Ecowatt/v4.0>`_
    """

    default_base_url: ClassVar[str] = "https://digital.iservices.rte-france.com/open_api/ecowatt/v4/"
    api_version: ClassVar[tuple[int, int, int]] = (4, 0, 1)

    def get_signals(self) -> APIResponse:
        return self._get("signals")
