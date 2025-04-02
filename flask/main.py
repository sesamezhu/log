from datetime import datetime

from flask import Flask, request

app = Flask(__name__)

def success_map(_data=None):
    return {"data": {"code": 0, "data": _data}}

@app.route("/log/post", methods=["POST"])
def flask_log_save():
    print(request.json)
    return success_map({"flask_stamp": datetime.now()})

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=3006)
