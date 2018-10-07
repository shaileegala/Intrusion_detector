# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from views.views import UserView

# [START gae_python37_render_template]
import datetime

from flask import Flask, render_template, request
from json import loads, dumps

app = Flask(__name__)


@app.route('/')
def root():
    # For the sake of example, use static information to inflate the template.
    # This will be replaced with real information in later steps.
    # dummy_times = [datetime.datetime(2018, 1, 1, 10, 0, 0),
    #                datetime.datetime(2018, 1, 2, 10, 30, 0),
    #                datetime.datetime(2018, 1, 3, 11, 0, 0),
    #                ]

    # return render_template('index.html', times=dummy_times)
    return render_template('index.html')


@app.route('/login', methods=['GET'])
def login():
    return render_template('Login.html')


@app.route('/login', methods=['POST'])
def loginSubmit():
    data = loads(request.data)
    # print(data)
    userName = data['userName']
    password = data['password']
    passwordTimeStamp = float(data['passwordTimeStamp'])//float(1000)
    response = UserView.login(username=userName,password=password,timestamp_array=passwordTimeStamp)
    return dumps(response.data_dict())


@app.route('/signup', methods=['GET'])
def signUp():
    # print("In get sign up")
    return render_template('SignUp.html')


@app.route('/signup', methods=['POST'])
def signUpSubmit():
    # print("In post sign up")
    # print(request.data)
    data = loads(request.data)
    # print(data)
    fName = data['fName']
    # print("fname: " + fName)
    lName = data['lName']
    userName = data['userName']
    password = data['password']
    password1TimeStamp = float(data['password1TimeStamp'])/float(1000)
    password2TimeStamp = float(data['password2TimeStamp'])/float(1000)
    password3TimeStamp = float(data['password3TimeStamp'])/float(1000)
    print(password1TimeStamp, password2TimeStamp, password3TimeStamp)
    response = UserView.register(username=userName,fname=fName,lname=lName,password=password,timestamp_array1=password1TimeStamp,timestamp_array2=password2TimeStamp,timestamp_array3=password3TimeStamp)
    return dumps(response.data_dict())


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [START gae_python37_render_template]
