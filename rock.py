import random

action = ['rock','paper','sessor']
while  True :
    User=input("Enter your choice [rock, paper, sessor] : ")

    computer_choice=random.choice(action)
 
    print(f"your choice id {User}, computer choice is {computer_choice}")

    if User == computer_choice:
        print("Its tie")
    elif User == "rock":
        if computer_choice == "sessor":
            print("You win! because Rock smashes scissors.")
        else:
            print("You lose :( Paper covers rock!")
    elif User == "paper":
        if computer_choice == "rock":
            print("You win! because Paper covers rock.")
        else:
            print("You lose :( Scissors cuts paper!")
    elif User == "sessor":
        if computer_choice == "paper":
            print("You win! because Scissors cuts paper.")
        else:
            print("You lose :( Rock smashes scissors!")
    play_again = input('Play again? (y/n)')
    if (play_again.lower() == 'n'):
        break