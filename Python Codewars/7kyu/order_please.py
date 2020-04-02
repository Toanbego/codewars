

def order(sentence):
	# Split words
	words = sentence.split(" ")

	# Extract digits
	words_order = get_order(words)

	# Order the words
	new_string = []
	sorted_words = sorted(words_order.keys())
	for key in sorted_words:
		new_string.append(words_order[key])
	return " ".join(new_string)


def get_order(words):
	sorted_words = {}
	for word in words:
		digit = ""
		for i in word:
			if i.isdigit():
				digit += i
		sorted_words[digit] = word
	return sorted_words


print(order('is2 Thi1s T4est 3a'))
print(order(''))
