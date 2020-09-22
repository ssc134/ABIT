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
    def __init__(self, action):
        self.beginningIndex = 0
        self.endingIndex = len(data) - 1
        self.currentIndex = 0
        # task state can have values
        # - running - 1
        #  paused - 2
        #  terminated - 3
        self.state = 3

    def get(self, action):
        if self.currentIndex <= self.endingIndex:
            return data[self.currentIndex]

    def put(self, action):
        # action can have values -
        # run - 1
        #  pause - 2
        #  terminate - 3
        if self.state == action:
            return {"response": "task already in the desired state."}
        if self.state == 2:
            # state = paused
            if action == 1:
                # action = run
                self.state = 1
                return get(self)
            if action == 3:
                # action = terminate
                self.state = 3
                return {"response": "task successfully terminated."}
        if self.state == 3:
            # state = terminated
            if action == 1:
                # action = run
                self.state = 1
                return get(self)
            if action == 2:
                # action = pause
                self.state = 2
                return {"response": "invalid action. task is in terminated state."}
        if self.state == 1:
            # state = running
            if action == 2:
                # action = pause
                self.state = 2
                return {"response": "task successfully paused."}
            if action == 3:
                # action = terminate
                self.state = 3
                return {"response": "task successfully terminated."}


api.add_resource(
    Upload, "/upload/client/<string:action>", "/upload/client/<int:action>"
)

if __name__ == "__main__":
    app.run(debug=True)