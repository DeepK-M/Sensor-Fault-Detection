import os

AWS_S3_BUCKET_NAME = ""
MONGO_DATABASE_NAME = "SensorFault"
MONGO_COLLECTION_NAME = "waferfault"

TARGET_COLUMN = "quality"
MONGO_DB_URL = "mongodb+srv://sensor:12345@data0.eu62c.mongodb.net/SensorFault?retryWrites=true&w=majority&appName=Data0"

MODEL_FILE_NAME = "model"
MODEL_FILE_EXTENSION = ".pkl"

artifact_folder = "artifacts"