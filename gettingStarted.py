

# This is a python file!  Woo!  It'll introduce printing and variable declaration.
# If you open it in a text editor like VS Code it should look nifty and like
#   well, a bunch of text.

# As you can see, all of this stuff is written without the computer doing anything about it
# These are things called comments.  

#T here's a few ways to leave comments in python3:
#Y ou can start a line with a # as I've done above

''' Or alternatively
If you want to do comments for multiple lines at a time like this
you can begin and end the block of text you want to comment
with tripple ticks as I did here.  ''' 

#--------------

# Unlike in lots of other programming languages, you can kinda just... start coding without
#   needing to wrap it in anything special.

print()

print("Sup bby")

print()
print("---------------")
print()

# We can also define variables without needing to be super precise about it:
x = 5
y = "bruh"
z = 5.12423
t = True
myList = [1, 2.123, 'a', y]

# We can print a bunch of things: 
print(x, y, z, t, myList)
print()

# But maybe we want a a bit of formatting:
print ("x: ", x, "\ny: ", y, "\nz: ", z, "\nt: ", t, "\nmyList: ", myList)
print()

# But that line of code hurts my eyes, we can make it look less ugly and more intuitive:
print(
    "x: ", x,
    "\ny: ", y,
    "\nz: ", z,
    "\nt: ", t,
    "\nmyList: ", myList
    )

print()
print("---------------")
print()

# We can also do things within our print statement:
print(x + z)
print(not(t))


print()
print("---------------")
print()

# We can also pass some arguments into our print statement to dictate how it works.
# We can write end='' to tell it not to make a new line:
print("hey ", end='')
print("bby")

print()
print("---------------")
print()

# Finally, we can redefine our variables and python won't complain, which is pretty cool!
print(x)
x = "pineapple"
print(x)