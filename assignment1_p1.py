__author__ = 'jjm011@ucsd.edu,a5velasc@ucsd.edu'

#checks whether the board has been solved
def is_complete(board):
    
    incr = 0
    #double for loop that checks each cell
    for line in board:
        for num in line:
            if num != incr:
            #if one cell is out of order return false
                return False
            else: incr += 1
    return True

def main():
    import sys
    board=[[int(n.strip()) for n in line.split(',')] for line in sys.stdin.readlines()]
    print(is_complete(board))
    

if __name__ == '__main__':
    main()

