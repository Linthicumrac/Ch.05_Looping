'''
ROSHAMBO PROGRAM
----------------
Create a program that randomly chooses a 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.(1 for rock, 2 for paper, 3 for scissors and 4 for quit)
I don't want to be asked to quit each time. I will enter a 4 if I want to quit.
Add conditional statements to figure out who wins and keep the records
Each round tell me what the computer chose, what I chose and also if I won, lost or tied.
When the user quits print an end game message and their win/loss/tie record
'''
import random
quitGame = True
win = 0
lose = 0
tie = 0
print("** If you ever want to stop playing, type in '4' to quit the game")
while quitGame:
    print("       ---------------------------")
    yourChoice = input("   Enter a choice ==> 1 for rock, 2 for paper, or 3 for scissors): ")
    threeChoices = ["1", "2", "3"]
    comChoice = random.choice(threeChoices)
    if comChoice == "1":
        comChoice = "rock"
    elif comChoice == "2":
        comChoice = "paper"
    elif comChoice == "4":
        quitGame = False
    else:
        comChoice = "scissors"
    print()
    if yourChoice == "1":
        yourChoice = "rock"
    elif yourChoice == "2":
        yourChoice = "paper"
    elif yourChoice == "4":
        quitGame = False
    else:
        yourChoice = "scissors"
    print("     - You chose", yourChoice, "and the computer chose", comChoice)
    print()
    if yourChoice == comChoice:
        print("     - Both players selected {yourChoice}. It's a tie!")
        tie += 1
    elif yourChoice == "rock":
        if comChoice == "scissors":
            print("     - Rock smashes scissors! You win!")
            win += 1
        else:
            print("     - Paper covers rock! You lose.")
            lose += 1
    elif yourChoice == "paper":
        if comChoice == "rock":
            print("     - Paper covers rock! You win!")
            win += 1
        else:
            print("     - Scissors cuts paper! You lose.")
            lose += 1
    elif yourChoice == "scissors":
        if comChoice == "paper":
            print("     - Scissors cuts paper! You win!")
            win += 1
        else:
            print("     - Rock smashes scissors! You lose.")
            lose += 1
    elif comChoice == "4":
        quitGame = True
    else:
        pass
print("       ---------------------------")
print("       ---------------------------")
print("Congrats you finally chose to quit playing")
print("  - Results")
print("    - You won", win, "time!")
print("    - You lost", lose, "time!")
print("    - You tied", tie, "time!")
