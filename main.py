from flask import Flask, render_template

app = Flask(__name__)


@app.route('/ratings')
def ratings():
    return render_template("ratings.html")

if __name__ == "__main__":
    app.run()
