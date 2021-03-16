from flask import Flask
from pymongo import MongoClient


app = Flask(__name__)
mongo_client = MongoClient("mongo:27017")
