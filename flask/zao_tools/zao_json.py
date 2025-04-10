import dataclasses
import decimal
import uuid
from datetime import date, datetime


def _json_date(o) -> str:
    if not isinstance(o, datetime):
        return o.strftime('%Y-%m-%d')
    elif o.microsecond:
        return o.strftime('%Y-%m-%d %H:%M:%S.%f')
    elif o.second or o.minute or o.hour:
        return o.strftime('%Y-%m-%d %H:%M:%S')
    else:
        return o.strftime('%Y-%m-%d')

def zao_json_default(o) -> str:
    if isinstance(o, date):
        return _json_date(o)

    if isinstance(o, (decimal.Decimal, uuid.UUID)):
        return str(o)

    if dataclasses and dataclasses.is_dataclass(o):
        return dataclasses.asdict(o)

    if hasattr(o, "__html__"):
        return str(o.__html__())

    raise TypeError(f"Object of type {type(o).__name__} is not JSON serializable")
