from datetime import datetime
from typing import List

from sqlalchemy import DateTime
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass
from sqlalchemy.orm import Mapped, mapped_column


def mapped_id_column():
    return mapped_column(primary_key=True,
                         autoincrement=True,
                         default=None)


class DeclarativeModel(MappedAsDataclass, DeclarativeBase):
    __abstract__ = True


class TableBaseModel(DeclarativeModel):
    __abstract__ = True
    id: Mapped[int] = mapped_id_column()
    created: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    updated: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    status: Mapped[int] = mapped_column(default=1)

    @property
    def has_id(self) -> bool:
        return self.id is not None and self.id > 0

    @staticmethod
    def readonly_keys() -> List[str]:
        return ["id", "created", "updated"]
