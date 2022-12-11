from typing import Any, Dict, Union, overload

from requests.models import CaseInsensitiveDict
from typing_extensions import Literal


class APIResponse:
    def __init__(self, data: Dict[str, Any], response_headers: CaseInsensitiveDict[str]) -> None:
        self.data = data
        self.headers = response_headers

    @overload
    def __getitem__(self, key: Literal["data"]) -> Dict[str, Any]:
        ...

    @overload
    def __getitem__(self, key: Literal["headers"]) -> CaseInsensitiveDict[str]:
        ...

    def __getitem__(self, key: Literal["data", "headers"]) -> Union[Dict[str, Any], CaseInsensitiveDict[str]]:
        rt: Union[Dict[str, Any], CaseInsensitiveDict[str]] = getattr(self, key)
        return rt
