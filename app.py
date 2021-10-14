from flask import Flask, render_template
import sys
import mock_data_generator.api as api

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/profile")
def say_profile():
    return api.get_profile()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int("31312"))

