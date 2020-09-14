from tkinter import *
from moldpieces import *
from window import Window
from colors import *
from generator import Generator
from pattern import *
from player import Player
from collections import defaultdict 

window = Window(800, 800)
starty=0

root = Tk()
canvas = Canvas(root, width=window.width, height=window.height)

class Generator():
	def __init__(self):
		mL = MoldableLine(400, 45)
		mL2 = MoldableLine(400, -45)
		mL.end(mL2)
		mlPieces, pos = mL.weld()
		self.carves =defaultdict(list)
		for piece in mlPieces.pieces:
			print( piece.point.x)
			self.carves[Point(0,0)].append(Carve(Point(0, 0), piece))

gen = Generator()
window.place(gen)

canvas.pack()
window.draw(canvas)


'''
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

#Player(root, window, canvas, gen, seqs).play(136)

'''