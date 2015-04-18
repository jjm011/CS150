__author__ = 'jjm011@ucsd.edu,a5velasc@ucsd.edu'

import copy

class Board(object):
	def __init__(self, board, row, col, move):
		self.board = board
		self.col = col
		self.row = row
		self.move = move
		self.solved = False
		#for j in range(len(board)):
		#	for i in range(len(board[0])):
		#		self.board[i][j] = board[i][j]
	def __eq__(self, next):
		return self.board == next
		
	def getBoard(self):
		return self.board
	def getCol(self):
		return self.col;
	def getRow(self):
		return self.row;
	def getMove(self):
		return self.move;
	def setSolved(self):
		self.solved = True
	def isSolved(self):
		return self.solved
		
def BFS(board):
    if(is_complete(board)): return "Solved"
    Q = [] 
    numCol = len(board[0])
    numRow = len(board)
    #myBoard = [[int for i in range(len(board[0]))] for j in range (len(board))]
    #print "FIRST",myBoard
    visit =  [[bool for i in range(len(board[0]))] for j in range (len(board))]
    solution = ""

    # find the empty tile position and create myBoard arrays
    for index,line in enumerate(board):
        for index2,num in enumerate(line):
           
            if board[index][index2] == 0:
				initial = Board(copy.deepcopy(board), index, index2, copy.deepcopy(solution))
				Q.append(initial)

            #myBoard[index][index2] = board[index][index2]
            #print "FIRST",index
            #print "SECOND",index2
            #print ""
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
    return Search(Q, visit)
	
def Search(Q, visit):
    
	while (Q):
		current = Q.pop(0)
		if visit[current.getRow()][current.getCol()]:
			#print "Visited."
			continue
		else:
			#print "X", current.getRow()
			#print "Y", current.getCol()
			visit[current.getRow()][current.getCol()] = True
			newb = Swap(current, 1)
			if(newb != current):
				#print "BOARD",newb.getBoard()
				if(is_complete(newb.getBoard())):
					current.setSolved()
					return newb.getMove()
				else:
					Q.append(newb)
			newb = Swap(current, 2)
			if(newb != current):
				#print "BOARD",newb.getBoard()
				if(is_complete(newb.getBoard())):
					current.setSolved()
					return newb.getMove()
				else:
					Q.append(newb)
			newb = Swap(current, 3)
			if(newb != current):
				#print "BOARD",newb.getBoard()
				if(is_complete(newb.getBoard())):
					current.setSolved()
					return newb.getMove()
				else:
					Q.append(newb)
			newb = Swap(current, 4)
			if(newb != current):
				#print "BOARD",newb.getBoard()
				if(is_complete(newb.getBoard())):
					current.setSolved()
					return newb.getMove()
				else:
					Q.append(newb)
	return "Unsolvable"

def Swap(myBoard, direction):
	board = [row[:] for row in myBoard.getBoard()]
	#print "MYBOARD",myBoard.getBoard()
	#print "NEWBOARD",board
	if(direction == 1):
		row = myBoard.getRow()-1
		#print "ROW",row
		col= myBoard.getCol()
		#print "COL",col
	if(direction == 2):
		row = myBoard.getRow()+1
		#print "ROW",row
		col = myBoard.getCol()
		#print "COL",col
	if(direction == 3):
		row = myBoard.getRow()
		#print "ROW",row
		col = myBoard.getCol()-1
		#print "COL",col
	if(direction == 4):
		row = myBoard.getRow()
		#print "ROW",row
		col= myBoard.getCol()+1
		#print "COL",col
      
	newState = (row,col)
	#print newState
	#print board
	if Movable(newState, len(board[0]), len(board)):
		#print "LENBOARD0",len(board[0])
		#print "LENBOARD",len(board)
		#print x
		#print y
		temp = board[row][col]
		board[row][col] = myBoard.getBoard()[myBoard.getRow()][myBoard.getCol()]
		board[myBoard.getRow()][myBoard.getCol()] = temp
		if(direction == 1):
			#print "U"
			newb = Board(copy.deepcopy(board), row, col, copy.deepcopy(myBoard.getMove())+("U"))
		elif(direction == 2):
			#print "D"
			newb = Board(copy.deepcopy(board), row, col, copy.deepcopy(myBoard.getMove())+("D"))
		elif(direction == 3):
			#print "L"
			newb = Board(copy.deepcopy(board), row, col, copy.deepcopy(myBoard.getMove())+("L"))
		elif(direction == 4):
			#print "R"
			newb = Board(copy.deepcopy(board), row, col, copy.deepcopy(myBoard.getMove())+("R"))
		#print direction
		#print newb.getMove()
		return newb
	return myBoard

def Movable(direction,numCol,numRow):
	if (direction[1] >= numCol or direction[1] < 0 or direction[0] >= numRow
    or direction[0] < 0): return False

	else: return True

def is_complete(board):
    # your code here
    incr = 0
    for line in board:
        for num in line:
            
            if num != incr:
                #print "False"
                return False
            else: incr += 1
    #print "True"
    return True

def main():
    import sys
    board=[[int(n.strip()) for n in line.split(',')] for line in sys.stdin.readlines()]
    print (BFS(board))
    #print(is_complete(board))
    #print board

if __name__ == '__main__':
    main()

