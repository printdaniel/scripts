import yfinance as yf
import time

def get_stock_price(ticket):
    """
    Obtiene el precio actual de una acción.

    Parámetros:
    - ticket: El símbolo de la acción que se va a consultar.

    Retorna:
    - price: El precio actual de la acción.
    """
    stock = yf.Ticker(ticket)
    price = stock.history(period='1d')['Close'].iloc[-1]
    return price

def monitor_stock_price(ticker, interval_seconds=60):
    """
    Monitoriza el precio de una acción a intervalos regulares.

    Parámetros:
    - ticker: El símbolo de la acción a monitorizar.
    - interval_seconds: El intervalo de tiempo en segundos entre cada consulta.

    Retorna:
    - None
    """
    while True:
        price = get_stock_price(ticker)
        print(f'{ticker} Stock Price: ${price:.2f}')
        time.sleep(interval_seconds)

if __name__ == '__main__':
    stock_symbol = 'BA'  # Símbolo de la acción a monitorizar
    monitor_stock_price(stock_symbol)
