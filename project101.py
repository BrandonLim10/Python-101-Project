import random

game_list = ["ROCK", "PAPER", "SCISSORS"]

while True:
    cpu = random.choices(game_list)
    user_input = input("Enter Rock, Paper, Scissors or Enter Q to  Quit: ").upper()
    print("...")
    cpu = cpu[0]

    print("Computer Played: ", cpu)
    print("User Played: ", user_input)
    print("...")

    if user_input == "ROCK" and cpu == "SCISSORS":
        print("You Won!")
        print("...")
        continue
    elif user_input == "ROCK" and cpu == "PAPER":
        print("You Lost!")
        print("...")
        continue
    elif user_input == "SCISSORS" and cpu == "PAPER":
        print("You Won")
        print("...")
        continue
    elif user_input == "SCISSORS" and cpu == "ROCK":
        print("You Lost")
        print("...")
        continue
    elif user_input == "PAPER" and cpu == "ROCK":
        print("You Won")
        print("...")
        continue
    elif user_input == "PAPER" and cpu == "SCISSORS":
        print("You Lost")
        print("...")
        continue
    elif user_input == cpu:
        print("Tie!")
        print("...")
        continue
    elif user_input == "Q":
        print("...")
        break
    elif user_input != ("ROCK" and "PAPER" and "SCISSORS"):
        print ("Please enter ROCK or PAPER or SCISSORS, No other input is valid")
        continue


