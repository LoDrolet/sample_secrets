# Save data to an AWS bucket

from typing import Dict

import aws_lib
import pymongo


def aws_upload(data: Dict):
    database = aws_lib.connect("AKIA08T6FBS4ZNDE5ADV", "RlBx0oVdV7OhsFkmYjcMNQ7c3cDYuv5UO072vxSc")
    database.push(data)


def transform_data(es_data: Dict) -> Dict:
    es_data = {**data, "origin": "ES"}

MONGO_URI = "mongodb+srv://testuser:hub25aoeu@gg-is-awesome-gg273.mongodb.net/test?retryWrites=true&w=majority"

def pull_data_from_mongo(query: Dict):
    return pymongo.connect(MONGO_URI).fetch(query)


def push_mongo_to_s3(query):
    for element in pull_data_from_mongo(query):
        upload(element)
