from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#url
uri="mongodb+srv://sensor:12345@data0.eu62c.mongodb.net/?retryWrites=true&w=majority&appName=Data0"

#create a new client and connectt to server
client = MongoClient(uri)

#create database name and collection name
DATABASE_NAME="SensorFault"
COLLECTION_NAME='waferfault'

df=pd.read_csv("notebooks\wafer_23012020_041211.csv")

df=df.drop("Unnamed: 0",axis=1)

json_record=list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)