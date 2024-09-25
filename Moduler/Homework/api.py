# Start med at impotere flask
from flask import Flask, request, jsonify


app = Flask(__name__)

#Create the root for our API (Endpoint)
@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    # Query parameter example
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200

#POST Metode - Man kunne tilføje flere på samme tid - POST, GET
# if request.method == "POST" Tjekker om request er post
@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()
    
    return jsonify(data), 201
    
@app.route("/")
def index():
    return "Hello world"


# Run flask application and update automatically
if __name__ == "__main__":
    app.run(debug=True)