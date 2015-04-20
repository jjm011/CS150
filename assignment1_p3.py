#Name: Junjie Ma, A10009633
#      Adam Velasco, A11761033
#Filename: assignment1_p3

__author__ = 'jjm011@ucsd.edu,a5velasc@ucsd.edu'
 
import copy
#max_depth for DFS
max_depth = 5
#Board class that represents the each unique board moves 
class Board(object):
  def __init__(self, board, row, col, move,depth):
    #member variables
    self.board = board
    self.col = col
    self.row = row
    self.move = move
    self.depth = depth
 
  def __eq__(self, other):
    return self.board == other.board
  #define a hash function for comparing the nodes
  def __hash__(self):
    return hash(str(self.board))

  #getter methods
  def getBoard(self):
    return self.board
  def getCol(self):
    return self.col
  def getRow(self):
    return self.row
  def getMove(self):
    return self.move
  def getDepth(self):
    return self.depth
 
#initialize the search by finding the initial zero tile pisition
def DFS(board):
    if(is_complete(board)): return "Solved"
    S = []
    numCol = len(board[0])
    numRow = len(board)
 
    visit = set()
    solution = ""
 
    # find the empty tile position and create visited array
    for index,line in enumerate(board):
        for index2,num in enumerate(line):
 
            if board[index][index2] == 0:
 
              initial = Board(copy.deepcopy(board), index, index2, copy.deepcopy(solution), 0)
              S.append(initial)
    #call the search
    return Search(S, visit)
 
#Uses DFS to search the board with UP, DOWN, LEFT, RIGHT direction
#Directions 1=UP, 2=DOWN, 3=LEFT, 4=RIGHT
def Search(S, visit):
  #if the Stack is not empty keep searching
  while (S):
    current = S.pop()

    #make sure the node is not in visited sit
    if current in visit:
      continue
 
    else:

      visit.add(current)
      #since stack has a reversed retrival order,
      #so reverse the inserting order

      #create a new state of the board with RIGHT move
      newb = Swap(current, 4)
      if(is_complete(newb.getBoard())):
        return newb.getMove()
      else:
        S.append(newb)
 
      #create a new state of the board with LEFT move
      newb = Swap(current, 3)
      if(is_complete(newb.getBoard())):
        return newb.getMove()
      else:
        S.append(newb)
 
      #create a new state of the board with DOWN move
      newb = Swap(current, 2)
      if(is_complete(newb.getBoard())):
        return newb.getMove()
      else:
        S.append(newb)
 
      #create a new state of the board with UP move
      newb = Swap(current, 1)
      if(is_complete(newb.getBoard())):
        return newb.getMove()
      else:
        S.append(newb)
  #All moves are made so unsolvable
  return "UNSOLVABLE"
 
#computes the swap with according direction
def Swap(myBoard, direction):
  #copy the board
  board = [row[:] for row in myBoard.getBoard()]
  
  #if the depth is under the max_depth(5)
  if(myBoard.getDepth() < max_depth):
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
    
    #if allowed to make the move
    if Movable(newState, len(board[0]), len(board)):
      #make the swap
      temp = board[row][col]
      board[row][col] = myBoard.getBoard()[myBoard.getRow()][myBoard.getCol()]
      board[myBoard.getRow()][myBoard.getCol()] = temp
      #create the board object according to its direction
      if(direction == 1):
        newb = Board(copy.deepcopy(board), row, col, copy.deepcopy(myBoard.getMove())+("U"), myBoard.getDepth()+1)
      
      elif(direction == 2):
        newb = Board(copy.deepcopy(board), row, col, copy.deepcopy(myBoard.getMove())+("D"), myBoard.getDepth()+1)
      
      elif(direction == 3):
        newb = Board(copy.deepcopy(board), row, col, copy.deepcopy(myBoard.getMove())+("L"), myBoard.getDepth()+1)
      
      elif(direction == 4):
        newb = Board(copy.deepcopy(board), row, col, copy.deepcopy(myBoard.getMove())+("R"), myBoard.getDepth()+1)
      
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
    print (DFS(board))
 
if __name__ == '__main__':
    main()

