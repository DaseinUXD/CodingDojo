words = "It's thanksgiving day. It's my birthday, too"
print words

x = [2,54,-2,7,12,98]
minimum = min(x)
maximum = max(x)

length = len(x)

print length, minimum, maximum

first = x[0]
last = x[length - 1]

print first, last

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
len = len(x)
print len

half = len/2
print half

firstHalf = x.range(0, half)
lastHalf = x.range(half, len - 1)

print firstHalf, lastHalf