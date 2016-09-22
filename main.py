from flask import Flask, render_template
import occupy

app = Flask(__name__)

@app.route("/")
def home():
    body = ""
    return render_template('base.html', bd = body, d = [])

@app.route("/occupations")
def occupate():
    lines = occupy.get_file()    
    return render_template('base.html', bd = "Here is a great table", d = lines)


if __name__ == "__main__":
    app.debug = True
    app.run()
