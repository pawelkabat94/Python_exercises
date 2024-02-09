# For Loop
"""
PLANET = "Earth"
for i in PLANET:
    print("Value if i is now ",i)

print("Rest of the code.")

VACCINES = ("Moderna", "Pfizer", "Sputnik v", "Covaxin", "AstraZeneca")

for vac in VACCINES:
    print(f"{vac} vaccine provides Immunization against covid19")

VACCINES = ["Moderna", "Pfizer", "Sputnik v", "Covaxin", "AstraZeneca"]

for vac in VACCINES:
    print(f"{vac} vaccine provides Immunization against covid19")
"""
# While Loop
x = 0
while x <= 10:
    print("Value of X is:", x)
    print("Looping")
    x+=1

print("Rest of the code.")


#pawel loops:
BoxerName = ("Usyk","Inoue","Bivol","Crawford","Haney","Lomachenko","Lopez","Beterbiev","Charlo","Canelo")
for boxer in BoxerName:
    print(boxer, "is in top 10 of P4P ranking.")

x = 0
while x <= 10:
    print("Value of x is",x)
    print("Looping")
    x+=1


BoxerName = ("Usyk","Inoue","Bivol","Crawford","Haney","Lomachenko","Lopez","Beterbiev","Charlo","Canelo")
for boxer in BoxerName:
    print("the best p4p figther is")
    for i in boxer:
        print(i)

import time
x = 0
while x <= 10:
    print("Value of x is",x)
    print("Looping")
    x+=1
    time.sleep(3)



import time

BoxerName = ("Usyk", "Inoue", "Bivol", "Crawford", "Haney", "Lomachenko", "Lopez", "Beterbiev", "Charlo", "Canelo")
for boxer in BoxerName:
    print("the best p4p figther is", boxer)
    time.sleep(2)
