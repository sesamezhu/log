from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from zao.zao_config import zao_db_conn
from zao_data.db_base_model import TableBaseModel

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
        with Session(da_engine) as session:
            if entity.id is None or entity.id <= 0:
                # load last row
                return session.query(entity.__class__).order_by(entity.__class__.id.desc()).first()
            return session.get(entity.__class__, entity.id)

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
