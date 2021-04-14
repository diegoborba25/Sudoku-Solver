from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from main import Solver

app = Flask(__name__)
app.secret_key = "segredo"
app.permanent_session_lifetime = timedelta(seconds=5)

solver = Solver()
solver.set_sudoku_size(9)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        column = 0
        inputed_sudoku = []
        for i in solver.idList:
            inputed_sudoku.append([])
            for n in i:
                inputed_sudoku[solver.idList.index(i)].append(request.form[n])
        solver.set_sudoku(inputed_sudoku)
        session.permanent = True
        solver.solveSudoku()

        return redirect(url_for("solved"))
    else:
        return render_template("index.html", idList=solver.idList)

@app.route("/solved", methods=["POST", "GET"])
def solved():
    if request.method == "POST":
        return redirect(url_for("home"))
    else:
        return render_template("solved.html", lista=solver.sudoku, idList=solver.idList)

if __name__ == "__main__":
    app.run(debug=True)