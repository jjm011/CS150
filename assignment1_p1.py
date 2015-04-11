__author__ = 'jjm011@ucsd.edu,a5velasc@ucsd.edu'
def is_complete(board):
    # your code here
    incr = 0
    for line in board:
        for num in line:
            print num
            if num != incr:
                return False
            else: incr += 1
    return True

def main():
    import sys
    board=[[int(n.strip()) for n in line.split(',')] for line in sys.stdin.readlines()]
    print(is_complete(board))
    

if __name__ == '__main__':
    main()

