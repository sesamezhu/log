from datetime import datetime

from sqlalchemy.orm import Session

from zao_tools.time_log import time_log
from zao_data.db_base_access import CvDatabaseAccess, da_engine
from zao_tools.query_pager_args import QueryPagerArgs
from zao_data.zao_log_type import ZaoLogType
from zao_tools.zao_utils import ZaoUtils


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

    @staticmethod
    def list(query: dict, pager: QueryPagerArgs):
        time_log(f"ZaoLogBiz.list: {query}, {pager}")
        with Session(da_engine) as _session:
            query = _session.query(ZaoLogType)
            query = query.filter_by(status=1)
            total = query.count()
            result = pager.all(query.order_by(ZaoLogType.id.desc()))
        return ZaoUtils.success_map({"list": result, "total": total})

    @staticmethod
    def update(_data: dict):
        time_log(f"ZaoLogBiz.post: {_data}")
        with Session(da_engine) as _session:
            row = _session.get(ZaoLogType, _data.get("id"))
            row.updated = datetime.now()
            if "happened" in _data:
                row.happened = ZaoUtils.parse_dt(_data.get("happened"))
            if "place" in _data:
                row.place = _data.get("place")
            if "loggee" in _data:
                row.loggee = _data.get("loggee")
            if "type" in _data:
                row.type = str.upper(_data.get("type"))
            if "text" in _data:
                row.text = _data.get("text")
            if "minutes" in _data:
                row.minutes = _data.get("minutes")
            if "status" in _data:
                row.status = _data.get("status")
            _session.commit()
        return ZaoUtils.success_map()

    @staticmethod
    def delete(ids: []):
        with Session(da_engine) as _session:
            ret = _session.query(ZaoLogType).filter(ZaoLogType.id.in_(ids)).delete()
            _session.commit()
        return ZaoUtils.success_map({"affected": ret})
