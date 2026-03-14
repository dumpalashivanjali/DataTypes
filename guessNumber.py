def guessing_game():
    secret_number = 33
    while True:
        num = int(input("Guess the number between 1 to 50:"))
        if num==secret_number:
            print("Correct Guess ! You won!")
            break
        elif num < secret_number:
            print("Too low")
        else:
            print("Too high")

guessing_game()


        

