from flask import Flask, render_template_string, request

app = Flask(__name__)

def is_palindrome(s):
    return s == s[::-1]

HTML = """
<!doctype html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <title>回文数检测器</title>
    <style>
        body {
            background: #f0f2f5;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            background: #fff;
            padding: 2.5rem 2rem 2rem 2rem;
            border-radius: 12px;
            box-shadow: 0 4px 24px rgba(0,0,0,0.08);
            text-align: center;
            min-width: 320px;
        }
        h2 {
            color: #1890ff;
            margin-bottom: 1.5rem;
        }
        input[type="text"] {
            padding: 0.5rem;
            border: 1px solid #d9d9d9;
            border-radius: 6px;
            width: 60%;
            font-size: 1rem;
            margin-bottom: 1rem;
        }
        input[type="submit"] {
            padding: 0.5rem 1.2rem;
            background: #1890ff;
            color: #fff;
            border: none;
            border-radius: 6px;
            font-size: 1rem;
            cursor: pointer;
            margin-left: 0.5rem;
            transition: background 0.2s;
        }
        input[type="submit"]:hover {
            background: #40a9ff;
        }
        .result {
            margin-top: 1.5rem;
            font-size: 1.1rem;
            color: #333;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>回文数检测器</h2>
        <form method="post">
            <input name="number" type="text" placeholder="请输入一个数字" required>
            <input type="submit" value="检测">
        </form>
        {% if result is not none %}
            <div class="result">{{ result }}</div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        user_input = request.form["number"]
        if user_input.isdigit():
            if is_palindrome(user_input):
                result = f"{user_input} 是回文数。"
            else:
                result = f"{user_input} 不是回文数。"
        else:
            result = "请输入有效的数字！"
    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=8000)
