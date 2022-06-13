"""
Loops and Iteration
"""
n = 5
while n > 0:
    print(n)
    n = n - 1
print('Blastoff!')
print(n)

"""
break statement to exit out of a loop
"""
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')

"""
continue ends the current iteration and jumps to the top
of the loop and starts the next iteration
"""
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done')

"""
A simple definite loop
for loop
"""
for i in [5,4,3,2,1]:
    print(i)
print('Blastoff!')

friends = ['Joseph', 'Glenn', 'Kevin']
for friend in friends:
    print('Happy New Year: ', friend)
print('Done')

"""
Looping through a set
"""
print('Before')
for thing in [9,41,12,3,74,15]:
    print(thing)
print('After')

"""
Finding the largest value
"""
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9,41,12,3,74,15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)
print('After', largest_so_far)

"""
Loop Idioms
"""

# Counting in a loop
zork = 0
print('Before', zork)
for thing in [9,41,12,3,74,15]:
    zork = zork + 1
    print(zork, thing)
print('After', zork)

# Summing a loop
total = 0
print('Before', total)
for thing in [9,41,12,3,74,15]:
    total = total + thing
    print(total, thing)
print('After', total)

# Finding the average
count = 0
sum = 0
print('Before', count, sum)
for value in [9,41,12,3,74,15]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum / count)

# Filtering a loop
print('Before')
for value in [9,41,12,3,74,15]:
    if value > 20:
        print('Large number', value)
print('After')

# Search using a Boolean variable
found = False
print('Before', found)
for value in [9,41,12,3,74,15]:
    if value == 3:
        found = True
        break
    print(found, value)
print('After', found)

"""
Finding the smallest value
"""
smallest_so_far = None
print('Before', smallest_so_far)
for the_num in [9,41,12,3,74,15]:
    if smallest_so_far is None:
        smallest_so_far = value
    elif value > smallest_so_far:
        smallest_so_far = value
    print(smallest_so_far, value)
print('After', smallest_so_far)

