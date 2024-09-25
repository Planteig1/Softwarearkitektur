from flask import Flask, jsonify, request
from students import read, updateUser, createUser, deleteUser
app = Flask(__name__)

@app.route('/members', methods = ["GET"])
def home():
    return jsonify(read())

@app.route('/members', methods = ['POST'])
def create():
    data = request.get_json()
    createUser(data)
  
    return jsonify(data), 201

@app.route('/members', methods=["PUT"])
def update():
    data = request.get_json()

    github_username = data.get("github_username")
    id = data.get("id")

    updateUser(github_username, id)

    return "successful", 204

@app.route('/members', methods = ["DELETE"])
def delete():
    data = request.get_json()
    id = data.get("id")
    
    deleteUser(id)
    return "Successful", 200

app.run(debug=True)