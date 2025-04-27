from flask import Flask, request
from flask.json.provider import DefaultJSONProvider

from zao_biz.zao_people_biz import ZaoPeopleBiz
from zao_data.db_base_access import CvDatabaseAccess
from zao_data.zao_log_type import ZaoLogType
from zao_biz.zao_log_biz import ZaoLogBiz
from zao_data.zao_people_type import ZaoPeopleType
from zao_tools.query_pager_args import QueryPagerArgs
from zao_tools.time_log import time_log
from zao_tools.zao_json import zao_json_default
from zao_tools.zao_video import push_rtmp_stream

app = Flask(__name__)
DefaultJSONProvider.default = staticmethod(zao_json_default)


@app.route("/log/list")
def flask_log_list():
    return ZaoLogBiz.list(request.args, QueryPagerArgs.parse_request())

@app.route("/log/update", methods=["POST"])
def flask_log_update():
    time_log(f"flask_log_update: {request.json}")
    return CvDatabaseAccess.save_dict(request.json, ZaoLogType())

@app.route("/log/delete", methods=["POST"])
def flask_log_delete():
    return CvDatabaseAccess.invalidate_ids(request.json.get("ids"), ZaoLogType())

@app.route("/people/list")
def flask_people_list():
    return ZaoPeopleBiz.list(request.args, QueryPagerArgs.parse_request())

@app.route("/people/update", methods=["POST"])
def flask_people_update():
    time_log(f"flask_people_update: {request.json}")
    return CvDatabaseAccess.save_dict(request.json, ZaoPeopleType())

@app.route("/people/delete", methods=["POST"])
def flask_people_delete():
    return CvDatabaseAccess.invalidate_ids(request.json.get("ids"), ZaoPeopleType())

@app.route("/people/tree")
def flask_people_tree():
    return ZaoPeopleBiz.tree(request.args)

if __name__ == "__main__":
    app.run(debug=False, host='127.0.0.1', port=3006)
