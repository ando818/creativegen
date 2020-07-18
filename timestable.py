from tkinter import *
from moldpieces import *
from window import Window
from colors import *

def genMolds(i):
	row = i
	col = 0
	base = MoldableRectangle(100, 100, row, col);
	orig = base
	for j in range(0,i-1):
		col += 1
		orig = orig.right(MoldableRectangle(100, 100, row, col))
	
	topBase = MoldableRectangle(100, 100, row, col);
	topOrig = topBase
	for j in range(0, i-2):
		print(row)
		topOrig = topOrig.top(MoldableRectangle(100, 100, row, col))
		row -= 1

	orig.top(topBase)
	return base

window = Window(800, 800)
starty=0
for i in range(1,10):
	rect2= genMolds(i)
	finalMold, pos = rect2.weld()
	window.place(Point(0,starty), finalMold)
	starty+=100

carves = window.getCarves()

root = Tk()
canvas = Canvas(root, width=window.width, height=window.height)
window.draw(canvas)

genMolds(3)
window.getByL1(3)