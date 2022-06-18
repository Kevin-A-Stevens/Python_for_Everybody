"""
A dictionary contains key:value pairs
"""

purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
print(purse['candy'])
purse['candy'] = purse['candy'] + 2
print(purse)

ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)
ccc['cwen'] = ccc['cwen'] + 1
print(ccc)

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']

# The get method
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)

# looping through a dictionary
people = {'chuck': 1, 'fred': 42, 'jan': 100}
for key in people:
    print(key, people[key])
