from flask import Flask, jsonify, request

app = Flask(__name__)

members = [
    {"id": 1, "name": "John Doe", "membership": "Gold"},
    {"id": 2, "name": "Jane Smith", "membership": "Silver"}
]

@app.route('/')
def home():
    return jsonify({"message": "Welcome to ACEest Fitness & Gym!"})

@app.route('/members', methods=['GET'])
def get_members():
    return jsonify(members)

@app.route('/members', methods=['POST']) 
def add_member():
    data = request.get_json()
    new_member = {
        "id": len(members) + 1,
        "name": data['name'],
        "membership": data['membership']
    }
    members.append(new_member)
    return jsonify(new_member), 201

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')