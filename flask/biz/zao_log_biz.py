from sqlalchemy.orm import Session

from data.db_base_access import da_engine
from data.zao_log_type import ZaoLogType


class ZaoLogBiz:
    @staticmethod
    def post_json(_data: dict):
        row = ZaoLogType()
        row.event_type = _data.get("event_type", 0)
        row.text = _data.get("text", "")
        with Session(da_engine) as session:
            session.add(row)
        return row
