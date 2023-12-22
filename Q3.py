# Q3.py

with open("sample_AAPL_for_mac_users.txt", "r") as f:
    apple_prices = [float(line) for line in f]

max_profit = 0
min_price = float('inf')

for price in apple_prices:
    min_price = min(min_price, price)
    max_profit = max(max_profit, price - min_price)

print("Largest possible profit:", max_profit)
