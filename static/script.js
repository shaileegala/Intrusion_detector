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

var passwordTimeStamp = [];
var password1TimeStamp = [];
var password2TimeStamp = [];
var password3TimeStamp = [];

$(document).ready(function () {
    $('#password').keyup(function (e) {
        var cursorAt = e.target.selectionStart;
        if (e.keyCode == 8 || e.keyCode == 46) {
            // console.log("back space");
            // console.log("Caret at: ", cursorAt);
            passwordTimeStamp.splice(cursorAt, 1);
        }
    });
    $('#password1').keyup(function (e) {
        var cursorAt = e.target.selectionStart;
        if (e.keyCode == 8 || e.keyCode == 46) {
            // console.log("back space");
            // console.log("Caret at: ", cursorAt);
            password1TimeStamp.splice(cursorAt, 1);
        }
    });
    $('#password2').keyup(function (e) {
        var cursorAt = e.target.selectionStart;
        if (e.keyCode == 8 || e.keyCode == 46) {
            // console.log("back space");
            // console.log("Caret at: ", cursorAt);
            password2TimeStamp.splice(cursorAt, 1);
        }
    });
    $('#password3').keyup(function (e) {
        var cursorAt = e.target.selectionStart;
        if (e.keyCode == 8 || e.keyCode == 46) {
            // console.log("back space");
            // console.log("Caret at: ", cursorAt);
            password3TimeStamp.splice(cursorAt, 1);
        }
    });

    $('#password').keypress(function (e) {
        if (e.keyCode != 13) {
            passwordTimeStamp.push(new Date().getTime());
        }
    });
    $('#password1').keypress(function (e) {
        if (e.keyCode != 13) {
            password1TimeStamp.push(new Date().getTime());
        }
    });
    $('#password2').keypress(function (e) {
        if (e.keyCode != 13) {
            password2TimeStamp.push(new Date().getTime());
        }
    });
    $('#password3').keypress(function (e) {
        if (e.keyCode != 13) {
            password3TimeStamp.push(new Date().getTime());
        }
    });
});

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
        data: JSON.stringify({"userName": username, "password": password, "passwordTimeStamp": passwordTimeStamp}),
        success: function (resp) {
            alert(JSON.parse(resp).message);
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
            "password1TimeStamp": password1TimeStamp,
            "password2TimeStamp": password2TimeStamp,
            "password3TimeStamp": password3TimeStamp
        }),
        success: function (resp) {
            alert(JSON.parse(resp).message);
        },
        error: function (req, status, err) {
            alert(err);
        }
    });
}