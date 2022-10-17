# Sign your name:Rachel Linthicum
# import random
'''
 1. Make the following program work.
'''
total = 0
for i in range(3):
    x = int(input("Enter a number: "))
    total += x
print("The total is:", total)
print()
'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''
for i in range(1, 51):
    print(i * 2)
print()
'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''
i = 10
while 0 <= i <= 10:
    print(i)
    i -= 1
print("Blast Off!")
print()
'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''
import random
for i in range(1):
    num = random.randint(1, 10)
    print(num)
# can change the range # to a different number so that there are # numbers.
# Right now, with range(1), it'll only print 1 number (that is between 1 and 10)
'''
  5. Write a Python program that will:
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.   
'''
import random
for i in range(7):
    num = random.randint(1, 10)
    print(num)
print("End of code")
