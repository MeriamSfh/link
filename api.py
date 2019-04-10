from flask import Flask
from flask_restful import Resource, Api
import tools as tt

app = Flask(__name__)
api = Api(app)

class Searchlink(Resource):
    def get(self, name):
        person = tt.linkedin(name)
        return person

api.add_resource(Searchlink, '/searchlink/<name>')


if __name__ == '__main__':
    app.run(debug=True)