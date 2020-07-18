from colors import *
from collections import defaultdict 

class Window:
	def __init__(self, width, height):
		self.width = width
		self.height = height;
		self.molds = {}
		self.carves = defaultdict(list)
		self.carvesByL1 = defaultdict(list)
		self.carvesByL2 = defaultdict(list)

	def place(self, point, mold):
		for piece in mold.pieces:
			self.carves[point].append(Carve(point, piece))
			if (hasattr(piece, "l1")):
				self.carvesByL1[piece.l1].append(Carve(point, piece))
			if (hasattr(piece, "l1")):
				self.carvesByL2[piece.l2].append(Carve(point, piece))

	def draw(self, canvas):
		for startP in self.carves:
			carves = self.carves[startP]
			for carve in carves:
				carveX = carve.piece.point.x
				carveY = carve.piece.point.y
				objWidth = carve.piece.obj.width
				objHeight = carve.piece.obj.height
				canvas.create_rectangle(startP.x + carveX, startP.y + carveY, startP.x + carveX + objWidth, startP.y + carveY + objHeight, fill=carve.color)
				canvas.pack()

	def getCarves(self):
		l = []
		for p in self.carves:
			l.extend(self.carves[p])
		return l
	def getByL1(self, l1):
		l =[]
		carves =  self.carvesByL1[l1]
		for carve in carves:
			for p in self.carves:
				for c in self.carves[p]:
					if (c.piece.l1 == carve.piece.l1):
						print(c.piece.l1)
						l.append(c)
		return l



class Carve():
	def __init__(self, point, piece):
		self.point = point
		self.piece = piece
		self.color = 'white'
	def color(self, color):
		self.color = color
