from enum import Enum


class ActionEnum(Enum):
  A_MOVE = 0
  A_REMOVE = 1
  A_ADD = 2
  A_INCREASEPOWER = 3
  # enum for new actions: dodge, swallow
  A_DODGE = 4
  A_SWALLOW = 5