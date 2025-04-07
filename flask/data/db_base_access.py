from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from cv_data.BB_Instrument import InstrumentRow
from cv_data.db_base_model import TableBaseModel, EquipBaseModel
from sqlalchemy import create_engine
from cv_tools.win_config import json_grid

_conn = json_grid["conn"]
da_engine = create_engine(_conn)
write_engine = create_engine(_conn, echo=True)


class CvDatabaseAccess:
    @staticmethod
    def insert(entity: TableBaseModel):
        entity.DateTime = datetime.now()
        with Session(write_engine, expire_on_commit=False) as session:
            session.add(entity)
            session.commit()
            return entity

    @staticmethod
    def load(entity: TableBaseModel):
        assert entity is not None, "load need __class__ from non-empty instance"
        with Session(da_engine) as session:
            if entity.Id is None or entity.Id <= 0:
                # load last row
                return session.query(entity.__class__).order_by(entity.__class__.Id.desc()).first()
            return session.get(entity.__class__, entity.Id)

    @staticmethod
    def delete(entity: TableBaseModel):
        with Session(write_engine) as session:
            _row = session.get(entity.__class__, entity.Id)
            session.delete(_row)
            session.commit()

    @staticmethod
    def last(_id_row: TableBaseModel):
        _cls = _id_row.__class__
        with Session(da_engine) as session:
            return session.query(_cls) \
                .order_by(_cls.Id.desc()).first()

    @staticmethod
    def load_by_equip(equip: EquipBaseModel, time_check: bool = True):
        with Session(da_engine) as session:
            if time_check:
                return session.query(equip.__class__) \
                   .filter_by(StationID=equip.StationID) \
                   .filter_by(EquipID=equip.EquipID) \
                   .filter(equip.__class__.DateTime >= datetime.now() - timedelta(hours=1))\
                   .order_by(equip.__class__.Id.desc()).first()
            return session.query(equip.__class__) \
                .filter_by(StationID=equip.StationID) \
                .filter_by(EquipID=equip.EquipID) \
                .order_by(equip.__class__.Id.desc()).first()

    @staticmethod
    def load_instrument(_id: int):
        with Session(da_engine) as session:
            return session.get(InstrumentRow, _id)

    @staticmethod
    def not_deleted(_row: TableBaseModel):
        _cls = _row.__class__
        with Session(da_engine, expire_on_commit=False) as session:
            return session.query(_cls).filter_by(IsDeleted=False).all()
