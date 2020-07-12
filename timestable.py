from tkinter import *
from moldpieces import *
from window import Window
from colors import *

def genMolds(i):
	base = MoldableRectangle(100, 100);
	orig = base
	for j in range(0,i-1):
		orig = orig.right(MoldableRectangle(100, 100))
		
	topBase = MoldableRectangle(100, 100);
	topOrig = topBase
	for j in range(0, i-2):
		topOrig = topOrig.top(MoldableRectangle(100, 100))
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

for p in window.carves:
	window.carves[p][0].color = 'red'

window.draw(canvas)
