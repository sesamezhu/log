from datetime import date
from typing import Optional, List, Dict

from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from zao_data.db_base_model import TableBaseModel


class ZaoPeopleType(TableBaseModel):
    __tablename__ = "zao_people"
    first: Mapped[str] = mapped_column(String(32), default="")
    last: Mapped[str] = mapped_column(String(32), default="")
    nick: Mapped[str] = mapped_column(String(32), default="")
    father: Mapped[int] = mapped_column(default=0)
    mother: Mapped[int] = mapped_column(default=0)
    mate: Mapped[int] = mapped_column(default=0)
    birth: Mapped[Optional[date]] = mapped_column(DateTime, default=None)
    death: Mapped[Optional[date]] = mapped_column(DateTime, default=None)
    gender: Mapped[int] = mapped_column(default=0)
    phone: Mapped[str] = mapped_column(default="")
    phone2: Mapped[str] = mapped_column(default="")
    email: Mapped[str] = mapped_column(default="")
    address: Mapped[str] = mapped_column(default="")
    address2: Mapped[str] = mapped_column(default="")
    work: Mapped[str] = mapped_column(String(32), default="")
    z_relation: Mapped[str] = mapped_column(String(32), default="")
    z_blood: Mapped[int] = mapped_column(default=0)
    """
        Result of 1/math.pow(2, blood) is the same share of dna with zao.
    """
    image: Mapped[int] = mapped_column(default=0)
    text: Mapped[str] = mapped_column(String(4096), default="")

    mates: Dict = None
    children: List = None
