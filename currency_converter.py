# Simple Currency Converter

# Hardcoded exchange rates
exchange_rates = {
    "USD": {"EUR": 0.85, "GBP": 0.75, "INR": 74.50},
    "EUR": {"USD": 1.18, "GBP": 0.88, "INR": 88.00},
    "GBP": {"USD": 1.34, "EUR": 1.14, "INR": 99.00},
    "INR": {"USD": 0.013, "EUR": 0.011, "GBP": 0.010}
}

def convert_currency(amount, from_currency, to_currency):
    if from_currency in exchange_rates and to_currency in exchange_rates[from_currency]:
        rate = exchange_rates[from_currency][to_currency]
        return amount * rate
    else:
        return None

def currency_converter():
    print("Welcome to the Simple Currency Converter!")
    
    amount = float(input("Enter the amount: "))
    from_currency = input("Enter the currency to convert from (e.g., USD): ").upper()
    to_currency = input("Enter the currency to convert to (e.g., EUR): ").upper()
    
    result = convert_currency(amount, from_currency, to_currency)
    if result is not None:
        print(f"{amount} {from_currency} is equal to {result:.2f} {to_currency}")
    else:
        print("Conversion failed. Please check the currency codes and try again.")

# Run the currency converter
if __name__ == "__main__":
    currency_converter()
