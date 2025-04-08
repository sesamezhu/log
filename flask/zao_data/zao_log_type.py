import datetime

from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from data.db_base_model import TableBaseModel


class ZaoLogType(TableBaseModel):
    __tablename__ = "zao_log"
    happened: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    place: Mapped[str] = mapped_column(String(128), default="")
    loggee: Mapped[int] = mapped_column(default=0)
    type: Mapped[str] = mapped_column(String(32), default="")
    text: Mapped[str] = mapped_column(String(1024), default="")
    minutes: Mapped[int] = mapped_column(default=0)
    creating: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
