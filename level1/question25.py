class Question25:
    Name = "Class Attribute"
    def __init__(self, name):
        self.Name = name
Kevin = Question25('Kevin')
print(Kevin.Name)
print(Question25.Name)
Question25.Name = "Changed Class Attribute"
print(Kevin.Name)
print(Question25.Name)