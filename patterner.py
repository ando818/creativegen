class Patterner:
	def __init__(self, symbols, numBits):
		self.symbols = symbols
		self.numBits = numBits
	def generate(self):
		pass

Patterner(
	{
		"loudness": ["S", "H"],
		"hitTogether": ["T", "F"]
	})