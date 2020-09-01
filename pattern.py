import random
class Pattern:
	def __init__(self, numSeqBits, numSymbolBits, symbolSet, transitions):
		self.numSeqBits = numSeqBits
		self.numSymbolBits = numSymbolBits
		self.symbolSet = symbolSet
		self.transitions = transitions
		self.seq = []

	def gen(self):
		symbolBits = self.fillBits()
		for i in range(0, self.numSeqBits):
			nextSet = self.transition(symbolBits)
			self.seq.append(nextSet)
			symbolBits = nextSet
		return self.seq

	def fillBits(self):
		symbolBits = []
		count = 0;
		for i in range(0, self.numSymbolBits):
			if (count == len(self.symbolSet)):
				count = 0
			symbolBits.append(self.symbolSet[count])
			count += 1
		return symbolBits

	def transition(self, symbolBits):
		rand = random.randrange(0, len(self.transitions))
		randTransition = self.transitions[rand]
		return randTransition.apply(symbolBits)

class Transition:
	def __init__(self):
		pass
	def apply(self, symbolBits):
		nextSet = symbolBits.copy()
		for i in range(0, len(nextSet) - 1):
			if (i %2 == 0):
				pass
			nextSymbol = nextSet[i+1]
			nextSet[i+1] = nextSet[0]
			nextSet[i] = nextSymbol
		return nextSet


seq = Pattern(16, 10, ['R', 'G'], [Transition()]).gen()
