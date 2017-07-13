import re

with open('gibberish.txt', 'r') as example:
    for line in example:
        print(re.sub('mach','inl',line))
