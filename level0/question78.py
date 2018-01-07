import random
print([random.randrange(100, 201, 2) for i in range(0, 5)])
print(random.sample([i for i in range(100,201) if i%2==0], 5))