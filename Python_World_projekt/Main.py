from World import World
from Position import Position
from Organisms.Grass import Grass
from Organisms.Sheep import Sheep
from Organisms.Dandelion import Dandelion
from Organisms.Wolf import Wolf
from Organisms.Toadstool import Toadstool
from Organisms.Antelope import Antelope
from Organisms.Turtle import Turtle
from Organisms.Ufo import Ufo
import os


if __name__ == '__main__':
  pyWorld = World(8, 8, 1)

  newOrg = Grass(position=Position(xPosition=4, yPosition=0), world=pyWorld)
  pyWorld.addOrganism(newOrg)

  newOrg = Wolf(position=Position(xPosition=3, yPosition=2), world=pyWorld)
  pyWorld.addOrganism(newOrg)

  newOrg = Toadstool(position=Position(xPosition=4, yPosition=1), world=pyWorld)
  pyWorld.addOrganism(newOrg)

  newOrg = Turtle(position=Position(xPosition=7, yPosition=3), world=pyWorld)
  pyWorld.addOrganism(newOrg)

  newOrg = Dandelion(position=Position(xPosition=7, yPosition=7), world=pyWorld)
  pyWorld.addOrganism(newOrg)

  newOrg = Antelope(position=Position(xPosition=4, yPosition=4), world=pyWorld)
  pyWorld.addOrganism(newOrg)

  newOrg = Ufo(position=Position(xPosition=6, yPosition=2), world=pyWorld)
  pyWorld.addOrganism(newOrg)

  newOrg = Sheep(position=Position(xPosition=2, yPosition=5), world=pyWorld)
  pyWorld.addOrganism(newOrg)

  print(pyWorld)

  for _ in range(0, 100):
    pyWorld.makeTurn()
    os.system('clear')
    print(pyWorld)
