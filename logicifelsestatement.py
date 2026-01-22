import random
secret_number = random.randint (1, 10)

number = int(input("Guess a number between 1 and 10: "))
if number == secret_number:
    print ("Well done, your guess is correct")
elif number > secret_number:
    print ("Your value is too high")
elif number < secret_number:
    print ("Your value is too low")
    
