import re

with open('gibberish.txt', 'r') as example:
    for line in example:
        if (re.match('boo',line)):
            print(line)
