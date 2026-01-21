# 122. Best Time to Buy and Sell Stock II

## Problem Statement
Given an array of stock prices, where prices[i] is the price on the ith day.  
You can buy and sell multiple times, but can hold at most one share at a time.  
Find the maximum profit.

## Example

## Approach
- Initialize `previous` as the first price, `total_profit = 0`.
- Traverse the array from the second element.
- If current > previous, add difference to `total_profit`.
- Update `previous` to current.
- Captures all upward steps for multiple transactions.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

## How to Run
```bash
python best_time_to_buy_and_sell_stock_ii.py

