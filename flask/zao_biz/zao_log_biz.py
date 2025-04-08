from zao_data.db_base_access import CvDatabaseAccess
from zao_data.zao_log_type import ZaoLogType
from zao_utils import ZaoUtils


class ZaoLogBiz:
    @staticmethod
    def post_json(_data: dict):
        row = ZaoLogType()
        row.happened = ZaoUtils.parse_dt(_data.get("happened", ""))
        row.place = _data.get("place", "")
        row.loggee = _data.get("loggee", "")
        row.type = str.upper(_data.get("type", ""))
        row.text = _data.get("text", "")
        row.minutes = _data.get("minutes", 0)
        row.logging = ZaoUtils.parse_dt(_data.get("logging", ""))
        CvDatabaseAccess.insert(row)
        return row
