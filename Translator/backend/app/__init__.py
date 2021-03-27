from flask import Flask
from pymongo import MongoClient
import os

app = Flask(__name__)
client = MongoClient(host="mongo",
                     port=27017,
                     username=os.environ.get("MONGO_INITDB_ROOT_USERNAME"),
                     password=os.environ.get("MONGO_INITDB_ROOT_PASSWORD"))
db = client.translator
