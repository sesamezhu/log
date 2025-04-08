from datetime import datetime


class ZaoUtils:
    @staticmethod
    def parse_dt(time_str: str) -> datetime:
        return datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%S")
