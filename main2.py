from flask import Flask
from flask_restful import Api, Resource
import json

app = Flask(__name__)
api = Api(app=app)

with open("Plant_Generation_Data.json") as f:
    data = json.load(f)

class UploadData(Resource):
    def get(self, action):
        #action can be : start, stop, resume, terminate
        action = action.lower()
        if action=='start':
            pass
        elif action=='stop':
            pass
        elif action=='resume':
            pass
        elif action=='terminate':
            pass
        return 200

    def put(self):
        


class CollectEndPoints(Resource):
    def get(self):
        pass


api.add_resource(ClientEndPoints, "/client/action/<string:action>")
api.add_resource(CollectEndPoints, "/collect/<string:name>")

if __name__ == "__main__":
    app.run(debug=True)
