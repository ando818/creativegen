from tkinter import *
from moldpieces import *
from window import Window
from colors import *
from generator import Generator
from pattern import *
from player import Player
from collections import defaultdict 
from shapes import *
window = Window(800, 800)
starty=0

root = Tk()
canvas = Canvas(root, width=window.width, height=window.height)

class Generator():
	def __init__(self):
		self.carves = defaultdict(list)
		self.objects = defaultdict(list)
		startX = 0
		for i in range(0,5):
			newBuilding = Building(150, 80)
			self.objects[Point(0, startX)].append(newBuilding)

	def getObjects():
		return self.objects

gen = Generator()
window.place(gen)
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