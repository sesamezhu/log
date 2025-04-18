from sqlalchemy.orm import Session

from zao_data.db_base_access import da_engine
from zao_data.zao_log_type import ZaoLogType
from zao_tools.query_pager_args import QueryPagerArgs
from zao_tools.zao_utils import ZaoUtils


class ZaoLogBiz:
    @staticmethod
    def list(args: dict, pager: QueryPagerArgs):
        with Session(da_engine) as _session:
            query = _session.query(ZaoLogType)
            query = query.filter_by(status=1)
            _field = ZaoLogType.type
            if _field.key in args:
                query = query.filter(_field.startswith(args.get(_field.key)))
            _field = ZaoLogType.loggee
            if _field.key in args:
                query = query.filter(_field.startswith(args.get(_field.key)))
            total = query.count()
            result = pager.all(query.order_by(ZaoLogType.id.desc()))
        return ZaoUtils.success_map({"list": result, "total": total})
