import requests
import json
from cfg import keys

class ConvertionExceptions(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionExceptions(f'Невозможно перевести одинаковые валюты {base}')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionExceptions(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionExceptions(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExceptions(f'Не удалось обработать количество {amount}')

        r = requests.get(f'http://api.exchangeratesapi.io/v1/latest?access_key=eaff29ed2a1187b9d05d65fe1080da9b&base={quote_ticker}&symbols={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base
