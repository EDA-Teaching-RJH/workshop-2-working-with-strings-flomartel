import math

def main():
    A = int(input("Input a value for side A: ")) #asks user for A value
    B = int(input("Input a value for side B: ")) #asks user for B value
    C = pythag(A,B) #this is C value

    print("The hypotenuse is", C) #prints C value


def pythag(A,B):
    return math.sqrt(A**2 + B**2) #calculates C value


main()
