import json
from flask import Flask, jsonify, request
import form

app = Flask(__name__, static_folder=".", static_url_path="")

@app.after_request
def add_header(res):
    res.headers["Access-Control-Allow-Origin"] = "*"
    return res
        
@app.route('/', methods=['GET', 'POST'])
def mypage():
    if request.method == "GET":
        query = request.args.get('query')
    elif request.method == "POST":
        query = request.form['query']
    data = form.select_book(query)
    return json.dumps(data, ensure_ascii=False)

if __name__=='__main__':
    app.run(port=8000)
