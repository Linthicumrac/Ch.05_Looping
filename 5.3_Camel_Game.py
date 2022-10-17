import random
'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book
'''
print("HOW TO PLAY/ HOW TO NOT DIE!")
print("- You are on a camel running from natives.")
print("- You will have 6 choices to choose from which will have different responses.")
print("- How not to die: keep your canteen full (so you don't die of dehydration), let your camel rest, and stay away"
      " from the native americans!")
print("- If you decide you're done, then choose 'Q' and you'll leave the game")
print("- Also, there is a chance you could find a sanctuary/oasis that will be very helpful."
      " I doubt you can do find one, since they are very rare.")
done = False
milesTraveled = 0
thirst = 0
drinkAmount = 10
camelTiredness = 0
nativeDistance = -20
while not done:
    print()
    print("------------------------------------")
    print()
    print("A. Drink from your canteen.")
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
        print("Drinks in canteen:", drinkAmount)
        print("The natives are", nativeDistance, "miles behind you")
    elif choice.lower() == "d":
        camelTiredness = 0
        print("Your camel is Happy!!")
        nativeDistance = random.randint(7, 14)
        print("The natives are", nativeDistance, "miles behind you")
    elif choice.lower() == "c":
        milesTraveled = random.randint(10, 20)
        print("You traveled", milesTraveled, "miles")
        thirst += 1
        camelTiredness += random.randint(1, 3)
        nativeDistance += random.randint(7, 14)
    elif choice.lower() == "b":
        milesTraveled = random.randint(5, 12)
        print("You traveled", milesTraveled, "miles")
        thirst += 1
        camelTiredness += 1
        nativeDistance += random.randint(7, 14)
    elif choice.lower() == "a":
        if drinkAmount != 0:
            drinkAmount -= 1
            print("You can drink", drinkAmount, "more times.")
            print("Don't let it get down to 0")
        else:
            print("error")
        if 6 < drinkAmount < 4:
            print("You are thirsty")
        elif 6 > drinkAmount < 4:
            print("You died of thirst")
            done = True
    else:
        print("Not a choice")
        print("Pick A, B, C, D, E, or Q")
# how close to death (camel's death or your death (by thirst or native americans))
    if 8 > camelTiredness > 5:
        print("Your camel is getting tired")
    elif 8 < camelTiredness:
        print("Your camel is DEAD")
    elif nativeDistance == 0:
        print("The natives caught up. You've been caught and now you are dead.")
    elif -15 < nativeDistance < 0:
        print("The natives are getting close!")
    elif milesTraveled > 200:
        if camelTiredness > 8:
            print("You are dead")
        elif nativeDistance == 0:
            print("You are dead")
        elif 6 < drinkAmount > 4:
            print("You are dead")
# Chance to find an oasis
    oasisChance = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18",
                   "19", "20"]
    comChoice = random.choice(oasisChance)
    chance = random.choice(oasisChance)
    if comChoice == chance:
        print("You found an Oasis!!!")
        print("You're so lucky!!")
        thirst = 0
        drinkAmount = 10
        camelTiredness = 0
    else:
        pass
