from tkinter import *
import math

class Rectangle:
	def __init__(self, width, height, color):
		self.width = width
		self.height = height
		self.color = color

	def color(self, color):
		self.color = color

	def getBox(self):
		return Box(0, self.width, 0, self.height)
class Line:
	def __init__(self, length, degrees):
		self.length = length
		self.degrees = degrees

	def getEndPoint(self):
		x = self.length * math.cos(math.radians(self.degrees))
		y = self.length * math.sin(math.radians(self.degrees))
		return Point(x,y)

	def getBox(self):
		endPoint = self.getEndPoint()
		if (endPoint.x >= 0 and endPoint.y >= 0):
			return Box(0, 0, endPoint.x, endPoint.y)
		if (endPoint.x >= 0 and endPoint.y <= 0):
			return Box(0, endPoint.y, endPoint.x, 0)
		if (endPoint.x <= 0 and endPoint.y < 0):
			return Box(endPoint.x, endPoint.y, 0, 0)
		if (endPoint.x <= 0 and endPoint.y >= 0):
			return Box(endPoint.x, 0, 0, endPoint.y)

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
		mTotal = Mold([Piece(pos, self.line, "")])
		if (self.endM):
			eMold, point = self.endM.weld()
			mTotal = mTotal.combine(eMold, self.getEndPoint(), point)
		return (mTotal, pos)

	def getEndPoint(self):
		x = self.length * math.cos(math.radians(self.degrees))
		y = self.length * math.sin(math.radians(self.degrees))
		return Point(x,y)

class MoldableRectangle:
	def __init__(self, width, height, color, name):
		self.rect = Rectangle(width, height, color)
		self.color = color
		self.name = name
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
		mTotal = Mold([Piece(pos, self.rect, self.name)])
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
	def __init__(self, point, obj, name):
		self.pos = point;
		self.name = name
		self.obj = obj
	def getBox(self):
		box = self.obj.getBox()
		box.topY += self.pos.y
		box.botY + self.pos.y
		box.topX += self.pos.x
		box.botX + self.pos.x
		return box

class Mold:
	def __init__(self, pieces):
		self.pieces = pieces

	def getPiece(self, name):
		for piece in self.pieces:
			if piece.name == name:
				return piece

	def combine(self, mold, pos1, pos2):
		xDiff = pos1.x - pos2.x
		yDiff = pos1.y - pos2.y
		for piece in mold.pieces:
			piece.pos.x += xDiff
			piece.pos.y += yDiff
		return Mold(self.pieces + mold.pieces)

	def getBox(self):
		topY = None
		topX = None
		botY = None
		botX = None
		for piece in self.pieces:
			pieceBox = piece.getBox()
			if (topY is None or pieceBox.topY < topY):
				topY = pieceBox.topY
			if (topX is None or pieceBox.topX < topX):
				topX = pieceBox.topX
			if (botX is None or pieceBox.botX > botX):
				botX = pieceBox.botX
			if (botY is None or pieceBox.botY > botY):
				botY = pieceBox.botY
		return Box(topX, topY, botX, botY)

	def Empty():
		return Mold([])

	def fitToOrigin(self):
		box = self.getBox()
		yOff = 0
		xOff = 0
		if (box.topY < 0):
			yOff = box.topY
		if (box.topX < 0):
			xOff = box.topX
		for piece in self.pieces:
			piece.pos.x -= xOff
			piece.pos.y -= yOff

class Box:
	def __init__(self, topX, topY, botX, botY):
		self.topX = topX
		self.topY = topY
		self.botX = botX
		self.botY = botY

	def combine(self, box2):
		topY = self.topY if self.topY > box2.topY else bot2.topY
		topX = self.topX if self.topX > box2.topX else bot2.topX
		botY = self.botY if self.botY < box2.botY else bot2.botY
		botX = self.botX if self.topY < box2.botX else bot2.botX

	def pointInside(self, point):
		return point.x > self.topX and point.x < botX and point.y < self.topY and point.y > self.botY

	def contains(self, box):
		return not (self.pointInside(Point(box.topX, box.topY)) or self.pointInside(Point(box.botX, box.botY)))

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __add__(self, o):
		return Point(self.x + o.x, self.y + o.y)