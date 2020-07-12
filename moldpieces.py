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
		self.bEnd = None
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
		mTotal = Mold([Piece(pos, self.rect)])
		if (self.lEnd): 
			lMold, lPos = self.lEnd.weld()
			newPos = Point(lPos.x + self.lEnd.rect.width, lPos.y)
			mTotal = lMold.combine(mTotal, pos, newPos);
			pos = newPos
		if (self.tEnd): 
			tMold, tPos = self.tEnd.weld()
			print(tPos.y)
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
	def __init__(self, point, obj):
		self.point = point;
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