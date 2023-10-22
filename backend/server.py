import os
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from flask import Flask

app = Flask(__name__)

mongo_client = MongoClient(os.getenv("MONGO_CONNECTION"), server_api=ServerApi('1'))
db = mongo_client['LLM']
users_collection = db['Values']

@app.route("/")
def insert():
    users_collection.insert_one({"bruh": "bruh"})
    
if __name__ == "__main__":
    app.run(debug=True, host = "localhost", port = 8080)
