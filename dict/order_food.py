menu = {'sandwich': 10, 'tea': 7}
def order():
	total = 0
	while True:
		item = input('Order: ')
		if item == '':
			break
		if item in menu:
			total += menu.get(item)
			print(f'{item} costs {menu.get(item)}, total is {total}')
		else:
			print(f'Sorry, we are fresh out of elephant today.')
	print(f'Your total is {total}')