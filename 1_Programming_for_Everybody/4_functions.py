"""
creating our own functions
functions are reusable pieces of code
functions
    max()
    min()
"""

big = max('Hello world')
print(big)  # w

tiny = min('Hello world')
print(tiny)  #


def print_lyrics():
    print("I'm a lumberjack, and I'm okay")
    print("I sleep all night and I work all day")


print_lyrics()
print_lyrics()

"""
function parameters
"""


def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')


greet('en')
greet('es')
greet('fr')

"""
Often a function will take its arguments, do some computation, and
return a value to be used as the value of the function call in the
calling expression. The return keyword is used for this
return does two things
    It stops the function
    It determines the residual value
"""


def greeting():
    return "Hello"


print(greeting(), "Kevin")


def greetings(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'


print(greetings('en'), 'Kevin')
print(greetings('es'), 'Glenn')
print(greetings('fr'), 'Michael')


def addtwo(a, b):
    added = a + b
    return added


x = addtwo(3, 5)
print(x)
