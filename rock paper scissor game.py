import random

user_wins = 0
computer_wins = 0
draw=0

options = ["rock", "paper", "scissor"]

while True:
    user_turn = input("Type rock/paper/scissor or q to quit the game: ")
    if user_turn.lower() == "q":
        break


    elif user_turn.lower() in options:
            


        computer_turn_index = random.randint(0, 2)
        computer_turn = options[computer_turn_index]
        print("Computer's turn:", computer_turn)


        if (user_turn.lower() == "rock" and computer_turn == "scissor") or \
           (user_turn.lower() == "paper" and computer_turn == "rock") or \
           (user_turn.lower() == "scissor" and computer_turn == "paper"):
            print("You win")
            user_wins += 1
        elif user_turn.lower() == computer_turn:
            print("It's a tie")
            draw +=1
        else:
            print("Computer wins")
            computer_wins += 1

    
    else:
        print("Please enter the word correctly")

print(f"You win {user_wins} times")
print(f"Computer win {computer_wins} times")
print(f"draw {draw} times")
print("Thank you for playing")
