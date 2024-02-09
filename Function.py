"""
def winning_boxing (fullname, fights):
    print(f"{fullname}, had {fights} winning fights.")
    if fights > 35 and fights < 40:
        print("He is considered as a good one")
    elif fights >= 40 and fights < 50:
        print("Great record")
    elif fights >= 50:
        print("This is a legend")
    else: print("Not should be included in p4p")

winning_boxing("Floyd Mayweather", 52)
"""

'''
def bestfootballerever(foot1, *args):
    print(f"The best footballer ever is {foot1}")
    for i in args:
        print(f"The best footballer ever is {i}")

bestfootballerever("Ronaldo","Messi","Maradona")
'''

'''
def order_food (order1,min_time):
    print(f"You have orderd {order1}")
    print(f"You have to wait {min_time}")

order_food("salad", 34)
'''

"""def basketball_players (*name):
   # print(f"This {name} is the GOAT")
    for i in name:
        print(f"This {i} is
basketball_players("Jordan", "Bird", "Magic", "Lebron")"""

import random

def time_activity (*args, **kwargs):
    print(args)
    print(kwargs)

    min = sum(args) + random.randint(0 ,40)
    print(min)

    activity = random.choice(list(kwargs.keys()))
    print(activity)

    print(f"You need to spend {min} minutes for {activity}, which is {kwargs[activity]}")

time_activity(10, 20, 30, hobby="reading", sport="boxing", work="DevOps", fun="family")
