from flask import Flask, request
from google.cloud import vision
from google.cloud import automl
from firebase import Firebase
import detect

API_KEY = open('api_key.txt').readline().split(':')[1].strip()

project_id = PROJECT_ID
model_id = MODEL_ID

config = {
    "apiKey": API_KEY,
    "authDomain": URL_DOMAIN,
    "databaseURL": URL_DB,
    "storageBucket": URL_BUCKET,
}

firebase = Firebase(config)
storage = firebase.storage()

app = Flask(__name__)


@app.route('/')
def default():
    return ""


@app.route('/detect_pack')
def detect_object():
    fname = request.args.get('file_name')
    storage.child("package_list/" + str(fname)
                  ).download('images/' + str(fname))
    res = detect.localize_objects(fname)
    return res


if __name__ == '__main__':
    app.run(host='192.168.45.253', port=10025)
    #app.run(host='192.168.1.8', port=8080)
