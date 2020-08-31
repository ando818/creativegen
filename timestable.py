from tkinter import *
from moldpieces import *
from window import Window
from colors import *
from generator import Generator

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


root = Tk()
canvas = Canvas(root, width=window.width, height=window.height)
gen = Generator()
window.place(gen)

def draw(counter, colorSet):
	counter +=1
	colorSet = {}
	for l in range(1,10):
		color = getRandColor()
		colorSet[l] = color
		if counter % 2 == 0:
			color = colorSet[l]
		if counter % 4 == 0:
			color = 'red'

		for point in gen.getLShape(l):
			carve = gen.getCarves(point[0], point[1])[0]
			carve.color = color
	canvas.pack()
	window.draw(canvas)
	root.after(430, draw, counter, colorSet)
draw(0, [])