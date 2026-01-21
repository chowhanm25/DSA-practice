# 122. Best Time to Buy and Sell Stock II
# Problem: You can buy and sell multiple times, holding at most one share.

prices = [7, 4, 3, 1, 6, 7, 9, 11]  # Example input

previous = prices[0]
total_profit = 0

for i in range(1, len(prices)):
    current = prices[i]
    if current > previous:
        total_profit += current - previous
    previous = current

print("122. Best Time to Buy and Sell Stock II - Profit:", total_profit)

