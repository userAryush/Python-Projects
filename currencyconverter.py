# Currency Converter

def convert_currency(amount, from_currency, to_currency):
    
    exchange_rates = {
        "USD": {"INR": 83.0, "EUR": 0.92, "GBP": 0.78},
        "INR": {"USD": 0.012, "EUR": 0.011, "GBP": 0.0094},
        "EUR": {"USD": 1.09, "INR": 89.5, "GBP": 0.85},
        "GBP": {"USD": 1.28, "INR": 106.4, "EUR": 1.18}
    }
    
    # Check if conversion exists
    if from_currency in exchange_rates and to_currency in exchange_rates[from_currency]:
        converted_amount = amount * exchange_rates[from_currency][to_currency]
        return round(converted_amount, 2)
    else:
        return None

amount = float(input("Enter the amount: "))
from_currency = input("Enter the currency you have (USD, INR, EUR, GBP): ").upper()
to_currency = input("Enter the currency to convert to (USD, INR, EUR, GBP): ").upper()


result = convert_currency(amount, from_currency, to_currency)
if result is not None:
    print(f"{amount} {from_currency} is equal to {result} {to_currency}.")
else:
    print("Invalid currency conversion request.")
