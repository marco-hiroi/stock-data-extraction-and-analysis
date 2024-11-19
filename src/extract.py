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
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Verifica erros HTTP
        data = response.json()

        # Verifica erros específicos da API
        if "code" in data:
            raise ValueError(f"Erro na API: {data['message']}")

        # Exibe a resposta para depuração
        print("Resposta da API:", data)

        # Retorna a cotação atual
        return data.get("price", None)
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Erro de conexão com a API: {e}")
    except ValueError as e:
        raise RuntimeError(f"Erro nos dados retornados pela API: {e}")

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
