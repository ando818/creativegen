from tkinter import *
import random
import time
from colors import colors

class Bar:
	def __init__(self, len, width, color):
		self.len = len
		self.width = width
		self.color = color

class Row:
	def __init__(self, bars):
		self.bars = bars;
	def draw(self):
		barStrs = []
		for bar in self.bars:
			barStrs.append("".join(['-' for i in range(0, bar.len)]))
		print("|".join(barStrs))
	def drawOnCanvas(self, startingHeight, canvas):
		point = 0;
		for bar in self.bars:
			canvas.create_rectangle(point, startingHeight, point+bar.len, startingHeight+bar.width, fill=bar.color)
			point += bar.len
		canvas.pack()
			

def createBars(screenSize, numBars, minBarSize, maxBarSize, barWidth):
	sizeRemain = screenSize;
	bars = []
	for i in range(0, numBars):
		numRemain = numBars - i -1;
		smallestPossible = sizeRemain - (numRemain*maxBarSize)
		largestPossible = sizeRemain - (numRemain*minBarSize)
		barLength = random.randint(max(smallestPossible, minBarSize), min(maxBarSize, largestPossible))
		sizeRemain -= barLength
		randColor = colors[random.randint(0, len(colors)-1)]
		bars.append(Bar(barLength, barWidth, randColor))
	return bars

def genRows(numRows):
        rows =[]
        for i in range(0,numRows):
                bars = createBars(2560, 8, 250, 600, 100);
                rows.append(Row(bars))
        return rows;

def moveRows(rows):
        rows.pop()
        bars = createBars(2560, 8, 100, 450, 100);
        rows.insert(0, Row(bars))
        return rows

root = Tk()
w = Canvas(root, width=2560, height=1000)
rrows = genRows(10)

def draw():
	startingHeight = 0;
	for row in genRows(10):
		row.drawOnCanvas(startingHeight, w)
		startingHeight += 100
	w.after(250, draw)

draw()
