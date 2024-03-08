# import random module
import random


# Function to play game
def start_game():
    # Print games rules and instructions
    print(" This is Javatpoint's Rock-Paper-Scissors! ")
    print(" Please Enter your choice: ")
    print(" choice 1: Rock ")
    print(" choice 2: Paper ")
    print(" choice 3: Scissors ")


# To take the user input
    choice_user = int(input(" Select any options from 1 - 3 : "))

    # randint() Function which generates a random number by computer
    choice_machine = random.randint(1, 3)

    # display the machines choice
    print(" Option choosed by Machine is: ", end=" ")
    if choice_machine == 1:
        print(" Rock ")
    elif choice_machine == 2:
        print("Paper")
    else:
        print("Scissors")

        # To declare who the winner is
    if choice_user == choice_machine:
        print(" Wow It's a tie! ")
    elif choice_user == 1 and choice_machine == 3:
        print(" Congratulations!! You won! ")
    elif choice_user == 2 and choice_machine == 1:
        print(" Congratulations!! You won! ")
    elif choice_user == 3 and choice_machine == 2:
        print(" Congratulations!! You won! ")
    else:
        print(" Sorry! The Machine Won the Game? ")

        # If user wants to play again
    play_again = input(" Want to Play again? ( yes / no ) ").lower()
    if play_again == " yes":
        start_game()
    else:
        print(" Thanks for playing Rock-Paper-Scissors! ")

# Begin the game
start_game()