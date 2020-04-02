

def unique_in_order(iterable):
	new_list = []
	if len(iterable) > 0:
		for i, ele in enumerate(iterable[:-1]):
			if iterable[i] != iterable[i+1]:
				new_list.append(ele)
		if len(new_list) == 0:
			new_list.append(iterable[0])
		if new_list[-1] != iterable[-1]:
			new_list.append(iterable[-1])
	return new_list

print(unique_in_order(''))
print(unique_in_order('AA'))
print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order([1,2,2,3,3]))
