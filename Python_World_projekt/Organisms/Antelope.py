from .Animal import Animal
from Position import Position
from Action import Action
from ActionEnum import ActionEnum

class Antelope(Animal):

	def __init__(self, antelope=None, position=None, world=None):
		super(Antelope, self).__init__(antelope, position, world)

	def clone(self):
		return Antelope(self, None, None)

	def initParams(self):
		self.power = 4
		self.initiative = 7
		self.liveLength = 12
		self.powerToReproduce = 8
		self.sign = 'A'

	def getNeighboringPositions(self):
			return self.world.filterPositionsWithOtherSpecies(self.world.getNeighboringPositions(self.position), Antelope)

	def consequences(self, atackingOrganism):
		result = []
		if self.power > atackingOrganism.power:
			result.append(Action(ActionEnum.A_REMOVE, Position(xPosition=-1, yPosition=-1), 0, atackingOrganism))
		else:
			result.append(Action(ActionEnum.A_REMOVE, Position(xPosition=-1, yPosition=-1), 0, self))
		return result