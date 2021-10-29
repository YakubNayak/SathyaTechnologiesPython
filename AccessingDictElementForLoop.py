# Accessing dictinaries elements by using for loop

colors={'r':'red','g':'green','b':'blue','w':'white'}




for key in colors.keys():
	print(key)

	
# display the values
for value in colors.values():
	print(value)
# display the items in dictionary
for k,v in colors.items():
	print('key={},value={}'.format(k,v))
