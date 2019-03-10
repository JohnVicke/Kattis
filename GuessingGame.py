import sys
import random

print("----- Program Information -----")
print(" The program will generate a nr")
print(" between 1 - 9. See if you can")
print("   guess the correct answer!")
print("    (type 'exit' to quit)" )
print("-------------------------------")

def game():
    guessNr = random.randint(1,9)
    running = 1
    while(running):
        nr = input("Guess a nr 1 - 9: ")
        if nr == "exit":
            sys.exit(0)
        else:
            if( int(nr) < guessNr):
                print("your guess was too low!")
            elif(int(nr) > guessNr):
                print("your guess was too high!")
            else:
                print("You guessed: " + nr + " which was the nr that was wanted!")
                hasChoosen = 1
                while(hasChoosen):
                    playAgain = input("Do you want to play again ? (yes/no)")
                    if(playAgain == "yes"):
                        guessNr = random.randint(1,9)
                        hasChoosen = 0
                    elif(playAgain == "no"):
                        print("okay thanks for playing!")
                        sys.exit(0)
                    else:
                        print("please enter yes or no :)")


game()
