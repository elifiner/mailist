<html>
<head>
    <meta charset="utf8">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
    <link href="/static/bootstrap.min.css" rel="stylesheet">
    <!-- <link href="bootstrap-rtl.min.css" rel="stylesheet"> -->
    <title></title>
</head>
<body>
    <div class="container">
        <h1>Message Template</h1>
        <form>
            <div class="form-group">
                <!-- <label for="addresses">Addresses</label> -->
                <textarea id="addresses" class="form-control" placeholder="Addresses"></textarea>
            </div>
            <div class="form-group">
                <!-- <label for="subject">Subject</label> -->
                <input id="subject" class="form-control" type="text" placeholder="Subject">
            </div>
            <div class="form-group">
                <!-- <label for="message">Message</label> -->
                <textarea id="message" class="form-control" placeholder="Message" rows="20"></textarea>
            </div>
            <div class="form-group">
                <button class="btn btn-primary">Generate</button>
            </div>

        </form>
    </div>
    <script src="/static/jquery.js"></script>
</body>
</html>