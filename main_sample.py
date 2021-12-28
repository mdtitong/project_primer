'''
Project: Guess the Number Game
'''
import logging
import random
import math

logging.basicConfig(filename='test.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)-8s %(message)s')
# starting range input
lower = int(input("Enter Lower bound: "))
# ending range input
upper = int(input("Enter Upper bound: "))
# generating random number between
# the lower and upper
x = random.randint(lower, upper)
print("\n\tYou've only ", round(math.log(upper - lower + 1, 2)),
      " chances to guess the number!\n")
# Initializing the number of guesses.
COUNT = 0
# for calculation of minimum number of
# guesses depends upon range
while COUNT < math.log(upper - lower + 1, 2):
    COUNT += 1

    # taking guessing number as input
    guess = int(input("Guess a number: "))

    # Condition testing
    if x == guess:
        print(f"Congratulations! You did it in {COUNT} try")
        logging.info("count: %d", COUNT)
        logging.info("number is %d", guess)
        # Once guessed, loop will break
        break
    if x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")
# If Guessing is more than required guesses,
# shows this output.
if COUNT >= math.log(upper - lower + 1, 2):
    print(f"\nThe number is {x}")
    print("\tBetter Luck Next time!")
