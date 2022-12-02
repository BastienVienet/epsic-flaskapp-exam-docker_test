from flask import Flask, render_template
import os
import random

app = Flask(__name__)

# list of funny memes
images = [
    "https://media.giphy.com/media/kusPzjBcmhc2yB06Tq/giphy.gif",
    "https://media.giphy.com/media/KEeyysnlLdJ4afgEhk/giphy.gif",
    "https://media.giphy.com/media/eSwGh3YK54JKU/giphy.gif",
    "https://media.giphy.com/media/AFdcYElkoNAUE/giphy.gif",
    "https://media.giphy.com/media/COYGe9rZvfiaQ/giphy.gif",
    "https://media.giphy.com/media/XIqCQx02E1U9W/giphy.gif"
    ]


@app.route("/")
def index():
    url = random.choice(images)
    return render_template("index.html", url=url)

@app.route("/hello")
def hello():
    return "ok"

@app.route("/exam-docker")
def exam_docker():
    return "Hello ! This is a test for the docker exam"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
