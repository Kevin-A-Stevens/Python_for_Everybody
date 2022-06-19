"""
before you can use regular expressions, you have to import
^ = beginning of line
. = any character
* = zero or more characters
[0-9] = One digit
[0-9]+ = One or more digits
\S = non blank character
"""
import re
hand = open('mbox.txt')
for line in hand:
    if line.find('Our') >= 0:
        print(line)

hand = open('mbox.txt')
for line in hand:
    line = line.rstrip()
    if re.search('Our', line):
        print(line)

hand = open('mbox.txt')
for line in hand:
    if line.startswith('Our') >= 0:
        print(line)

hand = open('mbox.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^Our', line):
        print(line)

x = 'My 2 favorite numbers are 9 and 42'
y = re.findall('[0-9]+', x)
print(y)

x = 'From: kevin.alan.stevens@gmail.com Sat Jun 18'
email = re.findall('\S+@\S+', x)
print(email)

"""
^ Matches the beginning of a line
$ Matches the end of the line
. Matches any character
\s Matches whitespace
\S Matches any non-whitespace character
* Repeats a character zero or more times
*? Repeats a character zero or more times (non-greedy)
+ Repeats a character one or more times
+? Repeats a character one or more times (non-greedy)
[aeiou] Matches a single character in the listed set
[^XYZ] Matches a single character not in the listed set
[a-z0-9] The set of characters can include a range
( Indicates where string extraction is to start
) Indicates where string extraction is to end
"""
