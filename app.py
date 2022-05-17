from flask import Flask, request, send_from_directory, jsonify, render_template
import json
import os
import requests
from vars import STYLE_SHEET_NUMBER
app = Flask(__name__)

@app.route("/")
def hello_world():
    return  render_template('base.html', 
            style_sheet_number=STYLE_SHEET_NUMBER)

@app.route("/users")
def users():
    with open('users.json') as users:
        text = json.loads(users.read())
    return jsonify(text)

@app.route("/comment")
def comment():
    username = request.args.get('username')
    comment  = request.args.get('comment')
    with open('users.json') as db:
       user_comments = json.loads(db.read())
    if len(user_comments) > 16:
       user_comments.pop(0)
    user_comments.append({
       "username": str(username),
       "comment": str(comment)
    })
    with open('users1.json','w') as db:
       db.write(json.dumps(user_comments, indent=4))

    os.rename('users1.json', 'users.json') 
    return jsonify(user_comments)
    


@app.route('/get-files/<path:path>',methods = ['GET','POST'])
def get_files(path):

    """Download a file."""
    try:
        return send_from_directory('downloads', path, as_attachment=True)
    except FileNotFoundError:
        abort(404)
