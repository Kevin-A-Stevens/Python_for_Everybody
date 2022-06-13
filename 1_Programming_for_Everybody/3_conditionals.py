"""
Comparison Operators
< Less than
<= Less than or equal to
== Equal to
>= Greater than or equal to
> Greater than
!= Not equal to

Functions
    print()
    range()
"""

x = 5
if x > 2:
    print('Bigger than 2')
    print('Still bigger')
print('Done with 2')

for i in range(5):
    print(i)
    if i > 2:
        print('Bigger than 2')
    print('Done with i', i)
print('All done')

if x > 2:
    print('Bigger')
else:
    print('Smaller')
print('All done')

if x > 2:
    print('small')
elif x < 10:
    print('Medium')
else:
    print('LARGE')
print('All done')

"""
Try Except conditional
"""
astr = 'Hello Kevin'
try:
    istr = int(astr)
except:
    istr = -1
print('First', istr)  # First -1

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print('Second', istr)  # Second 123

