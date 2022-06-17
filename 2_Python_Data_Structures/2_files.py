xfile = open('mbox.txt')
for cheese in xfile:
    print(cheese)

fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line count: ', count)

fhand = open('mbox.txt')
inp = fhand.read()
print(len(inp))

# searching through a file
fhand = open('mbox.txt')
for line in fhand:
    if line.startswith('Our'):
        print(line)

# print adds a new line by default
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    print(line)

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened', fname)
    quit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)



