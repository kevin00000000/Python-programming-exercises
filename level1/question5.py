class Question5:
    def __init__(self):
        self._string = ''
    def getString(self):
        self._string = input('input a string:')
    def printString(self):
        print(self._string.upper())
o = Question5()
o.getString()
o.printString()