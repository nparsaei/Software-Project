# Q1.py
with open("sample_AAPL_for_mac_users.txt", "r") as f:
    apple_prices = [float(line) for line in f]
    mean_price = sum(apple_prices) / len(apple_prices)
    std_deviation = (sum((price - mean_price) ** 2 for price in apple_prices) / len(apple_prices)) ** 0.5
print("Mean price:", mean_price)
print("Standard Deviation:", std_deviation)
