from flask import Flask, render_template, request, redirect, session
from colour import Color

app = Flask(__name__)
app.secret_key = 'darksecret'


@app.route("/")
def checker_8_by_8():
    return render_template("checker.html", num_rows=8, num_cols=8, colors=["salmon", "black"])

@app.route("/<x>")
def checker_x_by_8(x):
    try:
        return render_template("checker.html", num_rows=int(x), num_cols=8,colors=["salmon", "black"])
    except:
        return checker_8_by_8()

@app.route("/<x>/<y>")
def checker_x_by_y(x,y):
    try:
        return render_template("checker.html", num_rows=int(x), num_cols=int(y),colors=["salmon", "black"])
    except:
        return checker_x_by_8(x)

def is_valid_color(str):
    try:
        c = Color(str)
        return True
    except:
        return False

@app.route("/<x>/<y>/<color1>")
def checker_with_light_color(x,y,color1):
    if color1 == "black":
        color1="salmon"
    if not is_valid_color(color1):
        color1="salmon"
    try:
        return render_template("checker.html", num_rows=int(x), num_cols=int(y),colors=[color1,"black"]) 
    except:
        return checker_x_by_8(x)

@app.route("/<x>/<y>/<color1>/<color2>")
def checker_with_colors(x,y,color1,color2):
    if not is_valid_color(color1):
        color1="salmon"
    if not is_valid_color(color2):
        color2="black"
    if color1 == color2:
        color2 = "black"
        if color1 == "black":
            color1 = "salmon"
    try:
        return render_template("checker.html", num_rows=int(x), num_cols=int(y),colors=[color1,color2])
    except:
        return checker_x_by_8(x)

if __name__ == '__main__':
    app.run(debug=True)
