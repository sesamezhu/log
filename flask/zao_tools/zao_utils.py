from datetime import datetime


class ZaoUtils:
    @staticmethod
    def parse_dt(time_str: str) -> datetime:
        return datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")

    @staticmethod
    def parse_int(str_int: str) -> int:
        try:
            return int(str_int)
        except:
            return 0

    @staticmethod
    def success_map(_data="success"):
        return {"data": _data, "code": 0}
