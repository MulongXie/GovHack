from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
from queryData import *

app = Flask(__name__)
CORS(app)


@app.route('/population',methods=['POST'])
def population():
    # req_data = request.get_json(force=True)
    content = request.json
    year = content['Year']
    start = year['start']
    end = year['end']
    result = search(start,end)

    return result


@app.route('/crash',methods=['POST'])
def crash():
    content = request.json
    year = content['Year']
    start = year['start']
    end = year['end']
    result = searchCrash(start, end)
    return result

if __name__ == '__main__':
    app.run()
