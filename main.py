from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)                     #create a flask app
api = Api(app)                            # wrap the app with an api

names = { "JM":{"age":26,"gender":"male","birthday":"04/07/1995"},
          "KATE":{"age":27,"gender":"female","birthday":"03/14/1994"}       #This section is to store information in the memory by using dictionary
}

class HelloWorld(Resource):               # This is to create a class that contains a resource

    """
    def get(self):                        # GET request
        return {"data": "hello world!"}           # return message of the endpoint (key value pair for json format)

    def post(self):                       # POST request
        return {"data": "posted"}         # return message of the endpoint (key value pair for json format)

api.add_resource(HelloWorld, "/helloworld")          # registering the resource to the api , (class, "endpoint")
    """

    """
#THIS IS FOR PASSING ARGUMENT
    def get(self, name, age):                                                # GET request
        return {"name": name, "age": age}                                    # return message of the endpoint (key value pair for json format)
api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:age>")          # registering the resource to the api , (class, "endpoint"), argument <datatype:userinput>
   """

    def get(self, name):                                                # GET request
        return names[name]                                  # return message of the endpoint (key value pair for json format)
api.add_resource(HelloWorld, "/helloworld/<string:name>")          # registering the resource to the api , (class, "endpoint"), argument <datatype:userinput>


if __name__ == "__main__":
    app.run(debug=True)                   #run the app , use debug only on dev env
