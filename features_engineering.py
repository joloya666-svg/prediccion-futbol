import pandas as pd

# Cargar dataset
df = pd.read_csv("matches.csv")

df = df.rename(columns={
    'Date': 'date',
    'HomeTeam': 'home_team',
    'AwayTeam': 'away_team',
    'FTHG': 'home_goals',
    'FTAG': 'away_goals'
})

df['date'] = pd.to_datetime(df['date'], dayfirst=True)
df = df.sort_values(by='date')


# ============================
# FUNCIONES
# ============================

def get_team_matches(team):
    return df[(df['home_team'] == team) | (df['away_team'] == team)]


def calcular_forma(team, n=5):
    matches = get_team_matches(team).tail(n)
    puntos = 0

    for _, m in matches.iterrows():
        if m['home_team'] == team:
            if m['home_goals'] > m['away_goals']:
                puntos += 3
            elif m['home_goals'] == m['away_goals']:
                puntos += 1
        else:
            if m['away_goals'] > m['home_goals']:
                puntos += 3
            elif m['away_goals'] == m['home_goals']:
                puntos += 1

    return puntos


def calcular_goal_diff(team, n=5):
    matches = get_team_matches(team).tail(n)
    dif = 0

    for _, m in matches.iterrows():
        if m['home_team'] == team:
            dif += (m['home_goals'] - m['away_goals'])
        else:
            dif += (m['away_goals'] - m['home_goals'])

    return dif / n if len(matches) > 0 else 0


def calcular_elo_basico(team):
    matches = get_team_matches(team)
    return 1500 + len(matches) * 2  # simplificado


# ============================
# FUNCIÓN PRINCIPAL
# ============================

def generar_features(home_team, away_team):
    
    home_form = calcular_forma(home_team)
    away_form = calcular_forma(away_team)

    home_gd = calcular_goal_diff(home_team)
    away_gd = calcular_goal_diff(away_team)

    home_elo = calcular_elo_basico(home_team)
    away_elo = calcular_elo_basico(away_team)

    return {
        "home_team": home_team,
        "away_team": away_team,
        "home_form": home_form,
        "away_form": away_form,
        "home_gd": home_gd,
        "away_gd": away_gd,
        "home_elo": home_elo,
        "away_elo": away_elo
    }