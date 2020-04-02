import re
def solution(comment, markers):
	new_string = []
	for line in comment.splitlines():
		for marker in markers:
			line = line.replace(marker, "æ")
		line = re.sub(f"(\s*æ.*)", "", line)
		new_string.append("".join([line, "\n"]))
	return "".join(new_string)[:-1]


print(solution("apples, pears § and bananas\ngrapes\navocado *apples", ["*", "§"]))
# "apples, pears\ngrapes\nbananas
print(solution("a #b\nc\nd $e f g", ["#", "$"]))
# #"a\nc\nd"
pass