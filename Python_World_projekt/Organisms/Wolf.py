from .Animal import Animal


class Wolf(Animal):

	def __init__(self, wolf=None, position=None, world=None):
		super(Wolf, self).__init__(wolf, position, world)

	def clone(self):
		return Wolf(self, None, None)

	def initParams(self):
		self.power = 8
		self.initiative = 5
		self.liveLength = 12
		self.powerToReproduce = 12
		self.powerIncreaseRate = 1
		self.agingRate = 1
		self.sign = 'W'

	def getNeighboringPositions(self):
		return self.world.filterPositionsWithOtherSpecies(self.world.getNeighboringPositions(self.position), Wolf)
