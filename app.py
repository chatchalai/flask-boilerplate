from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

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

if __name__ == "__main__":
    app.run(debug = False, host="0.0.0.0", port=5000)