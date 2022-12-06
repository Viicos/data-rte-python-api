from datetime import datetime, timezone
from typing import Any, Dict, TypeVar

_K = TypeVar("_K")
_V = TypeVar("_V")


def is_aware(dt: datetime) -> bool:
    """Check whether the datetime object has a timezone or not.

    Args:
        dt (:obj:`datetime.datetime`): The datetime object to be checked.

    Returns:
        :obj:`bool`: If the datetime object is aware, return :obj:`True`.
    """
    return dt.tzinfo is not None and dt.tzinfo.utcoffset(dt) is not None


def to_utc_datetime(dt: datetime, trim_microsecond: bool = True, unaware_to_utc: bool = False) -> datetime:
    """Convert the datetime object timezone to UTC.

    Args:
        dt (:obj:`datetime.datetime`): The datetime object to be converted.
        trim_microsecond (:obj:`bool`, optional): Whether microseconds should be removed from the datetime object.
            Defaults to :obj:`True`.
        unaware_to_utc (:obj:`bool`, optional): Whether unaware datetime objects should be set to UTC. If :obj:`True`,
            the unaware datetime will be set to UTC, otherwise local timezone is used. Defaults to :obj:`False`.

    Returns:
        :obj:`datetime.datetime`: The converted datetime object.
    """
    if trim_microsecond:
        dt = dt.replace(microsecond=0)
    if unaware_to_utc and not is_aware(dt):
        return dt.replace(tzinfo=timezone.utc)
    else:
        return dt.astimezone(timezone.utc)


def filter_none_from_dict(dct: Dict[_K, _V]) -> Dict[_K, _V]:
    return {k: v for k, v in dct.items() if v is not None}
