class Person:
    pass
class Male(Person):
    def getGender(self):
        return 'Male'
class Female(Person):
    def getGender(self):
        return 'Female'

print(Male().getGender())
print(Female().getGender())