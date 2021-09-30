print("rock")
print("paper")
print("scissors")

player_one =  input("PLayer1 , make your move").lower()

import random
autobot = random.randint(0, 3)
if autobot == 0:
    computer = "rock"
elif autobot == 1:
    computer = "paper"
else:
    computer = "scissors"
print(f"Autobot Choosed : {computer}" )


if player_one == computer:
        print("you both have " +  player_one + "Play again")
elif player_one == "rock" and computer == "scissors":
        print("Player one wins")
elif player_one == "paper" and computer == "rock":
        print("Player one wins")
elif player_one == "scissors" and computer == "paper":
        print("player one wins ")
else:
    print("Computer wins")	

print("i'm trying to commit")
print("trying to add a new commit")		
				