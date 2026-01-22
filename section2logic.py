def main():
    age = int(input(" How old are you? ")) #asks user for their name
    if age < 18:
        print("You are a child")
    elif age >= 18:
        print ("You are an adult")

main()