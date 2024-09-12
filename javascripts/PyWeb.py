from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    result = 2 + 2  # 可以执行任何 Python 代码
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
