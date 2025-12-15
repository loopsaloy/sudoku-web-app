def Solve(board):
    for row in range(9):
        for col in range(9):
            if board.grid[row][col] == 0:
                for num in range(1,10,1):
                    if board.is_valid(num,row,col) == True:
                        board.grid[row][col] = num
                        if Solve(board) == True:
                            return True
                        else:
                            board.grid[row][col] = 0
           
                return False
    return True 
    

        
                        
                    
                    
                    
                        
                    
                
    
