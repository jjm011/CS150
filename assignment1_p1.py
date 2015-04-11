__author__ = 'jjm011@ucsd.edu,a5velasc@ucsd.edu'
def is_complete(board):
    # your code here
    return True
def main():
    import sys
board=[[int(n.strip()) for n in line.split(¡¯,¡¯)] for line in sys.stdin.readlines()]
print(is_complete(board))
if __name__ == '__main__':

main()

