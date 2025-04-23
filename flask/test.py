from sqlalchemy import DateTime
from sqlalchemy.orm import Session
from sqlalchemy.sql import sqltypes

from zao_data.db_base_access import da_engine
from zao_data.db_base_model import TableBaseModel
from zao_data.zao_file_type import ZaoFileType
from zao_data.zao_log_type import ZaoLogType
from zao_data.zao_people_type import ZaoPeopleType
from zao_tools.zao_utils import ZaoUtils


def create_all():
    with Session(da_engine) as session:
        _dict = ZaoPeopleType.metadata.tables
        _tables = [_dict.get("zao_people")]
        ZaoPeopleType.metadata.drop_all(da_engine, _tables)
        ZaoPeopleType.metadata.create_all(da_engine, _tables)
        # log = ZaoLogType()
        # session.add(log)
        # print(session.get(ZaoLogType, 1))


def columns():
    _meta = ZaoPeopleType.metadata
    column = ZaoPeopleType.__table__.columns["created"]
    print(column)
    print(column.type)
    print(isinstance(column.type, sqltypes.DateTime))
    print(isinstance(column.type, DateTime))
    # print(TableBaseModel.metadata.tables)
    # obj = ZaoPeopleType()
    # setattr(obj, "first", "")
    # getattr(obj, "first")


if __name__ == "__main__":
    create_all()
