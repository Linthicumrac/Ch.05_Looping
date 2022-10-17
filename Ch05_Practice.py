# LOOPING!!!
'''
for i in range(5):
    print("I must not tell lies.")
print("done")
print()
for i in range(10):
    print(i)
# numbering systems always start with ZERO
print()
for i in range(10):
    print(i + 10)
print()
for i in range(1, 10):
    print(i)
# (inclusive, exclusive) --> 1 would be included/printed, but 10 won't be printed
for i in range(0,51):
    print(i * 2)
print() # or do the following code
for i in range(0,101,2):
    print(i)
for i in range(100,-1,-2):
    print(i)
for i in [2, 6, 8, "hi", 3, "person"]:
    print(i)
for i in "Hi person":
    print(i)
print()
for i in range(3):
    print("a")
    for j in range(3):
        print("b")
print("done")
total = 0
for i in range(1, 101):  # (inclusive, exclusive)
    total += i
print("The total is:", total)
a = 0
for i in range(10):
    a += 1
    for j in range(10):
        a += 1
print(a)
# learning while
for i in range(10):
    print(i)
print()
i = 1
while i <= 2**32:
    i *= 2
    print(i)
# start
done = False
perseverance = 0
while not done:
    quit = input("Do you want to quit? Y or N")
    if quit.lower() == "y":
        done = True
    else:
        perseverance += 1
print("Goodbye! your perseverance is", perseverance)  # end

for i in range(10):
    num = random.randrange(100, 201, 2)
    print(num)
print()
for i in range(10):
    num = random.randint(100, 201)  # (inclusive, inclusive, can't use a step)
    print(num)
for i in range(10):
    num = random.random()*5+10
    print(num)
import random
print()
done = False
while not done:
    winner = False
    guesses = 0
    secret_num = random.randint(1, 100)
    while not winner:
        guess = int(input("Guess a number between 1 and 100"))
        guesses += 1
        if guess > secret_num:
            print("Too High")
        elif guess<secret_num:
            print("too low")
        else:
            print("Correct. You found the secret number in ", guesses, "tries"
            )
            print()
            play_again = input ("do you want to play again? y/n")
            if play_again.lower() == "n":
                done = True
            winner = True
print("Thanks for playing")
for letter in "Death Star":
    if letter == " ":
        break
    print("Current letter:", letter)
# break stops the if command/ gets out of the loop, while loop, etc.
var = 10
while var > 0:
    print("Current variable value:", var)
    var -= 1
    if var == 5:
        break
for letter in "Death Star":
    if letter == " ":
        continue
# Continue:
    # starts the loop (the beginning)
    # returns to the top of the for loop
    # doesn't break out;
    print("Current letter:", letter)
var = 0
while var <= 10:
    var += 1
    if var % 2 != 0:  # if the answer is an even number, then break; if the answer is an odd number, don't do anything
        pass  # pass is like a placeholder for future code
    print("Current variable value:", var)
print("Goodbye!")
'''
