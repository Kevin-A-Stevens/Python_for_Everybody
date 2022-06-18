counts = dict()
print('Enter a line of text: ')
line = input('')

words = line.split()

print('Words: ', words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts', counts)

# lst = list()
# for key, val in counts.items():
#     newtup = (val, key)
#     lst.append(newtup)
#
# lst = sorted(lst, reverse=True)
#
# for val, key in lst[:10]:
#     print(key, val)

# print(sorted( [(v, k) for k, v in counts.items()]))
