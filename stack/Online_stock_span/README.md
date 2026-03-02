# Stock Span Problem

## Problem
Design a StockSpanner class that returns the span of the stock’s price for the current day.

## Approach
We use a monotonic decreasing stack storing (price, span).

Each time a new price comes:
- Pop smaller or equal prices
- Add their spans
- Push (price, span)

## Time Complexity
O(1) amortized per call

## Space Complexity
O(n)

## Example
Input:
[100,80,60,70,60,75,85]

Output:
[1,1,1,2,1,4,6]
