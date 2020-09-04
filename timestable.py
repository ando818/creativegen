from tkinter import *
from moldpieces import *
from window import Window
from colors import *
from generator import Generator
from pattern import *
from player import Player

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

colorSet = []
for i in range(0,10):
	colorSet.append(getRandColor())


seqs = Pattern(200, 10, 4, colorSet, 
	{ 
		'symbol': {
			1: [Swap()]
		},
		'symbolSet': {
			4: [ChangeColorSet()] 
		}
	}).gen()
Player(root, window, canvas, gen, seqs).play(136)
