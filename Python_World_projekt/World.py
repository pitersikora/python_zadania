from Position import Position
from Organisms.Plant import Plant
from Organisms.Animal import Animal
from Action import Action
from ActionEnum import ActionEnum
from Organisms.Grass import Grass
from Organisms.Sheep import Sheep
from Organisms.Dandelion import Dandelion
from Organisms.Wolf import Wolf
from Organisms.Toadstool import Toadstool
from Organisms.Antelope import Antelope
from Organisms.Turtle import Turtle
from Organisms.Ufo import Ufo
import random


class World(object):

  def __init__(self, worldX, worldY, wellfarePenalty):
    self.__worldX = worldX
    self.__worldY = worldY
    """
    new attribute:

    wellfarePenalty - attribute which is a world parameter
    it is used in formula for increasing agingRate when
    there is many representants of one organism
    (e.g. formula is preventing from making too much Grass and Dandelion)
    the bigger wellfarePenalty value, more penalty is given
    """
    self.__wellfarePenalty = wellfarePenalty
    self.__turn = 0
    self.__organisms = []
    self.__newOrganisms = []
    """
    new "data containers":

    stopTime - list of positions where animals don't take any actions
    stopTime is filled with positions around Ufo
    if organism position is equal to any of the position from
    stopTime list, then this organism skips turn

    organismsAmmount - dict where each organism sign is key
    and value is ammount of this type of organism
    these values are used for agingRate calculation
    due to some implementations used in PythonWorld
    we have to count organisms each turn
    """
    self.__stopTime = []
    self.__organismsAmmount = {}
    self.__separator = ' '

  @property
  def worldX(self):
    return self.__worldX

  @property
  def worldY(self):
    return self.__worldY

  @property
  def wellfarePenalty(self):
    return self.__wellfarePenalty

  @property
  def turn(self):
    return self.__turn

  @turn.setter
  def turn(self, value):
    self.__turn = value

  @property
  def organisms(self):
    return self.__organisms

  @organisms.setter
  def organisms(self, value):
    self.__organisms = value

  @property
  def stopTime(self):
    return self.__stopTime

  @stopTime.setter
  def stopTime(self, value):
    self.__stopTime = value

  @property
  def newOrganisms(self):
    return self.__newOrganisms

  @newOrganisms.setter
  def newOrganisms(self, value):
    self.__newOrganisms = value

  @property
  def organismsAmmount(self):
    return self.__organismsAmmount

  @organismsAmmount.setter
  def organismsAmmount(self, value):
    self.__organismsAmmount = value

  @property
  def separator(self):
    return self.__separator

  def makeTurn(self):
    actions = []
    # loop for getting stopTime positions from every Ufo's surroundings
    for species in self.organisms:
      if isinstance(species, Ufo):
        self.stopTime.extend(self.getNeighboringPositions(species.position))
    for org in self.organisms:
      # if organism position is in stopTime list then don't make actions
      if self.positionOnBoard(org.position) and org.position not in self.stopTime:
        actions = org.move()
        for a in actions:
          self.makeMove(a)
        actions = []
        if self.positionOnBoard(org.position):
          actions = org.action()
          for a in actions:
            self.makeMove(a)
          actions = []

    self.organisms = [o for o in self.organisms if self.positionOnBoard(o.position)]
    for o in self.organisms:
      """
      if organism position is in stopTime list then
      don't reduce liveLength
      don't increase power
      """
      if o.position not in self.stopTime:
        # use aging formula to calculate how much liveLength has to be reduced
        o.liveLength -= self.calculateAging(o)
        # e.g. Ufo's powerIncreaseRate is 0 so Ufo doesn't get stronger
        o.power += o.powerIncreaseRate
        # if organism is animal and has something in stomach
        if isinstance(self.getOrganismFromPosition(o.position), Animal) and o.stomach is not None:
          # if turtle was swallowed earlier then release it from stomach
          if o.stomach.release is True:
            # filter for positions without animals around the animal who swallowed the turtle and choose random
            releasePosition = random.choice(self.filterPositionsWithoutAnimals(self.getNeighboringPositions(o.position)))
            """
            if there is any valid position to release the turtle then:
            change turtle position to releasePosition
            "close stomach" so next turtle swallowed won't be released at the same turn
            add turtle to newOrganisms list
            delete the remaining copy of turtle in stomach
            """
            if releasePosition:
              o.stomach.position = releasePosition
              o.stomach.release = False
              self.newOrganisms.append(o.stomach)
              o.stomach = None
          # if turtle is swallowed this turn switch stomach.release value to release turtle next turn
          else:
           o.stomach.release = True
        if o.liveLength < 1:
          print(str(o.__class__.__name__) + ': died of old age at: ' + str(o.position))
    self.organisms = [o for o in self.organisms if o.liveLength > 0]
    self.organismsAmmount = {}
    self.newOrganisms = [o for o in self.newOrganisms if self.positionOnBoard(o.position)]
    self.organisms.extend(self.newOrganisms)
    self.organisms.sort(key=lambda o: o.initiative, reverse=True)
    for creature in self.organisms:
    # go through organisms, count them and put results into organismsAmmount dict
      self.countOrganisms(creature)
    self.newOrganisms = []
    self.stopTime = []

    self.turn += 1

  def makeMove(self, action):
    print(action)
    # new actions added: dodge and swallow
    if action.action == ActionEnum.A_ADD:
      self.newOrganisms.append(action.organism)
    elif action.action == ActionEnum.A_INCREASEPOWER:
      action.organism.power += action.value
    elif action.action == ActionEnum.A_MOVE:
      action.organism.position = action.position
    elif action.action == ActionEnum.A_REMOVE:
      action.organism.position = Position(xPosition=-1, yPosition=-1)
    elif action.action == ActionEnum.A_DODGE:
      action.organism.position = action.position
    elif action.action == ActionEnum.A_SWALLOW:
      action.organism.position = Position(xPosition=-1, yPosition=-1)

  def addOrganism(self, newOrganism):
    newOrgPosition = Position(xPosition=newOrganism.position.x, yPosition=newOrganism.position.y)

    if self.positionOnBoard(newOrgPosition):
      self.organisms.append(newOrganism)
      # if/else for counting animals at turn 0
      if newOrganism.sign not in self.organismsAmmount:
        self.organismsAmmount[newOrganism.sign] = 1
      else:
        self.organismsAmmount[newOrganism.sign] += 1
      self.organisms.sort(key=lambda org: org.initiative, reverse=True)
      return True
    return False

  def positionOnBoard(self, position):
    return position.x >= 0 and position.y >= 0 and position.x < self.worldX and position.y < self.worldY

  # method for counting animals and puting results into organismsAmmount dict
  def countOrganisms(self, organism):
    if organism.sign not in self.organismsAmmount:
      self.organismsAmmount[organism.sign] = 1
    else:
      self.organismsAmmount[organism.sign] += 1

  """
  method for calulate aging:
  wellfarePenalty and organismsAmmount[organism.sign] are directly proportional to formula result
  """
  def calculateAging(self, organism):
    return organism.agingRate * (organism.agingRate + ((self.wellfarePenalty*self.organismsAmmount[organism.sign])*0.036))

  def getOrganismFromPosition(self, position):
    pomOrganism = None

    for org in self.organisms:
      if org.position == position:
        pomOrganism = org
        break
    if pomOrganism is None:
      for org in self.newOrganisms:
        if org.position == position:
          pomOrganism = org
          break
    return pomOrganism

  def getNeighboringPositions(self, position):
    result = []
    pomPosition = None

    for y in range(-1, 2):
      for x in range(-1, 2):
        pomPosition = Position(xPosition=position.x + x, yPosition=position.y + y)
        if self.positionOnBoard(pomPosition) and not (y == 0 and x == 0):
          result.append(pomPosition)
    return result

  def filterFreePositions(self, fields):
    result = []

    for field in fields:
      if self.getOrganismFromPosition(field) is None:
        result.append(field)
    return result

  def filterPositionsWithoutAnimals(self, fields):
    result = []
    pomOrg = None

    for filed in fields:
      pomOrg = self.getOrganismFromPosition(filed)
      if pomOrg is None or isinstance(pomOrg, Plant):
        result.append(filed)
    return result

  def filterPositionsWithOtherSpecies(self, fields, species):
    result = []
    for filed in fields:
      pomOrg = self.getOrganismFromPosition(filed)
      if not isinstance(pomOrg, species):
        result.append(filed)
    return result

  def manuallyAddOrganism(self):
    option = input('\nDo you want to add new organism? (type y to add)\n')
    if option == 'y':
      # get names of all organisms from subclasses Animal nad Plant to show them to user
      creatures = [cls.__name__ for cls in Animal.__subclasses__()]+[cls.__name__ for cls in Plant.__subclasses__()]
      creatureOption = ''
      # while user input doesn't match any of the organisms names ask user to pick organisms to add
      while creatureOption not in creatures:
        creatureOption = input("Choose one of the creatures to add: {}\n".format(creatures))
      positions = []
      # add every position in the world to positions list
      for x in range(0,self.worldX):
        for y in range(0, self.worldY):
          positions.append(Position(xPosition=x, yPosition=y))
      # filter positions if they are free
      positions = self.filterFreePositions(positions)
      # guard variable for printing postitions with same "x" value in same line
      printCounter = positions[0].x
      # print enumeration and free position "x" and "y" so user can choose position by its number
      for index, pos in enumerate(positions):
        if printCounter == pos.x:
          print('{0}. {1}'.format(index, pos), end='\t')
        # if position has new "x" set new guard variable and print it in new line
        else:
          printCounter = pos.x
          print('\n{0}. {1}'.format(index, pos), end='\t')
      posOption = -1
      # try/catch for user input validation
      while posOption not in range(0, len(positions)):
        try:
          posOption = int(input("\nChoose the number of position where to add the organism:\n"))
        except ValueError:
          print('\nPlease use digits only !!!')
      """
      globals() builtin is used to take creatureOption and position indexed with posOption:
      create instance of the same class as creatureOption string
      put new organism in the same position as position[posOption]
      """
      newOrg = globals()[creatureOption](
          position=Position(
            xPosition=positions[posOption].x,
            yPosition=positions[posOption].y
                           ),
          world=self
          )
      # prevent added organism from moving the same turn
      self.stopTime.append(newOrg.position)
      self.addOrganism(newOrg)


  def __str__(self):
    result = '\nturn: ' + str(self.__turn) + '\n'
    for wY in range(0, self.worldY):
      for wX in range(0, self.worldX):
        org = self.getOrganismFromPosition(Position(xPosition=wX, yPosition=wY))
        if org:
          result += str(org.sign)
        else:
          result += self.separator
      result += '\n'
    return result