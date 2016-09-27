from flask import Flask, render_template
from utils import occupy

app = Flask(__name__)

@app.route("/")
@app.route("/occupations/")
def occupate():
    lines = occupy.get_file()
    ranges = occupy.set_ranges(occupy.get_pcts(lines))
    rndOccu = occupy.pull_rand_occ(ranges, occupy.get_occs(lines))
    return render_template('base.html', bd = "", d = lines, header2 = "A Possible Career Path:", choice = rndOccu, header1 = "A List ofOccupations")

if __name__ == "__main__":
    app.debug = True
    app.run()
