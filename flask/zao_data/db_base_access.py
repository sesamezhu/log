from datetime import datetime
from typing import List

from sqlalchemy.orm import Session
from sqlalchemy import create_engine, DateTime

from zao.zao_config import zao_db_conn
from zao_data.db_base_model import TableBaseModel
from zao_tools.zao_utils import ZaoUtils

da_engine = create_engine(zao_db_conn)


class CvDatabaseAccess:
    @staticmethod
    def insert(entity: TableBaseModel):
        entity.created = datetime.now()
        with Session(da_engine, expire_on_commit=False) as session:
            session.add(entity)
            session.commit()
            return entity

    @staticmethod
    def load(entity: TableBaseModel):
        assert entity is not None, "load need __class__ from non-empty instance"
        _cls = entity.__class__
        with Session(da_engine) as session:
            if entity.id is None or entity.id <= 0:
                # load last row
                return session.query(_cls).order_by(_cls.id.desc()).first()
            return session.get(_cls, entity.id)

    @staticmethod
    def delete(entity: TableBaseModel):
        with Session(da_engine) as session:
            _row = session.get(entity.__class__, entity.id)
            session.delete(_row)
            session.commit()

    @staticmethod
    def last(_id_row: TableBaseModel):
        _cls = _id_row.__class__
        with Session(da_engine) as session:
            return session.query(_cls) \
                .order_by(_cls.id.desc()).first()

    @staticmethod
    def fetch_dict(_data: dict, entity: TableBaseModel):
        _table = entity.__table__
        for column in _table.columns:
            _name = column.name
            if _name in _data:
                if _name in entity.readonly_keys():
                    continue
                _value = _data.get(_name)
                if isinstance(column.type, DateTime):
                    _value = ZaoUtils.parse_dt(_value)
                setattr(entity, _name, _value)

    @staticmethod
    def save_dict(_data: dict, entity: TableBaseModel):
        with Session(da_engine) as _session:
            _id = _data.get("id")
            row = entity if _id is None else _session.get(entity.__class__, _id)
            CvDatabaseAccess.fetch_dict(_data, row)
            row.updated = datetime.now()
            if _id is None:
                row.status = 1
                row.created = datetime.now()
                _session.add(row)
            _session.commit()
        return ZaoUtils.success_map()

    @staticmethod
    def invalidate_ids(_ids: List[int], entity: TableBaseModel):
        result = []
        with Session(da_engine) as _session:
            for _id in _ids:
                row = _session.get(entity.__class__, _id)
                result.append(row is not None)
                if row is not None:
                    row.status = 0
            _session.commit()
        return ZaoUtils.success_map({"result": result})
