from flask import Flask,jsonify, request
from flask.json import jsonify
from flask_cors import CORS
from test import Test
import datetime

app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

test = Test()

@app.route('/',methods=['GET'])
def home():
    print("Prueba funcional")

    hora_actual = datetime.datetime.now().time()

    test.Prueba(int(hora_actual.hour),int(hora_actual.minute))

    return 'SERVER IS WORKING!'


if __name__=='__main__':
    app.run(host='localhost',debug=True)