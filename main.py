from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)                     #create a flask app
api = Api(app)                            # wrap the app with an api

class HelloWorld(Resource):               # This is to create a class that contains a resource
    def get(self):                        # Get request
        return {"data": "hello world!"}           # return message of the endpoint

api.add_resource(HelloWorld, "/helloworld")          # registering the resource to the api , (class, "endpoint")

if __name__ == "__main__":
    app.run(debug=True)                   #run the app , use debug only on dev env
