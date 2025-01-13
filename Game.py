from Grid import Grid
from Player  import Player


class Game:
    def __init__(self, player1, player2,grid,attemptGracePeriod=3,targetMatchingDisc=4):
        self.__player1 = player1
        self.__player2 = player2
        self.__grid = grid
        self.__attemptGracePeriod = attemptGracePeriod
        self.__targetMatchingDisc = targetMatchingDisc


    @property
    def player1(self):
        return self.__player1

    @property
    def player2(self):
        return self.__player2
    @property
    def grid(self):
        return self.__grid

    @property
    def attemptGracePeriod(self):
        return self.__attemptGracePeriod
    @property
    def targetMatchingDisc(self):
        return self.__targetMatchingDisc
    def play(self):
        self.grid.show_board()
        while True:
            player1Move= int(input("Player 1 move: "))
            counter=0;
            player1LastMoveLocation=[-1,-1];

            try:
                player1LastMoveLocation=self.grid.add_disc(player1Move, self.player1)
            except:
                while counter < self.attemptGracePeriod:
                    print("invalid move");
                    player1Move = int(input("Player 1 move: "))
                    try:
                        player1LastMoveLocation=self.grid.add_disc(player1Move, self.player1)
                        break
                    except:
                        counter += 1

            if self.grid.has_player_won(self.player1,player1LastMoveLocation,self.targetMatchingDisc):
                return "Player 1 won"

            player2Move = int(input("Player 2 move: "))
            counter = 0
            player2LastMoveLocation=[-1,-1]

            try:
                player2LastMoveLocation=self.grid.add_disc(player2Move, self.player2)
            except:
                while counter < self.attemptGracePeriod:
                    print("invalid move");
                    player2Move = int(input("Player 2 move: "))
                    try:
                        player2LastMoveLocation=self.grid.add_disc(player2Move,self.player2)
                        break
                    except:
                        counter += 1
            if self.grid.has_player_won(self.player2,player2LastMoveLocation,self.targetMatchingDisc):
                return "Player 2 won"




if __name__=="__main__":
    grid= Grid(4,4)
    game=Game(Player.RED,Player.YELLOW,grid)
    print(game.play())