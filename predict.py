import numpy as np
import pandas as pd
import joblib
from tensorflow.keras.models import load_model

# Cargar modelo y preprocesador
model = load_model("modelo_futbol.h5")
preprocessor = joblib.load("preprocessor.pkl")

def predecir(home_team, away_team, home_form, away_form, home_gd, away_gd, home_elo, away_elo):

    # 🔥 Crear DataFrame con nombres EXACTOS
    data = pd.DataFrame([{
        "home_team": home_team,
        "away_team": away_team,
        "home_form_5": home_form,
        "away_form_5": away_form,
        "home_goal_diff": home_gd,
        "away_goal_diff": away_gd,
        "home_elo": home_elo,
        "away_elo": away_elo,
        "elo_diff": home_elo - away_elo,
        "form_diff": home_form - away_form,
        "goal_diff": home_gd - away_gd
    }])

    # Transformar
    X = preprocessor.transform(data)

    # Predecir
    pred = model.predict(X)

    clases = ["Local", "Empate", "Visitante"]

    return clases[np.argmax(pred)]