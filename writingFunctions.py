

# We're gona do functions so that this shit is organized and not lots of commented in / out code
# I realize we also never formally touched loops.  We should do that.  Probably should've done that first but whatever.

# See  below, a function declaration:
def firstFunction():
    # Woo, we did it.  Notice that we're indented now 'cause we're within the function.  
    # Remember how whennever you did loops or functions or whatever in java you needed brackets like { } to start and end the contents?
    # Yea python just uses colons becuase it reads more like English or something idk. 
    # Because we don't denote the end of the function with a bracket or something like that, python uses indention to keep track of where you are.
    # So this is inside the function

# This is not, and once you leave the function you can't go back in
# So let's say I worte a line of code here

    # So even if I write code here, it won't be a part of my function since I've left the function.
    # Makes sense, ya?  Python is very visual while trying to reduce syntactical clutter. 
    # Also VSCode is really good about helping you track your indentations with the vertical lines to the right of the line numbers over on the left
    # It's convention to put comments on the same indentation level as your function/loop/whatever so that shit doesn't get wacky.
    # Some people put all their comments before their functions but yea it's all just stylistic at that point.

    # Anyway, python style things apart, the above line of code is something we should mention
    # You put 'def' if you want to define a function.  Self explanatory there.
    # And then the name of the function follows.  Functions may take an input to the function (think about the print function)
    # So whenever you write one, even if it doesn't take any input, you still need to put the parenthesis to denote as such.
    pass 
    # It's good convention to use the word 'pass' when you want your code to skip over something.  So rather than just leaving this empty,
    # I'm putting 'pass' in it cause it just... I dunno looks weird if there's nothing in here. Also it may crash when you try to run if funcs are empty

def add(num1, num2):
    # Something you may have noticed that's different from Java is that I don't have to denote return type OR parameter type.
    # In java, it may look like: public int realFirstFunction(int num1, int num2){ }
    # But we don't have to do that here.
    # This is probably a good time to also mention that in Java everyting has to be in a class, which we'll get to later
    # But in python it doesn't.  You can just write code and it runs without explicitly being in a class.
    # If that doesn't mean anything meaningful to you, ignore it.  But worth mentinioning if you remembered that stuff.

    output = float(num1) + float(num2)
    return output

# Woo we have a basic addition / subtraction funciton for two numbers.
# Notice that I included a typecast of the function's parameters into ints.
# We don't have to do that as long as we always pass in integers, but let's say that we want to get keybaord input via the input() function.
# We could either immediately typecast it and then pass it into the function or typecast it here.  Both works.
# A downside of not needing to specify input types and return types are that you can accidentally pass around data that's of the wrong type.

# Python does not allow for forced parameter / return typing, but you can annotate expected input/output like follows (but it won't enforce the datatype)
def typedAdd(num1: float, num2: float) -> float:
    output = num1 + num2
    return output


# ANYWAY, now that we have some (really just one) function, we can use it just like we use print() and GCD() and Sin() from the last file.
print(add(5, 4))
print(add(5, -4))
print(add(5.124, 2))
print("--")

# Note that python's default print formatting for floats is to include a ".0" after the 1's digit to indicate that we're using a float.


# For Loop - Designate an amount of times some code will run, and then run it that number of times (roughly).
def forLoops():

    # For loops are really... interesting in python.  They're really really nice, but personally I like Java's more maybe because I learned Java's first.
    # So in Java you do something like: for (int i = 0; i < 10; i++) { [do some code]}
    # And the above code will create an integer i, (i here stands for iterator)
    # and as long as i is less than 10 at the start of the loop, it will run. 
    # and whenever it finishes the loop it will add 1 to i. (i++ means i = i + 1 in java)
    
    # Python, like usual, is a lot less verbose, which is good and bad:
    for i in range(5):
        print(i)
    
    # Fist off, no parenthesis needed around the arguments in your for loop like in Java.
    # Secondly, there's this range(int) function.  I'll explain exactly what it does later, but for now it means your loop will run int times.
    # Thirdly, if you run the above code, you'll see it print 0, 1, 2, 3, 4.  Like most things CS'y, range(int) zero-indexes.  
    # You can also call range with more than 1 argument:
    # range(stop) takes one argument.
    # range(start, stop) takes two arguments.
    # range(start, stop, step) takes three arguments.

    # So for instance, the below prints the numbers from 1-10, the ending number ends BEFORE the number, so it's [start, stop) using math set notation
    for i in range(1, 11):
        print(i)

    # And the below prints the numbers 1, 3, 5, 7, 9:
    for i in range(1, 11, 2):
        print(i)
    

    # Now the REALLY COOL thing about python for loops is that you can iterate over a bunch of shit with them like lists, strings, and more.
    # So, the below will print s p a g h e t t i if you run it.  Cool.
    for i in "spaghetti":
        print(i, end=" ")

    # So where in Java your iterator is always an integer, here your for loop is actually iterating over a list, every time!
    # Even in the case where we use range().  All range(5) does is return the list [0, 1, 2, 3, 4]
    # So the following two for loops are the same:
    for i in [0, 1, 2, 3, 4]:
        print(i)
    
    for i in range(5):
        print (i)
    
    # It's really annoying though to make lists by hand, especially if our for loops are, I dunno, a few thousand long... or more...
    # So range is there to make our lives easier.
    # ALSO JUST TO CLARIFY:  your iterator doesn't have to be i.  It can be anything.  So for the spaghetti one, it would be convention to say something like:
        #for char in "spaghetti":
    # So, to recap the important bit here: our "iterator" is not just a number like it would be in Java.  It's ACTUALLY whatever item in your list is next.
    # So let's say that you've got a bunch of information about I dunno genes stored in a list
    # And each item in your list is the genome of a particular animal.
    # Then you could maybe (I dunno how anything about genes works) have something like this:
    # for genome in listOfGenomes:
        # print("Genome ID: ", genome.getID())
        # cut = splice(genome.getSequence(), locationA, locationB)
        # printDNA(cut)
    # where calling getID on a genome returns it's ID that it's associated with
    # where calling splice cuts a dna sequence (gotten from the genome via the getSequence() function) at locationA and locationB
    # and then prints the cut in a fancy graphic way using the printDNA(cut) funciton.

    # I'm not going to write out an equivalent function in Java, but it's more dense
    # Notably, since you'd have your itartor i which is an integer and not a genome, you may do something like the following for the first line of code there:
        # print("Genome ID: ", listOfGenomes[i].getID()") where listOfGenomes[i] is the genome at the i'th index in the listOfGenomes.  

    # So python doesn't let you do anything new per-se with for loops, but it just looks a lot cleaner
    # Also becuase python is loose with variable types, you don't run into errors if your list has different types:

    listOfShit = ["apple", 4, -9.123, True, ["Ooh look at me I'm a list in a list!", "Very Spooky"]]
    for item in listOfShit:
        print(item, end=" ")
    
    # The above prints apple 4 -9.123 True ["Ooh look at me I'm a list in a list!", "Very Spooky"] 
    
    # I think that's enough on for loops. 
        

# If Loop(?) - Execute code once if a (or many) condition(s) is/are met.  Idk if this is a loop but it fits about here so :shrug:
def ifLoop():

    #Super basic:
    # if [condition]:
        # [execute thing]
    
    number = 4
    if number == 4:
        print("Wow it's 4")


    # Note the double equals sign above:
    # The single equals sign is reserved for assignment.  And we're not trying to re-assign the value of the number variable in our if loop.
    # Double-equals is like asking "is equal to?" rather than asserting "is equal to"
    # The single vs double equals sign in if statments is something that your error-checker and compiler will catch and tell you is wrong
    # Which is great becuase they're really common mistakes that BOTH me and my partner who are Senior CS majors made in our Algorithms project while coding it up.

    # The way that Python looks at if loops is like I had it above with if [condition]
    # So the above python essentializes to if [number = 4]
    # and then it evalues the truth of the claim number = 4
    # and since that's true, it replaces number = 4 with True, and executes
    # So, the following code is also valid (thoguh not very useful):

    if True:
        print("Wow, it's true")

    #And similarly:
    if False:
        print("Wow, it's false")
    
    
    # We can chain together conditions in a single statement:
    if number == 5 and number == 4:
        print("lmao what how if this actually gets printed ill be sad")
    # to make stuff like this that shouldn't run

    #or stuff like this that should run, where != is the same as "is not equal to":
    if number == 5 and number != 4:
        pass
    
    #which is the same as:
    if number == 5 and not number == 4:
        pass
    
    # Becuase doing the logic out for the above, if (number == 5) and not (number == 4)
    # reduces to if (True) and not (False) => if (True) and (True) => (True)

    # I'm not going to go through all of the math behind logic gates and stuff but the following is kinda necessary.  It's obvious, but is good to explicitly state:

    # AND:
        # True AND True = True
        # True AND False = False
        # False AND True = False
        # False AND False = False
    # OR:
        # True OR True = True
        # True OR False = True
        # False OR True = True
        # False OR False = False
    # XOR (Exclusive-OR, I don't remember how python calls XOR but here it is nonetheless):
        # True XOR True = False
        # True XOR False = True
        # False XOR True = True
        # False XOR False = False
    # NOT: 
        # NOT True = False
        # NOT False = True

    # You can make really complex if statements, which are evaluated in PEMDAS style, with the most interior being calculated first.
    if ((True and True) or False) or (not True or not False):
        pass

    # Now, we don't want to have to make if-statements for every possability, so we have else and elif (else-if) statements which must follow an if statement:

    if (x == 5):
        pass
    elif (x == 6):
        pass
    elif (x > 10):
        pass
    elif (x < 0):
        pass
    else:
        pass

    # As you can see above, you can have lots of elif statements chained together.  The moment one executes, the rest of the chain is skipped.
    # So if x=5, the rest of the chain after the first block would get skipped.

    # You also don't need an elif, you can just have if and else:

    if (x == 5):
        print("x was 5")
    else:
        print("x was not 5")

def whileLoop():

    # while [some condition == True]:
        # Execute this code
    x = 0
    while x == 5:
        x = x + 1
        print(x)

    # You can do all the same logic engineering you could above with if's, but I'm not going to show all of those again becuase I don't feel I need to.
    # As long as the statement evaluates to True, the loop will continue
    # As such, it's really easy to get infinite loops:
    
    # while True:
        # print ("lmfao get fucked nerd")
    
    # That's pretty much it. 
    # A good example of while loops in use is during the algorithms project I made last term, we needed to randomly pick a box to put an item into
    # However, the item is already in a box, and we don't want to put the item back into the same box
    # So we ran a while loop which ran while the item was in the same box it started in, and stopped looping the moment it didn't rand into the same box.
    # Really whenenver you don't know how many iterations you need to get something done you use a while loop.

def doWhileLoop():
    # Oh JK python doesn't have a do-while loop.  You can always re-write a do-while loop into a while loop, although a do-while loop (or something equivalent) may sitll be prefered
    # Though I found a fun example online that emulates it in python and also shows how there are uses for "while True" or "while False"
    
    i = 1

    while True:
        print(i)
        i = i + 1
        if(i > 3):
            break
    
    # So the above code is equivalent to something that looks roughly like (in some python-stylized pseudocode):
    # do:
        # print(i)
        # i = i + 1
    # while i <= 3
    
    # This is also a time to talk about break!
    # Let's say you're in a loop, and for some reason you need to gtfo of that loop regardless of whatever rules it has in place
    # Well that's what break does.

    # So in the above example, in theory you loop forever
    # However the moment i > 3, you break out of the loop.  (Note that here if isn't considered a loop).
    # We used break statemenets in our algorithms project a lot, since we were doing random moves and testing them against other random moves
    # and we wanted to immediately commit a given move if it was a "really really good" move and stop checking other possible moves even though we had a loop to do so.
    # So even though it feels kinda hacky/wonky it's legit.




# Wow that was a lot more text than I thought this was going to take
# Anyway, you can use your functions just like any other, however because python is often interpreted it reads top to bottom.
# So if the first function you define calls like 3 others that you define later down, those won't work since your code doesn't know what those functions are.
# This is why unlike in java where it's common to put your "main" function at the top of your code, in Python it's always at the very bottom.



def main():
    # hey, it's your main function!  It's just convention for the main function to be the thing that controlls all the other things
    # So if you want to mess around here with all the function calls, this is a place to do all of it!
    doWhileLoop()
    #etc.



# Now we actually need to tell python to run our main method since it doesn't do that by default
# So __name__ == "__main__" will only execute if we're running this code as a script (from the command line).

if __name__ == "__main__":
    main()

# Why is this the syntax for it?  I dunno.  I mean I kinda do.  "__name__" means like, "what level is this being run from"
# If it's being run as a script from the command line, "__name__" is "__main__".
# Why are those the things?  Idk.  
    









