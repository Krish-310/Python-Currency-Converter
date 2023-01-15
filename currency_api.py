import requests

from_currency = str(input("Enter the currency you would like to convert from: ")).upper()

to_currency = str(input ("Enter the currency you would like to convert to: ")).upper()

amount = float(input("Enter the amount of money you would like to convert: "))

response = requests.get(f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")

print(f"{amount} {from_currency} is {response.json()['rates'][to_currency]}")






