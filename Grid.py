from Player import Player

class Grid:

    def __init__(self, columns, rows):
        self.__columns = columns
        self.__rows = rows
        self.__board = [[0 for x in range(columns)] for y in range(rows)]

    @property
    def columns(self):
        return self.__columns

    @property
    def rows(self):
        return self.__rows

    @property
    def board(self):
        return self.__board

    def show_board(self):
        # for(i, j) in enumerate(self.__board):
        #     print(j);

        for i in range(self.rows-1,-1,-1):
            print(self.board[i])

    def add_disc(self, column, player):
        lastLocation = [-1, -1];
        #find empty row in column
        for row in range(self.rows):
            if (self.__board[row][column] == 0):
                self.__board[row][column] = player.playerSignature
                lastLocation = [row, column];
                return lastLocation

        return lastLocation

    def has_player_won(self, player, lastLocation, winingScore):
        if lastLocation==[-1,-1]:
            return False
        return (self.did_player_win_diagonally(player, lastLocation, winingScore) or
                self.did_player_win_vertically(player, lastLocation, winingScore) or
                self.did_player_win_horizontally(player, lastLocation, winingScore))
    def did_player_win_diagonally(self, player, lastLocation, winingScore):
        lastRow = lastLocation[0]
        lastColumn = lastLocation[1]
        leftScoreCounter = 0
        rightScoreCounter = 0
        counter = 0
        for row in range(lastRow,-1, -1):
            leftColumn = lastColumn - counter
            if leftColumn >= 0:
                if self.board[row][leftColumn] == player.playerSignature:
                    leftScoreCounter = leftScoreCounter + 1
                else:
                    leftScoreCounter = 0

            rightColumn = lastColumn + counter
            if rightColumn < self.columns:
                if self.board[row][rightColumn] == player.playerSignature:
                    rightScoreCounter = rightScoreCounter + 1
                else:
                    rightScoreCounter = 0
            if leftScoreCounter == winingScore or rightScoreCounter == winingScore:
                return True;
            counter = counter + 1
        return False

    def did_player_win_vertically(self, player, lastLocation, winingScore):
        lastRow = lastLocation[0];
        lastColumn = lastLocation[1];
        scoreCounter = 0
        for row in range(lastRow, -1, -1):
            a=self.board[row][lastColumn]
            b=player.playerSignature
            if self.board[row][lastColumn] == player.playerSignature:
                scoreCounter = scoreCounter + 1;
            else:
                scoreCounter = 0;
            if scoreCounter == winingScore:
                return True;

        return False

    def did_player_win_horizontally(self, player, lastLocation, winingScore):
        lastRow = lastLocation[0];
        lastColumn = lastLocation[1];
        leftScoreCounter = 0
        rightScoreCounter = 0

        for i in range(lastColumn):
            leftColumn = lastColumn - i
            if leftColumn >= 0:
                if self.board[lastRow][leftColumn] == player.playerSignature:
                    leftScoreCounter = leftScoreCounter + 1
                else:
                    leftScoreCounter = 0

            rightColumn = lastColumn + i
            if rightColumn < self.columns:
                if self.board[lastRow][rightColumn] == player.playerSignature:
                    rightScoreCounter = rightScoreCounter + 1
                else:
                    rightScoreCounter = 0
            if leftScoreCounter == winingScore or rightScoreCounter == winingScore:
                return True;

        return False

if __name__ == "__main__":
    grid = Grid(3, 4)
    lastlocation= grid.add_disc(0,Player.RED)
    print(grid.show_board())
    print(f"Did player win {grid.has_player_won(Player.RED, lastlocation, 4)}")

    lastlocation=grid.add_disc(0, Player.RED)
    print(grid.show_board())
    print(f"Did player win {grid.has_player_won(Player.RED, lastlocation, 4)}")

    lastlocation=grid.add_disc(0, Player.RED)
    print(grid.show_board())
    print(f"Did player win {grid.has_player_won(Player.RED, lastlocation, 4)}")

    lastlocation=grid.add_disc(0, Player.RED)

    print(grid.show_board())
    print(f"Did player win {grid.has_player_won(Player.RED, lastlocation, 4)}")


