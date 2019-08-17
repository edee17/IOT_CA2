import boto3
import botocore
from flask import Flask, render_template, jsonify, request,Response
from picamera import PiCamera
from time import sleep

import gevent
import gevent.monkey
from gevent.pywsgi import WSGIServer

import dynamodb
import jsonconverter as jsonc

import mysql.connector
import sys

import json
import numpy
import datetime
import decimal

from functools import wraps

gevent.monkey.patch_all()


# Set the filename and bucket name
BUCKET = 'sp-p1846809-s3-bucket' # replace with your own unique bucket name
location = {'LocationConstraint': 'us-east-1'}
file_path = "/home/pi/Desktop"
file_name = "test.jpg"

def takePhoto(file_path,file_name):
    with PiCamera() as camera:
        #camera.resolution = (1024, 768)
        full_path = file_path + "/" + file_name
        camera.capture(full_path)
        sleep(3)

def uploadToS3(file_path,file_name, bucket_name,location):
    s3 = boto3.resource('s3') # Create an S3 resource
    exists = True

    try:
        s3.meta.client.head_bucket(Bucket=bucket_name)
    except botocore.exceptions.ClientError as e:
        error_code = int(e.response['Error']['Code'])
        if error_code == 404:
            exists = False
        if exists == False:
            s3.create_bucket(Bucket=bucket_name,CreateBucketConfiguration=location)
    
    # Upload the file
    full_path = file_path + "/" + file_name
    s3.Object(bucket_name, file_name).put(Body=open(full_path, 'rb'))
    print("File uploaded")


def detect_labels(bucket, key, max_labels=10, min_confidence=90, region="us-east-1"):
	rekognition = boto3.client("rekognition", region)
	response = rekognition.detect_labels(
		Image={
			"S3Object": {
				"Bucket": bucket,
				"Name": key,
			}
		},
		MaxLabels=max_labels,
		MinConfidence=min_confidence,
	)
	return response['Labels']

def RunRekognition():
    takePhoto(file_path, file_name)
    uploadToS3(file_path,file_name, BUCKET,location)
    highestconfidence = 0
    best_bet_item = "Unknown"
    for label in detect_labels(BUCKET, file_name):
        print("{Name} - {Confidence}%".format(**label))
        if label["Confidence"] >= highestconfidence:
            highestconfidence = label["Confidence"]
            best_bet_item = label["Name"]

    if best_bet_item!= "Unknown":
        print("This should be a {} with confidence {}".format(best_bet_item, highestconfidence))

app = Flask(__name__)

from Adafruit_DHT import DHT11, read_retry
sensor = DHT11
pin = 4

def support_jsonp(f):
    """Wraps JSONified output for JSONP"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        callback = request.args.get("callback", False)
        if callback:
            content = str(callback) + "(" + str(f(*args,**kwargs)) + ")"
            return current_app.response_class(content, mimetype="application/javascript")
        else:
            return f(*args, **kwargs)
    return decorated_function

@app.route("/")
def hello():
    hum, temp = raw_dht()
    return render_template('index.html', humidity = hum, temperature = temp)

@app.route("/dht")
@support_jsonp
def api_dht():
    humidity, temperature = raw_dht()
    if humidity is not None and temperature is not None:
        return "{ temperature: '" + "{0:0.0f}".format(temperature) +  "', humidity: '" + "{0:0.0f}".format(humidity) + "' }"
    else:
        return "Failed to get reading. Try again!", 500


def raw_dht():
    return read_retry(sensor, pin)

@app.route("/writePhoto/On",methods = ['GET'])
def startLapse():
    RunRekognition()
    response = "Rekognition started."

    return render_template('index.html', response = response)

@app.route("/api/getdata",methods=['POST','GET'])
def apidata_getdata():
    if request.method == 'POST' or request.method == 'GET':
        try:
            data = {'chart_data': jsonc.data_to_json(dynamodb.get_data_from_dynamodb()), 
             'title': "IOT Data"}
            return jsonify(data)

        except:
            import sys
            print(sys.exc_info()[0])
            print(sys.exc_info()[1])

@app.route("/")
def home():
    return render_template("index.html")

from gpiozero import LED
led = LED(18)

def ledOn():
  led.blink()

def ledOff():
  led.off()

@app.route("/writeLED/<status>")
def writePin(status):

   if status == 'On':
     response = ledOn()
   else:
     response = ledOff()

   return response

app.run(debug=True,host="0.0.0.0")

if __name__ == '__main__':
   try:
        http_server = WSGIServer(('0.0.0.0', 8001), app)
        app.debug = True
        http_server.serve_forever()
   except:
        print("Exception")