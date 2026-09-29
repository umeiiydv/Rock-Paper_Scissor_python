# Rock paper Scissor Game Project
import random
moves = ["rock","scissor","paper"]
"""
rock v/s paper = paper wins
rock v/s scissor = rock wins
paper v/s scissor = scissor wins

"""

while True:
    comp_score = 0
    user_score = 0
    user_choice = int(input(''' 
Game start....
1 Yes
2 No | Exit

'''))
    if user_choice ==1 :
        for a in range(1,6):
            userMoves = int(input('''  
1 Rock
2 Scissor
3 Paper
            '''))
            if userMoves ==1:
                uchoice = "rock"
            elif userMoves ==2:
                uchoice = "scissor"
            elif userMoves == 3:
                uchoice = "paper"
            comp_choice = random.choice(moves)
            if comp_choice ==uchoice:
               print("Computer Value",comp_choice)
               print("User Value",uchoice)
               print("Game Draw")
               user_score = user_score +1
               comp_score = comp_score +1
            elif (uchoice == "rock" and comp_choice == "scissor") or (uchoice == "paper" and comp_choice == "rock") or (uchoice== "scissor" and comp_choice == "paper"):
                print("Computer Value",comp_choice)
                print("User Value", uchoice)
                print("You Win")
                user_score = user_score + 1
            else:
                print("Computer Value",comp_choice)
                print("User Value", uchoice)
                print("Computer Win")
                comp_score = comp_score + 1
        if user_score == comp_score:
            print("Final Game series draw...")
            print("User Score",user_score)
            print("Computer Score",comp_score)
        elif user_score> comp_score:
            print("Final You Win the Game series...")
            print("User Score",user_score)
            print("Computer Score", comp_score)
        else:
            print("Computer Win the Game series")
            print("User Score",user_score)
            print("Computer Score",comp_score)

    
    else:
        break
    