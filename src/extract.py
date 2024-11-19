import requests
from config import API_KEY, BASE_URL

def fetch_current_price(symbol):
    """
    Busca a cotação atual de um ativo usando a API Twelve Data.
    """
    url = f"{BASE_URL}/quote"
    params = {
        "symbol": symbol,
        "apikey": API_KEY
    }
    response = requests.get(url, params=params)
    response.raise_for_status()  # Lança um erro se a resposta for inválida
    data = response.json()

    # Verifica se há erro na resposta
    if "code" in data:
        raise ValueError(f"Erro: {data['message']}")

    # Retorna a cotação atual
    return data.get("price")

if __name__ == "__main__":
    symbol = "PETR4"  # Ativo da B3
    try:
        print(f"Buscando cotação atual para o ativo: {symbol}")
        current_price = fetch_current_price(symbol)
        if current_price:
            print(f"A cotação atual de {symbol} é: R$ {current_price}")
        else:
            print(f"Não foi possível obter a cotação de {symbol}.")
    except Exception as e:
        print(f"Erro ao buscar cotação: {e}")
