import re
listPwd = [x for x in input(
    "Input  a sequence of password separated by comma:").split(',')]
result = []

for x in listPwd:
    if re.search(r"[a-z]+", x) and re.search(r"[0-9]+", x) and re.search(r"[A-Z]+", x) and re.search(r"[$#@]+", x) and len(x) >= 6 and len(x) <= 12:
        result.append(x)
print(','.join(result))
