import numpy as np
board = np.array([[7,8,0,4,0,0,1,2,0],
                  [6,0,0,0,7,5,0,0,9],
                  [0,0,0,6,0,1,0,7,8],
                  [0,0,7,0,4,0,2,6,0],
                  [0,0,1,0,5,0,9,3,0],
                  [9,0,4,0,6,0,0,0,5],
                  [0,7,0,3,0,0,0,1,2],
                  [1,2,0,0,0,7,4,0,0],
                  [0,4,9,2,0,6,0,0,7]])
test = np.array([[7,8,5,4,3,9,1,2,6],
                  [6,1,2,8,7,5,3,4,9],
                  [4,9,3,6,0,1,0,7,8],
                  [0,0,7,0,4,0,2,6,0],
                  [0,0,1,0,5,0,9,3,0],
                  [9,0,4,0,6,0,0,0,5],
                  [0,7,0,3,0,0,0,1,2],
                  [1,2,0,0,0,7,4,0,0],
                  [0,4,9,2,0,6,0,0,7]])                  

def print_board(bo):
    for i in range(len(bo)):
        if i %3 == 0 and i!= 0:
            print("- - - - - - - - - -")
        for j in range(len(bo[i])):
            if(j%3 == 0 and j!=0 and j!= 9):
                print("|", end = "")
            print(str(bo[i,j]) + " ",end = "")
            
        print("\n", end = "")
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[i])):
            if(bo[i,j]==0):
                return (i,j)
    return None
    
def is_valid(bo, num, pos):
    row = bo[pos[0],:]
    col = bo[:,pos[1]]
    x = pos[0]//3
    y = pos[1]//3
    box = bo[x*3:x*3+3,y*3:y*3+3]
    print(box)
    return len(row[row == num]) == 0 and len(col[col==num]) == 0 and len(box[box == num]) == 0
def solve(bo):
    find = find_empty(bo)
    if(find == None):
        print("hi")
        return True
    else:
        row, col = find
    for i in range(1,10):
        if is_valid(bo,i,find):
            bo[find] = i
            print(bo)
            if(solve(bo)):
                
                return True
            
            bo[row,col] = 0
    return False
solve(board)
print_board(board)