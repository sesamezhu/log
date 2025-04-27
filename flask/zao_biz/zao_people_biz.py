from sqlalchemy.orm import Session

from zao_data.db_base_access import da_engine, CvDatabaseAccess
from zao_data.zao_people_type import ZaoPeopleType
from zao_tools.query_pager_args import QueryPagerArgs
from zao_tools.zao_utils import ZaoUtils


class ZaoPeopleBiz:
    @staticmethod
    def list(args: dict, pager: QueryPagerArgs):
        with Session(da_engine) as _session:
            query = _session.query(ZaoPeopleType)
            query = query.filter_by(status=1)
            _field = ZaoPeopleType.first
            if _field.key in args:
                query = query.filter(_field.like(f'%{args.get(_field.key)}%'))
            _field = ZaoPeopleType.last
            if _field.key in args:
                query = query.filter(_field.is_(args.get(_field.key)))
            total = query.count()
            result = pager.all(query.order_by(ZaoPeopleType.id.desc()))
        return ZaoUtils.success_map({"list": result, "total": total})

    @staticmethod
    def tree(args: dict):
        _id = ZaoUtils.parse_int(args.get("id"))
        root: ZaoPeopleType = CvDatabaseAccess.load(ZaoPeopleType(id=_id))
        root.mates = {}
        if root.mate > 0:
            root.mates["mate"] = CvDatabaseAccess.load(ZaoPeopleType(id=root.mate))
        if root.father > 0:
            root.mates["father"] = CvDatabaseAccess.load(ZaoPeopleType(id=root.father))
        if root.mother > 0:
            root.mates["mother"] = CvDatabaseAccess.load(ZaoPeopleType(id=root.mother))
        ZaoPeopleBiz.put_child(root)
        return ZaoUtils.success_map(root)

    @staticmethod
    def put_child(parent):
        with Session(da_engine) as _session:
            query = _session.query(ZaoPeopleType)
            query = query.filter_by(status=1)
            query = query.filter((ZaoPeopleType.mother == parent.id) | (ZaoPeopleType.father == parent.id))
            parent.children = query.all()
        for child in parent.children:
            ZaoPeopleBiz.put_child(child)
