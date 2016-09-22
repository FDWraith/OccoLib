from flask import Flask, render_template
import occupy

app = Flask(__name__)

@app.route("/")
def home():
    body = ""
    return render_template('base.html', bd = body)

@app.route("/occupations")
def occupate():
    lines = occupy.get_file()
    dict = { "Occupations" : occupy.get_occs( lines ),
             "Percentages" : occupy.get_pcts( lines ) }
    
    
    return render_template('base.html', bd = "I don't know what goes here")


if __name__ == "__main__":
    app.debug = True
    app.run()
