import random
'''
CAMEL GAME 
---------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book
deer running away from hunters
'''
print("HOW TO PLAY/ HOW TO NOT DIE!")
print("- You are deer running from hunters.")
print("- You will have 6 choices to choose from which will have different responses.")
print("     - If A: You will stop to eat and drink. This will slow you down, but in turn, you won't die from lack of "
      "food and water")
print("     - If B: You should be able to get about 8 miles farther than the hunters.")
print("     - If C: You should be able to get about 15 miles farther than the hunters.")
print("     - If D: You get to rest!! - But don't forget about the hunters chasing you.")
print("     - If E: You'll be able to look at: how far teh hunter are from you, how many miles you've traveled, and"
      "the amount of times you've stopped to eat and drink.")
print("     - If Q: You'll leave the game. Neither winning nor losing, though I'd say losing as HOW DARE YOU QUIT THIS "
      "GAME!")
print("- How NOT to die: maintain your needs (don't get dehydrated nor hungry), rest, and stay away"
      " from the hunters!")
print("- Also, there is a chance you could find a sanctuary/oasis that will be very helpful."
      " I doubt you can do find one, since they are very rare.")
done = False
milesTraveled = 0
sustenance = 0
sustenanceAmount = 10
tiredness = 0
hunterDistance = -20
while not done:
    print()
    print("------------------------------------")
    print()
    print("A. Stop to eat and drink.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit")
    choice = str(input("     Choose which one you want to do."))
    print()
    if choice.lower() == "q":
        done = True
        print("Bye!")
    elif choice.lower() == "e":
        print("Miles traveled:", milesTraveled)
        print("Times you've stopped to eat and drink:", sustenanceAmount)
        print("The hunters are", hunterDistance, "miles behind you")
    elif choice.lower() == "d":
        tiredness = 0
        print("You are Happy!! - Especially since you're not dead... Yet")
        hunterDistance = random.randint(7, 14)
        print("The hunters are", hunterDistance, "miles behind you")
    elif choice.lower() == "c":
        milesTraveled = random.randint(10, 20)
        print("You traveled", milesTraveled, "miles")
        sustenance += 1
        tiredness += random.randint(1, 3)
        hunterDistance += random.randint(7, 14)
    elif choice.lower() == "b":
        milesTraveled = random.randint(5, 12)
        print("You traveled", milesTraveled, "miles")
        sustenance += 1
        tiredness += 1
        hunterDistance += random.randint(7, 14)
    elif choice.lower() == "a":
        if sustenanceAmount != 0:
            sustenanceAmount -= 1
            if sustenanceAmount == 1:
                print("You can eat & drink 1 more time.")
            elif sustenanceAmount != 1:
                print("You can eat & drink", sustenanceAmount, "more times.")
                print("Don't let it get down to 0")
        else:
            print("error")
        if 6 < sustenanceAmount < 4:
            print("You are hungry and thirsty")
        elif 6 > sustenanceAmount < 4:
            print("You died because you lost energy and were too thirsty to continue.")
            done = True
        else:
            pass
    else:
        print("Not a choice")
        print("Pick A, B, C, D, E, or Q")
# how close to death are you?
    if 8 > tiredness > 5:
        print("You are getting tired")
    elif 8 < tiredness:
        print("You are DEAD")
        done = True
    elif hunterDistance == 0:
        print("The hunters caught up. You've been caught and now you are someone else's dinner.")
        done = True
    elif -15 < hunterDistance < 0:
        print("The hunters are getting close!")
    elif milesTraveled > 200:
        if tiredness > 8:
            print("You are dead. Shot because you were too tired to carry on.")
            done = True
        elif hunterDistance == 0:
            print("You are dead. The hunters caught up to you and shot you.")
            done = True
        elif 6 < sustenanceAmount > 4:
            print("You are dead. You died because you lost energy and were too thirsty to continue.")
            done = True
# Chance to find an oasis
    oasisChance = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18",
                   "19", "20"]
    comChoice = random.choice(oasisChance)
    chance = random.choice(oasisChance)
    if comChoice == chance:
        print("You found an Oasis!!!")
        print("You're so lucky!!")
        thirst = 0
        hungerAmount = 10
        tiredness = 0
    else:
        pass
print("Better luck next time. Unless you pressed Q, then (like in my instructions) HOW DARE YOU QUIT THIS GAME")
