from moldpieces import *
from collections import defaultdict

class Shape:
	def __init__(self):
		self.x = None
		self.y = None
		self.molds = None


class Star(Shape):
	def __init__(self, pos, l, orient, color):
		self.pos = pos
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

		lines = [l1,l2,l3,l4,l5]


		self.carves = defaultdict(list)
		mold, point = l1.weld()
		mold.fitToOrigin()
		points = []
		for piece in mold.pieces:
			points.append(piece.pos)
			points.append(piece.pos + piece.obj.getEndPoint())

		self.molds = [mold]
		self.components = []
	def getCarves(self):
		return self.carves


class BuildingWindow(Shape):
	def __init__(self, pos, w, color):
		self.pos = pos;
		self.mold, self.point = MoldableRectangle(w/4, w/4, color,  "windowRect").weld()
		self.molds = [self.mold]
		self.components = []

	def setColor(self, color):
		self.mold.getPiece("windowRect").obj.color = color

class BuildingShell(Shape):
	def __init__(self, pos, h, w, color):
		self.pos = pos;
		l1 = MoldableRectangle(w, h, color, "shell")
		lMold, point = l1.weld()
		self.molds = [lMold]

class Building(Shape):
	def __init__(self, pos, h, w, windowHeight, shellColor, w1Color, w2Color):
		self.pos = pos
		self.molds = []

		self.bShell = BuildingShell(Point(0,0), h, w, shellColor)
		self.window = BuildingWindow(Point(10,10), windowHeight, w1Color);
		self.window2 = BuildingWindow(Point(50,10), windowHeight, w2Color);
		self.components = [self.bShell, self.window, self.window2]

	def setColor(self, color):
		self.window.setColor(color)

	def setColor2(self, color):
		self.window2.setColor(color)

	def drawOnCanvas(self, canvas):
		pass

	def getCarves(self):
		return self.carves

class Road(Shape):
	def __init__(self, pos, l, w):
		self.pos = pos
		self.components = []

		road, pos = MoldableRectangle(l, w, "black", "road").weld()

		stripe = Mold([])
		x = 0
		for i in range(0, 10):
			newStripe, pos = MoldableRectangle(60, w/7, "yellow", "stripe").weld()
			road = road.combine(newStripe, Point(x,w/2 - w/14), Point(0,0))
			x +=200
		print(len(road.pieces))
		self.molds = [road]

	def setColor(self, color):
		self.window.setColor(color)

	def setColor2(self, color):
		self.window2.setColor(color)

	def drawOnCanvas(self, canvas):
		pass

	def getCarves(self):
		return self.carves
