from flask import Flask, render_template, request
from board import Board
from solver import Solve 
import random
import copy 

app = Flask(__name__)
    
@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/play")
def play():
    difficulty = request.args.get('difficulty', 'easy')
    if difficulty == 'easy':
        cells_to_remove = 36
    elif difficulty == 'medium':
        cells_to_remove = 45
    elif difficulty == 'hard':
        cells_to_remove = 54
    else:
        cells_to_remove = 36  # default to easy if invalid difficulty
    b = Board()
    Solve(b)
    solved_board = copy.deepcopy(b.grid)

    positions = [(row, col) for row in range(9) for col in range(9)]
    random.shuffle(positions)
    
    for row,col in positions[:cells_to_remove]:
        b.grid[row][col] = 0
        
    return render_template("puzzle.html", board=b.grid, solution=solved_board)


if __name__ == "__main__":
    app.run(debug=True)

