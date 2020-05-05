from .Organism import Organism
from Action import Action
from ActionEnum import ActionEnum
from Position import Position
import random


class Animal(Organism):

	def __init__(self, animal=None, position=None, world=None):
		super(Animal, self).__init__(animal, position, world)
		self.__lastPosition = position
		self.__stomach = None

	@property
	def lastPosition(self):
		return self.__lastPosition

	@lastPosition.setter
	def lastPosition(self, value):
		self.__lastPosition = value

	@property
	def stomach(self):
		return self.__stomach

	@stomach.setter
	def stomach(self, value):
		self.__stomach = value

	def move(self):
		result = []
		pomPositions = self.getNeighboringPositions()
		newPosition = None

		if pomPositions:
			newPosition = random.choice(pomPositions)
			result.append(Action(ActionEnum.A_MOVE, newPosition, 0, self))
			self.lastPosition = self.position
			metOrganism = self.world.getOrganismFromPosition(newPosition)
			if metOrganism is not None:
				result.extend(metOrganism.consequences(self))
		return result

	def action(self):
		result = []
		newAnimal = None
		birthPositions = self.getNeighboringBirthPositions()

		if self.ifReproduce() and birthPositions:
			newAnimalPosition = random.choice(birthPositions)
			newAnimal = self.clone()
			newAnimal.initParams()
			newAnimal.position = newAnimalPosition
			self.power = self.power / 2
			result.append(Action(ActionEnum.A_ADD, newAnimalPosition, 0, newAnimal))
		return result

	def getNeighboringPositions(self):
		return self.world.getNeighboringPositions(self.position)

	def getNeighboringBirthPositions(self):
		return self.world.filterFreePositions(self.world.getNeighboringPositions(self.position))

	def consequences(self, atackingOrganism):
		result = []

		if self.power > atackingOrganism.power:
			result.append(Action(ActionEnum.A_REMOVE, Position(xPosition=-1, yPosition=-1), 0, atackingOrganism))
		else:
			if self.sign is "@":
				result.append(Action(ActionEnum.A_REMOVE, Position(xPosition=-1, yPosition=-1), 0, self))
				atackingOrganism.stomach = self
			elif self.sign is "U":
				atackingOrganism.position = atackingOrganism.lastPosition
			else:
				result.append(Action(ActionEnum.A_REMOVE, Position(xPosition=-1, yPosition=-1), 0, self))
		return result