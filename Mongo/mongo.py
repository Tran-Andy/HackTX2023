import os
from pymongo import MongoClient

mongo_client = MongoClient(os.getenv("MONGO_URL"), server_api=ServerApi('1'))
db = mongo_client['PixEraDB']
users_collection = db['Users']