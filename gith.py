#Python uses interpreter that means it directly runs on an virtual machine





spam_amount = 0
#Variable assignment** : Here we create a variable called spam_amount and assign it the value of 0 using =,
#which is called the assignment operator.
----------






print(spam_amount)
#Function calls:. print is a Python function that displays the value passed to it on the screen. 
#We call functions by putting parentheses after their name, and putting the inputs (or arguments) to the function in those parentheses.
-----------






if spam_amount > 0:
    print("But I don't want ANY spam!")

viking_song = "Spam Spam Spam"
print(viking_song)
#Python is prized for its readability and the simplicity.
#Note how we indicated which code belongs to the if. "But I don't want ANY spam!" is only supposed to be printed 
#if spam_amount is positive. But the later code (like print(viking_song)) should be executed no matter what. How do we (and Python) know that?
#The colon (:) at the end of the if line indicates that a new code block is starting. Subsequent lines which are indented are part of that code block.



"But I don't want ANY spam!"
#This code snippet is also our first sighting of a string in Python^
#Strings can be marked either by double or single quotation marks. (But because this particular string contains a single-quote character, 
#we might confuse Python by trying to surround it with single-quotes, unless we're careful.)
# -------------------------



type(spam_amount)
#this function is very useful in python to find the type of a variable. 
#There are 4 types of types-- Float(19.32), Integer(3), boolean(True/False), string("any word written")
# -------------------------
# Operator	Name	Description
# a + b:	Addition	Sum of a and b
# a - b:	Subtraction	Difference of a and b
# a * b:	Multiplication	Product of a and b
# a / b:	True division	Quotient of a and b
# a // b:	Floor division	Quotient of a and b, removing fractional parts
# a % b:	Modulus	Integer remainder after division of a by b
# a ** b:	Exponentiation	a raised to the power of b
# -a:	Negation	The negative of a
# -------------------------








#Order of operations
#The arithmetic we learned in primary school has conventions about the order in which operations are evaluated. 
# Some remember these by a mnemonic such as PEMDAS - Parentheses, Exponents, Multiplication/Division, Addition/Subtraction.
#----------------





#Builtin functions are the ones that are already implied or used in the python IDE
#-------------------------









# min and max return the minimum and maximum of their arguments, respectively.
print(min(1, 2, 3))
#output 1
print(max(1, 2, 3))
#output 3
#abs returns the absolute value of an argument:
print(abs(32))
print(abs(-32))
#both 32
#--------------






# The help() function is possibly the most important Python function you can learn. 
#If you can remember how to use help(), you hold the key to understanding most other functions.





print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
# file:  a file-like object (stream); defaults to the current sys.stdout.
#     sep:   string inserted between values, default a space.
#     end:   string appended after the last value, default a newline.
#     flush: whether to forcibly flush the stream.

#-----------------------------------









def least_difference(a, b, c):
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
     return min(diff1, diff2, diff3)
#   This creates a function called least_difference, which takes three arguments, a, b, and c.

# Functions start with a header introduced by the def keyword. The indented block of code following the : is run when the function is called.

# return is another keyword uniquely associated with functions. When Python encounters a return statement, it exits the function immediately, and passes the value on the right hand side to the calling context.

# The docstring is a triple-quoted string (which may span multiple lines) that comes immediately after the header of a function. When we call help() on a function, it shows the docstring.

# Aside: The last two lines of the docstring are an example function call and result. (The >>> is a reference to the command prompt used in Python interactive shells.) 
# Python doesn't run the example call - it's just there for the benefit of the reader. 
# The convention of including 1 or more example calls in a function's 
# docstring is far from universally observed, but it can be very effective at helping someone understand your function.
print(1, 2, 3, sep=' < ')
#Know how to use a sep func
#----------------------------------






def greet(who="Colin"):
    print("Hello,", who)
    
greet()
greet(who="Kaggle")
# (In this case, we don't need to specify the name of the argument, because it's unambiguous.)
greet("world")
# Hello, Colin
# Hello, Kaggle
# Hello, world
#def function
#-------------------------------------












def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)

def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))

print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1), 
    sep='\n', # '\n' is the newline character - it starts a new line
)
# mult_by_five(x): This function takes an argument x and returns the result of multiplying x by 5.
# call(fn, arg): This function takes two arguments: fn (a function) and arg (an argument to be passed to the function). It calls the function fn with the argument arg and returns the result.
# squared_call(fn, arg): This function also takes two arguments: fn (a function) and arg (an argument to be passed to the function). It calls the function fn twice with the argument arg and returns the result of the second call of fn on the result of the first call.
# The print statement at the end demonstrates the usage of these functions:
# call(mult_by_five, 1): Calls the mult_by_five function with the argument 1, resulting in 5 because 5 * 1 = 5.
# squared_call(mult_by_five, 1): Calls the mult_by_five function with the argument 1, and then calls it again on the result (5). This results in 25 because 5 * 5 = 25.

#---------------------------






def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5

print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),
    sep='\n',
)


# This code snippet demonstrates the use of the max() function along with a custom function mod_5(x)
#--------------------------












True or True and False

and is evaluated before or. That's why the first expression above is True. If we evaluated it from left to right, we would have calculated True or True first (which is True), 
and then taken the and of that result with False, giving a final value of False.





























