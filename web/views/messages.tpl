<html>
<head>
    <meta charset="utf8">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
    <link href="/static/bootstrap.min.css" rel="stylesheet">
    <!-- <link href="bootstrap-rtl.min.css" rel="stylesheet"> -->
    <title></title>
    <style>
    form {
        padding: 30px 30px 10px 30px;
        border: 1px solid #ccc;
        border-radius: 5px;
        background: #eee;
        margin: 30px 0;
    }
    </style>
</head>
<body>
    <div class="container">
        <h1>Generated Messages</h1>
        % for message in messages:
        <form>
            <div class="form-group">
                <input id="addresses" name="addresses" class="form-control" value="{{message.address}}"></input>
            </div>
            <div class="form-group">
                <input id="subject" name="subject" class="form-control" type="text" value="{{message.subject}}">
            </div>
            <div class="form-group">
                <textarea id="message" name="message" class="form-control" value="message.text" rows="10"></textarea>
            </div>
            <div class="form-group">
                <input type="submit" value="Send" class="btn btn-primary">
            </div>
        </form>
        % end
    </div>
    <script src="/static/jquery.js"></script>
</body>
</html>