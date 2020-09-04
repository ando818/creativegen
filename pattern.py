import random

def getRand( num, range):
	randNums = []
	while len(randNums) < num:
		rand = random.randrange(0, range)
		if (not rand in randNums):
			randNums.append(rand)
	return randNums

class Pattern:
	def __init__(self, numSeqBits, numSymbolBits, numSymbolsPerSet, symbolSet, transitions):
		self.numSeqBits = numSeqBits
		self.numSymbolBits = numSymbolBits
		self.numSymbolsPerSet = numSymbolsPerSet
		self.symbolSet = symbolSet
		self.transitions = transitions
		self.seq = []

	def gen(self):
		symbolBits, symbolsNotUsed = self.symbolSetTransition(self.symbolSet)
		for i in range(0, self.numSeqBits):
			if (i % 5 == 0):
				symbolBits, symbolsNotUsed = self.symbolSetTransition(symbolsNotUsed)
			nextSet = self.symbolTransition(symbolBits)
			self.seq.append(nextSet)
			symbolBits = nextSet
		return self.seq

	def fillBits(self):
		symbolBits = []
		count = 0;
		randNums = self.getRand(self.numSymbolsPerSet, len(self.symbolSet));
		symbolsToUse = []
		symbolsNotUsed = []
		for i in range(0, len(self.symbolSet)):
			if i in randNums:
				symbolsToUse.append(self.symbolSet[i])
			else:
				symbolsNotUsed.append(self.symbolSet[i])
		for i in range(0, self.numSymbolBits):
			if (count == len(symbolsToUse)):
				count = 0
			symbolBits.append(symbolsToUse[count])
			count += 1
		return (symbolBits, symbolsNotUsed) 

	def symbolSetTransition(self, symbolsNotUsed):
		rand = random.randrange(0, len(self.transitions['symbolSet'][4]))
		symbolSetTransition = self.transitions['symbolSet'][4][rand]
		return symbolSetTransition.apply(self.symbolSet, symbolsNotUsed, self.numSymbolBits, self.numSymbolsPerSet)

	def symbolTransition(self, symbolBits):
		rand = random.randrange(0, len(self.transitions['symbol'][1]))
		randTransition = self.transitions['symbol'][1][rand]
		trasitionedBits =  randTransition.apply(symbolBits)
		return trasitionedBits



class SymbolTransition:
	def __init__(self):
		pass

class SymbolSetTransition:
	def __init__(self):
		pass

class Swap(SymbolTransition):
	def __init__(self):
		pass
	def apply(self, symbolBits):
		nextSet = symbolBits.copy()
		skipNext = False
		for i in range(0, len(nextSet) - 1, 2):
			nextSymbol = nextSet[i+1]
			nextSet[i+1] = nextSet[i]
			nextSet[i] = nextSymbol
		return nextSet

class ChangeColorSet(SymbolSetTransition):
	def __init__(self):
		pass
	def apply(self, symbolSet, symbolsNotUsed, numSymbolBits, numSymbolsPerSet):
		if (len(symbolsNotUsed) < numSymbolsPerSet):
			symbolsNotUsed = symbolSet
		count = 0;
		randNums = getRand(numSymbolsPerSet, len(symbolsNotUsed));
		symbolsToUse = []
		newSymbolsNotUsed = []

		symbolBits = []
		for i in range(0, len(symbolsNotUsed)):
			if i in randNums:
				symbolsToUse.append(symbolsNotUsed[i])
			else:
				newSymbolsNotUsed.append(symbolsNotUsed[i])
		for i in range(0, numSymbolBits):
			if (count == len(symbolsToUse)):
				count = 0
			symbolBits.append(symbolsToUse[count])
			count += 1
		return symbolBits, newSymbolsNotUsed
		