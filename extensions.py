import requests
import json
from config import apiKey, keys

class ConvertionException(Exception):
    pass

class APIException(Exception):
    pass

class СurrencyConverter:
    #@staticmethod
    def get_price(base, quote, amount):

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обрабоатать валюьу:{base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обрабоатать валюьу:{quote}')

        try:
            amount=float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обрабоатать количество:{amount}')

        if base == quote:
            raise ConvertionException('Невозможно перевести валюты одинаковых типов')

        currency=f"{base_ticker}_{quote_ticker}"
        req = requests.get(f'https://free.currconv.com/api/v7/convert?q={currency}&compact=ultra&apiKey={apiKey}')
        result=float(json.loads(req.content)[currency])*amount
        return result





