#Determine what the following code snippet prints. First solve it in your head or on paper, then run it in your Python environment to check the result.

speed = 0
acceleration = 24
braking_force = 19
is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
print(is_moving)

# braking_force=19 < acceleration=24 and (speed=0 > 0 or acceleration=19 > 0)
# True


#Bonus question: Do we need the parentheses in the boolean expression or could we have written the following?:

is_moving = braking_force < acceleration and speed > 0 or acceleration > 0
print(is_moving)

# without the parentheses it would be True and False or True resulting in False or True still returning True in this particular case
# this wouldn't work with edge cases, the parentheses are therefore necessary for accuracy