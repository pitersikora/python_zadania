from abc import ABC, abstractmethod
from Position import Position
from Action import Action
from ActionEnum import ActionEnum


class Organism(ABC):

  def __init__(self, organism, position, world):
    self.__power = None
    self.__initiative = None
    self.__position = None
    self.__liveLength = None
    self.__powerToReproduce = None
    """
    new attributes:

    powerIncreaseRate - to differenciate power increase between
    Turtle (slow metabolism)
    Ufo (no power increase)
    and other organisms powerIncreaseRate has been added
    to give an opportunity to set this parameter without making "ifs"
    in world.makeTurn

    agingRate - to differenciate aging rate between
    Ufo (no aging)
    and other organisms
    and to help implement aging formula agingRate has been added
    also this variable reduces number of "ifs"
    in world.makeTurn

    """
    self.__powerIncreaseRate = None
    self.__agingRate = None
    self.__sign = None
    self.__world = None

    if organism is not None:
      self.__power = organism.power
      self.__initiative = organism.initiative
      self.__position = organism.position
      self.__liveLength = organism.liveLength
      self.__powerToReproduce = organism.powerToReproduce
      self.__powerIncreaseRate = organism.powerIncreaseRate
      self.__agingRate = organism.agingRate
      self.__sign = organism.sign
      self.__world = organism.__world
    else:
      if position is not None:
        self.__position = position
      if world is not None:
        self.__world = world
      self.initParams()


  @property
  def power(self):
    return self.__power

  @power.setter
  def power(self, value):
    self.__power = value

  @property
  def initiative(self):
    return self.__initiative

  @initiative.setter
  def initiative(self, value):
    self.__initiative = value

  @property
  def position(self):
    return self.__position

  @position.setter
  def position(self, value):
    self.__position = value

  @property
  def liveLength(self):
    return self.__liveLength

  @liveLength.setter
  def liveLength(self, value):
    self.__liveLength = value

  @property
  def powerToReproduce(self):
    return self.__powerToReproduce

  @powerToReproduce.setter
  def powerToReproduce(self, value):
    self.__powerToReproduce = value

  @property
  def powerIncreaseRate(self):
    return self.__powerIncreaseRate

  @powerIncreaseRate.setter
  def powerIncreaseRate(self, value):
    self.__powerIncreaseRate = value

  @property
  def agingRate(self):
    return self.__agingRate

  @agingRate.setter
  def agingRate(self, value):
    self.__agingRate = value

  @property
  def sign(self):
    return self.__sign

  @sign.setter
  def sign(self, value):
    self.__sign = value

  @property
  def world(self):
    return self.__world

  @world.setter
  def world(self, value):
    self.__world = value

  @abstractmethod
  def move(self):
    pass

  @abstractmethod
  def action(self):
    pass

  @abstractmethod
  def initParams(self):
    pass

  @abstractmethod
  def clone(self):
    pass

  def consequences(self, atackingOrganism):
    result = []

    if self.power > atackingOrganism.power:
      result.append(Action(ActionEnum.A_REMOVE, Position(xPosition=-1, yPosition=-1), 0, atackingOrganism, self))
    else:
      result.append(Action(ActionEnum.A_REMOVE, Position(xPosition=-1, yPosition=-1), 0, self, self))
    return result

  def ifReproduce(self):
    result = False

    if self.power >= self.powerToReproduce:
      result = True
    return result

  def __str__(self):
    return '{0}: power: {1} initiative: {2} liveLength {3} position: {4}'\
        .format(self.__class__.__name__, self.power, self.initiative, self.liveLength, self.position)
