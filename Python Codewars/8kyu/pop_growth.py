
def nb_year(p0, percent, aug, p):
	year = 0
	percent = percent/100
	year = population_increase(p0, percent, aug, p, year)

	return year


def population_increase(p0, percent, aug, p, year):
	p0 = p0 + p0 * percent + aug
	year += 1
	if p0 <= p:
		year = population_increase(p0, percent, aug, p, year)
	return year


print(nb_year(1500, 5, 100, 5000))
