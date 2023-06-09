from flask import Flask, request, jsonify
from pymongo import MongoClient

# Connect to MongoDB Atlas
mongo_uri = "mongodb+srv://username:password@cluster.mongodb.net/database_name?retryWrites=true&w=majority"
client = MongoClient(mongo_uri)
db = client["database_name"]
names_collection = db["names_collection"]

app = Flask(__name__)

@app.route('/greet', methods=['GET'])
def greet_person():
    name = request.args.get('name', 'Guest')
    return jsonify(message=f"Hello, {name}!")

@app.route('/save_name', methods=['POST'])
def save_name():
    name = request.form.get('name')
    if name:
        names_collection.insert_one({"name": name})
        return jsonify(message=f"Name {name} saved successfully!")
    else:
        return jsonify(error="Name not provided"), 400

@app.route('/fetch_names', methods=['GET'])
def fetch_names():
    names = [name_doc["name"] for name_doc in names_collection.find()]
    return jsonify(names=names)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4540)
