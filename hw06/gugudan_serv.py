from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("gugudan.html")

@app.route("/gugudan")
def gugudan():
    dan = request.args.get("dan", type=int)

    resp = ""

    for i in range(1, 10):
        resp += f"<p><font color='skyblue'>{dan} * {i} = <font color='pink'>{dan * i}</font></font></p>"

    return resp

app.run(debug=True)