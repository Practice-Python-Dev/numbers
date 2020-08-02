#------------------------------
# LOOP THROUGH NUMBERS
#------------------------------

# ----- FOR LOOP -----
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Numbers in List:")
for i in num_list:
    if i < len(num_list):
        i = str(i) + ", "
        print(i, end="") # 'end' parameter stops defualt new line at the end of print (from python3)
    else:
        print(i)
print("\n" *1)

# ----- WHILE LOOP -----
iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print("Iteration", str(iteration), "- Count:", str(count))
    iteration +=1
print("\n" *1)

#------------------------------
# GUESS NUMBER PUZZLE: 
#------------------------------

# Import the random module - Provides access to functions (generate a random number, etc.)
import random

# Wrap it in a funciton for practice ...
def numberGuess():
    # Generate a random number ...
    random_number = random.randrange(1, 11) # Generate a random number
    # Initialize variable ...
    user_guess = 0
    # Ask user for guest in the loop ...
    while user_guess != random_number:
        user_guess = int(input("Guess a number between 1 and 10: "))
        if (user_guess > random_number):
            print("Wrong. You guessed too high...")
        if (user_guess < random_number):
            print("Wrong. You guessed too low...")
    print("You guessed", user_guess, "which is correct!")
    print("\n" *1)

# Call the function
numberGuess()

#------------------------------
# SAME PUZZLE - Using 'while True'
#------------------------------

# Keep using 'import random'
def numberGuess_v2():
    random_number_two = random.randrange(1, 101)
    pre_loop_guess = int(input("Guess a number between 1 and 100: "))
    while True:
        if (pre_loop_guess == random_number_two):
            print("Damn. You got it!")
            break
        if (pre_loop_guess > random_number_two):
            print("You guessed too high...")
            pre_loop_guess = int(input("Guess again: "))
        if (pre_loop_guess < random_number_two):
            print("You guessed too low...")
            pre_loop_guess = int(input("Guess again: "))

# Call the function
numberGuess_v2()


