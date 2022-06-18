"""
tuples are immutable
You can't sort a tuple
"""
x = ('Glenn', 'Sally', 'Joseph')
print(x[2])

y = (1, 9, 2)
print(max(y))

for iter in y:
    print(iter)

# tuples and assignment - can put a tuple on the left-hand side

(x, y) = (4, 'fred')
print(y)
(a, b) = (99, 98)
print(a)

# tuples are comparable
print((0,1,2) < (5,1,2))
