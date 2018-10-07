/**
 * Copyright 2018, Google LLC
 * Licensed under the Apache License, Version 2.0 (the `License`);
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an `AS IS` BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

// [START gae_python37_log]
'use strict';

/*window.addEventListener('load', function () {

  console.log("Hello World!");

});
// [END gae_python37_log]*/

function logIn() {
    var username = $('#username')[0].value;
    var password = $('#password')[0].value;
    // console.log(fname);
    $.ajax({
        type: "POST",
        url: "/login",
        contentType: "application/json",
        processData: false,
        cache: false,
        data: JSON.stringify({"userName": username, "password": password, "passwordTime": []}),
        success: function (resp) {
            alert("Success");
        },
        error: function (req, status, err) {
            alert(err);
        }
    });
}

function register() {
    var fname = $('#fname')[0].value;
    var lname = $('#lname')[0].value;
    var username = $('#username')[0].value;
    var password1 = $('#password1')[0].value;
    var password2 = $('#password2')[0].value;
    var password3 = $('#password3')[0].value;
    if (!(password1 == password2 && password2 == password3)) {
        alert("Password does not matches.");
        return;
    }
    var password = password1;
    // console.log(fname);
    $.ajax({
        type: "POST",
        url: "/signup",
        contentType: "application/json",
        processData: false,
        cache: false,
        data: JSON.stringify({
            "fName": fname,
            "lName": lname,
            "userName": username,
            "password": password,
            "password1Time": [],
            "password2Time": [],
            "password3Time": []
        }),
        success: function (resp) {
            alert("Success");
        },
        error: function (req, status, err) {
            alert(err);
        }
    });
}