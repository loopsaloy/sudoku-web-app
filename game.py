import random
#4A: ask user their difficulty level and how many cells to remove
user_input = True
while user_input: 
    diff_level = input("Enter difficulty level: (E/M/H):")
    if diff_level.lower() == "e":
        cells_to_remove = 81 - 45
        user_input = False
    elif diff_level.lower() == "m":
        cells_to_remove = 81 - 35
        user_input = False
    elif diff_level.lower() == "h":
        cells_to_remove = 81 - 25
        user_input = False 
    else:
        user_input = True 
       
#4B: use previous backtracking solver
from board import Board
from solver import Solve
          
if __name__ == "__main__":
    b = Board()
    Solve(b)
    
#4C: randomly remove cells to generate the puzzle
def random_puzzle_generator(board):
    positions = []
    for row in range(9):
        for col in range(9):
            positions.append((row,col))
    return positions
positions = random_puzzle_generator(b)
random.shuffle(positions)
for row,col in positions[:cells_to_remove]:
    b.grid[row][col] = 0

b.display()

#4D: allowing the user to play and solve the game!

def play_game(board):
    mistake_counter = 0
    max_mistake = 3
    while mistake_counter < max_mistake and any(num == 0 for row in board.grid for num in row):
        while True:
            row = int(input("Enter row number from 1-9: "))-1
            if 0 <= row <= 8:
                break
            print("invalid row! Try again!")
            
        while True:
            col = int(input("Enter col number from 1-9: "))-1
            if 0 <= col <= 8:
                break
            print("invalid column! Try again!")
            
        while True: 
            num = int(input("Enter a number from 1-9: "))
            if 1 <= num <= 9:
                break
            print("invalid num! Try again!")
            

        if board.grid[row][col] == 0 and 1 <= num <= 9:
            if board.is_valid(num, row, col) == True:
                board.grid[row][col] = num 
                board.display()
                print(f"Mistakes: {mistake_counter}/{max_mistake}")
            else:
                mistake_counter += 1
                print(f"Mistakes: {mistake_counter}/{max_mistake}")
                print("Oops! you've made a wrong move!")
                board.display()
  
    if mistake_counter == max_mistake:
        print("Game Over!")
        
    else:
        print("Congratulations! You solved the puzzle!")
        board.display()
play_game(b)

        


        
    


