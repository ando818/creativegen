from collections import defaultdict 
from moldpieces import *

class Generator:
	def __init__(self):
		pass
		self.molds = []
		self.carves = defaultdict(list)
		self.setup()

	def setup(self):
		starty = 0
		for i in range(1,10):
			rect2= self.genRow(i)
			finalMold, pos = rect2.weld()
			self.molds.append(finalMold)
			for piece in finalMold.pieces:
				self.carves[Point(0, starty)].append(Carve(Point(0, starty), piece))
			starty +=100

	def genRow(self, i):
		if i == 1:
			return MoldableRectangle(100, 100, 1, 1);
		row = i
		col = 1
		base = MoldableRectangle(100, 100, row, col);
		orig = base
		for j in range(0,i-1):
			col += 1
			orig = orig.right(MoldableRectangle(100, 100, row, col))
		
		row -=1
		topBase = MoldableRectangle(100, 100, row, col);
		topOrig = topBase
		for j in range(0, i-2):
			row -= 1
			topOrig = topOrig.top(MoldableRectangle(100, 100, row, col))
			
		orig.top(topBase)
		return base

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

	def getLShape(self, i):
		if i == 1:
			return [(1,1)]
		points = []
		row = i
		col = row
		for j in range(1, row+1):
			points.append((row, j))

		for k in range(i-1, 0, -1):
			row -=1
			points.append((row, col))
		return points