from enum import Enum

from Disc import Disc
class Player(Enum):
    RED=("R",Disc.BLUE)
    YELLOW=("Y",Disc.GREEN)

    def __init__(self,PlayerSignature,Disc):
        self.__PlayerSignature=PlayerSignature
        self.__Disc=Disc

    @property
    def disc(self):
        return self.__Disc

    @property
    def playerSignature(self):
        return self.__PlayerSignature
