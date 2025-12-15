#step 3A; 
class Board:
    def __init__(self):
        #initalizes the board 
        self.grid = [[0]*9 for i in range(9)]

    def display(self):
        #to create the rows of numbers
        for row in self.grid:
            print(row)
            
    def is_valid(self, num, row, col):
        #check the row
        for i in range(9):
            if self.grid[row][i] == num:
                return False
        #check the column
        for j in range(9):
            if self.grid[j][col] == num:
                return False
        #check per 3x3 square
        top_left_row = row - (row%3)
        top_left_col = col - (col%3)
        for i in range(top_left_row,top_left_row + 3):
            for j in range(top_left_col,top_left_col + 3):
                if self.grid[i][j] == num:
                    return False 
        return True
    


