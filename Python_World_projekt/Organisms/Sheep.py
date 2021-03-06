from .Animal import Animal


class Sheep(Animal):

  def __init__(self, sheep=None, position=None, world=None):
    super(Sheep, self).__init__(sheep, position, world)

  def clone(self):
    return Sheep(self, None, None)

  def initParams(self):
    self.power = 6
    self.initiative = 4
    self.liveLength = 10
    self.powerToReproduce = 11
    self.powerIncreaseRate = 1
    self.agingRate = 0.88
    self.sign = 'S'

  def getNeighboringPositions(self):
    return self.world.filterPositionsWithoutAnimals(self.world.getNeighboringPositions(self.position))
