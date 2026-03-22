from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
    <!DOCTYPE html>
    <html lang="kr">
    <head>
    <meta charset="UTF-8">
    <title>Flask Home Page</title>
    </head>
    <body>
    <form method="GET" action="/gugudan">
    <h2>구구단 출력하기</h2>
    <label>단 :
    <input type="text" name="dan">
    </label>
    <button type="submit">출력</button>
    </form>
    </body>
    </html>
"""

@app.route("/gugudan")
def gugudan():
    dan = request.args.get("dan", type=int)
    resp = "<head><title>gugudan</title></head><body>"
    
    for i in range(1, 10):
        resp += f"<p><font color='skyblue'>{dan} * {i} = <font color='pink'>{dan * i}</font></font></p>"
    
    resp += "</body>"
    resp += "</html>"
    return resp

app.run(debug=True)