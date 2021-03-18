from flask import Flask
from pymongo import MongoClient


app = Flask(__name__)
client = MongoClient("mongo", 27017)
db = client.translator
