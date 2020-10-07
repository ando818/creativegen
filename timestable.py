from tkinter import *
from moldpieces import *
from window import Window
from colors import *
from generator import Generator
from pattern import *
from player import Player
from collections import defaultdict 
from shapes import *
from util import *

window = Window(2080, 2080)
starty=0

root = Tk()
canvas = Canvas(root, bg="#000099", width=window.width, height=window.height)

class Generator():
	def __init__(self):
		self.carves = defaultdict(list)
		self.objects = defaultdict(list)
		self.molds = defaultdict(list)
		self.shapes = []
		layer1 = self.genLayer(0, 400, 800, 150,  "#3b023b")
		layer2 = self.genLayer(40, 550, 800, 150, "black")
		road = Road(Point(0,300), 2080, 100)
		self.shapes.extend(layer1)
		self.shapes.extend(layer2)
		self.shapes.append(road)
	def genLayer(self,startX, startY, endY, hRange, color):
		startX = startX
		startY = startY
		endY = endY
		buildings = []
		for i in range(0,20):
			startOff = getRand(20, hRange)
			height = endY - (startY+startOff)
			building = Building(Point(startX,startY+startOff), height, 80, 80, color, "#990000", "#990000")
			buildings.append(building)
			startX += 100
		return buildings

	def getBuilding(self, n):
		return self.shapes[n]
	def getObjects():
		return self.objects
	def getInPane(self, wBox):
		shapes = []
		for shape in self.shapes:
			for mold in shape.molds:
				box = mold.getBox()
				if wBox.contains(box):
					shapes.append(wBox)
				
gen = Generator()
window.place(gen)

colorSet = []
for i in range(0,40):
	colorSet.append(getRandColor())

seqs = Pattern(200, 40, 4, colorSet, 
	{ 
		'symbol': {
			1: [Swap()]
		},
		'symbolSet': {
			4: [ChangeColorSet()] 
		}
	}).gen()

Player(root, window, canvas, seqs).play(0, 118)

