MENU = {'sandwich': 10, 'tea': 7, 'salad': 9}

def restaurant():
	total = 0
	while True:
		order = input('Order: ').strip()
		
		if not order:
			break
		
		if order in MENU:
			price = MENU.get(order)
			total += price
			print(f'{order} costs {price}, total is {total}')

		else:
			print(f'Sorry, we are fresh out of elephant today.')

	print(f'Your total is {total}')


restaurant()