class Grid:

    def __init__(self, column, rows):
        self.__column = column
        self.__rows = rows
        self.__board=[[0 for x in range(column)] for y in range(rows)]

    @property
    def columns(self):
        return self.columns

    @property
    def rows(self):
        return self.rows


    def show_board(self):
        # for(i, j) in enumerate(self.__board):
        #     print(j);

        for i in range(len(self.__board)):
                print(self.__board[i])


if __name__=="__main__":
    grid=Grid(3,4)
    print(grid.show_board())
