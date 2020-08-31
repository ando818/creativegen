from colors import *
from collections import defaultdict 
from moldpieces import Carve
class Window:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.molds = {}
		self.carves = defaultdict(list)
		self.generator = None

	def place(self, generator):
		self.generator = generator

	def draw(self, canvas):
		for startP in self.generator.carves:
			carves = self.generator.carves[startP]
			for carve in carves:
				carveX = carve.piece.point.x
				carveY = carve.piece.point.y
				objWidth = carve.piece.obj.width
				objHeight = carve.piece.obj.height
				canvas.create_rectangle(startP.x + carveX, startP.y + carveY, startP.x + carveX + objWidth, startP.y + carveY + objHeight, fill=carve.color)
				canvas.pack()

	def getCarves(self, l1, l2):
		l =[]
		for point in self.carves:
			for carve in self.carves[point]:
				meets = True
				meets = True if l1 == None else carve.piece.l1 == l1 
				meets = meets and (True if l2 == None else carve.piece.l2 == l2)
				if (meets):
					l.append(carve)
		return l

