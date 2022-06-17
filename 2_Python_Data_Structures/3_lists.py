"""
A list is a collection
allows us to put many variables in a single variable
function
    range() = returns a list
"""

friends = ['Joseph', 'Glenn', 'Sally']

for friend in friends:
    print('Happy New Year: ', friend)
print('Done')

print(friends[1])
print(len(friends))
r = range(5)
print(r)

# lists can be added together
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)

# lists can be sliced
t = [9, 41, 12, 3, 74, 15]
print(t[1:3])

# building a list from scratch
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)

# searching a list
some = [1, 9, 21, 10, 16]
print(9 in some)
print(20 not in some)

# Can sort a list
some.sort()
print(some)

print(len(some))
print(max(some))
print(min(some))
print(sum(some))
print(sum(some) / len(some))

# Strings and lists
abc = 'With three words'
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])

for w in stuff:
    print(w)

# The double split pattern
line = 'From kevin.alan.stevens@gmail.com Thu Jun 16 09:19:10 2022'
words = line.split()  # first split
email = words[1]
print(words)
print(email)
pieces = email.split('@')  # second split
print(pieces)




