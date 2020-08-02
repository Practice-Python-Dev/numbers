#------------------------------
# GET THE CUBE ROOT OF A NUMBER
#------------------------------

# ----- USER INPUT -----

# Ask the user for a number to cube
user_cube = int(input("Input an integer to be cubed: "))

# ----- SET VARIABLES -----

# Establish how close we need to get - (the smallest positive quantity)
epsilon = 0.01

# Set the amount to increment by (per guess)
increment = 0.0001

# Each guess counts as 1.0 (float)
comp_guess = 0.0

# Variable to store total guesses
total_guesses = 0

# ----- NOW CALCULATE! -----

# 1) while: absolute value of (comp_guess **3 >= user_cube):
# 2) if: 
# 3) else:

while abs(comp_guess**3 - user_cube) >= epsilon:
    comp_guess += increment
    total_guesses += 1
print("Computer Guesses =", total_guesses)
if abs(comp_guess**3 - user_cube) >= epsilon:
    print("Failed on cube root of", user_cube)
else:
    print(comp_guess, "is close to the cube root of", user_cube)
