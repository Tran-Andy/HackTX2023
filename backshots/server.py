# import os
# from pymongo import MongoClient
# from pymongo.errors import PyMongoError
# from pymongo.server_api import ServerApi
# from flask import Flask

# app = Flask(__name__)

# mongo_client = MongoClient(os.getenv("MONGO_CONNECTION"), server_api=ServerApi('1'), maxPoolSize = 100)
# db = mongo_client['LLM']
# users_collection = db['Values']

# @app.route("/")
# def insert():
#     try:
#         users_collection.insert_one({"bruh": "bruh"})
#         return "Inserted successfully!"
#     except PyMongoError as e:
#         # Handle the exception (e.g., log the error)
#         return "Error inserting data: " + str(e)
    
# if __name__ == "__main__":
#     app.run(debug=True, host = "localhost", port = 8080)
import os
import logging
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from pymongo.errors import PyMongoError  # Import PyMongoError for error handling
from flask import Flask

app = Flask(__name__)

# Configure the logger to capture MongoDB-related errors
logging.basicConfig(level=logging.DEBUG)

mongo_client = MongoClient(os.getenv("MONGO_CONNECTION"), server_api=ServerApi('1'), maxPoolSize = 100)
db = mongo_client['LLM']
users_collection = db['Values']

@app.route("/")
def insert():
    try:
        app.logger.info("Before insert operation")
        users_collection.insert_one({"bruh": "bruh"})
        app.logger.info("After insert operation") 
        return "Inserted successfully!"
    except PyMongoError as e:
        # Log the MongoDB error
        logging.error(f"MongoDB Error: {e}")
        return "Error inserting data: " + str(e)

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8080)

