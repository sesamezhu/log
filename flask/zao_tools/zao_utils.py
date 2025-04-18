from datetime import datetime


class ZaoUtils:
    @staticmethod
    def parse_dt(time_str: str) -> datetime:
        assert time_str, "time_str is empty"
        _len = len(time_str)
        assert _len == 19 or _len == 26 or _len == 10, "time_str is invalid"
        if _len == 26:
            return datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S.%f")
        elif _len == 19:
            return datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
        else:
            return datetime.strptime(time_str, "%Y-%m-%d")

    @staticmethod
    def parse_int(str_int: str) -> int:
        try:
            return int(str_int)
        except:
            return 0

    @staticmethod
    def success_map(_data="success"):
        return {"data": _data, "code": 0}
