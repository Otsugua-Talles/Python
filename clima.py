import requests
import pandas as pd
from datetime import datetime

# Lista com estados, capitais e coordenadas aproximadas
capitais = [
    ("Acre", "Rio Branco", -9.97499, -67.8243),
    ("Alagoas", "Maceió", -9.66599, -35.735),
    ("Amapá", "Macapá", 0.034934, -51.0694),
    ("Amazonas", "Manaus", -3.10194, -60.025),
    ("Bahia", "Salvador", -12.9714, -38.5014),
    ("Ceará", "Fortaleza", -3.71722, -38.5433),
    ("Distrito Federal", "Brasília", -15.7797, -47.9297),
    ("Espírito Santo", "Vitória", -20.3155, -40.3128),
    ("Goiás", "Goiânia", -16.6864, -49.2643),
    ("Maranhão", "São Luís", -2.52972, -44.3028),
    ("Mato Grosso", "Cuiabá", -15.5989, -56.0949),
    ("Mato Grosso do Sul", "Campo Grande", -20.4428, -54.6464),
    ("Minas Gerais", "Belo Horizonte", -19.9208, -43.9378),
    ("Pará", "Belém", -1.45583, -48.5039),
    ("Paraíba", "João Pessoa", -7.115, -34.8631),
    ("Paraná", "Curitiba", -25.4284, -49.2733),
    ("Pernambuco", "Recife", -8.05, -34.9),
    ("Piauí", "Teresina", -5.08917, -42.8019),
    ("Rio de Janeiro", "Rio de Janeiro", -22.9028, -43.2075),
    ("Rio Grande do Norte", "Natal", -5.795, -35.2094),
    ("Rio Grande do Sul", "Porto Alegre", -30.0331, -51.23),
    ("Rondônia", "Porto Velho", -8.76194, -63.9039),
    ("Roraima", "Boa Vista", 2.81972, -60.6733),
    ("Santa Catarina", "Florianópolis", -27.5969, -48.5495),
    ("São Paulo", "São Paulo", -23.55, -46.633),
    ("Sergipe", "Aracaju", -10.9111, -37.0717),
    ("Tocantins", "Palmas", -10.1675, -48.3277)
]

# Mapeamento dos códigos do Open-Meteo para texto
weather_map = {
    0: "Céu limpo",
    1: "Principalmente limpo",
    2: "Parcialmente nublado",
    3: "Nublado",
    45: "Névoa",
    48: "Névoa congelante",
    51: "Garoa leve",
    53: "Garoa moderada",
    55: "Garoa intensa",
    61: "Chuva leve",
    63: "Chuva moderada",
    65: "Chuva forte",
    71: "Neve leve",
    73: "Neve moderada",
    75: "Neve forte",
    80: "Pancadas leves",
    81: "Pancadas moderadas",
    82: "Pancadas fortes",
    95: "Trovoadas",
    96: "Trovoadas com granizo leve",
    99: "Trovoadas com granizo forte"
}

# Função que busca a previsão para uma capital
def get_forecast(lat, lon):
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        f"&daily=temperature_2m_max,temperature_2m_min,weathercode"
        f"&timezone=America/Sao_Paulo"
        f"&forecast_days=7"
    )
    r = requests.get(url)
    r.raise_for_status()
    data = r.json()["daily"]

    forecast = []
    for date, tmax, tmin, code in zip(
        data["time"], data["temperature_2m_max"], data["temperature_2m_min"], data["weathercode"]
    ):
        forecast.append((date, tmax, tmin, weather_map.get(code, "Desconhecido")))
    return forecast

# Monta a tabela
linhas = []
print("🔄 Buscando previsões das capitais brasileiras...")
for estado, capital, lat, lon in capitais:
    previsoes = get_forecast(lat, lon)
    for dia, tmax, tmin, clima in previsoes:
        linhas.append([estado, capital, dia, tmax, tmin, clima])

# Cria DataFrame
df = pd.DataFrame(linhas, columns=["Estado", "Capital", "Data", "Temp Max (°C)", "Temp Min (°C)", "Condição"])

# Salva Excel
arquivo = f"clima_brasil_{datetime.now().strftime('%Y%m%d')}.xlsx"
df.to_excel(arquivo, index=False)

print(f"✅ Planilha gerada: {arquivo}")
