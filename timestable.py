from tkinter import *

class Rectangle:
	def __init__(self, width, height):
		self.width = width
		self.height = height

class MoldableRectangle:
	def __init__(self, width, height):
		self.rect = Rectangle(width, height)
		self.lEnd = None
		self.rEnd = None
		self.tEnd = None

	def attachLeft(self, mRect):
		self.lEnd = mRect
	def attachRight(self, mRect):
		self.rEnd = mRect
	def attachTop(self, mRect):
		self.tEnd = mRect
	def asBox(self):
		return 
	def weld(self):
		if (self.rect == None):
			return Mold([])

		mTotal = Mold([Piece(Point(0,0), self.rect)])
		if (self.tEnd):
			mTotal = self.tEnd.weld().combine(mTotal, Point(0, self.tEnd.rect.height,))
		if (self.rEnd):
			print("yO?")
			mTotal.combine(self.rEnd.weld(), Point(self.rect.width, 0))
		return mTotal

class Piece:
	def __init__(self, point, obj):
		self.point = point;
		self.obj = obj

class Mold:
	def __init__(self, pieces):
		self.pieces = pieces
	def combine(self, mold, connPoint):
		for piece in mold.pieces:
			piece.point.x += connPoint.x
			piece.point.y += connPoint.y
		return Mold(self.pieces + mold.pieces)
	def Empty():
		return Mold([])

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Window:
	def __init__(self, width, height):
		self.width = width
		self.height = height;
		self.molds = {}

	def place(self, point, mold):
		self.molds[point] = mold

	def draw(self, canvas):
		for point in self.molds:
			mold = self.molds[point]
			for piece in mold.pieces:
				canvas.create_rectangle(point.x + piece.point.x, point.y + piece.point.y, point.x + piece.point.x+ piece.obj.width, point.y + piece.point.y + piece.obj.height)
				canvas.pack()

def genMolds():
	for i in range(0,5):
		rect = MoldableRectangle(100, 100);



rect = MoldableRectangle(100, 100);
rect2 = MoldableRectangle(100, 100);
rect3 = MoldableRectangle(200, 100);

rect.attachTop(rect2)
rect.attachRight(rect3)

window = Window(400, 400)
window.place(Point(100,100), rect.weld())
root = Tk()
canvas = Canvas(root, width=window.width, height=window.height)
window.draw(canvas)
