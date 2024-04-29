#The following code raises a TypeError:

tweet = 'Woohoo! :-)'

if len(tweet) > 140:
    print('Tweet is too long!')

length_of_tweet = len(tweet) + 5

#What does a TypeError indicate? 
#Try running the above code, then use the resulting error message to determine exactly what is wrong. (You don't have to fix this code.)

# type error indicates the type being used 
# the len function is given two arguments. a string and an integer. this function cannot accept integers or concatenate different value types
