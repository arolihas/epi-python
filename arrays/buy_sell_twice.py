# O(n) time and space solution
def buy_sell_stock_twice(prices):
    min_price = float('inf')
    max_profit = 0
    first_buy_sell = []
    for i in range(len(prices):
        min_price = min(min_price, prices[i])
        max_profit = max(max_profit, prices[i] - min_price)
        first_buy_sell[i] = max_profit
    max_price = float('-inf')
    for i in reversed(range(1, len(prices)):
        max_price = max(max_price, prices[i])
        max_profit = max(max_profit, 
                         max_price - prices[i] + first_buy_sell[i - 1])
    return max_profit


# O(n) time and O(1) space
def better_buy_sell_twice(prices):
    min_price = float('inf')
    max_profit = 0
    max_price = float('-inf')
    for i in range(len(prices)):
        rev = len(prices) - i  - 1
        min_price = min(min_price, prices[i])
        max_price = max(max_price, prices[rev])
        max_profit = max(max_profit, 
                         max_price - prices[rev] + prices[i] - min_price)
    return max_profit
    
