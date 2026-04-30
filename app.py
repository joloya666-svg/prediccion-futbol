from flask import Flask, render_template, request
from predict import predecir
from features_engineering import generar_features

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    resultado = None
    detalles = None

    if request.method == "POST":
        try:
            home_team = request.form["home_team"]
            away_team = request.form["away_team"]

            # 🔥 Generar features automáticamente
            data = generar_features(home_team, away_team)

            resultado = predecir(
                data["home_team"],
                data["away_team"],
                data["home_form"],
                data["away_form"],
                data["home_gd"],
                data["away_gd"],
                data["home_elo"],
                data["away_elo"]
            )

            detalles = data  # para mostrar en pantalla

        except Exception as e:
            resultado = f"Error: {str(e)}"

    return render_template("index.html", resultado=resultado, detalles=detalles)


if __name__ == "__main__":
    app.run(debug=True)