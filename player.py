import time
class Player:
	def __init__(self, root, window, canvas, patternSeq):
		self.window = window
		self.root = root
		self.canvas = canvas
		self.patternSeq = patternSeq
		self.beat = 0

	def play(self, count, bpm):
		perSec = int(1 / (bpm/60) * 1000)
		seq = self.patternSeq[self.beat]
		for i in range(0,40):
			self.window.generator.getBuilding(i).setColor(seq[i-1])
			self.window.generator.getBuilding(i).setColor2(seq[i-1])
		count +=1 
		self.window.xPos +=20
		self.canvas.pack()
		self.window.draw(self.canvas)
		self.beat +=1
		self.root.after(perSec, self.play, count, bpm)


