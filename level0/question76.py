import random
print(random.choice([i for i in range(1, 201) if i%5==0 and i%7==0]))