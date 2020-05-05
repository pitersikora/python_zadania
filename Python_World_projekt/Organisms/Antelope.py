from .Animal import Animal
from Position import Position
from Action import Action
from ActionEnum import ActionEnum
import random

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
		return self.world.filterPositionsWithoutAnimals(self.world.getNeighboringPositions(self.position))

	def consequences(self, atackingOrganism):
		result = []
		if atackingOrganism.sign == 'W':
			attacker = atackingOrganism.lastPosition
			newPosition = None
			pomPositions = self.filterDodgePositions(attacker)
			if pomPositions:
				newPosition = random.choice(pomPositions)
				result.append(Action(ActionEnum.A_DODGE, newPosition, 0, self))
				self.lastPosition = self.position
				metOrganism = self.world.getOrganismFromPosition(newPosition)
				if metOrganism is not None:
					result.extend(metOrganism.consequences(self))
			else:
				if self.power > atackingOrganism.power:
					result.append(Action(ActionEnum.A_REMOVE, Position(xPosition=-1, yPosition=-1), 0, atackingOrganism))
				else:
					result.append(Action(ActionEnum.A_REMOVE, Position(xPosition=-1, yPosition=-1), 0, self))
		else:
			if self.power > atackingOrganism.power:
				result.append(Action(ActionEnum.A_REMOVE, Position(xPosition=-1, yPosition=-1), 0, atackingOrganism))
			else:
				result.append(Action(ActionEnum.A_REMOVE, Position(xPosition=-1, yPosition=-1), 0, self))
		return result

	def filterDodgePositions(self, attackerLastPosition):
		result = []
		pomPositions = []
		pomPositions = self.calculateDodgePath(attackerLastPosition)
		for filed in pomPositions:
			posToCheck = []
			posToCheck.append(filed)
			if self.world.positionOnBoard(filed):
				if filed in self.world.filterPositionsWithoutAnimals(posToCheck):
					result.append(filed)
		return result

	def calculateDodgePath(self, attackPosition):
		positionsToDodge = []
		if attackPosition.x == self.position.x:
			"""
			wolf attacking
			  |1|2|3|4|5|
			|1|D   D   D
			|2|
			|3|    A
			|4|    W

			OR

			wolf attacking
			  |1|2|3|4|5|
			|1|    W
			|2|    A
			|3|
			|4|D   D   D
			"""
			positionsToDodge.append(Position(xPosition=self.position.x - (attackPosition.y-self.position.y)*2, yPosition=self.position.y-(attackPosition.y-self.position.y)*2))
			positionsToDodge.append(Position(xPosition=self.position.x, yPosition=self.position.y-(attackPosition.y-self.position.y)*2))
			positionsToDodge.append(Position(xPosition=self.position.x + (attackPosition.y-self.position.y)*2, yPosition=self.position.y-(attackPosition.y-self.position.y)*2))
		elif attackPosition.y == self.position.y:
			"""
			wolf attacking
			  |1|2|3|4|5|
			|1|      D
			|2|
			|3|W A   D
			|4|
			|5|      D

			OR

			wolf attacking
			  |1|2|3|4|5|
			|1|  D
			|2|
			|3|  D   A W
			|4|
			|5|  D
			"""
			positionsToDodge.append(Position(xPosition=self.position.x - (attackPosition.x-self.position.x)*2, yPosition=self.position.y - (attackPosition.x-self.position.x)*2))
			positionsToDodge.append(Position(xPosition=self.position.x - (attackPosition.x-self.position.x)*2, yPosition=self.position.y))
			positionsToDodge.append(Position(xPosition=self.position.x - (attackPosition.x-self.position.x)*2, yPosition=self.position.y + (attackPosition.x-self.position.x)*2))
		else:
			"""
			wolf attacking
			  |1|2|3|4|5|
			|1|    D   D
			|2|
			|3|    A   D
			|4|  W
			|5|

			ETC.
			"""
			positionsToDodge.append(Position(xPosition=self.position.x + (self.position.x-attackPosition.x)*2, yPosition=self.position.y))
			positionsToDodge.append(Position(xPosition=self.position.x + (self.position.x-attackPosition.x)*2, yPosition=self.position.y + (self.position.y-attackPosition.y)*2))
			positionsToDodge.append(Position(xPosition=self.position.x, yPosition=self.position.y + (self.position.y-attackPosition.y)*2))
		return positionsToDodge