

def high_and_low(numbers):
	numbers = sorted(numbers.split(" "), reverse=True)
	for i in range(len(numbers)):
		numbers[i] = int(numbers[i])
	numbers = str(max(numbers)) + " " + str(min(numbers))
	return numbers


print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))