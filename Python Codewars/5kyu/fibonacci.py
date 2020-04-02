
def fibonacci(n):
	fibonacci = [0, 1]
	if n in [0, 1]:
		return n
	for i in range(n-1):
		fibonacci.append(fibonacci[i] + fibonacci[i+1])
	return fibonacci[-1]


print(fibonacci(50))
