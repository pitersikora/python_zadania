from .Animal import Animal


class Ufo(Animal):

  def __init__(self, ufo=None, position=None, world=None):
    super(Ufo, self).__init__(ufo, position, world)

  def clone(self):
    return Ufo(self, None, None)

  def initParams(self):
    self.power = 0
    self.initiative = 3
    self.liveLength = 10
    self.powerToReproduce = 1
    self.powerIncreaseRate = 0
    self.agingRate = 0
    self.sign = 'U'

  def getNeighboringPositions(self):
    return self.world.filterFreePositions(self.world.getNeighboringPositions(self.position))
