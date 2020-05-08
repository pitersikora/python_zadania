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
    self.power = 6
    self.initiative = 7
    self.liveLength = 12
    self.powerToReproduce = 12
    self.powerIncreaseRate = 1
    self.agingRate = 0.75
    self.sign = 'A'


  def getNeighboringPositions(self):
    return self.world.filterPositionsWithoutAnimals(self.world.getNeighboringPositions(self.position))

# for antelope consequences are different because of dodge mechanics
  def consequences(self, atackingOrganism):
    result = []
    """
    if Wolf is attacking an Antelope, filter available position to dodge
    dodge positions are 2 fields away from the Antelope
    rest is the same as move action
    """
    if atackingOrganism.sign == 'W':
      """
      attacker position is taken to choose proper positions to dodge
      look into calculateDodgePath method
      """
      attacker = atackingOrganism.lastPosition
      newPosition = None
      # filter for dodge positions availability
      pomPositions = self.filterDodgePositions(attacker)
      # if there are positions to dodge then do it
      if pomPositions:
        newPosition = random.choice(pomPositions)
        result.append(Action(ActionEnum.A_DODGE, newPosition, 0, self, self))
        self.lastPosition = self.position
        metOrganism = self.world.getOrganismFromPosition(newPosition)
        if metOrganism is not None:
          result.extend(metOrganism.consequences(self))
      # if dodge positions are not free do the usual fighting
      else:
        if self.power > atackingOrganism.power:
          result.append(Action(ActionEnum.A_REMOVE, Position(xPosition=-1, yPosition=-1), 0, atackingOrganism, self))
        else:
          result.append(Action(ActionEnum.A_REMOVE, Position(xPosition=-1, yPosition=-1), 0, self, self))
    else:
      if self.power > atackingOrganism.power:
        result.append(Action(ActionEnum.A_REMOVE, Position(xPosition=-1, yPosition=-1), 0, atackingOrganism, self))
      else:
        result.append(Action(ActionEnum.A_REMOVE, Position(xPosition=-1, yPosition=-1), 0, self, self))
    return result

  def filterDodgePositions(self, attackerLastPosition):
    """
    Method for checking dodge fields availability
    Antelope can dodge into plant. It will eat it after dodging
    """
    result = []
    pomPositions = []
    pomPositions = self.calculateDodgePath(attackerLastPosition)
    for filed in pomPositions:
      posToCheck = []
      posToCheck.append(filed)
      if self.world.positionOnBoard(filed):
        # field with plant in it is valid for dodging
        if filed in self.world.filterPositionsWithoutAnimals(posToCheck):
          result.append(filed)
    return result

  def calculateDodgePath(self, attackPosition):
    positionsToDodge = []
    if attackPosition.x == self.position.x:
      """
      W is Wolf
      A is Antelope
      D are Dodge positions

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