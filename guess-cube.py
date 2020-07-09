# GUESS AND CHECK CUBE ROOT OF A NUMBER (COUNT UP FROM 0)

# ---------- Initialize Variables ----------

# Ask what number the user wants cubed
cube = int(input("Input an integer to be cubed: "))
# Establish how close we need to get (smallest positive quantity)
epsilon = 0.01
# Each guess counts as 1.0 (float)
guess = 0.0
# Increment by this amount per guess
increment = 0.0001
# Store total guesses made
num_guesses = 0

while abs(guess**3 - cube) >= epsilon:
    guess += increment
    num_guesses += 1
print('num guesses =', num_guesses)
if abs(guess**3 - cube) >= epsilon:
    print('Failed on cube root of', cube)
else:
    print(guess, 'is close to the cube root of', cube)