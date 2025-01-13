from enum import Enum

class Disc(Enum):
    BLUE = ("Blue","B")
    GREEN = ("Green","G")

    def __init__(self,discColor,discColorSignature):
        self.__discColor = discColor
        self.__discColorSignature = discColorSignature

    @property
    def discColor(self):
        return self.__discColor

    @property
    def discColorSignature(self):
        return self.__discColorSignature



