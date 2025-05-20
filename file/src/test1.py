corteval = [2288.514339, 8565.514233, 18263.37411, 65618.92567]

def cortes(areakm2):
	j = 1
	for i in corteval:
		if areakm2 <= i:
			return j
		j += 1

print('Corte: ' + str(cortes(50000)))