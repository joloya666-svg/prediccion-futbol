from flask import Flask, render_template, request
from predict import predecir

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    resultado = None

    if request.method == "POST":
        try:
            home_team = request.form["home_team"]
            away_team = request.form["away_team"]

            home_form = float(request.form["home_form"])
            away_form = float(request.form["away_form"])

            home_gd = float(request.form["home_gd"])
            away_gd = float(request.form["away_gd"])

            home_elo = float(request.form["home_elo"])
            away_elo = float(request.form["away_elo"])

            resultado = predecir(
                home_team,
                away_team,
                home_form,
                away_form,
                home_gd,
                away_gd,
                home_elo,
                away_elo
            )

        except Exception as e:
            resultado = f"Error: {str(e)}"

    return render_template("index.html", resultado=resultado)


if __name__ == "__main__":
    app.run(debug=True)