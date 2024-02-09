import random

def time_activity (*args, **kwargs):
    print(args)
    print(kwargs)

    min = sum(args) + random.randint(0 ,40)
    print(min)

    activity = random.choice(list(kwargs.keys()))
    print(activity)

    print(f"You need to spend {min} minutes for {activity}, which is {kwargs[activity]}")