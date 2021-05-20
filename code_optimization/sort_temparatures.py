temp_hash = {97.0: 0, 97.1: 0, 97.2: 0, 97.3: 0, 97.4: 0, 97.5: 0, 97.6: 0, 97.7: 0, 97.8: 0, 97.9: 0, 98.0: 0, 98.1: 0, 98.2: 0, 98.3: 0, 98.4: 0, 98.5: 0, 98.6: 0, 98.7: 0, 98.8: 0, 98.9: 0, 99.0: 0}


array = [98.6, 98.0, 97.1, 99.0, 98.9, 97.8, 98.5, 98.2, 98.0, 97.1]

for tmp in array:
	if tmp in temp_hash:
		temp_hash[tmp] += 1

sorted_array = []
for key, value in temp_hash.items():
	if value > 0:
		for x in range(0, value):
			sorted_array.append(key)

print(sorted_array)
