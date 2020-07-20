from tkinter import *
from moldpieces import *
from window import Window
from colors import *

def genMolds(i):
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

window = Window(800, 800)
starty=0

for i in range(1,4):
	rect2= genMolds(i)
	finalMold, pos = rect2.weld()
	window.place(Point(0,starty), finalMold)
	starty+=100

carves = window.getCarves(None, None)

root = Tk()
canvas = Canvas(root, width=window.width, height=window.height)
window.draw(canvas)

for carve in window.getCarves(1, None):
	carve.color = 'red'

window.draw(canvas)