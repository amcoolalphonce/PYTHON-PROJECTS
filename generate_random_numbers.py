#generate random values
import random

random.random()

for i in range(3):
    print(random.random())# generates numbers btwn 0 and one
    print(random.randint(3, 20))#btwn 3 and 20

members=['John', 'Price', 'Collins', 'Will', 'Jane']
leader=random.choice(members)#chooses randomly from the list
print(leader)
