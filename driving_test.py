country = input('國家')
age = int(input('年齡'))
if country == '台灣':
	if age >= 18:
		print('can')
	else:
		print("can't")
elif country == '美國':
	if age >=16:
		print('can')
	else:
		print("can't")