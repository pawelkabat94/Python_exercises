
#break
'''
for i in "qwertyuioplkjhgfvdsamzx":
    print (i)
    if i == "j":
        print("found my letter")
        break
'''

#continue
'''
for i in "qwertyuioplkjhgfvdsamzx":
    print (i)
    if i == "j":
        print("found my letter")
        continue
'''
#shuffle
'''
import random
Footballers = ["Messi", "Ronaldo", "Pele", "Maradona", "Cruyff", "Beckenbauer", "Zidane", "Iniesta", "Platini", "Di Stefano"]
random.shuffle(Footballers)
print(Footballers)
'''

import random
Footballers = ["Messi", "Ronaldo", "Pele", "Maradona", "Cruyff", "Beckenbauer", "Zidane", "Iniesta", "Platini", "Di Stefano"]
random.shuffle(Footballers)
print(f"among all mentioned footballers:",Footballers)

Lucky = random.choice(Footballers)

for fot in Footballers:
    print(fot)
    if fot == Lucky:
        print(f"the best footballer is:",Lucky)
        continue


