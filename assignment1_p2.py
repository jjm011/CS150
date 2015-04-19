__author__ = 'jjm011@ucsd.edu,a5velasc@ucsd.edu'


def BFS(board):
    Q = [] 
    numCol = len(board[0])
    numRow = len(board)
    myBoard = [[int for i in range(len(board[0]))] for j in range (len(board))]
    visit =  [[bool for i in range(len(board[0]))] for j in range (len(board))]


    # find the empty tile position and create myBoard arrays
    for index,line in enumerate(board):
        for index2,num in enumerate(line):
           
            if board[index][index2] == 0:
                
                Q.append( (index,index2,'') )

            myBoard[index][index2] = board[index][index2]
            visit[index][index2] = False

    #current = Q.pop(0)
    #if (current[0] - 1) >= 0:
     # Q.append((current[0]-1, current[1], 'U') )
     # solution.append('U')

    #if (current[1] - 1) >= 0:
     # Q.append((current[0], current[1] - 1,'L'))
      #solution.append('L')

    #if (current[1] + 1) < numCol:
     # Q.append((current[0], current[1] + 1, 'R'))
     # solution.append('R')

    #if (current[0] + 1) < numRow:
     # Q.append((current[0] + 1, current[1], 'D'))
     # solution.append('D')

    #print Q
    #while(Q):
     #   current = Q.pop(0)
      #  current[3] = True

      #  break
    Search(Q,myBoard)

def Search(Q, myBoard):
    
    while (Q):
        current = Q.pop(0)
     
        Swap(current, 1, myBoard)
        
        break

def Swap(node, direction, myBoard):
    if(direction == 1):
       x = node[0] -1
       y= node[1]
      
       newState = (x,y)
       if Movable(newState, len(myBoard[0]), len(myBoard)):
         temp = myBoard[x][y]
         myBoard[x][y] = myBoard[node[0]][node[1]]
         myBoard[node[0]][node[1]] = temp

def Movable(direction,numCol,numRow):

    if (direction[0] >= numCol or direction[0] < 0 or direction[1] >= numRow
    or direction[1] < 0): return False

    else: return True

def is_complete(board):
    # your code here
    incr = 0
    for line in board:
        for num in line:
            
            if num != incr:
                return False
            else: incr += 1
    return True

def main():
    import sys
    board=[[int(n.strip()) for n in line.split(',')] for line in sys.stdin.readlines()]
    BFS(board)
    #print(is_complete(board))
    #print board

if __name__ == '__main__':
    main()

