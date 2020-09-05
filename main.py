from flask import Flask, render_template
from datetime import datetime

def dtime():
    return datetime.today().strftime("%Y-%m-%d")

app = Flask(__name__)

@app.route("/")
def index():
    world = "測試"
    return render_template("index.html", title=world ,dtime = dtime())

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)

#render_template將會找尋html檔案傳送給使用者
#前往 http://localhost:5000/