from datetime import datetime


class ZaoUtils:
    @staticmethod
    def parse_dt(time_str: str) -> datetime:
        return datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%S")

    @staticmethod
    def parse_int(str_int: str) -> int:
        try:
            return int(str_int)
        except:
            return 0

    @staticmethod
    def success_map(_data=None):
        return {"data": _data, "code": 0}
