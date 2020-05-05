from .Animal import Animal


class Turtle(Animal):

	def __init__(self, turtle=None, position=None, world=None):
		super(Turtle, self).__init__(turtle, position, world)

	def clone(self):
		return Turtle(self, None, None)

	def initParams(self):
		self.power = 6
		self.initiative = 2
		self.liveLength = 80
		self.powerToReproduce = 10
		self.sign = '@'
		self.release = False

	def getNeighboringPositions(self):
		return self.world.filterPositionsWithoutAnimals(self.world.getNeighboringPositions(self.position))
