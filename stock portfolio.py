# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "MSFT": 330,
    "AMZN": 135
}

# Dictionary to store user portfolio
portfolio = {}

# Taking input
print("Enter stock symbols and quantities. Type 'done' to finish.")

while True:
    stock = input("Stock Symbol: ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not in the price list.")
        continue
    try:
        quantity = int(input(f"Quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Please enter a valid number.")

# Calculate total investment
total_value = 0
print("\nYour Portfolio Summary:")
for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    total_value += value
    print(f"{stock}: {quantity} shares × ₹{stock_prices[stock]} = ₹{value}")

print(f"\nTotal Investment Value: ₹{total_value}")

# Optionally write to file
save = input("\nDo you want to save this to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        for stock, quantity in portfolio.items():
            value = stock_prices[stock] * quantity
            file.write(f"{stock}: {quantity} shares × ₹{stock_prices[stock]} = ₹{value}\n")
        file.write(f"\nTotal Investment Value: ₹{total_value}")
    print("Portfolio saved to 'portfolio_summary.txt'")