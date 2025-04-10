import dataclasses

from flask import request
from zao_tools.zao_utils import ZaoUtils


def range_int(i: int, _max=50, _min=10):
    return min(max(i, _min), _max)


@dataclasses.dataclass
class QueryPagerArgs:
    DEFAULT_SIZE = 10
    DEFAULT_INDEX = 1

    size: int = DEFAULT_SIZE
    index: int = DEFAULT_INDEX

    def all(self, query):
        return query.offset(self.size * (self.index - 1)).limit(self.size).all()

    @staticmethod
    def parse_request():
        pager = QueryPagerArgs()
        _value = ZaoUtils.parse_int(request.args.get("pageSize"))
        pager.size = range_int(_value, _max=50, _min=QueryPagerArgs.DEFAULT_SIZE)
        _value = ZaoUtils.parse_int(request.args.get("pageIndex"))
        pager.index = max(_value, QueryPagerArgs.DEFAULT_INDEX)
        return pager
