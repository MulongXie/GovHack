function router() {
    var express = require('express');
    var app = express();
    app.use(express.static(__dirname));
    app.use(express.static(__dirname + '/Front-end'));
    app.use(express.static(__dirname + '/Front-end/img'));

    app.get('/', function (req, res) {
        res.sendfile(__dirname + '\\index.html');
        // res.send('aaa')
    });

    app.listen(8000, function () {
        console.log('Server created with port: 8000\n');
    });
}

router();