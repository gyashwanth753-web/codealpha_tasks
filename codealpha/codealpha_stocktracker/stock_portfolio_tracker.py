# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 135,
    "TCS": 3900,
    "ITC": 450
}

total_investment = 0

print(" Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))
print("Type 'done' to finish\n")

while True:
    stock = input("Enter stock name: ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))
        value = stock_prices[stock] * quantity
        total_investment += value
        print(f"Added {stock}: ₹{value}\n")
    else:
        print("Stock not available!\n")

print(" Total Investment Value: ₹", total_investment)

save = input("Do you want to save the result? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w", encoding="utf-8") as file:
        file.write(f"Total Investment Value: ₹{total_investment}")
    print(" Saved to portfolio.txt")
