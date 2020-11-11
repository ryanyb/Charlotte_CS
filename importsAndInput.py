# Similar to the print function, there's a ton of functions we can use (and even write!)
# Lots of people have written functions that we can use in our own code.
# People cluster functions, classes, datastructures, and similar things into Libraries.
# There's a ton of libraries supported by python, and python will innately recognize them.
# There's others that you need to install inedpendently if you want to use.


# Python includes a lot of math operations by default (+, -, /, *, etc)
# But what if we want to do like, I dunno, matrix multiplcation 
# It would be a PAIN to do all of that by hand.  Like, a huge fucking pain.
# Now, someone  had to do it, but they made the functions they wrote available to others

# So, if you want to use some of these library functions in your code, up at the top you write
# what's called an import statement to "import" these functions into your file.
# Once imported, they'll be treated like a normal python function you can call like any other.
# Let's import the 'math' library that has additional functions similar to those on a grpahing calculator
import math

# The library "math" is recognized by Python, so we don't need to donwload anything new to use it!
# It's not automatically included though every time we run a file becuase if we ran EVERY library,
# it would take FOREVER to get our code up and running.  
# Each aditional library we include means more things the computer needs to keep track of in memory
# so they're not included by default, but you shouldn't hesitate to include them when you need them.

# So now that we have math, we can use the functions included in math!
# for instance:

x = 1295712034
y = 9834912872
z = 31

greatestCommonDenominator = math.gcd(x, y)
z_factorial = math.factorial(z)
sinX = math.sin(x)
cosY = math.cos(y)
sinXDegrees = math.degrees(sinX)
cosYDegrees = math.degrees(cosY)

print("x = ", x)
print("y = ", y)
print("z = ", z)
print("---")
print("GCD(x,y): ", greatestCommonDenominator)
print("z!: ", z_factorial)  
print("Sin(x): ", sinX, " radians, or ", sinXDegrees, " degrees")
print("Cos(y): ", cosY, " radians, or ", cosYDegrees, " degrees")
print()

# Notice that we're putting "math." in front of everything.  
# That's because these functions are a member of the "math" library 
# We don't write stuff like python.print("sup") becuase print() is one of the 
# built in functions in python3. https://docs.python.org/3/library/functions.html


# NOTE: Uncomment the code below when you get here but I didn't want it to interupt running
#       stuff above

# Now changing gears slightly, we can ask the user for input through the command prompt:
# name = input("What is your name? ")
# quest = input("What is your quest? ")
# color = input("What is your favorite color? ")

# When you run the above, you can see that python prints whatever you pass into the input function
#  to the command line and then waits and stores whatever we put in into the variable
# print()
# print()

# print("Your name is ", name)
# print("Your quest is ", quest)
# print("Your favorite color is ", color)

# Now, this is kind of a fun trick, but does it work if want to do math with it?
num = input("Enter a number: ")
num2 = input("Enter a second number: ")

total = num + num2
print("First num + second num = ", total)