import time
class Player:
	def __init__(self, root, window, canvas, generator, patternSeq):
		self.window = window
		self.root = root
		self.canvas = canvas
		self.generator = generator
		self.patternSeq = patternSeq
		self.beat = 0

	def play(self, bpm):
		perSec = int(1 / (bpm/60) * 1000)
		seq = self.patternSeq[self.beat]
		for l in range(1,10):
			color = seq[l-1]
			for point in self.generator.getLShape(l):
				carve = self.generator.getCarves(point[0], point[1])[0]
				carve.color = color
		self.canvas.pack()
		self.window.draw(self.canvas)
		self.beat +=1
		self.root.after(perSec, self.play, bpm)


