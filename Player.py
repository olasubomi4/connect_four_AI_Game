from enum import Enum

from Disc import Disc
class Player(Enum):
    RED=("R",Disc.BLUE)
    YELLOW=("Y",Disc.GREEN)

    def __init__(self,PlayerSignature,Disc):
        self.__playerSignature=PlayerSignature
        self.__disc=Disc

    @property
    def disc(self):
        return self.__disc

    @property
    def playerSignature(self):
        return self.__playerSignature
