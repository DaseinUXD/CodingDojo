import random
random_num = random.random()
print random_num

random_int = random.randint(0,100)
print random_int

def grades_scores (x):
    for i in range(x):
        a = random.randint(60,100)
        if a < 70:
            print "Score: " + str(a)+"; Your grade is D"
        elif a < 80:
            print "Score: " + str(a) +"; Your grade is C"
        elif a < 90:
            print "Score: " + str(a) +"; Your grade is B"
        else:
            print "Score: " + str(a) +"; Your grade is A"

grades_scores(10)


