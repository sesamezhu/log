from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from data.db_base_model import TableBaseModel


class ZaoMoneyType(TableBaseModel):
    __tablename__ = "zao_money"
    credit: Mapped[int] = mapped_column(default=0)
    debit: Mapped[int] = mapped_column(default=0)
    amount: Mapped[int] = mapped_column(default=0)
    happened: Mapped[int] = mapped_column(default=0)
    text: Mapped[str] = mapped_column(String(128), default="")
