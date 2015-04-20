#Name: Junjie Ma, A10009633
#      Adam Velasco, A11761033
#Filename: assignment1_p2

__author__ = 'jjm011@ucsd.edu,a5velasc@ucsd.edu'

import copy

#Board class that represents the each unique board moves 
class Board(object):
  #member variables
  def __init__(self, board, row, col, move):
    self.board = board
    self.col = col
    self.row = row
    self.move = move

  def __eq__(self, other):
    return self.board == other.board
  #create a hash function for comparing the nodes
  def __hash__(self):
    return hash(str(self.board))
  #getter functions
  def getBoard(self):
    return self.board
  def getCol(self):
    return self.col
  def getRow(self):
    return self.row
  def getMove(self):
    return self.move

#initialize the search by finding the initial zero tile pisition
def BFS(board):
    if(is_complete(board)): return "Solved"
    #using a list as Queue
    Q = []
    numCol = len(board[0])
    numRow = len(board)

    #visit =  [[bool for i in range(len(board[0]))] for j in range (len(board))]
    visit = set()
    solution = ""

    # find the empty tile position and create visited array
    for index,line in enumerate(board):
        for index2,num in enumerate(line):

            if board[index][index2] == 0:
              #create the intial board state and insert into the list
              initial = Board(copy.deepcopy(board), index, index2, copy.deepcopy(solution))
              Q.append(initial)

            #visit[index][index2] = False
    #call the search
    return Search(Q, visit)

#Uses BFS to search the board with UP, DOWN, LEFT, RIGHT direction
#Directions 1=UP, 2=DOWN, 3=LEFT, 4=RIGHT
def Search(Q, visit):
  #if the Queue is not empty keep searching
  while (Q):
    current = Q.pop(0)
    #make sure the node is not in visited sit
    if current in visit:
      continue

    else:
      visit.add(current)
      #create a new state of the board with UP move
      newb = Swap(current, 1)

      if(is_complete(newb.getBoard())):
        return newb.getMove()
      else:
        Q.append(newb)

      #create a new state of the board with DOWN move
      newb = Swap(current, 2)
      if(is_complete(newb.getBoard())):
        return newb.getMove()
      else:
        Q.append(newb)

      #create a new state of the board with LEFT move
      newb = Swap(current, 3)

      if(is_complete(newb.getBoard())):
        return newb.getMove()
      else:
        Q.append(newb)

      #create a new state of the board with RIGHT move
      newb = Swap(current, 4)
      if(is_complete(newb.getBoard())):
        return newb.getMove()
      else:
        Q.append(newb)

  #All moves are made so unsolvable
  return "UNSOLVABLE"

#computes the swap with according direction
def Swap(myBoard, direction):
  board = [row[:] for row in myBoard.getBoard()]
  #UP
  if(direction == 1):
    row = myBoard.getRow()-1
    col= myBoard.getCol()
  #DOWN 
  if(direction == 2):
    row = myBoard.getRow()+1
    col = myBoard.getCol()
  #LEFT
  if(direction == 3):
    row = myBoard.getRow()
    col = myBoard.getCol()-1
  #RIGHT
  if(direction == 4):
		row = myBoard.getRow()
		col= myBoard.getCol()+1
      
  newState = (row,col)
  
  #check if is allowed to move
  if Movable(newState, len(board[0]), len(board)):
    #make the swap
    temp = board[row][col]
    board[row][col] = myBoard.getBoard()[myBoard.getRow()][myBoard.getCol()]
    board[myBoard.getRow()][myBoard.getCol()] = temp
    
    #create each board object according to the direction
    if(direction == 1):
      newb = Board(copy.deepcopy(board), row, col, copy.deepcopy(myBoard.getMove())+("U"))
     
    elif(direction == 2):
      newb = Board(copy.deepcopy(board), row, col, copy.deepcopy(myBoard.getMove())+("D"))
      
    elif(direction == 3):
      newb = Board(copy.deepcopy(board), row, col, copy.deepcopy(myBoard.getMove())+("L"))
      
    elif(direction == 4):
      newb = Board(copy.deepcopy(board), row, col, copy.deepcopy(myBoard.getMove())+("R"))
     
    return newb

  return myBoard

#checks the next move is allowed or not
def Movable(direction,numCol,numRow):
	if (direction[1] >= numCol or direction[1] < 0 or direction[0] >= numRow
    or direction[0] < 0): return False

	else: return True

#checks whether the board has been solved
def is_complete(board):
    incr = 0
    #double loop that checks whether each tile is in order
    for line in board:
        for num in line:
            
            if num != incr:
                return False
            else: incr += 1
    return True
#main function that reads in the board from a txt file
def main():
    import sys
    board=[[int(n.strip()) for n in line.split(',')] for line in sys.stdin.readlines()]
    print (BFS(board))

if __name__ == '__main__':
    main()

