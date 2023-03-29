import yfinance as yf


def get_price(ticker):
    yticker = yf.Ticker(ticker).fast_info
    data = {
        "price": yticker["last_price"],
        "previous_close": yticker["previous_close"],
        "currency": yticker["currency"],
    }
    return data
