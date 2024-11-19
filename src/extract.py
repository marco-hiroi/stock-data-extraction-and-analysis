import requests

def validate_symbol(symbol):
    """Valida a disponibilidade do símbolo na API Twelve Data."""
    url = f"https://api.twelvedata.com/symbol_search"
    params = {"symbol": symbol, "exchange": "SAO", "apikey": "54d9e27bbaed4e819a5a6e977d801a1f" }
    response = requests.get(url, params=params)
    data = response.json()

    if "data" in data and len(data["data"]) > 0:
        return True  # Símbolo válido
    else:
        raise ValueError(f"O símbolo '{symbol}' não é suportado pela API ou está incorreto.")

# Uso:
try:
    validate_symbol("PETR4")
    print("Símbolo válido e suportado pela API.")
except ValueError as e:
    print(e)
