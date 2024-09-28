import random
playerscore=0
computerscore=0
listgame=['rock','paper','scissors']
while True:
    print("\nPlayer turn")
    player=input("Enter rock/paper/scissors or quit to end -> ").lower()
    if player == 'quit':
        
        break
    input("Enter for computer to play")
    computer=random.choice(listgame)
    print(f"Computer choose -> {computer}")
    
    if player == computer:
        print("Matched tied")
        print(f"Player Score::{playerscore} || Computer Score::{computerscore}")
    elif player == 'rock' and computer=='scissors':
        print("Player won\n")
        playerscore+=1
        print(f"Player Score::{playerscore} || Computer Score::{computerscore}")
    elif player == 'paper' and computer=='rock':
        print("Player won\n")
        playerscore+=1
        print(f"Player Score::{playerscore} || Computer Score::{computerscore}")
    elif player == 'scissors' and computer=='paper':
        print("Player won\n")
        playerscore+=1
        print(f"Player Score::{playerscore} || Computer Score::{computerscore}")
    elif player == 'rock' and computer=='paper':
        print("Computer won\n")
        computerscore+=1
        print(f"Player Score::{playerscore} || Computer Score::{computerscore}") 
    elif player == 'paper' and computer=='scissors':
        print("Computer won\n") 
        computerscore+=1 
        print(f"Player Score::{playerscore} || Computer Score::{computerscore}")
    elif player == 'scissors' and computer=='rock':
        print("Computer won\n") 
        computerscore+=1 
        print(f"Player Score::{playerscore} || Computer Score::{computerscore}")
    
    else:
        print("Enter only 'rock/paper/scissors' or 'quit' \n")
print()        
if playerscore>computerscore:
    print("You wonn!!")   
elif playerscore==computerscore:
    print("Match Tied")
else:
    print("Computer won!!")    
    