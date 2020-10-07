import random
def getRandN( num, range):
	randNums = []
	while len(randNums) < num:
		rand = random.randrange(0, range)
		if (not rand in randNums):
			randNums.append(rand)
	return randNums

def getRand(start, end):
	return random.randrange(start, end)
	