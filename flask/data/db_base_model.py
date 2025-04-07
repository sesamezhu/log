from datetime import datetime
from typing import Tuple

from sqlalchemy import String, DateTime
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass
from sqlalchemy.orm import Mapped, mapped_column


def get_default_column(default=None):
    return mapped_column(default=default)


def mapped_id_column():
    return mapped_column(primary_key=True,
                         autoincrement=True,
                         default=None)


def mapped_int_column():
    return mapped_column(default=0)


def mapped_str_column(default=''):
    return mapped_column(String(50), default=default)


def mapped_bool_column():
    return mapped_column(default=False)


def mapped_dt_column():
    return mapped_column(DateTime, default=datetime.now())


class DeclarativeModel(MappedAsDataclass, DeclarativeBase):
    __abstract__ = True


class TableBaseModel(DeclarativeModel):
    __abstract__ = True
    Id: Mapped[int] = mapped_id_column()
    DateTime: Mapped[datetime] = mapped_column(DateTime, name='CreateTime', default=datetime.now())
    IsDeleted: Mapped[bool] = get_default_column(False)

    @property
    def is_id_valid(self) -> bool:
        return self.Id is not None and self.Id > 0


class EquipBaseModel(TableBaseModel):
    __abstract__ = True
    FactoryID: Mapped[str] = mapped_str_column()
    StationID: Mapped[str] = mapped_str_column()
    EquipID: Mapped[str] = mapped_str_column()
    ModifyTime: Mapped[datetime] = mapped_dt_column()

    def match(self, _row):
        return self.equip_key == _row.equip_key

    @property
    def modified(self) -> datetime:
        _time = self.DateTime if self.ModifyTime is None else self.ModifyTime
        return _time.replace(tzinfo=None)

    @property
    def equip_key(self) -> Tuple[str, str]:
        return self.StationID, self.EquipID
