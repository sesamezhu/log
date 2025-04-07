from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from data.db_base_model import TableBaseModel


class ZaoAccountType(TableBaseModel):
    __tablename__ = "zao_account"
    text: Mapped[str] = mapped_column(String(1024), default="")
    loggee: Mapped[int] = mapped_column(default=0)
    event_type: Mapped[int] = mapped_column(default=0)
    happened: Mapped[int] = mapped_column(default=0)
    minutes: Mapped[int] = mapped_column(default=0)
