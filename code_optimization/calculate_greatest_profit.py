def calculate_greatest_profit(array):
	buy_price = array[0]
	greatest_profit = 0
	for price in array:
		if price < buy_price:
			buy_price = price
		else:
			potential_profit = price - buy_price
			greatest_profit = potential_profit if potential_profit > greatest_profit else greatest_profit
	return greatest_profit


prices = [10, 7, 5, 8, 11, 2, 6]
calculate_greatest_profit(prices)
