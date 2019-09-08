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
    result = searchPop(int(start),int(end))

    return result


@app.route('/crash',methods=['POST'])
def crash():
    content = request.json
    year = content['Year']
    start = year['start']
    end = year['end']
    result = searchCrash(int(start), int(end))
    return result


@app.route('/bus',methods=['POST'])
def Bus():
    result = searchBus()
    return result


@app.route('/housing',methods=['POST'])
def Housing():
    content = request.json
    year = content['Year']
    start = year['start']
    end = year['end']
    result = searchHousing((int)(start),(int)(end))
    return result


if __name__ == '__main__':
    app.run('0.0.0.0')
