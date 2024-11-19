import requests

from config import API_KEY, BASE_URL

def is_symbol_available(symbol, exchange="SAO"):
    """
    Verifica se um símbolo está disponível na API Twelve Data.
    """
    url = f"{BASE_URL}/symbol_search"
    params = {"symbol": symbol, "exchange": exchange, "apikey": API_KEY}
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    if "data" in data and len(data["data"]) > 0:
        return True  # Símbolo disponível
    else:
        return False  # Símbolo não disponível

# Teste o ativo PETR4
symbol = "PETR4"
if is_symbol_available(symbol):
    print(f"O ativo {symbol} está disponível na sua conta.")
else:
    print(f"O ativo {symbol} não está disponível na sua conta ou no plano atual.")