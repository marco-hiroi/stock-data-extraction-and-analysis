import requests
import os
from config import API_KEY, BASE_URL

def fetch_stock_data(symbol, interval="1day", outputsize=30):
    """Extrai dados históricos de um ativo da B3 da API Twelve Data."""
    url = f"{BASE_URL}/time_series"
    params = {
        "symbol": symbol,
        "interval": interval,
        "outputsize": outputsize,
        "apikey": API_KEY
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    # Verifica erros retornados pela API
    if "code" in data:
        raise ValueError(f"Erro: {data['message']}")

    return data.get("values", [])

def save_data_to_file(data, filename):
    """Salva os dados extraídos em um arquivo local."""
    os.makedirs("data/raw", exist_ok=True)
    filepath = os.path.join("data/raw", filename)
    with open(filepath, "w") as f:
        for line in data:
            f.write(f"{line}\n")

if __name__ == "__main__":
    symbol = "PETR4.SA"  # Ativo da B3
    try:
        data = fetch_stock_data(symbol)
        save_data_to_file(data, f"{symbol}_data.json")
        print(f"Dados salvos em data/raw/{symbol}_data.json")
    except Exception as e:
        print(f"Erro: {e}")
