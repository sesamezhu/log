from datetime import datetime

from sqlalchemy import String, BLOB
from sqlalchemy.orm import Mapped, mapped_column

from zao_data.db_base_model import TableBaseModel


class ZaoFileType(TableBaseModel):
    __tablename__ = "zao_file"
    type: Mapped[str] = mapped_column(String(32), default="")
    name: Mapped[str] = mapped_column(String(128), default="")
    blob: Mapped[bytes] = mapped_column(default=None)
    text: Mapped[str] = mapped_column(String(128), default="")
