#!/usr/bin/python3.8
from flask import Flask, request
from flask_restful import Api, Resource, abort
import json
import os

# print(os.environ.get("PORT"))
# HTTP_PORT = int(os.environ.get("PORT"))

with open("Plant_Generation_Data.json") as f:
    data = json.load(f)


app = Flask(__name__)
api = Api(app=app)


@app.route("/")
def index():
    return "Congratulations! Your server is running."


class Upload(Resource):
    def __init__(self):
        self.beginningIndex = 0
        self.endingIndex = len(data) - 1

    def get(self, req):
        reqType, reqIndex = req.split("_")
        #        print(arr)
        print(reqType, reqIndex)
        reqType, reqIndex = int(reqType), int(reqIndex)
        # type 1 corresponds to sending the data's beginning and ending index.
        # type 2 corresponds to sending the json object of the data.
        if reqType == 1:
            packet = {
                "beginningIndex": self.beginningIndex,
                "endingIndex": self.endingIndex,
            }
            return packet
        if reqType == 2:
            if reqIndex >= self.beginningIndex and reqIndex <= self.endingIndex:
                packet = json.dumps(data[reqIndex], indent=4)
                return packet
            else:
                abort(404)
        else:
            abort(404)


api.add_resource(Upload, "/upload/request/<string:req>")

if __name__ == "__main__":
    app.run(debug=True, port=8888, host="0.0.0.0")
