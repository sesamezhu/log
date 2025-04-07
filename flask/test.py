from sqlalchemy.orm import Session

from data.db_base_access import da_engine
from data.zao_log_type import ZaoLogType

with Session(da_engine) as session:
    # ZaoLogType.metadata.drop_all(da_engine)
    # ZaoLogType.metadata.create_all(da_engine)
    log = ZaoLogType()
    session.add(log)
    print(session.get(ZaoLogType, 1))

if __name__ == "__main__":
    pass
