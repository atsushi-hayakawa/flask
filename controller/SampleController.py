from flask import *

app = Blueprint('controller', __name__)


# getの場合、文字列(HTML)を返却
# ex) http://localhost:8080/getSample?id=123&name=Jack
@app.route("/getSample", methods=["get"])
def getSample():
    user_id = request.args.get("id")
    user_name = request.args.get("name")
    return "<h1>" + user_id + ":" + user_name + " Hello!" + "</h1>"


# postの場合、文字列(HTML)を返却
# ex) PostSample.html
@app.route("/postSample", methods=["post"])
def postSample():
    user_id = request.form.get("id")
    user_name = request.form.get("name")
    return "<h1>" + str(user_id) + ":" + user_name + " Hello!" + "</h1>"


# テンプレートエンジンで表示
# ex) http://localhost:8080/templateSample?id=123&name=Jack
@app.route("/templateSample", methods=["get"])
def templateSample():
    user_id = request.args.get("id")
    user_name = request.args.get("name")
    return render_template("templateSample.html", user_id=user_id, user_name=user_name)


# RestfulなAPIを作成、JSONで受けてJSONで返す
# ex) RestSample.html
@app.route("/restSample", methods=['POST'])
def restSample():
    request_json = request.get_json()
    res_str = request_json.get("user_id") + ":" + request_json.get("user_name") + " Hello!"
    return jsonify({"message": res_str})
