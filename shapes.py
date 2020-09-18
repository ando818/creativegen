from moldpieces import *
from collections import defaultdict
class Star:
	def __init__(self, l, orient):
		self.orient = orient
		l1 = MoldableLine(l*1.36, self.orient + 60)
		l2 = MoldableLine(l, self.orient +  15)
		l3 = MoldableLine(l, self.orient +  150)
		l4 = MoldableLine(l, self.orient +  85)
		l5 = MoldableLine(l, self.orient +  210)
		l6 = MoldableLine(l, self.orient +  150)
		l7 = MoldableLine(l, self.orient +  275)
		l8 = MoldableLine(l, self.orient +  210)
		l9 = MoldableLine(l, self.orient +  345)
		l9 = MoldableLine(l, self.orient +  345)
		l10 = MoldableLine(l*1.36, self.orient + 300)
		l1.end(l2)
		l2.end(l3)
		l3.end(l4)
		l4.end(l5)
		l5.end(l6)
		l6.end(l7)
		l7.end(l8)
		l8.end(l9)
		l9.end(l10)

		self.carves = defaultdict(list)
		mold, point = l1.weld()
		mold.fitToOrigin()
		for piece in mold.pieces:
			self.carves[Point(0, 50)].append(Carve(Point(0, 0), piece))

	def getCarves(self):
		return self.carves

class Building:
	def __init__(self, l, w):
		l1 = MoldableLine(l, 270)
		l2 = MoldableLine(w, 0)
		l3 = MoldableLine(l, 90)
		window = MoldableRectangle(w/4, w/4, "", "")

		l1.end(l2)
		l2.end(l3)
		self.molds = defaultdict(list)
		mold, point = l1.weld()
		mold.fitToOrigin()
		self.molds[point].append(mold)
			
		wmold, point = window.weld()
		wPoint = Point(point.x + 20, point.y + 20)
		self.molds[wPoint].append(wmold)

	def drawOnCanvas(self, canvas):
		pass

	def getCarves(self):
		return self.carves
