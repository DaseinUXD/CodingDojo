import random


def randint(min='', max=''):
    rnd = round(random.random() * max)
    rnd5 = round(random.random() * min)
    print(rnd, rnd5)


randint(min=25, max=100)

# I still have questions about this one
