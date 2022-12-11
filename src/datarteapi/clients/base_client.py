from abc import ABC
from typing import Any, ClassVar, Dict, Optional
from urllib.parse import urljoin

import requests

from datarteapi.apiresponse import APIResponse
from datarteapi.exceptions import APIException, TooManyRequestsAPIException, UnauthenticatedException
from datarteapi.oauth_manager import OAuthManager


class BaseClient(ABC):
    """Abstract base class for the different clients of the RTE APIs.

    Args:
        client_id (:obj:`str`): The client ID of the application.
        client_secret (:obj:`str`): The client secret of the application.
        base_url (:obj:`str`, optional): The base URL of the API. Will override the default one if provided.
        authentify (:obj:`bool`, optional): Whether the client should authentify upon initialization.
            If :obj:`False`, the user will have to explicitly call :meth:`authentify`. Defaults to `True`
        oauth_url (:obj:`str`, optional): The OAuth URL to use. Will override the default one if provided.
    """

    default_base_url: ClassVar[str]
    api_version: ClassVar[Optional[tuple[int, ...]]]

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        base_url: Optional[str] = None,
        authentify: bool = True,
        oauth_url: Optional[str] = None,
        **kwargs: Any,
    ) -> None:
        self.oauth_manager = OAuthManager(client_id=client_id, client_secret=client_secret, oauth_url=oauth_url)
        self.base_url = base_url or self.default_base_url
        self.session = requests.Session(**kwargs)
        if authentify:
            self.authentify()

    def __str__(self) -> str:
        return f"{self.__class__.__qualname__}(authentified={self.authentified})"

    @property
    def authentified(self) -> bool:
        """:obj:`bool`: Whether the client is authentified or not."""
        return bool(self.session.headers.get("Authorization"))

    def _request(self, method: str, endpoint: str, retry: bool = True, **kwargs: Any) -> APIResponse:
        if not self.authentified:
            raise UnauthenticatedException(
                f"Client {self.__class__.__qualname__!r} must be authentified before making requests. Consider calling 'authentify' before."
            )
        url = urljoin(self.base_url, endpoint)
        response = self.session.request(method, url, **kwargs)

        if response.status_code == 429:
            raise TooManyRequestsAPIException(retry_after=response.headers.get("Retry-After"))
        if response.status_code == 401:
            # Trying to authentify in case the Bearer token has expired
            if retry:
                self.authentify()
                self._request(method, endpoint, retry=False, **kwargs)
            else:
                raise APIException(status_code=response.status_code)
        if response.status_code == 400:
            raise APIException(**response.json())
        try:
            response.raise_for_status()
        except requests.HTTPError:
            raise APIException(status_code=response.status_code)

        data: Dict[str, Any] = response.json()
        return APIResponse(data=data, response_headers=response.headers)

    def _get(self, endpoint: str, params: Optional[Dict[str, Any]] = None, **kwargs: Any) -> APIResponse:
        return self._request("get", endpoint, params=params, **kwargs)

    def _post(
        self,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> APIResponse:
        return self._request("post", endpoint, params=params, json=json, **kwargs)

    def authentify(self) -> None:
        """Authentify the client using the provided client ID and secret."""
        self.session.headers.update({"Authorization": self.oauth_manager.get_token_header()})
