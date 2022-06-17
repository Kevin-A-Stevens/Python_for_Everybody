"""
input() gives us back a string
functions
    len()
    print()
    .lower() - a method built into every string
    type() - method is class str
    dir() - method is class str
A function is some stored code that we use
A function takes some input and produces an output
strings are objects
"""

# indexing
fruit = 'banana'
letter = fruit[1]
print(letter)  # a

x = 3
w = fruit[x - 1]
print(w)  # n

y = len(fruit)
print(y)  # 6

# loop through a string
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

print()
for letter in fruit:
    print(letter)

print()
# counting
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

# slicing
# end is up to but do not include
print()
s = 'Monty Python'
print(s[0:4])
print(s[6:7])
print(s[6:20])
print(s[:2])
print(s[8:])
print(s[:])

# using n as a logical operator
print('n' in fruit)
if 'a' in fruit:
    print('Found it!')

# compare strings
if word == 'banana':
    print('All right, bananas')

# string library
greet = 'Hello Kevin'
zap = greet.lower()
print(zap)
print(greet)

stuff = 'Hello world'
print(type(stuff))
print(dir(stuff))

# Other string library
"""
str.capitalize()                        str.replace(old, new[, count])
str.center(width[, fillchar])           str.lower()
str.endswith(suffix[, start[, end]])    str.rstrip)[chars])
str.find(sub[, start[, end]])           str.strip([chars])
str.lstrip([chars)                      str.upper()
"""

pos = fruit.find('na')
print(pos)

aa = fruit.find('z')
print(aa)  # -1 = did not find it

# search and replace
nstr = greet.replace('Kevin', 'Bob')
print(nstr)

# strip white space
greet = '   Hello Kevin   '
print(greet.lstrip())
print(greet.rstrip())
print(greet.strip())

# prefixes
line = 'Please have a nice day'
print(line.startswith('Please'))
