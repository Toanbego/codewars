class User:
	def __init__(self):
		self.ranks = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]
		self.rank = self.ranks[0]
		self.progress = 0


	def inc_progress(self, activity_rank):
		"""
		increments progress
		:return:
		"""
		# print("Current rank: ", self.rank, "\nCurrent progress: ", self.progress, "\nActivity rank: ", activity_rank)
		if self.ranks.index(activity_rank) == self.ranks.index(self.rank):
			self.progress += 3
		elif self.ranks.index(activity_rank) == self.ranks.index(self.rank) - 1:
			self.progress += 1
		elif self.ranks.index(activity_rank) < self.ranks.index(self.rank) - 1:
			pass
		elif self.ranks.index(activity_rank) > self.ranks.index(self.rank):

			self.progress += 10 * (self.ranks.index(activity_rank) - self.ranks.index(self.rank)) * (self.ranks.index(activity_rank) - self.ranks.index(self.rank))
		self.check_progress()
		# print("New rank: ", self.rank, "\nNew progress: ", self.progress, "\nActivity rank: ", activity_rank)

	def check_progress(self):
		leftover = self.progress
		rank_idx = self.ranks.index(self.rank)
		while leftover >= 100 and not rank_idx > 17:
			rank_idx += 1
			leftover -= 100
		self.rank = self.ranks[rank_idx]
		if self.rank == 8:
			self.progress = 0
		else:
			self.progress = leftover


user = User()
user.rank = 7
user.progress = 91
user.inc_progress(8)
print(user.progress, 0)
print(user.rank, 8)
# user.inc_progress(-5)
# print(user.progress, 0)
# print(user.rank, -7)

