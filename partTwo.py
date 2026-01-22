import math

def main():
    A = int(input(" Input a value for A: "))
    B = int(input(" Input a value for B: "))
    C = pythag(A,B)

def pythag(A,B):
    print( math.sqrt(A**2 + B**2))


main()
