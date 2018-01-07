import math
listMove = [(x.split(' ')[0], int(x.split(' ')[1])) for x in iter(input, 'OK')]

X = 0
Y = 0
for step in listMove:
    if step[0]=="UP":
        Y += step[1]
    elif step[0] == 'DOWN':
        Y -= step[1]
    elif step[0] == 'LEFT':
        X -= step[1]
    elif step[0] == 'RIGHT':
        X += step[1]
    else:
        pass
distance = round(math.sqrt(X**2+Y**2))

print('The distance from current point to original point is {:d}'.format(distance))