

def format_duration(seconds):
	# seconds, minutes, hours, days, months, years = 0, 0, 0, 0, 0, 0
	# Find years
	years = seconds/31556926
	print(years)


format_duration(62)  # returns "1 minute and 2 seconds"
format_duration(31556926*2.2)  # returns "1 hour, 1 minute and 2 seconds"