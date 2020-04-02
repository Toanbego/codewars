
def likes(like_names):
	"""
	:param like_names
	:return:
	"""
	if len(like_names) == 0:
		return "no one likes this"
	elif len(like_names) == 1:
		return f"{like_names[0]} likes this"
	elif len(like_names) == 2:
		return f"{like_names[0]} and {like_names[1]} like this"
	elif len(like_names) == 3:
		return f"{like_names[0]}, {like_names[1]} and {like_names[2]} like this"
	elif len(like_names) >= 4:
		return f"{like_names[0]}, {like_names[1]} and {len(like_names)-2} others likes this"


print(likes([]))  # must be "no one likes this"
print(likes(["Peter"]))  # must be "Peter likes this"
print(likes(["Jacob", "Alex"]))  # must be "Jacob and Alex like this"
print(likes(["Max", "John", "Mark"])) # must be "Max, John and Mark like this"
print(likes(["Alex", "Jacob", "Mark", "Max"]))  # must be "Alex, Jacob and 2 others like this"