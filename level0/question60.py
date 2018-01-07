import re
print([x for x in input('Input a sequence of words separated by whitespace: ').split(' ') if re.search(r'\b\d+\b', x)!=None])