from datetime import datetime

from flask import Flask, request

from time_log import time_log
from zao_biz.zao_log_biz import ZaoLogBiz

app = Flask(__name__)

def success_map(_data=None):
    return {"data": {"code": 0, "data": _data}}

@app.route("/log/post", methods=["POST"])
def flask_log_save():
    row = ZaoLogBiz.post_json(request.json)
    row.text = None
    time_log(row)
    return success_map({"log.id": row.id})

if __name__ == "__main__":
    app.run(debug=False, host='127.0.0.1', port=3006)
