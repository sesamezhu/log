from datetime import datetime

from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from zao_data.db_base_model import TableBaseModel


class ZaoLogType(TableBaseModel):
    __tablename__ = "zao_log"
    happened: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    place: Mapped[str] = mapped_column(String(128), default="")
    loggee: Mapped[str] = mapped_column(String(32), default="")
    type: Mapped[str] = mapped_column(String(32), default="")
    text: Mapped[str] = mapped_column(String(4096), default="")
    minutes: Mapped[int] = mapped_column(default=0)
    logging: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
