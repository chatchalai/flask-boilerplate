from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

import postgresql_api

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

@app.route('/')
def root():
    return "Working"

@app.route('/hello')
def new_one_function():
    username = request.args.get('name')
    print(username)
    return "chat" + username

@app.route('/mypage')
def mypage():
    username = request.args.get("name")
    return render_template('home.html',name = username)

@app.route('/std_list')
def std_list():
    student_list= postgresql_api.get_student_data()
    return render_template('table.html',student_list=student_list)


if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0", port=5000)