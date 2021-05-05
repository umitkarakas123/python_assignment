sales = {
    "cost_value" : 65.87,
    "sell_value" : 95.48,
    "inventory" : 10000
}
cost = sales["cost_value"]
sell = sales["sell_value"]
inven = sales["inventory"]
total_profit = ((sell - cost) * inven)
total_profit = int(total_profit)
print("Total Profit: ", total_profit)