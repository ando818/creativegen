from colors import *
from collections import defaultdict 
from moldpieces import Carve, Line, Rectangle, Box

class Window:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.molds = {}
		self.carves = defaultdict(list)
		self.generator = None
		self.xPos = 0
	def place(self, generator):
		self.generator = generator

	def draw(self, canvas):
		canvas.delete("all")

		for shape in self.generator.shapes:
			shapePos = shape.pos
			for component in shape.components:
				componentPos = component.pos
				self.drawMolds(canvas, component.molds, shapePos + componentPos)
			self.drawMolds(canvas, shape.molds, shapePos)

		canvas.pack()

	def drawMolds(self, canvas, molds, startPos):
		wBox = Box(self.xPos, self.xPos+self.width, 0, self.height)
		for mold in molds:
			print(mold)
			moldBox = mold.getBox()
			if (wBox.contains(moldBox)):
				for piece in mold.pieces:
					windowPos = startPos + piece.pos
					windowPos.x += self.xPos
					if (isinstance(piece.obj, Line)):
						canvas.create_line(windowPos.x, windowPos.y, windowPos.x + piece.obj.getEndPoint().x, windowPos.y + piece.obj.getEndPoint().y)
					if (isinstance(piece.obj, Rectangle)):
						xwidth = windowPos.x + piece.obj.width
						yheight = windowPos.y + piece.obj.height
						canvas.create_rectangle(windowPos.x, windowPos.y, xwidth, yheight, fill=piece.obj.color)

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