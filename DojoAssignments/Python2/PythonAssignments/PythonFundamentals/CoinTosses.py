import random

def toss_coin(x):
    a = 0
    b = 0
    for i in range(x):
        print i + 1
        t = random.randint(0,1)
        # print t
        # print x
        # # if i == 0:
        #     a = a + 1
        #     b = b + 0
        #     print "Attempt #"+str(i)+":  Throwing a coin... it's a head!... Got "+str(a)+"head(s) so far and "+str(b)+"tail(s) so far"
        # else:
        #     b = b + 1
        #     a = a + 0
        #     print "Attempt #"+str(i)+":  Throwing a coin... it's a head!... Got "+str(a)+"head(s) so far and "+str(b)+"tail(s) so far"
toss_coin(20)