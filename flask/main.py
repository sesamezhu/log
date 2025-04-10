from flask import Flask, request
from flask.json.provider import DefaultJSONProvider

from zao_tools.time_log import time_log
from zao_biz.zao_log_biz import ZaoLogBiz
from zao_tools.query_pager_args import QueryPagerArgs
from zao_tools.zao_json import zao_json_default
from zao_tools.zao_utils import ZaoUtils


app = Flask(__name__)
DefaultJSONProvider.default = staticmethod(zao_json_default)

@app.route("/log/post", methods=["POST"])
def flask_log_save():
    row = ZaoLogBiz.post_json(request.json)
    row.text = None
    time_log(f"post: {row}")
    return ZaoUtils.success_map({"log.id": row.id})

@app.route("/log/list", methods=["GET", "POST"])
def flask_log_list():
    return ZaoLogBiz.list(request.args, QueryPagerArgs.parse_request())

@app.route("/log/update", methods=["POST"])
def flask_log_update():
    return ZaoLogBiz.update(request.json)

@app.route("/log/delete", methods=["POST"])
def flask_log_delete():
    return ZaoLogBiz.delete(request.json.get("ids"))

if __name__ == "__main__":
    app.run(debug=False, host='127.0.0.1', port=3006)
