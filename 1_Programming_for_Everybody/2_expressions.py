"""
Cannot use reserved words as a variable, function, or class name
Variable names - asking Python to allocate a place in memory
    Can start with a letter or underscore
    avoid underscores as python uses these for its own purposes
    tend to use mostly lower case
    choose a variable name that makes sense (Mnemonic)
Expressions
    + addition
    - subtraction
    * multiplication
    / division
    ** power
    % remainder
    = assignment
Order of evaluation
    parentheses
    exponents (power)
    multiplication, division, remainder
    addition, subtraction
    left to right
Functions
    print()
    type()
    float()
    int()
    input()
"""

xx = 2
xx = xx + 2
print(xx)

yy = 440 * 12
print(yy)

zz = yy / 1000
print(zz)

jj = 23
kk = jj % 5
print(kk)

print(4 ** 3)

"""
concatenate = put together
cannot concatenate a string with an integer
can use casting to do this instead. Will see later
"""
ddd = 1 + 4
print(ddd)

eee = 'hello ' + 'there'
print(eee)

# The type function
print(type(eee))
print(type('hello'))
print(type(1))

# The float function
print(float(99) + 100)

# An example of casting
i = 42
print(type(i))
f = float(i)
print(f)
print(type(f))

# Integer division produces a floating point result
print(10 / 2)

"""
String Conversions
You can use int() and float() to convert types
"""
sval = '123'
print(type(sval))

ival = int(sval)
print(type(ival))
print(ival + 1)

"""
User input
"""
nam = input('Who are you? ')
print('Welcome', nam)
