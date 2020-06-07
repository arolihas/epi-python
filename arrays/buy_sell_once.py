def buy_sell_stock_once(prices):
    max_profit = 0
    min_price = float('inf')
    for i in range(len(prices)):
        max_profit = max(max_profit, prices[i] - min_price)
        min_price = min(min_price, prices[i])
    return max_profit
