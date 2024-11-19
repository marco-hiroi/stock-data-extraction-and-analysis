import requests
from config import API_KEY, BASE_URL

def fetch_current_price(symbol):
    url = f"{BASE_URL}/quote"
    params = {"symbol": symbol, "apikey": API_KEY}
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    if "price" in data:
        return data["price"]
    else:
        raise ValueError(f"Erro na resposta: {data}")

# Teste com o ativo PETR4
symbol = "PETR4"
try:
    price = fetch_current_price(symbol)
    print(f"A cotação atual de {symbol} é: R$ {price}")
except Exception as e:
    print(f"Erro: {e}")