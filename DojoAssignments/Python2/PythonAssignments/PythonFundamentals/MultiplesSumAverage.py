a = [1, 2, 5, 10, 25, 3]
print a
a.sort()

aSum = sum(a)
print aSum

n = len(a)


mean = aSum/n

print mean

r = range(1000)
print r

oddRange = range(1, 1000, 2)

print oddRange

oddRangeSum = sum(oddRange)

print oddRangeSum

numbers = range(1, 1000, 2)
print numbers

for n in numbers:
    if len('n') < 1000:
        numbers.insert(0, n)

print numbers