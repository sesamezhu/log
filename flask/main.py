from datetime import datetime

from flask import Flask, request

from biz.zao_log_biz import ZaoLogBiz

app = Flask(__name__)

def success_map(_data=None):
    return {"data": {"code": 0, "data": _data}}

@app.route("/log/post", methods=["POST"])
def flask_log_save():
    row = ZaoLogBiz.post_json(request.json)
    print(row)
    return success_map({"flask_stamp": datetime.now()})

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=3006)
