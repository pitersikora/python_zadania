from ActionEnum import ActionEnum


class Action(object):

  def __init__(self, action, position, value, organism, attacker):
    self.__action = action
    self.__position = position
    self.__value = value
    self.__organism = organism
    self.__attacker = attacker

  @property
  def action(self):
    return self.__action

  @property
  def position(self):
    return self.__position

  @property
  def value(self):
    return self.__value

  @property
  def organism(self):
    return self.__organism

  @property
  def attacker(self):
    return self.__attacker

  def __str__(self):
    organismName = self.organism.__class__.__name__
    attackerName = self.attacker.__class__.__name__
    choice = {
      ActionEnum.A_ADD: '{0}: add at: {1}'.format(organismName, self.position),
      ActionEnum.A_INCREASEPOWER: '{0} increase power: {1}'.format(organismName, self.value),
      ActionEnum.A_MOVE: '{0} move from: {1} to: {2}'.format(organismName, self.organism.position, self.position),
      ActionEnum.A_REMOVE: '{0} remove from: {1}'.format(organismName, self.organism.position),
      ActionEnum.A_DODGE: '{0} dodged from: {1} to: {2}'.format(organismName, self.organism.position, self.position),
      ActionEnum.A_SWALLOW: '{0}: swallowed a turtle at: {1}'.format(attackerName, self.attacker.position)
    }
    return choice[self.action]
