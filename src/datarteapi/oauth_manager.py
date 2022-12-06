from base64 import b64encode
from typing import ClassVar, Optional

import requests

from datarteapi.exceptions import APIException


class OAuthManager:

    default_base_url: ClassVar[str] = "https://digital.iservices.rte-france.com/token/oauth/"

    def __init__(self, client_id: str, client_secret: str, oauth_url: Optional[str] = None) -> None:
        self.client_id = client_id
        self.client_secret = client_secret
        self.oauth_url = oauth_url or self.default_base_url

    @property
    def authorization_header(self) -> str:
        base64_encoded_auth = b64encode(f"{self.client_id}:{self.client_secret}".encode()).decode()
        return f"Basic {base64_encoded_auth}"

    def get_token_header(self) -> str:
        oauth_rq = requests.post(
            self.oauth_url,
            headers={
                "Authorization": self.authorization_header,
                "Content-Type": "application/x-www-form-urlencoded",
            },
        )
        data = oauth_rq.json()
        try:
            oauth_rq.raise_for_status()
        except requests.HTTPError as e:
            raise APIException(
                status_code=oauth_rq.status_code,
                error_code=data["error"],
                error_description=data["error_description"],
            ) from e

        return f"{data['token_type']} {data['access_token']}"
