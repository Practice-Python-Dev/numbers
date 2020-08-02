#------------------------------
# GET THE CUBE ROOT OF A NUMBER
#------------------------------

# ----- USER INPUT -----

# Ask the user for a number to cube
cube = int(input("Input an integer to be cubed: "))

# ----- SET VARIABLES -----

# Establish how close we need to get - (the smallest positive quantity)
epsilon = 0.01

# Set the amount to increment by (per guess)
increment = 0.0001

# Each guess counts as 1.0 (float)
guess = 0.0

# Variable to store total guesses
total_guesses = 0

# ----- NOW CALCULATE! -----

while abs(guess**3 - cube) >= epsilon:
    guess += increment
    total_guesses += 1
print("Computer Guesses =", total_guesses)
if abs(guess**3 - cube) >= epsilon:
    print("Failed on cube root of", cube)
else:
    print(guess, "is close to the cube root of", cube)

# Note, the abs() function returns the absolute value of a number
