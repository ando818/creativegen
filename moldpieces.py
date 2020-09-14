from tkinter import *
import math

class Rectangle:
	def __init__(self, width, height):
		self.width = width
		self.height = height

class Line:
	def __init__(self, length, degrees):
		self.length = length
		self.degrees = degrees

	def getEndPoint(self):
		x = self.length * math.cos(math.radians(self.degrees))
		y = self.length * math.sin(math.radians(self.degrees))
		return Point(x,y)

class Hollow:
	def __init_(self, width, height, image):
		self.width = width;
		self.height = height;

class Carve():
	def __init__(self, point, piece):
		self.point = point
		self.piece = piece
		self.color = 'white'
	def color(self, color):
		self.color = color

class MoldableLine:
	def __init__(self, length, degrees):
		self.line = Line(length, degrees)
		self.length = length
		self.degrees = degrees
		self.endM = None

	def end(self, mLine):
		self.endM = mLine
	
	def weld(self):
		if (self.line == None):
			return Mold([])
		pos = Point(0,0)
		mTotal = Mold([Piece(pos, self.line, "", "")])
		if (self.endM):
			eMold, point = self.endM.weld()
			mTotal = mTotal.combine(eMold, point, self.getEndPoint())
		return (mTotal, pos)

	def getEndPoint(self):
		x = self.length * math.cos(math.radians(self.degrees))
		y = self.length * math.sin(math.radians(self.degrees))
		print(x)
		return Point(x,y)

class MoldableRectangle:
	def __init__(self, width, height, l1, l2):
		self.rect = Rectangle(width, height)
		self.lEnd = None
		self.rEnd = None
		self.tEnd = None
		self.bEnd = None
		self.l1 = l1
		self.l2 = l2
	def left(self, mRect):
		self.lEnd = mRect
		return mRect
	def right(self, mRect):
		self.rEnd = mRect
		return mRect
	def top(self, mRect):
		self.tEnd = mRect
		return mRect
	def bot(self, mRect):
		self.bEnd = mRect;
		return mRect
	def asBox(self):
		return 
	def weld(self):
		if (self.rect == None):
			return Mold([])

		pos = Point(0,0)
		mTotal = Mold([Piece(pos, self.rect, self.l1, self.l2)])
		if (self.lEnd): 
			lMold, lPos = self.lEnd.weld()
			newPos = Point(lPos.x + self.lEnd.rect.width, lPos.y)
			mTotal = lMold.combine(mTotal, pos, newPos);
			pos = newPos
		if (self.tEnd): 
			tMold, tPos = self.tEnd.weld()
			newPos = Point(tPos.x, tPos.y + self.tEnd.rect.height)
			mTotal = tMold.combine(mTotal, pos, newPos); 
			pos = newPos
		if (self.rEnd):
			rMold, rPos = self.rEnd.weld()
			mTotal = mTotal.combine(rMold, rPos, Point(pos.x + self.rect.width, pos.y));
		if (self.bEnd): 
			bMold, bPos = self.bEnd.weld()
			mTotal = mTotal.combine(bMold, bPos, Point(pos.x, pos.y + self.rect.height))
		return (mTotal, pos)

class Piece:
	def __init__(self, point, obj, l1, l2):
		self.point = point;
		self.l1 = l1
		self.l2 = l2
		self.obj = obj

class Mold:
	def __init__(self, pieces):
		self.pieces = pieces
	def combine(self, mold, pos1, pos2):
		xDiff = (pos2.x - pos1.x)
		yDiff = (pos2.y - pos1.y)
		for piece in mold.pieces:
			piece.point.x += xDiff
			piece.point.y += yDiff
		return Mold(self.pieces + mold.pieces)

	def Empty():
		return Mold([])

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y