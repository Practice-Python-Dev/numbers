# DETERMINE PERFECT SQUARE IF NUMBER IS POSITIVE

# Initialize variables
answer = 0
flag = False

# Request an integer from the user
x = int(input('Enter an integer: '))

# GUESS AND CHECK:
  # 1) Switch flag to True if number is negative
  # 2) while: answer (0) squared is less than your input, keep incrementing by one
  # 3) if: answer squared == x, print success
  # 4) else: print failure msg, if: negative print failure msg
if x < 0:
    flag = True
while answer **2 < x:
    answer += 1
if answer **2 == x:
    print('Square root of ', x, ' is ', answer)
else:
    print(x, 'is not a perfect square')
    if flag:
        print(x, 'is negative. Try', -x, 'instead ...')