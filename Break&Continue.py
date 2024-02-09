import random
BoxerName = ["Usyk","Inoue","Bivol","Crawford","Haney","Lomachenko","Lopez","Beterbiev","Charlo","Canelo"]
random.shuffle(BoxerName)


Lucky = random.choice(BoxerName)
print(f"the p4p king is {Lucky}")

for box in BoxerName:
    print(f"In top 10 p4p is {box}")
    if box == Lucky:
        print("Found my p4p king.")
        continue
