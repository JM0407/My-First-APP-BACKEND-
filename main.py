from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)                     #create a flask app
api = Api(app)                            # wrap the app with an api

if __name__ == "__main__":
    app.run(debug=True)                   #run the app , use debug only on dev env
