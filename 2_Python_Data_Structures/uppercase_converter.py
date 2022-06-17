fh = open('mbox.txt')
print(fh)

for lx in fh:
    ly = lx.rstrip()  # remove extra new line since print adds one
    print(ly.upper())

