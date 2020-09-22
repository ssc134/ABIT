from flask import Flask
from flask_restful import Api, Resource, abort
from flask import request
import json


with open("Plant_Generation_Data.json") as f:
    data = json.load(f)


app = Flask(__name__)
api = Api(app=app)


# This function is included so that server doesnt crash
# due to an invalid PUT request.
# It will just raise an exception and move on.
def abort_if_video_doesnt_exist(video_id):
    # Executes when the provided video_id is invalid.
    if video_id not in videos:
        # abort() raises an exception.
        abort(404, message="Video with that Id doesnt exits...")


def abort_if_video_exists(video_id):
    if video_id in videos:
        abort(409, message="Video with that ID already exists...")


class Upload(Resource):
    beginningIndex = 0
    endingIndex = len(data) - 1

    def get(self, action):
        index = self.beginningIndex
        while index >= self.beginningIndex and index <= self.endingIndex:
            return data[index]
        

    def put(self, beginningIndex, endingIndex):
        if self.beginningIndex < beginningIndex and self.endingIndex > endingIndex:
            return {
                "valid index range": {
                    "beginning index": self.beginningIndex,
                    "ending index": self.endingIndex,
                }
            }
        self.beginningIndex = beginningIndex
        self.endingIndex = endingIndex
        return {
            "beginning index": self.beginningIndex,
            "ending index": self.endingIndex,
        }

    def post(self, beginningIndex, endingIndex):
        if self.beginningIndex < beginningIndex and self.endingIndex > endingIndex:
            return {
                "valid index range": {
                    "beginning index": self.beginningIndex,
                    "ending index": self.endingIndex,
                }
            }
        self.beginningIndex = beginningIndex
        self.endingIndex = endingIndex
        return {
            "beginning index": self.beginningIndex,
            "ending index": self.endingIndex,
        }

    def delete(self):
        self.beginningIndex = 0
        self.endingIndex = len(data) - 1
        return {
            "beginning index": self.beginningIndex,
            "ending index": self.endingIndex,
        }


api.add_resource(Upload, "/upload/client/<string:action>", "/upload/client/<string:action>")

if __name__ == "__main__":

    # followig line will run our app
    # and debug=True will enable logging.
    # debug=True should NOT be used in production environmet.
    app.run(debug=True)