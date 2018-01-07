def square(num):
    if type(num) == str:
        if num.isdigit():
            return int(num)**2
        if num.isdecimal():
            return float(num)**2
    elif type(num)==int or type(num)==float:
        return num**2
    else:
        return None

print(square('4'))
print(square('abc'))
print(square(5))
print(square(list([1])))