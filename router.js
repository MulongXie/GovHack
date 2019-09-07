
function router() {
    var express = require('express');
    var app = express();

    var request = require('request');

    function updateClient(postData){
        var clientServerOptions = {
            uri: "loclhost:5000/population",
            body: JSON.stringify(postData),
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        };
        request(clientServerOptions, function (error, response) {
            console.log(error,response.body);
            return;
        });
    }

    app.use(express.static(__dirname + '/Front-end'));
    app.use(express.static(__dirname + '/Back-end'));

    app.get('/', function (req, res) {
        res.sendfile('index.html');
    });


}

router();