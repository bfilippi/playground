import json
from flask import Flask, Response
from flask_restx import Resource, Api

app = Flask(__name__)
api = Api(app)

@api.route('/hello',methods = ['GET', 'POST'])
class HelloWorld(Resource):
    def get(self):
        
        diceroll_out = {"response_type": "ephemeral", "icon_url":
                        "https://funcamp.net/w/dice.png", "username":
                        "vegas", "text": '### this is it '}
        response: Response = app.response_class(response=json.dumps(diceroll_out) + '\n', status=200, mimetype="application/json")
        return response

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
