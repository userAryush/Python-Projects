# import random
# num = random.randint(1,20)
# print("WELCOME TO THE NUMBER GUESSING GAME")
# print("You have 5 chances to guess the number. START")

# for i in range(1,6):
#     user= int(input(f'Attempt {i} Enter a number:: '))
#     if user == num:
#         print("---------Congratulations the number matched!!!!!!!!!-----------")
#         break
#     elif user>=num+5:
#         print("--too high--")
#     elif user<=num-5:
#         print("--too low--")
#     elif user>num and user<num+5:
#         print("--little high--")
#     elif user<num and user>num-5:
#         print("--little low--")
# else:
#     print("You have run out of guesses")

          #2.	Suppose you are working on a program that simulates a game of dice where the player rolls two six-sided dice and tries to guess the total value. You have already implemented the logic to generate random dice rolls and compare them to the player's guess, but now you need to implement a loop to allow the player to play multiple rounds without having to restart the program each time.
        

# import random

# while True:
#     guess= int(input("Enter your guesss between 2 and 12: "))
#     if guess>=2 and guess<=12:
#         gsum = random.randint(1,7) + random.randint(1,7)
#         print("Dice rolls :: ", gsum)

#         if guess==gsum:
#             print("The guess matched you've won!!!!!!!!")

#         else:
#             print("Guess is incorrect.")
    
#     else:
#         print("Choose betweeen 2 to 12 only")
#     playagn=input("Do you want to continue?(y/n): ").lower()
#     if playagn=='y':
#         print("Let's play againn")
#     else:
#         print("Endingggg....")
#         break
    
    
# 3.	Write a Python program that uses a loop to repeatedly prompt the player to guess the total value of two dice, generate random dice rolls, compare the rolls to the guess, and display the result. The program should continue looping until the player chooses to quit the game. At the end of each round, the program should display the number of rounds played and the player's win percentage.

# import random
# round_count=0
# win=0
# while True:
#     guess= input("Enter your guesss between 2 and 12 and q to end: ")
#     if guess.isdigit():
#         guess= int(guess)
#         if guess>=2 and guess<=12:
#             gsum = random.randint(1,7) + random.randint(1,7)
#             print("Dice rolls :: ", gsum)

#             if guess==gsum:
#                 print("The guess matched you've won!!!!!!!!")
#                 win+=1
        

#             else:
#                 print("Guess is incorrect.")
#     elif guess=='q':
#             print("Ending.....")
#             break
#     else:
#         print("Guess whould be between 2 and 12")
#     round_count+=1
#     print("Number of round played: ",round_count)
#     win_per=(win/round_count)*100
#     print(f"Win percentage is {win_per}%")


import random
def play():
    print()
    players= int(input("Enter the number of players you want to play: "))
    player_score=[]

    for i in range(players):
        score=0
        print(f"\nPlayer {i+1} turn has just started!!!\n")
        print(f"Your initial score is {score}\n")
        
        while True:
            ask=input("Would you like to play(y/n):: ").lower()
            if ask == "y":            
                
                roll=random.randint(1,6)
                print(f"Dice rolls:: {roll}")
                score+=roll
                print(f"Your score is {score}")
                print()
            elif ask == "n":
                print()
                break
            else:
                print("Enter only y or n")
        player_score.append(score)
    return player_score

def winner(score):
    max=0
    for player in range(len(score)):
        if score[player]>max:
            max=score[player]
    return max,player

score=play()  
winscore,index=winner(score)
print(f"----------------The winner is player { index} with score {winscore}----------------")
    
        
    