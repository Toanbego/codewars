def add(number):
	return CustomInt(number)


class CustomInt(int):
	def __call__(self, v):
		return CustomInt(self + v)



