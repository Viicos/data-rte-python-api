from typing import Any, Dict, Optional


class UnauthenticatedException(Exception):
    pass


class BaseAPIException(Exception):
    def __init__(self, status_code: int, *args: Any) -> None:
        super().__init__(*args)
        self.attrs: Dict[str, Any] = {"status_code": status_code}

    def __str__(self) -> str:
        return f"{type(self).__qualname__}({', '.join(f'{attr}={value}' for attr, value in self.attrs.items() if value is not None)})"


class TooManyRequestsAPIException(BaseAPIException):
    def __init__(self, *args: Any, retry_after: Optional[str] = None) -> None:
        super().__init__(429, *args)
        self.attrs["retry_after"] = retry_after


class APIException(BaseAPIException):
    def __init__(self, *args: Any, status_code: int, **kwargs: dict[str, Any]) -> None:
        super().__init__(status_code, *args)
        self.attrs.update(kwargs)
