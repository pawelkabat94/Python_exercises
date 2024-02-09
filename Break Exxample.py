import random
VACCINES = ["Moderna", "Pfizer", "Sputnik v", "Covaxin", "AstraZeneca", "CoronaVac"]

random.shuffle(VACCINES)
print(VACCINES)

LUCKY = random.choice(VACCINES)
print(LUCKY)

for vac in VACCINES:
    print(f"******TESTING VACCINE {vac}")
    if vac == LUCKY:
        print("###################################")
        print(f"{LUCKY} Vaccine, Test SUCCESSFUL")
        print("###################################")
        print()
        break
    print("XXXXXXXXXXXX")
    print("Test Failed")
    print("XXXXXXXXXXXX")
    print()



# pawel break example


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