from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="kr">
    <head>
    <meta charset="UTF-8">
    <title>단위 변환</title>
    </head>
    <body>
    <h2>단위 변환기</h2>

    <form method="GET" action="/convert">
        <label>변환 종류:
            <select name="type">
                <option value="temp">온도 (섭씨 ↔ 화씨)</option>
                <option value="length">길이 (m ↔ inch)</option>
            </select>
        </label>
        <br><br>

        <label>값:
            <input type="text" name="value">
        </label>
        <br><br>

        <label>변환 방향:
            <select name="direction">
                <option value="c_to_f">섭씨 → 화씨</option>
                <option value="f_to_c">화씨 → 섭씨</option>
                <option value="m_to_in">미터 → 인치</option>
                <option value="in_to_m">인치 → 미터</option>
            </select>
        </label>
        <br><br>

        <button type="submit">변환</button>
    </form>

    </body>
    </html>
    """

@app.route("/convert")
def convert():
    value = request.args.get("value", type=float)
    conv_type = request.args.get("type")
    direction = request.args.get("direction")

    resp = "<head><title>변환 결과</title></head><body>"

    if value is None:
        resp += "<p>값을 입력하세요.</p>"
    else:
        if conv_type == "temp":
            if direction == "c_to_f":
                result = (value * 9/5) + 32
                resp += f"<p>{value}℃ → {result:.2f}℉</p>"

            elif direction == "f_to_c":
                result = (value - 32) * 5/9
                resp += f"<p>{value}℉ → {result:.2f}℃</p>"

        elif conv_type == "length":
            if direction == "m_to_in":
                result = value * 39.3701
                resp += f"<p>{value} m → {result:.2f} inch</p>"

            elif direction == "in_to_m":
                result = value / 39.3701
                resp += f"<p>{value} inch → {result:.2f} m</p>"

    resp += "</body>"
    resp += "</html>"
    return resp

app.run(debug=True)