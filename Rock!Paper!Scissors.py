import random
player = input("rock, paper or scissors?")
computer = random.choice(["rock", "paper", "scissors"])
print(f"My choice is: {player}")
print(f"Opponent Choose: {computer}")
if player == computer:
    print(f"It's a tie. Both of you selected {player}")
elif player == "rock":
    if computer =="scissors":
        print("Rock smashes scissors.. I win!!")
    else:
        print("Opponent Win!! paper covers rock")
elif player == "paper":
    if computer == "rock":
        print("I win!!! paper covers rock")
    else:
        print("Opponent Win!! scissors cut paper")
elif player == "scissors":
    if computer == "paper":
        print("I Win!!! Scissors cut paper")
    else:
        print("Opponent Win.. Rock smashes scissors")
    
