# Q2.py

import matplotlib.pyplot as plt

with open("sample_AAPL_for_mac_users.txt", "r") as f:
    apple_prices = [float(line) for line in f]

x_values = range(1, len(apple_prices) + 1)

plt.plot(x_values, apple_prices)
plt.title('Apple Stock Price, Nov 2019 to Nov 2020')
plt.xlabel('Day')
plt.ylabel('Trading price')
plt.show()
