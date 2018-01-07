from operator import itemgetter, attrgetter
listPerson = [(x.split(',')[0], int(x.split(',')[1]), int(x.split(',')[2]))
              for x in iter(input, 'OK')]
print(sorted(listPerson, key=itemgetter(0, 1, 2)))
